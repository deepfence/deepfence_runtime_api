# Deepfencev13enumerateFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ContainerName** | **[]string** | Container name (for type &#x60;container&#x60;, &#x60;container_image&#x60;) | [optional] [default to null]
**HostName** | **[]string** | Host names | [optional] [default to null]
**ImageName** | **[]string** | Container image names (for type &#x60;container&#x60;, &#x60;container_image&#x60;) | [optional] [default to null]
**InterfaceNames** | **[]string** | Interface names (for type &#x60;host&#x60;) | [optional] [default to null]
**KernelVersion** | **[]string** | Kernel version (for type &#x60;host&#x60;) | [optional] [default to null]
**KubernetesNamespace** | **[]string** | kubernetes namespace (for type &#x60;pod&#x60;, &#x60;kube_controller&#x60;, &#x60;kube_service&#x60;). Empty means all. | [optional] [default to null]
**KubernetesNodeType** | **[]string** | kubernetes node type (for type &#x60;kube_controller&#x60;) | [optional] [default to null]
**LocalNetworks** | **[]string** | Local networks in CIDR format (for type &#x60;host&#x60;) | [optional] [default to null]
**Os** | **[]string** | Operating system (for type &#x60;host&#x60;) | [optional] [default to null]
**PacketCapture** | **[]string** | Packet capture state (for type &#x60;host&#x60;) | [optional] [default to null]
**Pid** | **int32** | Process ID (for type &#x60;process&#x60;) | [optional] [default to null]
**Ppid** | **int32** | Parent process ID (for type &#x60;process&#x60;) | [optional] [default to null]
**Pseudo** | **[]bool** | Pseudo node or not | [optional] [default to null]
**PublicIpAddress** | **[]string** | Public IP of host (for type &#x60;host&#x60;) | [optional] [default to null]
**Type_** | **[]string** | Types of node | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


