# \NodeControlApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**NodeDetails**](NodeControlApi.md#NodeDetails) | **Get** /deepfence/v1.5/node/{node_id} | Node Details API
[**PacketCaptureStatus**](NodeControlApi.md#PacketCaptureStatus) | **Get** /deepfence/v1.5/node/{node_id}/packet_capture_status | Node Control API - Packet Capture Status
[**PauseNode**](NodeControlApi.md#PauseNode) | **Post** /deepfence/v1.5/node/{node_id}/pause | Node Control API - Pause Node
[**RestartNode**](NodeControlApi.md#RestartNode) | **Post** /deepfence/v1.5/node/{node_id}/restart | Node Control API - Restart Node
[**ScaleDown**](NodeControlApi.md#ScaleDown) | **Post** /deepfence/v1.5/node/{node_id}/kubernetes_scale_down | Node Control API - Scale Down
[**ScaleUp**](NodeControlApi.md#ScaleUp) | **Post** /deepfence/v1.5/node/{node_id}/kubernetes_scale_up | Node Control API - Scale Up
[**StartNode**](NodeControlApi.md#StartNode) | **Post** /deepfence/v1.5/node/{node_id}/start | Node Control API - Start Node
[**StartPacketCapture**](NodeControlApi.md#StartPacketCapture) | **Post** /deepfence/v1.5/node/{node_id}/packet_capture_start | Node Control - Start Packet Capture
[**StopNode**](NodeControlApi.md#StopNode) | **Post** /deepfence/v1.5/node/{node_id}/stop | Node Control API - Stop Node
[**StopPacketCapture**](NodeControlApi.md#StopPacketCapture) | **Post** /deepfence/v1.5/node/{node_id}/packet_capture_stop | Node Control API - Stop Packet Capture
[**UnpauseNode**](NodeControlApi.md#UnpauseNode) | **Post** /deepfence/v1.5/node/{node_id}/unpause | Node Control API - Unpause Node


# **NodeDetails**
> NodeDetails(ctx, nodeId)
Node Details API

Get full details of a node (hosts, containers, images, processes) by node_id

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PacketCaptureStatus**
> PacketCaptureStatus(ctx, nodeId)
Node Control API - Packet Capture Status

Packet Capture Status for a node (Applicable node type - `host`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PauseNode**
> PauseNode(ctx, nodeId, optional)
Node Control API - Pause Node

Pause a node (Applicable node type - `container`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeId** | **string**| Node ID (refer enumerate api) | 
 **options** | [**interface{}**](interface{}.md)| Options (if applicable) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **RestartNode**
> RestartNode(ctx, nodeId, optional)
Node Control API - Restart Node

Restart a node (Applicable node type - `container`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeId** | **string**| Node ID (refer enumerate api) | 
 **options** | [**interface{}**](interface{}.md)| Options (if applicable) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ScaleDown**
> ScaleDown(ctx, nodeId)
Node Control API - Scale Down

Scale down kubernetes deployments (Applicable node type - `kube_controllers` with kubernetes_node_type is Deployment or ReplicaSet)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ScaleUp**
> ScaleUp(ctx, nodeId)
Node Control API - Scale Up

Scale up kubernetes deployments (Applicable node type - `kube_controllers` with kubernetes_node_type is Deployment or ReplicaSet)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StartNode**
> StartNode(ctx, nodeId, optional)
Node Control API - Start Node

Start a node (Applicable node type - `container`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeId** | **string**| Node ID (refer enumerate api) | 
 **options** | [**interface{}**](interface{}.md)| Options (if applicable) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StartPacketCapture**
> StartPacketCapture(ctx, nodeId, optional)
Node Control - Start Packet Capture

Start Packet Capture on a node (Applicable node type - `host`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeId** | **string**| Node ID (refer enumerate api) | 
 **options** | [**Options4**](Options4.md)| Options to start packet capture | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StopNode**
> StopNode(ctx, nodeId, optional)
Node Control API - Stop Node

Stop a node (Applicable node type - `container`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeId** | **string**| Node ID (refer enumerate api) | 
 **options** | [**interface{}**](interface{}.md)| Options (if applicable) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StopPacketCapture**
> StopPacketCapture(ctx, nodeId, optional)
Node Control API - Stop Packet Capture

Stop Packet Capture on a node (Applicable node type - `host`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeId** | **string**| Node ID (refer enumerate api) | 
 **options** | [**interface{}**](interface{}.md)| Options (if applicable) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UnpauseNode**
> UnpauseNode(ctx, nodeId, optional)
Node Control API - Unpause Node

Unpause a node (Applicable node type - `container`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeId** | **string**| Node ID (refer enumerate api) | 
 **options** | [**interface{}**](interface{}.md)| Options (if applicable) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

