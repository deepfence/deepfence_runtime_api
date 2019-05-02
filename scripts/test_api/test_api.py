import requests
from sys import argv, maxsize
from time import sleep
import json
import signal
from collections import defaultdict
import urllib.parse as urlparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning

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
        self.node_types = ["Host", "Container", "Process", "Pod"]
        self.headers = {"Content-Type": "application/json", "Authorization": ""}
        self.test_choices = [
            "List Process, Containers & Hosts", "Alert Management", "Vulnerability Management",
            "Operations on Containers", "Capture Network Traffic", "Policy Management", "Websocket Streaming",
            "Compliance Check"]

        self.test_choice_methods = ["enumerate", "alert_management", "cve", "node_control", "packet_capture",
                                    "policy_management", "websocket_streaming", "compliance_check", "exit_program"]

    def exit_program(self):
        print("\n Exiting the test now...")
        exit(0)

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
                             json={"filters": {"type": node_types, "pseudo": False}, "size": maxsize},
                             headers=self.headers,
                             verify=False).json()
        if not resp["success"]:
            return "Error", False
        if not "data" in resp.get("data", {}):
            return "No " + ''.join(node_types) + " running", False
        return resp["data"]["data"], True

    def __get_cloud_credentials(self):
        print("Select Cloud Provider")
        cloud_types = ["AWS", "Google Cloud", "Azure"]
        user_choice = self.__get_user_input(cloud_types)
        cloud_provider = cloud_types[user_choice]
        payload = {}
        cloud_type = ""
        if cloud_provider == "AWS":
            cloud_type = "aws"
            print("Enter Instance ID, Access ID, Secret Key.(Comma Separated)")
            credentials = input("-->").split(",")
            payload = {"cloud_provider": cloud_type, "vm_instance_id": credentials[0],
                       "aws_access_id": credentials[1], "aws_secret_key": credentials[2]}
        elif cloud_provider == "Google Cloud":
            cloud_type = "gce_cloud_credentials"
        #             print("Enter Instance ID, Service Account Email, Project ID.(Comma Separated)")
        #             credentials = input("-->").split(",")
        #             print("Provide File Path for GCE Key File")
        #             key_file_path = input("-->").strip()
        #             filename = os.path.basename(key_file_path)
        #             key_file_path = "/fenced/mnt/host" + key_file_path
        #             key_file = open(key_file_path, 'r')
        #             credentials_key = str(key_file.read())
        #             payload = {"cloud_provider": cloud_type, "vm_instance_id": credentials[0],
        #                     "sa_email_address": credentials[1], "project_id": credentials[2],
        #                     "filename": filename, "credentials_key":credentials_key}
        elif cloud_provider == "Azure":
            cloud_type = "azure"
            print(
                "Enter Instance ID, Access ID, Tenant ID, Subscription ID, Application Client Key, Application Client Secret.(Comma Separated)")
            credentials = input("-->").split(",")
            payload = {"cloud_provider": cloud_type, "vm_instance_id": credentials[0],
                       "azure_tenant_id": credentials[1], "azure_subscription_id": credentials[2],
                       "azure_key": credentials[3], "azure_password": credentials[4]}
        return payload, cloud_type

    def __get_quarantine_policy_params(self):
        print(
            "Enter Alert Level(Critical,High,Medium,Low), Action(Restart,Stop,Pause), Node Type(Container,Host,Pod), Alert Count.(Comma Separated)")
        params = input("-->").split(",")
        for i in range(0, len(params)):
            params[i] = params[i].lower()
        payload = {"alert_level": params[0], "action": params[1], "node_type": params[2],
                   "alert_count_threshold": params[3]}
        return payload

    def __get_network_policy_params(self):
        print(
            "Enter Alert Level(Critical,High,Medium,Low), Block Duration(seconds. Input 0 for permanent blocking), Alert Monitoring Duration(seconds),Alert Count.(Comma Separated)")
        params = input("-->").split(",")
        for i in range(0, len(params)):
            params[i] = params[i].lower()
        payload = {"alert_level": params[0], "action": "block", "node_type": "host", "block_duration": params[1],
                   "alert_from_time": params[2], "alert_count_threshold": params[3]}
        return payload

    def __get_node_network_policy_params(self, host_name, node_policy_type):
        print(
            "Enter Node Type(Container,Host,Pod), Block Duration(seconds. Input 0 for permanent blocking), Packet Direction(Inbound,Outbound)")
        params = input("-->").split(",")
        print("Enter IP Address List(2.2.2.2,55.65.76.87)")
        ip_address_list = input("-->").split(",")
        print("Enter Port List (8080,9000)")
        port_list = input("-->").split(",")
        for i in range(0, len(params)):
            params[i] = params[i].lower()

        payload = {"action": "block", "host_name": host_name, "node_type": params[0], "block_duration": params[1],
                   "node_policy_type": node_policy_type, "packet_direction": params[2],
                   "ip_address_list": ip_address_list, "port_list": port_list}
        return payload

    def enumerate(self):
        user_choice = self.__get_user_input(self.node_types)
        data, success = self.__enumerate_helper([self.node_types[user_choice].lower()])
        if not success:
            print(data)
            return
        self.__list_print_helper(list(self.__dump_nodes(data).values()), add_new_line=True)

    def websocket_streaming(self):
        print("Run following command:\n")
        url_parsed = urlparse.urlparse(self.api_url)
        print(
            "docker run --rm -it --name=deepfence_test_api deepfenceio/deepfence_test_api go run /app/websocket_streaming.go -api_url \"{0}\" -api_key \"{1}\" -node_type \"host\"".format(url_parsed.netloc, self.api_key))

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
        for container_data_value in container_data_values:
            container_prompt.append(container_data_value + " (" + container_data_value + ")")
        print("\nChoose a container to perform actions on it")
        container_idx = self.__get_user_input(container_prompt)
        print("\nChoose an action to be performed on this container")
        action_idx = self.__get_user_input(container_action_values)
        container_id = data_keys[container_idx]
        if (container_action_values[action_idx] == "Stop"):
            print("Now stopping the container. Please wait.....")
            resp = requests.post("{0}/node/{1}/stop".format(self.api_url, container_id), json={}, headers=self.headers,
                                 verify=False).json()
            sleep(5)
            self.__print_resp(resp)
            # self.__dump_resp_to_file("stop_container_" + container_data_values[container_idx], resp)
        elif (container_action_values[action_idx] == "Pause"):
            print("Now pausing the container. Please wait.....")
            resp = requests.post("{0}/node/{1}/pause".format(self.api_url, container_id), json={}, headers=self.headers,
                                 verify=False).json()
            sleep(5)
            self.__print_resp(resp)
            # Storing response in file not required
            # self.__dump_resp_to_file("pause_container_" + container_data_values[container_idx], resp)
        elif (container_action_values[action_idx] == "Un-Pause"):
            print("Now doing un-pause on the the container. Please wait....")
            resp = requests.post("{0}/node/{1}/unpause".format(self.api_url, container_id), json={},
                                 headers=self.headers, verify=False).json()
            sleep(5)
            self.__print_resp(resp)
            # Storing response in file not required
            # self.__dump_resp_to_file("un-pause_container_" + container_data_values[container_idx], resp)
        elif (container_action_values[action_idx] == "Start"):
            resp = requests.post("{0}/node/{1}/start".format(self.api_url, container_id), json={}, headers=self.headers,
                                 verify=False).json()
            sleep(5)
            self.__print_resp(resp)
            # Storing response in file not required
            # self.__dump_resp_to_file("start_container_" + container_data_values[container_idx], resp)

    def cve(self):
        node_action_values = ["Start-CVE", "Stop-CVE", "List Detected Vulnerabilities"]
        data, success = self.__enumerate_helper(["container", "host"])
        if not success:
            print(data)
            return
        data = self.__dump_nodes(data)
        data_keys = list(data.keys())
        tmp_data_values = list(data.values())
        node_data_values = []
        node_data_state = []
        image_name_list = []
        for i in range(0, len(tmp_data_values)):
            json_val = json.loads(tmp_data_values[i])
            node_name = json_val["host_name"]
            image_name = json_val.get("image_name")
            image_tag = json_val.get("image_tag")
            if image_name and image_tag:
                image_name_list.append(image_name + ":" + image_tag)
            else:
                image_name_list.append(node_name)
            container_name = json_val.get("container_name", "")
            if container_name:
                node_name = container_name + " ( HOST : " + node_name + " )"
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
            node_prompt.append(node_data_values[i] + " ( STATUS : " + node_data_state[i] + " )")
        print("\nChoose a node to perform actions on it")
        node_idx = self.__get_user_input(node_prompt)
        print("\nChoose an action to be performed on this node")
        action_idx = self.__get_user_input(node_action_values)
        node_id = data_keys[node_idx]
        node_name = node_data_values[node_idx]
        if (node_action_values[action_idx] == "Start-CVE"):
            print("Now starting CVE. Please wait.....")
            resp = requests.post("{0}/node/{1}/cve_scan_start".format(self.api_url, node_id), json={},
                                 headers=self.headers, verify=False).json()
            sleep(10)
            self.__print_resp(resp)
            # Storing response in file not required
            # self.__dump_resp_to_file("start_cve_" + node_data_values[action_idx], resp)
        elif (node_action_values[action_idx] == "Stop-CVE"):
            print("Now stopping CVE. Please wait.....")

            resp = requests.post("{0}/node/{1}/cve_scan_stop".format(self.api_url, node_id), json={},
                                 headers=self.headers, verify=False).json()
            sleep(10)
            self.__print_resp(resp)
            # Storing response in file not required
            # self.__dump_resp_to_file("stop_cve_" + node_data_values[action_idx], resp)
        elif (node_action_values[action_idx] == "List Detected Vulnerabilities"):
            print("Retrieving detected vulnerabilities. Please wait...")
            image_name = image_name_list[node_idx]
            resp = requests.post("{0}/vulnerability".format(self.api_url),
                                 json={"filters": {"cve_container_image": [image_name]}},
                                 headers=self.headers, verify=False).json()
            if resp["data"]:
                print(json.dumps(resp["data"], indent=4))
            else:
                print("No Vulnerabilities found")

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
            print("Initiating " + pkt_cpt_keys[user_choice] + ". Please wait.....")
            resp = requests.post("{0}/node/{1}/{2}".format(self.api_url, node_id, action), json={},
                                 headers=self.headers, verify=False).json()
        print(json.dumps(resp, indent=4))

    def alert_management(self):
        print("\nAlerts by host/container\n")
        host_alerts = defaultdict(dict)
        resp = requests.post("{0}/alerts".format(self.api_url),
                             json={"filters": {}, "action": "get", "start_index": 0, "size": 10000},
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
        cloud_credentials_api = "Cloud Credentials"
        policy_type_choices = [quar_policy, net_policy, node_blacklist_policy, node_whitelist_policy,
                               cloud_credentials_api]
        policy_type_api_path = ["quarantine_protection_policy", "network_protection_policy",
                                "blacklist_node_network_protection_policy", "whitelist_node_network_protection_policy",
                                "cloud_credentials"]
        user_policy_type_choice = self.__get_user_input(policy_type_choices)
        policy_type = policy_type_api_path[user_policy_type_choice]
        policy_choices = ["Add", "List", "Delete", "List Policy Logs", "Delete Policy Logs"]
        if policy_type.startswith("blacklist_") or policy_type.startswith("whitelist_") or policy_type.startswith(
                "cloud_"):
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
        no_data_msg = "No policies found"
        if policy_type.startswith("cloud_"):
            no_data_msg = "No credentials found"
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
                payload = self.__get_quarantine_policy_params()
            elif policy_type == "network_protection_policy":
                payload = self.__get_network_policy_params()
            elif node_policy_type == "blacklist":
                host_name = hosts_data[user_choice_host]
                payload = self.__get_node_network_policy_params(host_name, node_policy_type)
            elif node_policy_type == "whitelist":
                host_name = hosts_data[user_choice_host]
                payload = self.__get_node_network_policy_params(host_name, node_policy_type)
            elif policy_type == "cloud_credentials":
                payload, cloud_provider = self.__get_cloud_credentials()
                if cloud_provider == "gce_cloud_credentials":
                    print("Google Cloud Engine is not supported in this test program.")
                    return
                api_url += "/" + cloud_provider
            else:
                return
            resp = requests.post(api_url, headers=self.headers, verify=False, json=payload).json()
            print(json.dumps(resp, indent=4))
        elif user_policy_choice == "List":
            # List policies
            resp = requests.get(api_url, headers=self.headers, verify=False).json()
            if not resp["data"]:
                print(no_data_msg)
            else:
                resp = resp["data"][policy_type.replace("policy", "policies")]
                if not resp:
                    print(no_data_msg)
                self.__list_print_helper(resp)
        elif user_policy_choice == "Delete":
            # Delete policy
            print("Enter serial number to delete")
            resp = requests.get(api_url, headers=self.headers, verify=False).json()
            if not resp["data"]:
                print(no_data_msg)
                return
            else:
                resp = resp["data"][policy_type.replace("policy", "policies")]
                if not resp:
                    print(no_data_msg)
                    return
                user_policy_del = self.__get_user_input(resp)
                policy_id = resp[user_policy_del]["id"]
                if policy_type.startswith("cloud_"):
                    cloud_provider = resp[user_policy_del]["cloud_provider"]
                    policy_id = cloud_provider + '/' + str(policy_id)
                requests.delete("{0}/users/{1}/{2}".format(self.api_url, policy_type, policy_id),
                                headers=self.headers, verify=False)
                print("Successfully deleted")
        elif user_policy_choice == "List Policy Logs":
            # List policy log
            payload = {"size": 20, "start_index": 0, "action": "get"}
            resp = requests.post("{0}/users/{1}".format(self.api_url, policy_type + "_log"), headers=self.headers,
                                 verify=False, json=payload).json()["data"]
            if not resp:
                print("No policy logs found")
                return
            self.__list_print_helper(resp)
        elif user_policy_choice == "Delete Policy Logs":
            # Delete policy logs
            print("Enter serial number to delete")
            payload = {"size": 20, "start_index": 0, "action": "get"}
            resp = requests.post("{0}/users/{1}".format(self.api_url, policy_type + "_log"), headers=self.headers,
                                 verify=False, json=payload).json()["data"]
            if not resp:
                print("No policy logs found")
                return
            user_policy_log_del = self.__get_user_input(resp)
            policy_log_id = resp[user_policy_log_del]["policy_log_id"]
            requests.delete("{0}/users/{1}/{2}".format(self.api_url, policy_type + "_log", policy_log_id),
                            headers=self.headers, verify=False)
            print("Successfully deleted")

    def compliance_check(self):
        print("\nChoose whether Host or Container")
        node_types = ["Host", "Container"]
        node_choice = self.__get_user_input(node_types)

        if (node_types[node_choice] == "Host"):
            self.compliance_check_by_node_type("host")
        elif (node_types[node_choice] == "Container"):
            # TODO: to be implemented
            self.compliance_check_by_node_type("container")

    def compliance_check_by_node_type(self, node_type):
        data, success = self.__enumerate_helper([node_type])
        if not success:
            print(data)
            return
        data = self.__dump_nodes(data)
        data_keys = list(data.keys())
        data_values = list(data.values())
        host_names = []
        for values in data_values:
            dict_values = json.loads(values)
            for key, val in dict_values.items():
                if node_type == "host":
                    if key.lower() == "host_name":
                        host_names.append(val)
                elif node_type == "container":
                    if key.lower() == "container_name":
                        host_names.append(val)
        if node_type == "host":
            print("\nEnter host number")
        elif node_type == "container":
            print("\nEnter container number")
        user_choice = self.__get_user_input(host_names)
        node_id = data_keys[user_choice]
        resp = requests.get("{0}/node/{1}/applicable_compliance_scans".format(self.api_url, node_id),
                            headers=self.headers, verify=False).json()
        if not resp.get("data"):
            print("\nNo compliance scans available for this node")
            return
        print("\nChoose any of the available compliance types")
        list_compliances = json.loads(json.dumps(resp["data"]["complianceScanLists"], indent=4))
        compliance_labels = []
        compliance_codes = []
        for compliances in list_compliances:
            for key, val in compliances.items():
                if key.lower() == "code":
                    compliance_codes.append(val)
                elif key.lower() == "label":
                    compliance_labels.append(val)
        compliance_status = []
        for code in compliance_codes:
            resp = requests.get("{0}/compliance/{1}/{2}/scan_status".format(self.api_url, node_id, code),
                                headers=self.headers, verify=False).json()
            if resp.get("data"):
                compliance_status.append(json.dumps(resp["data"]["scan_status"]).strip('\"') + " at " + json.dumps(
                    resp["data"]["@timestamp"]).strip('\"'))
            else:
                compliance_status.append("NOT SCANNED")

        compliance_detailed_labels = []
        for i in range(len(compliance_labels)):
            compliance_detailed_labels.append(compliance_labels[i] + " (" + compliance_status[i] + ")")
        compliance_choice = self.__get_user_input(compliance_detailed_labels)
        compliance_actions = ["Start Compliance Scan", "Get Status Logs of Previous Scan"]
        print("\nChoose an action for the particular compliance type")
        compliance_action_choice = self.__get_user_input(compliance_actions)
        if (compliance_actions[compliance_action_choice] == "Start Compliance Scan"):
            body = {"compliance_check_type": compliance_codes[compliance_choice]}
            resp = requests.post("{0}/node/{1}/start_compliance_scan".format(self.api_url, node_id),
                                 headers=self.headers, data=json.dumps(body), verify=False).json()
            if resp.get("data"):
                print("\n" + json.dumps(resp["data"]["complianceCheck"], indent=4))
            else:
                print("\nError " + json.dumps(resp["error"]) + " while starting compliance scan.")
        elif (compliance_actions[compliance_action_choice] == "Get Status Logs of Previous Scan"):
            code_id = compliance_codes[compliance_choice]
            print("\nStatus logs of the previous scan")
            resp = requests.get("{0}/compliance/{1}/{2}/scan_status".format(self.api_url, node_id, code_id),
                                headers=self.headers, verify=False).json()
            if resp.get("data"):
                print("\n" + json.dumps(resp["data"], indent=4))
            else:
                print("\nThe node has not been scanned previously for this compliance type")

    def __list_print_helper(self, list_items, add_new_line=False):
        for idx, list_item in enumerate(list_items):
            if type(list_item) == dict:
                print(str(idx + 1) + "  :  " + json.dumps(list_item, indent=4))
            else:
                print(str(idx + 1) + "  :  " + str(list_item))
            if add_new_line:
                print("")

    def __main_menu(self):
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

    def __get_user_input(self, list_items):
        self.__list_print_helper(list_items)
        print(str(len(list_items) + 1) + "  :  " + "Exit this menu")
        print("\n")
        print("Enter your choice: ")
        user_input = ""
        while not user_input:
            user_input = input("-->")
        # If user is at main menu and presses exit button, exit the program else take user back to main menu.
        if (self.test_choices[0] == list_items[0] and int(user_input) == (len(list_items) + 1)):
            self.exit_program()
        if (int(user_input) == (len(list_items) + 1)):
            self.__main_menu()
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
            self.__main_menu()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_sigint)
    if len(argv) != 3:
        print("Usage:")
        print("python test_api.py \"https://<IPAddress of DeepFenceUI Machine>/deepfence/v1.5\" \"API Key\"")
    else:
        deepfence_api_test = DeepfenceAPITest(argv[1], argv[2])
        deepfence_api_test.start_testing()
