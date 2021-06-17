import requests
import yaml, json
from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_fim_config(api_url, api_key, node_name):
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

    # We need to find the node_id for this node_name, if not global config
    print("\ngetting fim config...")

    try:
        response = requests.get("{0}/node/{1}/get_fim_config".format(api_url, node_name), headers=default_headers,
                                 verify=False)
        print("response: ", response.text)
        fim_config = json.loads(response.text)["data"]
        print("fim_config: \n", fim_config)
        # print(json.dumps(fim_config, indent=4))
    except:
        print("Error in api call")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: python3 get_fim_config.py <mgmt_console_ip_address> <api_key> <node_name>")
        exit(1)
    if len(sys.argv) == 3:
        node_name = "df_global_default_fim"
    else:
        node_name = sys.argv[3]
    get_fim_config("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2], node_name)
