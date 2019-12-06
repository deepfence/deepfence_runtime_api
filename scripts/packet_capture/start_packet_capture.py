import requests
from threading import Thread
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def start_packet_capture(api_url, api_key):
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

    enumerate_filters = {"type": ["host", "kube_service"], "pseudo": False}
    api_response = requests.post("{0}/enumerate".format(api_url),
                                 json={"filters": enumerate_filters, "size": 1000},
                                 headers=default_headers, verify=False).json()
    nodes_list = []
    counter = 1
    print("\nStart Packet Capture")
    api_response_nodes = api_response.get("data", {}).get("data", [])
    if not api_response_nodes:
        print("No nodes found")
        return
    for node in api_response_nodes:
        if node["type"] == "kube_service":
            node_name = "{0} (kubernetes service)".format(node.get("name", ""))
        else:
            node_name = "{0} (host)".format(node.get("host_name", ""))
        print("{0}: {1}".format(counter, node_name))
        nodes_list.append({"id": node["id"], "node_name": node_name})
        counter += 1
    print("\nEnter comma separated list of node numbers to start packet capture. Eg: 1,3,4")
    print("Enter \"all\" (without quotes) to start packet capture on all nodes\n")
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
    print("\nEncrypted packet capture? Enter Y or N:")
    is_encrypted_capture = str(input("-->"))
    for node in nodes_selected:
        process = Thread(args=["{0}/node/{1}/packet_capture_start".format(api_url, node["id"]), default_headers,
                               node["node_name"], is_encrypted_capture], target=call_api)
        process.start()


def call_api(url, headers, node_name, is_encrypted_capture):
    try:
        resp = requests.post(url, headers=headers, verify=False,
                             json={"port_list": [], "interface_name": "All", "snap_length": 65535,
                                   "percent_capture": 100, "is_encrypted_capture": is_encrypted_capture}).json()
        print("\n{0}:\n{1}".format(node_name, resp))
    except:
        print(node_name + ": Error in api call")
    return True


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 start_packet_capture.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    start_packet_capture("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
