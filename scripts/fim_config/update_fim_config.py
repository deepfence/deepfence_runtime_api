import requests
import yaml, json
from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def update_fim_config(api_url, api_key, config_filename):
    default_headers = {"Content-Type": "application/json", "Authorization": ""}
    api_response = requests.post("{0}/users/auth".format(api_url),
                                 json={"api_key": api_key}, headers=default_headers,
                                 verify=False).json()
    if api_response["success"]:
        print("Authentication successful")
    else:
        print("Authentication failed")
        return
    default_headers["Authorization"] = "Bearer " + api_response["data"]["access_token"]

    enumerate_filters = {"type": ["host"], "pseudo": False}
    api_response = requests.post("{0}/enumerate".format(api_url),
                                 json={"filters": enumerate_filters, "size": 10000},
                                 headers=default_headers, verify=False).json()
    nodes_list = []
    counter = 1
    print("\nupdate fim config")
    api_response_nodes = api_response.get("data", {}).get("data", [])
    if not api_response_nodes:
        print("No nodes found")
        return
    for node in api_response_nodes:
        if node.get("is_ui_vm", False):
            continue
        if node["type"] == "kube_service":
            node_name = "{0} (kubernetes service)".format(node.get("name", ""))
        else:
            node_name = "{0} (host)".format(node.get("host_name", ""))
        print("{0}: {1}".format(counter, node_name))
        nodes_list.append({"id": node["id"], "node_name": node_name, "node_type": node["type"]})
        counter += 1
    print("\nEnter comma separated list of node numbers to update fim config. Eg: 1,3,4\n")
    print("Enter \"all\" (without quotes) to update fim config on all nodes\n")
    user_input = input("-->").split(",")
    if "all" in user_input:
        nodes_selected = nodes_list
    else:
        nodes_selected = []
        for user_input_no in user_input:
            try:
                nodes_selected.append(nodes_list[int(user_input_no) - 1])
            except:
                pass
    if not nodes_selected:
        print("No nodes selected. Select at least one node.")
        exit(0)
    # print("\nEncrypted packet capture? Enter Y or N:")
    # is_encrypted_capture = str(input("-->"))
    is_encrypted_capture = "N"
    with open (config_filename, "r") as configfile:
        fim_config=configfile.read()
    with open ("fim_config_schema.json", "r") as schemafile:
        fim_schema=schemafile.read()    
    # print("Fim Config: ", fim_config)
    # print("Fim Schema: ", fim_schema)
    # print("config yaml: ", yaml.load(fim_config))
    # print("schema json: ", json.loads(fim_schema))
    try:
        validate(yaml.safe_load(fim_config), json.loads(fim_schema))
    except ValidationError as ex:
        print("Fim Config is not valid: \n", ex)
        exit(1)
    except SchemaError as ex:
        print("Fim Schema is not valid: \n", ex)
        exit(1)
    except Exception as ex:
        print("Error: ", ex)
        exit(1)

    post_data = {
        "fim_config": str(fim_config)
    }
    for node in nodes_selected:
        try:
            response = requests.post("{0}/node/{1}/update_fim_config?os=linux".format(api_url, node["id"]), headers=default_headers,
                                     verify=False, json=post_data)
            print(response.text)
            print("FIM config will be updated in selected nodes")
        except:
            print("Error in api call")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 4:
        print("Usage: python3 update_fim_config.py <mgmt_console_ip_address> <api_key> <config_filename>")
        exit(1)
    update_fim_config("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2], sys.argv[3])
