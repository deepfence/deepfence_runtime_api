# deepfence_runtime_api.EnumerateApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_api**](EnumerateApi.md#data_api) | **POST** /deepfence/v1.3/data | Data API
[**enumerate_nodes**](EnumerateApi.md#enumerate_nodes) | **POST** /deepfence/v1.3/enumerate | Enumerate API
[**status_api**](EnumerateApi.md#status_api) | **POST** /deepfence/v1.3/status | Status API


# **data_api**
> data_api(options=options)

Data API

Get data of a previous request by status_id

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
api_instance = deepfence_runtime_api.EnumerateApi(deepfence_runtime_api.ApiClient(configuration))
options = deepfence_runtime_api.Options1() # Options1 | Options (optional)

try:
    # Data API
    api_instance.data_api(options=options)
except ApiException as e:
    print("Exception when calling EnumerateApi->data_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options1**](Options1.md)| Options | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumerate_nodes**
> enumerate_nodes(options=options)

Enumerate API

Enumerate nodes (hosts, containers, images, processes) with optional filters

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
api_instance = deepfence_runtime_api.EnumerateApi(deepfence_runtime_api.ApiClient(configuration))
options = deepfence_runtime_api.Options2() # Options2 | Options to enumerate nodes (optional)

try:
    # Enumerate API
    api_instance.enumerate_nodes(options=options)
except ApiException as e:
    print("Exception when calling EnumerateApi->enumerate_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options2**](Options2.md)| Options to enumerate nodes | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_api**
> status_api(options=options)

Status API

Get status of a previous request by status_id

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
api_instance = deepfence_runtime_api.EnumerateApi(deepfence_runtime_api.ApiClient(configuration))
options = deepfence_runtime_api.Options4() # Options4 | Options (optional)

try:
    # Status API
    api_instance.status_api(options=options)
except ApiException as e:
    print("Exception when calling EnumerateApi->status_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options4**](Options4.md)| Options | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

