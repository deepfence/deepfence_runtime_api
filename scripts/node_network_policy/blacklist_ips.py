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


def blacklist_ips_inbound(api_url, api_key):
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

    # Enumerate nodes
    enumerate_response = requests.post(
        "{0}/enumerate".format(api_url),
        json={"filters": {"type": ["host"], "pseudo": False}, "size": 10000},
        headers=default_headers, verify=False).json()
    nodes_list = []
    counter = 1
    enumerate_response_nodes = enumerate_response.get("data", {}).get("data", [])
    if not enumerate_response_nodes:
        print("No nodes found")
        return
    for node in enumerate_response_nodes:
        if node.get("type") == "host":
            if node.get("is_ui_vm", False):
                continue
            node_name = "{0} (host)".format(node.get("host_name", ""))
            print("{0}: {1}".format(counter, node_name))
            nodes_list.append(
                {"id": node["id"], "node_name": node_name, "scope_id": node["scope_id"], "type": node["type"]})
            counter += 1
    print("\nEnter comma separated list of host serial numbers to blacklist IP addresses. Eg: 1,3,4")
    print("Enter \"all\" (without quotes) to blacklist on all hosts\n")
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
    counter = 1
    ip_address_to_blacklist = []
    my_file = Path("./ip_addresses.txt")
    if my_file.is_file():
        blacklist_ips_file = open("ip_addresses.txt")
        ip_addresses = blacklist_ips_file.read().split('\n')
        for ip in ip_addresses:
            if validate(ip):
                ip_address_to_blacklist.append(ip)
    else:
        print("ip_addresses.txt file missing")
        return

    blacklist_ips_file.close()
    if not ip_address_to_blacklist:
        print("ip_addresses.txt file is empty")
        return

    for node in nodes_selected:
        print("\n{0}: Blacklisting IP addresses {1} on node {2}".format(
            counter, ip_address_to_blacklist, node["node_name"]))
        payload = json.dumps({
            "packet_direction": "inbound",
            "node_policy_type": "blacklist",
            "ip_address_list": ip_address_to_blacklist,
            "block_duration": 0,
            "port_list": [],
            "scope_id": node['scope_id'],
            "node_type": node['type']
        })
        counter += 1
        try:
            res = requests.post("{0}/users/node_network_protection_policy".format(api_url), data=payload,
                                headers=default_headers, verify=False)
            if res.status_code != 200:
                raise Exception(res.text)
        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 blacklist_ips.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    blacklist_ips_inbound("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
