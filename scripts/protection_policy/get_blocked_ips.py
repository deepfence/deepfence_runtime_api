import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_blocked_ips(api_url, api_key):
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
    page_no = 1
    page_size = 500
    protection_policy_actions = requests.get(
        "{0}/users/network_protection_policy_action?page_no={1}&size={2}".format(api_url, page_no, page_size),
        headers=default_headers, verify=False).json()
    if not protection_policy_actions.get("success", False):
        print(protection_policy_actions.get("error", ""))
        return
    if not protection_policy_actions.get("data", {}).get("network_protection_policy_actions", []):
        print("No ip addresses blocked by network policy")
        return
    total_size = protection_policy_actions["data"]["total"]
    blocked_ips = protection_policy_actions["data"]["network_protection_policy_actions"]
    while len(blocked_ips) < total_size:
        page_no += 1
        protection_policy_actions = requests.get(
            "{0}/users/network_protection_policy_action?page_no={1}&size={2}".format(api_url, page_no, page_size),
            headers=default_headers, verify=False).json()
        blocked_ips.extend(protection_policy_actions["data"]["network_protection_policy_actions"])
    print("Total blocked ips:", len(blocked_ips))
    for blocked_ip_detail in blocked_ips:
        print(json.dumps(blocked_ip_detail, indent=2))


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 get_blocked_ips.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    get_blocked_ips("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
