# deepfence_runtime_api.NetworkProtectionPolicyLogsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_network_protection_policy_log**](NetworkProtectionPolicyLogsApi.md#delete_network_protection_policy_log) | **DELETE** /deepfence/v1.3/users/network_protection_policy_log/{policy_log_id} | Delete network protection policy log by policy_log_id
[**find_network_protection_policy_logs**](NetworkProtectionPolicyLogsApi.md#find_network_protection_policy_logs) | **POST** /deepfence/v1.3/users/network_protection_policy_log | Get/Delete network protection policy logs by filter
[**get_network_protection_policy_log**](NetworkProtectionPolicyLogsApi.md#get_network_protection_policy_log) | **GET** /deepfence/v1.3/users/network_protection_policy_log/{policy_log_id} | Get network protection policy log by given policy_log_id


# **delete_network_protection_policy_log**
> delete_network_protection_policy_log(policy_log_id)

Delete network protection policy log by policy_log_id

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
api_instance = deepfence_runtime_api.NetworkProtectionPolicyLogsApi(deepfence_runtime_api.ApiClient(configuration))
policy_log_id = 'policy_log_id_example' # str | 

try:
    # Delete network protection policy log by policy_log_id
    api_instance.delete_network_protection_policy_log(policy_log_id)
except ApiException as e:
    print("Exception when calling NetworkProtectionPolicyLogsApi->delete_network_protection_policy_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_log_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_network_protection_policy_logs**
> find_network_protection_policy_logs(options=options)

Get/Delete network protection policy logs by filter

Get/Delete network protection policy logs by filter

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
api_instance = deepfence_runtime_api.NetworkProtectionPolicyLogsApi(deepfence_runtime_api.ApiClient(configuration))
options = deepfence_runtime_api.Options7() # Options7 | Options to get or delete policy logs (optional)

try:
    # Get/Delete network protection policy logs by filter
    api_instance.find_network_protection_policy_logs(options=options)
except ApiException as e:
    print("Exception when calling NetworkProtectionPolicyLogsApi->find_network_protection_policy_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options7**](Options7.md)| Options to get or delete policy logs | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_protection_policy_log**
> get_network_protection_policy_log(policy_log_id)

Get network protection policy log by given policy_log_id

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
api_instance = deepfence_runtime_api.NetworkProtectionPolicyLogsApi(deepfence_runtime_api.ApiClient(configuration))
policy_log_id = 'policy_log_id_example' # str | Policy log ID

try:
    # Get network protection policy log by given policy_log_id
    api_instance.get_network_protection_policy_log(policy_log_id)
except ApiException as e:
    print("Exception when calling NetworkProtectionPolicyLogsApi->get_network_protection_policy_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_log_id** | **str**| Policy log ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

