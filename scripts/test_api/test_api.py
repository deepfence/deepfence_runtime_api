from __future__ import print_function
import gevent

from gevent import monkey

monkey.patch_socket()
monkey.patch_ssl()
import requests
from sys import argv
from time import sleep
import json
import signal
from copy import deepcopy
from socketio_client_deepfence.manager import Manager
from collections import defaultdict
from requests.packages.urllib3.exceptions import InsecureRequestWarning

try:
    # python2
    from urlparse import urlparse
except ImportError:
    # python3
    from urllib.parse import urlparse

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

"""
Test Deepfence Runtime API's

1. Get access_token using demo api_key
2. Enumerate all hosts, containers, images, processes, process names
"""


def handle_sigint(sig, frame):
    print("\n Exiting the test now...")
    exit(0)


class DeepfenceAPITest(object):
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.node_types = ["Host", "Container", "Process"]
        self.headers = {"Content-Type": "application/json", "Authorization": ""}
        self.test_choices = [
            "List Process, Containers & Hosts", "Alert Management", "Vulnerability Management",
            "Operations on Containers", "Capture Network Traffic", "Policy Management", "Websocket Streaming"]

        self.test_choice_methods = ["enumerate", "alert_management", "cve", "node_control", "packet_capture",
                                    "policy_management", "websocket_streaming"]

    def __print_resp(self, resp, print_all=False):
        if print_all:
            print(resp)
        else:
            print("Success:", resp["success"])
            if not resp["success"]:
                print(resp)

    def __dump_resp_to_file(self, file_name, resp):
        with open("/tmp/" + file_name + ".json", 'w') as file:
            if type(resp) == dict:
                file.write(json.dumps(resp))
            else:
                file.write(str(resp))

    def __print_resp_data_count(self, resp):
        print("Success:", resp["success"])
        if not resp["success"]:
            print(resp)
        else:
            print(len(resp["data"]))

    def __dump_nodes(self, nodes):
        new_data = {}
        for node in nodes:
            new_data[node["id"]] = json.dumps(node, indent=4)
        return new_data

    def __enumerate_helper(self, node_types):
        resp = requests.post("{0}/enumerate".format(self.api_url),
                             json={"filter": {"type": node_types, "pseudo": False}}, headers=self.headers,
                             verify=False).json()
        if not resp["success"]:
            return "Error", False
        if not "data" in resp.get("data", {}):
            return "No " + ''.join(node_types) + " running", False
        return resp["data"]["data"], True

    def enumerate(self):
        user_choice = self.__get_user_input(self.node_types)
        data, success = self.__enumerate_helper([self.node_types[user_choice].lower()])
        if not success:
            print(data)
            return
        self.__list_print_helper(list(self.__dump_nodes(data).values()), add_new_line=True)

    def websocket_streaming(self):
        user_choice = self.__get_user_input(self.node_types)
        node_type = self.node_types[user_choice].lower()
        api_url = urlparse(self.api_url)
        url_port = api_url.netloc.split(":")
        if len(url_port) == 1:
            port = 443 if api_url.scheme == "https" else 80
        else:
            port = url_port[1]
        io = Manager(api_url.scheme, url_port[0], port, auto_connect=True, ssl_verify=False,
                     params={"api_key": self.api_key})
        socketio = io.socket('/websockets')

        print_keys = ["host_name", "container_name", "pid", "image_name", "process", "name", "adjacency",
                      "publicIpAddress", "docker_container_ips", "id"]
        nodes_data = {}

        def format_node(node, parse_adjacencies=False):
            if not node:
                return {}
            if "adjacency" in node:
                if parse_adjacencies:
                    adjacencies = []
                    for adj_node_id in deepcopy(node["adjacency"]):
                        formatted_adj_data = format_node(nodes_data.get(adj_node_id, {}), parse_adjacencies=False)
                        if formatted_adj_data:
                            adjacencies.append(formatted_adj_data)
                    node["adjacency"] = adjacencies
                else:
                    node["adjacency"] = []
            return {k: v for k, v in node.items() if k in print_keys and v}

        @socketio.on(node_type)
        def on_node_data(*args, **kwargs):
            print("\nReceived ", node_type)
            if not args:
                return
            if args[0]["add"]:
                print("New nodes")
                for node in args[0]["add"]:
                    nodes_data[node["id"]] = node
                    print(json.dumps(format_node(node, parse_adjacencies=True), indent=4))
                    # print(format_node(node, parse_adjacencies=True))
            if args[0]["update"]:
                print("Updated nodes")
                for node in args[0]["update"]:
                    nodes_data[node["id"]] = node
                    print(json.dumps(format_node(node, parse_adjacencies=True), indent=4))
                    # print(format_node(node, parse_adjacencies=True))

        @socketio.on_connect()
        def on_connect():
            print("Websocket connected")

        @socketio.on("established")
        def on_established(*args, **kwargs):
            print("Connection established")
            print(args)
            socketio.emit("join", {"channel": node_type})

        socketio.connect()
        gevent.wait()

    def node_control(self):
        '''
        container_action_values = ["Stop", "Pause", "Un-Pause", "Start"]
        '''
        container_action_values = ["Pause", "Un-Pause"]
        data, success = self.__enumerate_helper(["container"])
        if not success:
            print(data)
            return
        data = self.__dump_nodes(data)
        data_keys = list(data.keys())
        tmp_data_values = list(data.values())
        container_data_values = []
        container_data_state = []
        for i in range(0, len(tmp_data_values)):
            json_val = json.loads(tmp_data_values[i])
            for key, value in json_val.items():
                if (key.lower() == "container_name"):
                    container_data_values.append(value)
                if (key.lower() == "docker_container_state_human"):
                    if "Paused" in value:
                        container_data_state.append("Paused")
                    else:
                        container_data_state.append("Running")
        if (len(container_data_values) == 0):
            print("\nNo containers available for actions on it")
            return
        container_prompt = []
        for i in range(0, len(container_data_values)):
            container_prompt.append(container_data_values[i] + " (" +
                                    container_data_state[i] + ")")
        print("\nChoose a container to perform actions on it")
        container_idx = self.__get_user_input(container_prompt)
        print("\nChoose an action to be performed on this container")
        action_idx = self.__get_user_input(container_action_values)
        container_id = data_keys[container_idx]
        if (container_action_values[action_idx] == "Stop"):
            print("Now stopping the container. Please wait.....")
            resp = requests.post("{0}/node/{1}/stop".format(self.api_url, container_id), json={}, headers=self.headers,
                                 verify=False).json()
            sleep(10)
            self.__print_resp(resp)
            self.__dump_resp_to_file("stop_container_" + container_data_values[container_idx], resp)
        elif (container_action_values[action_idx] == "Pause"):
            print("Now pausing the container. Please wait.....")
            resp = requests.post("{0}/node/{1}/pause".format(self.api_url, container_id), json={}, headers=self.headers,
                                 verify=False).json()
            sleep(10)
            self.__print_resp(resp)
            self.__dump_resp_to_file("pause_container_" + container_data_values[container_idx], resp)
        elif (container_action_values[action_idx] == "Un-Pause"):
            print("Now doing un-pause on the the container. Please wait....")
            resp = requests.post("{0}/node/{1}/unpause".format(self.api_url, container_id), json={},
                                 headers=self.headers, verify=False).json()
            sleep(10)
            self.__print_resp(resp)
            self.__dump_resp_to_file("un-pause_container_" + container_data_values[container_idx], resp)
        elif (container_action_values[action_idx] == "Start"):
            resp = requests.post("{0}/node/{1}/start".format(self.api_url, container_id), json={}, headers=self.headers,
                                 verify=False).json()
            sleep(10)
            self.__print_resp(resp)
            self.__dump_resp_to_file("start_container_" + container_data_values[container_idx], resp)

    def cve(self):
        node_action_values = ["Start-CVE", "Stop-CVE"]
        data, success = self.__enumerate_helper(["container", "host"])
        if not success:
            print(data)
            return
        data = self.__dump_nodes(data)
        data_keys = list(data.keys())
        tmp_data_values = list(data.values())
        node_data_values = []
        node_data_state = []
        for i in range(0, len(tmp_data_values)):
            json_val = json.loads(tmp_data_values[i])
            node_name = json_val["host_name"]
            container_name = json_val.get("container_name", "")
            if container_name:
                node_name = container_name + "--" + node_name
            node_data_values.append(node_name)
        for i in range(0, len(data_keys)):
            resp = requests.get("{0}/node/{1}/cve_scan_status".format(self.api_url, data_keys[i]),
                                headers=self.headers, verify=False).json()
            status = resp["data"]["action"]
            if resp["data"].get("cve_scan_message", ""):
                status += ": " + str(resp["data"]["cve_scan_message"])
            node_data_state.append(status)
        if (len(node_data_values) == 0):
            print("\nNo nodes available for actions on it")
            return
        node_prompt = []
        for i in range(0, len(node_data_values)):
            node_prompt.append(node_data_values[i] + " (" + node_data_state[i] + ")")
        print("\nChoose a node to perform actions on it")
        node_idx = self.__get_user_input(node_prompt)
        print("\nChoose an action to be performed on this node")
        action_idx = self.__get_user_input(node_action_values)
        node_id = data_keys[node_idx]
        if (node_action_values[action_idx] == "Start-CVE"):
            print("Now starting CVE. Please wait.....")
            resp = requests.post("{0}/node/{1}/cve_scan_start".format(self.api_url, node_id), json={},
                                 headers=self.headers, verify=False).json()
            sleep(10)
            self.__print_resp(resp)
            self.__dump_resp_to_file("start_cve_" + node_data_values[action_idx], resp)
        elif (node_action_values[action_idx] == "Stop-CVE"):
            print("Now stopping CVE. Please wait.....")
            resp = requests.post("{0}/node/{1}/cve_scan_stop".format(self.api_url, node_id), json={},
                                 headers=self.headers, verify=False).json()
            sleep(10)
            self.__print_resp(resp)
            self.__dump_resp_to_file("stop_cve_" + node_data_values[action_idx], resp)

    def packet_capture(self):
        data, success = self.__enumerate_helper(["host"])
        if not success:
            print(data)
            return
        data = self.__dump_nodes(data)
        data_keys = list(data.keys())
        tmp_data_values = list(data.values())
        data_values = []
        for i in range(0, len(tmp_data_values)):
            json_val = json.loads(tmp_data_values[i])
            for key, value in json_val.items():
                if (key.lower() == "host_name"):
                    data_values.append(value)
        print("Enter host number")
        user_choice = self.__get_user_input(data_values)
        node_id = data_keys[user_choice]
        pkt_cpt_keys = ["Start Packet Capture", "Stop Packet Capture", "Packet Capture Status"]
        pkt_cpt_vals = ["packet_capture_start", "packet_capture_stop", "packet_capture_status"]
        user_choice = self.__get_user_input(pkt_cpt_keys)
        action = pkt_cpt_vals[user_choice]
        if action == "packet_capture_status":
            print("Getting packet capture status. Please wait......")
            resp = requests.get("{0}/node/{1}/{2}".format(self.api_url, node_id, action),
                                headers=self.headers, verify=False).json()
        else:
            print(action + " packet capture. Please wait.....")
            resp = requests.post("{0}/node/{1}/{2}".format(self.api_url, node_id, action), json={},
                                 headers=self.headers, verify=False).json()
        print(json.dumps(resp, indent=4))

    def alert_management(self):
        print("\nAlerts by host/container\n")
        host_alerts = defaultdict(dict)
        resp = requests.post("{0}/alerts".format(self.api_url),
                             json={"filter": {}, "action": "get", "start_index": 0, "size": 10000},
                             headers=self.headers, verify=False).json()
        if resp["data"]:
            for alert in resp["data"]:
                c_host_name = alert["host_name"] + "/" + alert["container_name"]
                if alert["severity"] in host_alerts[c_host_name]:
                    host_alerts[c_host_name][alert["severity"]] += 1
                else:
                    host_alerts[c_host_name][alert["severity"]] = 1
            print(json.dumps(dict(host_alerts), indent=4))
            print("\nSample alert\n")
            print(json.dumps(resp["data"][0], indent=4))
        else:
            print("No alerts")

    def policy_management(self):
        quar_policy = "Quarantine Protection Policy"
        net_policy = "Network Protection Policy"
        node_blacklist_policy = "Node Blacklist Policy"
        node_whitelist_policy = "Node Whitelist Policy"
        policy_type_choices = [quar_policy, net_policy, node_blacklist_policy, node_whitelist_policy]
        policy_type_api_path = ["quarantine_protection_policy", "network_protection_policy",
                                "blacklist_node_network_protection_policy", "whitelist_node_network_protection_policy"]
        user_policy_type_choice = self.__get_user_input(policy_type_choices)
        policy_type = policy_type_api_path[user_policy_type_choice]
        policy_choices = ["Add", "List", "Delete", "List Policy Logs", "Delete Policy Logs"]
        if policy_type.startswith("blacklist_") or policy_type.startswith("whitelist_"):
            policy_choices = policy_choices[:3]
        user_policy_choice = policy_choices[self.__get_user_input(policy_choices)]
        node_policy_type = ""
        api_url = "{0}/users/{1}".format(self.api_url, policy_type)
        if policy_type.startswith("blacklist_"):
            node_policy_type = "blacklist"
            api_url = "{0}/users/{1}?node_policy_type=blacklist".format(self.api_url,
                                                                        policy_type.replace("blacklist_", ""))
        elif policy_type.startswith("whitelist_"):
            node_policy_type = "whitelist"
            api_url = "{0}/users/{1}?node_policy_type=whitelist".format(self.api_url,
                                                                        policy_type.replace("whitelist_", ""))
        policy_type = policy_type.replace("blacklist_", "").replace("whitelist_", "")
        if user_policy_choice == "Add":
            user_choice_host = 0
            hosts_data = []
            if node_policy_type:
                hosts_data, success = self.__enumerate_helper(["host"])
                hosts_data = [i["host_name"] for i in hosts_data]
                print("On which host to add the policy?")
                user_choice_host = self.__get_user_input(hosts_data)
            # Add policy
            if policy_type == "quarantine_protection_policy":
                payload = {"alert_level": "critical", "action": "restart", "node_type": "container",
                           "alert_count_threshold": "1"}
            elif policy_type == "network_protection_policy":
                payload = {"alert_level": "high", "action": "block", "node_type": "host", "block_duration": 216000,
                           "alert_from_time": 216000, "alert_count_threshold": "2"}
            elif node_policy_type == "blacklist":
                payload = {"action": "block", "host_name": hosts_data[user_choice_host], "block_duration": 216000,
                           "node_policy_type": node_policy_type, "packet_direction": "inbound",
                           "ip_address_list": ["1.2.3.4"], "port_list": ["8080"]}
            elif node_policy_type == "whitelist":
                payload = {"action": "block", "host_name": hosts_data[user_choice_host], "block_duration": 216000,
                           "node_policy_type": node_policy_type, "packet_direction": "inbound",
                           "ip_address_list": ["1.2.3.4"], "port_list": ["8080"]}
            else:
                return
            resp = requests.post(api_url, headers=self.headers, verify=False, json=payload).json()
            print(json.dumps(resp, indent=4))
        elif user_policy_choice == "List":
            # List policies
            resp = requests.get(api_url, headers=self.headers, verify=False).json()
            if not resp["data"]:
                print("No policies")
            else:
                resp = resp["data"][policy_type.replace("policy", "policies")]
                if not resp:
                    print("No policies")
                self.__list_print_helper(resp)
        elif user_policy_choice == "Delete":
            # Delete policy
            print("Enter policy id to delete")
            resp = requests.get(api_url, headers=self.headers, verify=False).json()
            if not resp["data"]:
                print("No policies")
                return
            else:
                resp = resp["data"][policy_type.replace("policy", "policies")]
                if not resp:
                    print("No policies")
                    return
                user_policy_del = self.__get_user_input(resp)
                policy_id = resp[user_policy_del]["id"]
                requests.delete("{0}/users/{1}/{2}".format(self.api_url, policy_type, policy_id),
                                headers=self.headers, verify=False)
                print("Successfully deleted")
        elif user_policy_choice == "List Policy Logs":
            # List policy log
            payload = {"size": 20, "start_index": 0, "action": "get"}
            resp = requests.post("{0}/users/{1}".format(self.api_url, policy_type + "_log"), headers=self.headers,
                                 verify=False, json=payload).json()["data"]
            self.__list_print_helper(resp)
        elif user_policy_choice == "Delete Policy Logs":
            # Delete policy logs
            print("Enter policy_log_id to delete")
            payload = {"size": 20, "start_index": 0, "action": "get"}
            resp = requests.post("{0}/users/{1}".format(self.api_url, policy_type + "_log"), headers=self.headers,
                                 verify=False, json=payload).json()["data"]
            if not resp:
                print("No policy logs")
                return
            user_policy_log_del = self.__get_user_input(resp)
            policy_log_id = resp[user_policy_log_del]["policy_log_id"]
            requests.delete("{0}/users/{1}/{2}".format(self.api_url, policy_type + "_log", policy_log_id),
                            headers=self.headers, verify=False)
            print("Successfully deleted")

    def __list_print_helper(self, list_items, add_new_line=False):
        for idx, list_item in enumerate(list_items):
            if type(list_item) == dict:
                print(str(idx + 1) + "  :  " + json.dumps(list_item, indent=4))
            else:
                print(str(idx + 1) + "  :  " + str(list_item))
            if add_new_line:
                print("")

    def __get_user_input(self, list_items):
        self.__list_print_helper(list_items)
        print(str(len(list_items) + 1) + "  :  " + "Exit the program")
        print("\n")
        print("Enter your choice: ")
        user_input = input("-->")
        if (int(user_input) == (len(list_items) + 1)):
            print("Exiting the program")
            exit(0)
        return int(user_input) - 1

    def start_testing(self):
        print("\n **** Initiating Deepfence API Test cases **** ")
        print("\n")
        print("Authenticating user with backend. Please wait ....... ")
        payload = {"api_key": self.api_key}
        resp = requests.post("{0}/users/auth".format(self.api_url), json=payload, headers=self.headers,
                             verify=False).json()
        if resp["success"]:
            print("Authentication successful")
        else:
            print("Authentication failed")
            exit()
        print("\n")
        self.headers["Authorization"] = "Bearer " + resp["data"]["access_token"]
        while True:
            try:
                print("\n")
                print("Available test cases are : ")
                user_choice = self.__get_user_input(self.test_choices)
                print("Now running test cases for \"" + self.test_choices[user_choice] + "\"")
                getattr(self, self.test_choice_methods[user_choice])()
            except IndexError:
                print("Wrong number entered")
            except Exception as ex:
                print("Error: {0}".format(str(ex)))
                exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_sigint)
    if len(argv) != 3:
        print("Usage:")
        print("python test_api.py \"https://<IPAddress of DeepFenceUI Machine>/deepfence/v1.3\" \"API Key\"")
    else:
        deepfence_api_test = DeepfenceAPITest(argv[1], argv[2])
        deepfence_api_test.start_testing()
