Packet Capture API

* Get the list of processes running across all agents.

```
python3 get_process_list.py <management_console_IP_address> <API_key>

Output: ['nginx', 'java']

```

* Start packet capture on all/selected agents.

```
python3 start_packet_capture_for_processes.py <management_console_IP_address> <API_key> <comma_separated_string_containing_process_names> <pcap_mode>

pcap_mode is either 'allow', 'deny' or 'all'.
process_names include the process names chosen from step 1

```

* Stop packet capture on all/selected agents.

```
python3 stop_packet_capture_for_processes.py <management_console_IP_address> <API_key>

```
