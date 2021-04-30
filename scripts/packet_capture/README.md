Packet Capture API

* Get the list of processes running across all agents.

```
python3 get_process_list.py <management_console_IP_address> <API_key>

Parameters:

management_console_IP_address: IP address of management console

API_key: API key

Output: 

['nginx', 'java']

```

* Start packet capture on all/selected agents.

```
python3 start_packet_capture_for_processes.py <management_console_IP_address> <API_key> <process_names> <pcap_mode>

Parameters:

management_console_IP_address: IP address of management console.

API_key: API key

process_names: comma separated string of process names chosen from step 1 (eg. 'nginx, java, python')

pcap_mode: either 'allow', 'deny' or 'all'. 'allow' mode is the preferred mode.

'allow' means allow the processes in the process list
'deny' means deny the processes in the process list
'all' means run packet capture on all processes

```

* Stop packet capture on all/selected agents.

```
python3 stop_packet_capture_for_processes.py <management_console_IP_address> <API_key>

Parameters:

management_console_IP_address: IP address of management console

API_key: API key


```
