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
        print("\n{0}: Starting compliance scan on {1}".format(counter, node["node_name"]))
        print(requests.post("{0}/node/{1}/start_compliance_scan".format(api_url, node["id"]),
                            headers=default_headers, verify=False,
                            json={"compliance_check_type": compliance_check_type}).json())
        counter += 1


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print(
            "Usage: python3 start_compliance_scan_for_tag.py <mgmt_console_ip_address> <api_key> <tag> <compliance_check_type>")
        print("Options for compliance_check_type: cis, nist_master, nist_slave, pcidss, hipaa, standard")
        exit(1)
    run_compliance_scan("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4])
