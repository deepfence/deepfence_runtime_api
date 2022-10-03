import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re
import json
from pathlib import Path

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def validate(Ip):
    if re.search(regex, Ip):
        return True
    else:
        return False


def delete_blacklist_ips_inbound_rule(api_url, api_key):
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

    my_file = Path("./ip_addresses.txt")
    if my_file.is_file():
        blacklist_ips_file = open("ip_addresses.txt")
        Ips = blacklist_ips_file.read().split('\n')
        final_ips = []
        for ip in Ips:
            if validate(ip):
                final_ips.append(ip)
    else:
        print("ip_addresses.txt file missing")
        return

    blacklist_ips_file.close()
    id_list = []

    url = f"{api_url}/users/node_network_protection_policy?node_policy_type=blacklist&"
    response = requests.request("GET", url, headers=default_headers, data={}, verify=False)
    if response.status_code == 200:
        json_response = response.json()
        for row in json_response.get('data', {}).get('node_network_protection_policies', []):
            if row.get('node_policy_type') == 'blacklist' and row.get('packet_direction') == "inbound":
                if row.get('ip_address') in final_ips:
                    id_list.append(row.get('id'))
    else:
        print(response.text)

    if id_list:
        payload = json.dumps({
            "policy_id_list": [str(id) for id in id_list]
        })
        delete_url = f"{api_url}/users/node_network_protection_policy"
        del_response = requests.request("DELETE", delete_url, headers=default_headers, data=payload, verify=False)

        if del_response.status_code != 200:
            print(del_response.text)
        print("Node network policies deleted successfully")
    else:
        print("There are no rules to be deleted")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 delete_blacklisted_ip_rules.py.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    delete_blacklist_ips_inbound_rule("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
