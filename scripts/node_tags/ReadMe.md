## Node Tags

Example scripts to apply tags for some nodes (eg: prod) and run vulnerability scan for nodes with tag=prod

1. `add_tag_to_nodes.py`

Change this map and add hosts you want to tag as `prod`
```python
hosts_to_tag = {
    "prod1": ["prod"],
    "prod2": ["prod"],
    "prod3": ["prod"],
    "prod4": ["prod"],
    "prod5": ["prod"],
}
```

2. `start_vulnerability_scan_for_tag.py`

Filter nodes by tag=prod and run vulnerability scan for those nodes
```python
enumerate_filters = {
    "type": ["host", "container"],
    "tags": ["prod"],
    "pseudo": False
}
```