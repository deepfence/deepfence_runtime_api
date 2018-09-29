# deepfence_runtime_api.NodeControlApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**node_details**](NodeControlApi.md#node_details) | **GET** /deepfence/v1.3/node/{node_id} | Node Details API
[**packet_capture_status**](NodeControlApi.md#packet_capture_status) | **GET** /deepfence/v1.3/node/{node_id}/packet_capture_status | Node Control API - Packet Capture Status
[**pause_node**](NodeControlApi.md#pause_node) | **POST** /deepfence/v1.3/node/{node_id}/pause | Node Control API - Pause Node
[**restart_node**](NodeControlApi.md#restart_node) | **POST** /deepfence/v1.3/node/{node_id}/restart | Node Control API - Restart Node
[**scale_down**](NodeControlApi.md#scale_down) | **POST** /deepfence/v1.3/node/{node_id}/kubernetes_scale_down | Node Control API - Scale Down
[**scale_up**](NodeControlApi.md#scale_up) | **POST** /deepfence/v1.3/node/{node_id}/kubernetes_scale_up | Node Control API - Scale Up
[**start_node**](NodeControlApi.md#start_node) | **POST** /deepfence/v1.3/node/{node_id}/start | Node Control API - Start Node
[**start_packet_capture**](NodeControlApi.md#start_packet_capture) | **POST** /deepfence/v1.3/node/{node_id}/packet_capture_start | Node Control - Start Packet Capture
[**stop_node**](NodeControlApi.md#stop_node) | **POST** /deepfence/v1.3/node/{node_id}/stop | Node Control API - Stop Node
[**stop_packet_capture**](NodeControlApi.md#stop_packet_capture) | **POST** /deepfence/v1.3/node/{node_id}/packet_capture_stop | Node Control API - Stop Packet Capture
[**unpause_node**](NodeControlApi.md#unpause_node) | **POST** /deepfence/v1.3/node/{node_id}/unpause | Node Control API - Unpause Node


# **node_details**
> node_details(node_id)

Node Details API

Get full details of a node (hosts, containers, images, processes) by node_id

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)

try:
    # Node Details API
    api_instance.node_details(node_id)
except ApiException as e:
    print("Exception when calling NodeControlApi->node_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packet_capture_status**
> packet_capture_status(node_id)

Node Control API - Packet Capture Status

Packet Capture Status for a node (Applicable node type - `host`)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)

try:
    # Node Control API - Packet Capture Status
    api_instance.packet_capture_status(node_id)
except ApiException as e:
    print("Exception when calling NodeControlApi->packet_capture_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_node**
> pause_node(node_id, options=options)

Node Control API - Pause Node

Pause a node (Applicable node type - `container`)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
options = NULL # object | Options (if applicable) (optional)

try:
    # Node Control API - Pause Node
    api_instance.pause_node(node_id, options=options)
except ApiException as e:
    print("Exception when calling NodeControlApi->pause_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **options** | **object**| Options (if applicable) | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_node**
> restart_node(node_id, options=options)

Node Control API - Restart Node

Restart a node (Applicable node type - `container`)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
options = NULL # object | Options (if applicable) (optional)

try:
    # Node Control API - Restart Node
    api_instance.restart_node(node_id, options=options)
except ApiException as e:
    print("Exception when calling NodeControlApi->restart_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **options** | **object**| Options (if applicable) | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scale_down**
> scale_down(node_id)

Node Control API - Scale Down

Scale down kubernetes deployments (Applicable node type - `kube_controllers` with kubernetes_node_type is Deployment or ReplicaSet)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)

try:
    # Node Control API - Scale Down
    api_instance.scale_down(node_id)
except ApiException as e:
    print("Exception when calling NodeControlApi->scale_down: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scale_up**
> scale_up(node_id)

Node Control API - Scale Up

Scale up kubernetes deployments (Applicable node type - `kube_controllers` with kubernetes_node_type is Deployment or ReplicaSet)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)

try:
    # Node Control API - Scale Up
    api_instance.scale_up(node_id)
except ApiException as e:
    print("Exception when calling NodeControlApi->scale_up: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_node**
> start_node(node_id, options=options)

Node Control API - Start Node

Start a node (Applicable node type - `container`)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
options = NULL # object | Options (if applicable) (optional)

try:
    # Node Control API - Start Node
    api_instance.start_node(node_id, options=options)
except ApiException as e:
    print("Exception when calling NodeControlApi->start_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **options** | **object**| Options (if applicable) | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_packet_capture**
> start_packet_capture(node_id, options=options)

Node Control - Start Packet Capture

Start Packet Capture on a node (Applicable node type - `host`)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
options = deepfence_runtime_api.Options4() # Options4 | Options to start packet capture (optional)

try:
    # Node Control - Start Packet Capture
    api_instance.start_packet_capture(node_id, options=options)
except ApiException as e:
    print("Exception when calling NodeControlApi->start_packet_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **options** | [**Options4**](Options4.md)| Options to start packet capture | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_node**
> stop_node(node_id, options=options)

Node Control API - Stop Node

Stop a node (Applicable node type - `container`)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
options = NULL # object | Options (if applicable) (optional)

try:
    # Node Control API - Stop Node
    api_instance.stop_node(node_id, options=options)
except ApiException as e:
    print("Exception when calling NodeControlApi->stop_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **options** | **object**| Options (if applicable) | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_packet_capture**
> stop_packet_capture(node_id, options=options)

Node Control API - Stop Packet Capture

Stop Packet Capture on a node (Applicable node type - `host`)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
options = NULL # object | Options (if applicable) (optional)

try:
    # Node Control API - Stop Packet Capture
    api_instance.stop_packet_capture(node_id, options=options)
except ApiException as e:
    print("Exception when calling NodeControlApi->stop_packet_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **options** | **object**| Options (if applicable) | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpause_node**
> unpause_node(node_id, options=options)

Node Control API - Unpause Node

Unpause a node (Applicable node type - `container`)

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = deepfence_runtime_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = deepfence_runtime_api.NodeControlApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
options = NULL # object | Options (if applicable) (optional)

try:
    # Node Control API - Unpause Node
    api_instance.unpause_node(node_id, options=options)
except ApiException as e:
    print("Exception when calling NodeControlApi->unpause_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **options** | **object**| Options (if applicable) | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

