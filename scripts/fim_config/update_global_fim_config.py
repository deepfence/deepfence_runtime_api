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

    print("\nupdate global fim config")

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
    try:
        response = requests.post("{0}/node/df_global_default_fim/update_fim_config".format(api_url), headers=default_headers,
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
