import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def export_protection_policy(api_url, api_key):
    # Auth
    default_headers = {"Content-Type": "application/json"}
    auth_response = requests.post("{0}/users/auth".format(api_url), json={"api_key": api_key}, headers=default_headers,
                                  verify=False).json()
    if auth_response["success"]:
        print("Authentication successful")
    else:
        print("Authentication failed")
        return
    default_headers["Authorization"] = "Bearer " + auth_response["data"]["access_token"]

    response = requests.post("{0}/export".format(api_url), headers=default_headers,
                             json={"resource_types": ["network_protection_policy"]})
    print("Exported the protection policies")
    return response.json()


def import_protection_policy(api_url, api_key, policy):
    # Auth
    auth_response = requests.post("{0}/users/auth".format(api_url), json={"api_key": api_key},
                                  headers={"Content-Type": "application/json"}, verify=False).json()
    if auth_response["success"]:
        print("Authentication successful")
    else:
        print("Authentication failed")
        return

    files = {
        'deepfence_export': ('network_protection_policy.json', json.dumps(policy)),
        'resource_types': (None, '["network_protection_policy"]'),
    }
    response = requests.post("{0}/import".format(api_url),
                             headers={"Authorization": "Bearer " + auth_response["data"]["access_token"]}, files=files)
    print(response.text)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 5:
        print(
            "Usage: python3 export_protection_policy.py <mgmt_console_ip_address_1> <api_key_1> <mgmt_console_ip_address_2> <api_key_2>")
        exit(1)
    policy = export_protection_policy("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
    import_protection_policy("https://{0}/deepfence/v1.5".format(sys.argv[3]), sys.argv[4], policy)
