## Node Tags

Example scripts to apply tags for some nodes (eg: prod) and run vulnerability scan for nodes with tag=prod

1. `add_tag_to_nodes.py`

Run it
```shell script
python3 add_tag_to_nodes.py <mgmt_console_ip_address> <api_key>
```
`api_key` can be found here in UI: `Settings` => `User Management`

- Enter `tag` you want to add. Eg: `prod`
- Enter comma separated list of node numbers you want to apply above `tag`

2. `start_vulnerability_scan_for_tag.py`

Filter nodes by tag=prod and run vulnerability scan for those nodes
```shell script
python3 start_vulnerability_scan_for_tag.py <mgmt_console_ip_address> <api_key>
```
- Enter the same `tag` you entered in above step. Eg: `prod`
- Enter comma separated list of node numbers to run vulnerability scan