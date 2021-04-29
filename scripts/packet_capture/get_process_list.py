import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_connected_processes(api_url, api_key):
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
    connected_process_list = []
    counter = 1
    print("\nGetting connected processes in all agents")
    api_response_nodes = api_response.get("data", {}).get("data", [])
    if not api_response_nodes:
        print("No nodes found")
        return
    for node in api_response_nodes:
        if node.get("is_ui_vm", False):
            continue
        connected_process_list.extend(
                [k.split(":")[0] for k, v in node.get("connectedProcesses", {}).items() if k not in connected_process_list])
        counter += 1
    print(list(set(connected_process_list)))


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 get_connected_processes.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    get_connected_processes("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
