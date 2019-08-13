import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

hosts_to_tag = {
    "prod1": ["prod"],
    "prod2": ["prod"],
    "prod3": ["prod"],
    "prod4": ["prod"],
    "prod5": ["prod"],
}
maxsize = 100


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

    # Enumerate nodes
    counter = 1
    enumerate_response = requests.post("{0}/enumerate".format(api_url),
                                       json={"filters": {"type": ["host", "container"], "pseudo": False},
                                             "size": maxsize}, headers=default_headers, verify=False).json()
    for node in enumerate_response["data"]["data"]:
        if node.get("host_name", "") not in hosts_to_tag:
            continue
        tags_to_add = hosts_to_tag[node.get("host_name", "")]
        node_name = "{0} (host)".format(node.get("host_name", "")) if node["type"] == "host" \
            else "{0}/{1} (container)".format(node.get("container_name", ""), node.get("host_name", ""))
        print("\n{0}: Add tag {1} to {2}".format(counter, tags_to_add, node_name))
        print(requests.post("{0}/node/{1}/add_tags".format(api_url, node["id"]),
                            json={"tags": tags_to_add}, headers=default_headers, verify=False).json())
        counter += 1


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 add_tag_to_nodes.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    add_tags("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
