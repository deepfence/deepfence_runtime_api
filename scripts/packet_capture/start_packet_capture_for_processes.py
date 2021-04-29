import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def start_packet_capture(api_url, api_key, process_list, pcap_mode):
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

    enumerate_filters = {"type": ["host"], "pseudo": False}
    api_response = requests.post("{0}/enumerate".format(api_url),
                                 json={"filters": enumerate_filters, "size": 5000},
                                 headers=default_headers, verify=False).json()
    nodes_list = []
    counter = 1
    api_response_nodes = api_response.get("data", {}).get("data", [])
    if not api_response_nodes:
        print("No nodes found")
        return
    for node in api_response_nodes:
        if node.get("is_ui_vm", False) or node.get("pseudo", False):
            continue
        nodes_list.append({"id": node["id"], "node_name": node.get("host_name", "")})
        counter += 1
    print("\nEnter comma separated list of node numbers to start packet capture. Eg: 1,3,4\n")
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
    if not nodes_selected:
        print("No nodes selected. Select at least one node.")
        exit(0)
    print("Total hosts: {0}".format(counter))
    print("\nStopping Packet Capture on all hosts, if not already stopped.")
    post_data = {
        "action": "packet_capture_stop",
        "node_type": "host",
        "node_id_list": [n["id"] for n in nodes_selected]
    }
    try:
        response = requests.post("{0}/node_action".format(api_url), headers=default_headers,
                                 verify=False, json=post_data)
        print(response.text)
        print("Packet capture will be stopped in a moment")
    except:
        print("Error in api call")

    time.sleep(60)
    print("\nDeleting the saved packet capture config.")
    post_data = {
        "host_name_list": ["all"]        
    }
    try:
        response = requests.delete("{0}/packet_capture_config".format(api_url), headers=default_headers,
                                    verify=False, json=post_data)
        print(response.text)
    except:
        print("Error in API to delete existing packet capture config")

    is_encrypted_capture = "N"
    print("\nSaving selected packet capture config")
    post_data = {
        "config_list": [{"config":{"process_list":process_list, 
                                   "snap_length":65535, 
                                   "capture_percentage":100, 
                                   "is_encrypted_capture":is_encrypted_capture, 
                                   "pcap_mode":pcap_mode}, "host_name":"all"}]        
    }
    try:
        response = requests.post("{0}/packet_capture_config".format(api_url), headers=default_headers,
                                    verify=False, json=post_data)
        print(response.text)
    except:
        print("Error in API while saving packet capture config.")

    print("\nStarting Packet Capture")
    for node in nodes_selected:
        post_data = {
            "process_list": process_list, "snap_length": 65535,
            "capture_percentage": 100, "is_encrypted_capture": is_encrypted_capture, "pcap_mode": pcap_mode
        }
        try:
            response = requests.post("{0}/node/{1}/packet_capture_start".format(api_url, node["id"]),
                                     headers=default_headers, verify=False, json=post_data)
            print(response.text)
        except:
            print("Error in api call")
    print("Packet capture started")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 packet_capture.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    process_list = ['java']
    pcap_mode = "allow"     #should either be 'allow', 'deny' or 'all'
    start_packet_capture("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2], process_list, pcap_mode)
