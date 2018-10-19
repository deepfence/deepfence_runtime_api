# deepfence_runtime_api.AlertManagementApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alert**](AlertManagementApi.md#delete_alert) | **DELETE** /deepfence/v1.5/alerts/{alert_id} | Delete an alert by alert_id
[**find_alerts**](AlertManagementApi.md#find_alerts) | **POST** /deepfence/v1.5/alerts | Get/Delete alerts by filter
[**get_alert**](AlertManagementApi.md#get_alert) | **GET** /deepfence/v1.5/alerts/{alert_id} | Get alert by given alert_id
[**get_node_severity**](AlertManagementApi.md#get_node_severity) | **GET** /deepfence/v1.5/node-severities | Get the severity of all nodes


# **delete_alert**
> delete_alert(alert_id)

Delete an alert by alert_id

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
api_instance = deepfence_runtime_api.AlertManagementApi(deepfence_runtime_api.ApiClient(configuration))
alert_id = 'alert_id_example' # str | 

try:
    # Delete an alert by alert_id
    api_instance.delete_alert(alert_id)
except ApiException as e:
    print("Exception when calling AlertManagementApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_alerts**
> find_alerts(options=options)

Get/Delete alerts by filter

Get/Delete alerts by filter

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
api_instance = deepfence_runtime_api.AlertManagementApi(deepfence_runtime_api.ApiClient(configuration))
options = deepfence_runtime_api.Options() # Options | Options to get or delete alerts (optional)

try:
    # Get/Delete alerts by filter
    api_instance.find_alerts(options=options)
except ApiException as e:
    print("Exception when calling AlertManagementApi->find_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options**](Options.md)| Options to get or delete alerts | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> get_alert(alert_id)

Get alert by given alert_id

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
api_instance = deepfence_runtime_api.AlertManagementApi(deepfence_runtime_api.ApiClient(configuration))
alert_id = 'alert_id_example' # str | Alert ID

try:
    # Get alert by given alert_id
    api_instance.get_alert(alert_id)
except ApiException as e:
    print("Exception when calling AlertManagementApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**| Alert ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_severity**
> get_node_severity()

Get the severity of all nodes

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
api_instance = deepfence_runtime_api.AlertManagementApi(deepfence_runtime_api.ApiClient(configuration))

try:
    # Get the severity of all nodes
    api_instance.get_node_severity()
except ApiException as e:
    print("Exception when calling AlertManagementApi->get_node_severity: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

