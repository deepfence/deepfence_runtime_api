import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def start_traffic_analysis(api_url, api_key):
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
                                 json={"filters": enumerate_filters, "size": 10000},
                                 headers=default_headers, verify=False).json()
    nodes_list = []
    counter = 1
    print("\nStart traffic analysis")
    api_response_nodes = api_response.get("data", {}).get("data", [])
    if not api_response_nodes:
        print("No nodes found")
        return
    for node in api_response_nodes:
        if node.get("is_ui_vm", False):
            continue
        if node["type"] == "kube_service":
            node_name = "{0} (kubernetes service)".format(node.get("name", ""))
        else:
            node_name = "{0} (host)".format(node.get("host_name", ""))
        print("{0}: {1}".format(counter, node_name))
        nodes_list.append({"id": node["id"], "node_name": node_name, "node_type": node["type"]})
        counter += 1
    print("\nEnter comma separated list of node numbers to start traffic analysis. Eg: 1,3,4\n")
    print("Enter \"all\" (without quotes) to start traffic analysis on all nodes\n")
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

    payload = {
        "inbound_protos": "http,tcp",
        "outbound_protos": "http,tcp",
        "inbound_ruleset": "rules/emerging_threats/inbound/from_2019/emerging-coinminer.rules,rules/emerging_threats/inbound/from_2019/threatview_CS_c2.rules,rules/emerging_threats/inbound/from_2019/emerging-current_events.rules,rules/emerging_threats/inbound/from_2019/emerging-dns.rules,rules/emerging_threats/inbound/from_2019/emerging-exploit.rules,rules/emerging_threats/inbound/from_2019/emerging-exploit_kit.rules,rules/core_rule_set/REQUEST-934-APPLICATION-ATTACK-GENERIC.conf,rules/emerging_threats/inbound/from_2019/emerging-attack_response.rules,rules/emerging_threats/inbound/from_2019/emerging-hunting.rules,rules/emerging_threats/inbound/from_2019/emerging-ja3.rules,rules/core_rule_set/REQUEST-944-APPLICATION-ATTACK-JAVA.conf,rules/core_rule_set/REQUEST-930-APPLICATION-ATTACK-LFI.conf,rules/emerging_threats/inbound/from_2019/emerging-malware.rules,rules/core_rule_set/REQUEST-922-MULTIPART-ATTACK.conf,rules/core_rule_set/REQUEST-933-APPLICATION-ATTACK-PHP.conf,rules/emerging_threats/inbound/from_2019/emerging-policy.rules,rules/core_rule_set/REQUEST-921-PROTOCOL-ATTACK.conf,rules/core_rule_set/REQUEST-932-APPLICATION-ATTACK-RCE.conf,rules/core_rule_set/REQUEST-931-APPLICATION-ATTACK-RFI.conf,rules/core_rule_set/REQUEST-942-APPLICATION-ATTACK-SQLI.conf,rules/core_rule_set/REQUEST-913-SCANNER-DETECTION.conf,rules/emerging_threats/inbound/from_2019/emerging-user_agents.rules,rules/emerging_threats/inbound/from_2019/emerging-web_client.rules,rules/emerging_threats/inbound/from_2019/emerging-web_server.rules,rules/core_rule_set/RESPONSE-955-WEB-SHELLS.conf,rules/emerging_threats/inbound/from_2019/emerging-web_specific_apps.rules",
        "outbound_ruleset": "rules/emerging_threats/outbound/from_2019/emerging-coinminer.rules,rules/emerging_threats/outbound/from_2019/threatview_CS_c2.rules,rules/emerging_threats/outbound/from_2019/emerging-current_events.rules,rules/emerging_threats/outbound/from_2019/emerging-dns.rules,rules/emerging_threats/outbound/from_2019/emerging-exploit.rules,rules/emerging_threats/outbound/from_2019/emerging-exploit_kit.rules,rules/core_rule_set/REQUEST-934-APPLICATION-ATTACK-GENERIC.conf,rules/emerging_threats/outbound/from_2019/emerging-attack_response.rules,rules/emerging_threats/outbound/from_2019/emerging-hunting.rules,rules/emerging_threats/outbound/from_2019/emerging-ja3.rules,rules/core_rule_set/REQUEST-944-APPLICATION-ATTACK-JAVA.conf,rules/core_rule_set/REQUEST-930-APPLICATION-ATTACK-LFI.conf,rules/emerging_threats/outbound/from_2019/emerging-malware.rules,rules/core_rule_set/REQUEST-922-MULTIPART-ATTACK.conf,rules/core_rule_set/REQUEST-933-APPLICATION-ATTACK-PHP.conf,rules/emerging_threats/outbound/from_2019/emerging-policy.rules,rules/core_rule_set/REQUEST-921-PROTOCOL-ATTACK.conf,rules/core_rule_set/REQUEST-932-APPLICATION-ATTACK-RCE.conf,rules/core_rule_set/REQUEST-931-APPLICATION-ATTACK-RFI.conf,rules/core_rule_set/REQUEST-942-APPLICATION-ATTACK-SQLI.conf,rules/core_rule_set/REQUEST-913-SCANNER-DETECTION.conf,rules/emerging_threats/outbound/from_2019/emerging-user_agents.rules,rules/emerging_threats/outbound/from_2019/emerging-web_client.rules,rules/emerging_threats/outbound/from_2019/emerging-web_server.rules,rules/core_rule_set/RESPONSE-955-WEB-SHELLS.conf,rules/emerging_threats/outbound/from_2019/emerging-web_specific_apps.rules",
        "pcap_mode": "all",
        "process_list": []
    }

    for node in nodes_selected:
        try:
            response = requests.post("{0}/node/{1}/packet_capture_start?".format(api_url, node["id"]),
                                     headers=default_headers, verify=False, json=payload)
            print(response.text)
            print("Started traffic analysis on selected nodes")
        except:
            print("Error in api call")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 start_traffic_analysis.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    start_traffic_analysis("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
