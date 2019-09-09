import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def add_tags(api_url, api_key):
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

    print("Enter tag to add to selected nodes. Eg: prod")
    tags_to_add = input("-->").split(",")
    # Enumerate nodes
    enumerate_response = requests.post(
        "{0}/enumerate".format(api_url),
        json={"filters": {"type": ["host", "container", "container_image"], "pseudo": False}, "size": 500},
        headers=default_headers, verify=False).json()
    nodes_list = []
    counter = 1
    print("\nDeepfence Vulnerability Scan")
    for node in enumerate_response["data"]["data"]:
        if node["type"] == "container":
            node_name = "{0} / {1} (container)".format(node.get("container_name", ""), node.get("host_name", ""))
        elif node["type"] == "container_image":
            node_name = "{0} (container_image)".format(node.get("image_name_with_tag", ""))
        else:
            node_name = "{0} (host)".format(node.get("host_name", ""))
        print("{0}: {1}".format(counter, node_name))
        nodes_list.append({"id": node["id"], "node_name": node_name})
        counter += 1
    print("\nEnter comma separated list of node numbers to add tag {0}. Eg: 1,3,4".format(tags_to_add))
    print("Enter \"all\" (without quotes) to add tag {0} to all nodes\n".format(tags_to_add))
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
    for node in nodes_selected:
        print("\n{0}: Add tag {1} to {2}".format(counter, tags_to_add, node["node_name"]))
        print(requests.post("{0}/node/{1}/add_tags".format(api_url, node["id"]),
                            json={"user_defined_tags": tags_to_add}, headers=default_headers, verify=False).json())
        counter += 1


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 add_tag_to_nodes.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    add_tags("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
