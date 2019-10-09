import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def apply_network_policy(api_url, api_key, tag, node_policy_type, packet_direction, ip_address_to_block, port,
                         block_duration):
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

    enumerate_filters = {"type": ["host", "container"], "tags": [tag], "pseudo": False}
    api_response = requests.post("{0}/enumerate".format(api_url),
                                 json={"filters": enumerate_filters, "size": 1000},
                                 headers=default_headers, verify=False).json()
    nodes_list = []
    counter = 1
    print("\nNodes with tag \"{0}\"".format(tag))
    for node in api_response["data"]["data"]:
        node_name = "{0} (host)".format(node.get("host_name", "")) if node["type"] == "host" \
            else "{0} / {1} (container)".format(node.get("container_name", ""), node.get("host_name", ""))
        print("{0}: {1}".format(counter, node_name))
        nodes_list.append({"id": node["id"], "node_name": node_name})
        counter += 1
    counter = 1
    for node in nodes_list:
        print("\n{0}: Applying node network policy on {1}".format(counter, node["node_name"]))
        post_data = {"node_id": node["id"], "node_policy_type": node_policy_type, "packet_direction": packet_direction,
                     "ip_address_list": [ip_address_to_block], "port_list": [port], "block_duration": block_duration,
                     "action": "block"}
        print(requests.post("{0}/users/node_network_protection_policy".format(api_url),
                            headers=default_headers, verify=False, json=post_data).json())
        counter += 1


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 9:
        print(
            "Usage: python3 apply_network_policy_for_tag.py <mgmt_console_ip_address> <api_key> <tag> <node_policy_type>"
            " <packet_direction> <ip_address_to_block> <port> <block_duration>")
        print("node_policy_type: blacklist, whitelist")
        print("packet_direction: inbound, outbound")
        print("ip_address_to_block: external ip address to block")
        print("port: internal port")
        print("block_duration: Number of seconds to block the external ip address. '0' for indefinite blocking")
        exit(1)
    apply_network_policy("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4],
                         sys.argv[5], sys.argv[6], int(sys.argv[7]), int(sys.argv[8]))
