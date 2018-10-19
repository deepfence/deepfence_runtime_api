# Deepfencev15enumerateFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **list[str]** | Container name (for type &#x60;container&#x60;, &#x60;container_image&#x60;) | [optional] 
**host_name** | **list[str]** | Host names | [optional] 
**image_name** | **list[str]** | Container image names (for type &#x60;container&#x60;, &#x60;container_image&#x60;) | [optional] 
**interface_names** | **list[str]** | Interface names (for type &#x60;host&#x60;) | [optional] 
**kernel_version** | **list[str]** | Kernel version (for type &#x60;host&#x60;) | [optional] 
**kubernetes_namespace** | **list[str]** | kubernetes namespace (for type &#x60;pod&#x60;, &#x60;kube_controller&#x60;, &#x60;kube_service&#x60;). Empty means all. | [optional] 
**kubernetes_node_type** | **list[str]** | kubernetes node type (for type &#x60;kube_controller&#x60;) | [optional] 
**local_networks** | **list[str]** | Local networks in CIDR format (for type &#x60;host&#x60;) | [optional] 
**os** | **list[str]** | Operating system (for type &#x60;host&#x60;) | [optional] 
**packet_capture** | **list[str]** | Packet capture state (for type &#x60;host&#x60;) | [optional] 
**pid** | **int** | Process ID (for type &#x60;process&#x60;) | [optional] 
**ppid** | **int** | Parent process ID (for type &#x60;process&#x60;) | [optional] 
**pseudo** | **list[bool]** | Pseudo node or not | [optional] 
**public_ip_address** | **list[str]** | Public IP of host (for type &#x60;host&#x60;) | [optional] 
**type** | **list[str]** | Types of node | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


