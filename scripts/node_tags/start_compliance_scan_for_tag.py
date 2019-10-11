import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def run_compliance_scan(api_url, api_key, tag, compliance_check_type):
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

    enumerate_filters = {"type": ["host", "container", "container_image"], "user_defined_tags": [tag], "pseudo": False}
    api_response = requests.post("{0}/enumerate".format(api_url),
                                 json={"filters": enumerate_filters, "size": 1000},
                                 headers=default_headers, verify=False).json()
    nodes_list = []
    counter = 1
    api_response_nodes = api_response.get("data", {}).get("data", [])
    if not api_response_nodes:
        print("No nodes found with tag {0}".format(tag))
        return
    print("\nNodes with tag \"{0}\"".format(tag))
    for node in api_response_nodes:
        if node["type"] == "container":
            node_name = "{0} / {1} (container)".format(node.get("container_name", ""), node.get("host_name", ""))
        elif node["type"] == "container_image":
            node_name = "{0} (container_image)".format(node.get("image_name_with_tag", ""))
        else:
            node_name = "{0} (host)".format(node.get("host_name", ""))
        print("{0}: {1}".format(counter, node_name))
        nodes_list.append({"id": node["id"], "node_name": node_name})
        counter += 1
    counter = 1
    for node in nodes_list:
        print("\n{0}: Starting compliance scan on {1}".format(counter, node["node_name"]))
        print(requests.post("{0}/node/{1}/start_compliance_scan".format(api_url, node["id"]),
                            headers=default_headers, verify=False,
                            json={"compliance_check_type": compliance_check_type}).json())
        counter += 1


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 5:
        print(
            "Usage: python3 start_compliance_scan_for_tag.py <mgmt_console_ip_address> <api_key> <tag> <compliance_check_type>")
        print("Options for compliance_check_type: cis, nist_master, nist_slave, pcidss, hipaa, standard")
        exit(1)
    run_compliance_scan("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4])
