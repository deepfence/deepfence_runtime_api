# deepfence_runtime_api.WorkloadProtectionPolicyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_workload_protection_policy**](WorkloadProtectionPolicyApi.md#add_workload_protection_policy) | **POST** /deepfence/v1.3/users/node_network_protection_policy | Add a node network protection policy.
[**bulk_delete_workload_protection_policy**](WorkloadProtectionPolicyApi.md#bulk_delete_workload_protection_policy) | **DELETE** /deepfence/v1.3/users/node_network_protection_policy | Delete multiple node network protection policies
[**delete_workload_protection_policy**](WorkloadProtectionPolicyApi.md#delete_workload_protection_policy) | **DELETE** /deepfence/v1.3/users/node_network_protection_policy/{policy_id} | Delete a node network protection policy
[**get_workload_protection_policy**](WorkloadProtectionPolicyApi.md#get_workload_protection_policy) | **GET** /deepfence/v1.3/users/node_network_protection_policy | Get all node network protection policies created by the user.


# **add_workload_protection_policy**
> add_workload_protection_policy(body=body)

Add a node network protection policy.

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
api_instance = deepfence_runtime_api.WorkloadProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))
body = deepfence_runtime_api.Body2() # Body2 | JSON parameters. (optional)

try:
    # Add a node network protection policy.
    api_instance.add_workload_protection_policy(body=body)
except ApiException as e:
    print("Exception when calling WorkloadProtectionPolicyApi->add_workload_protection_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| JSON parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_workload_protection_policy**
> bulk_delete_workload_protection_policy(body=body)

Delete multiple node network protection policies

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
api_instance = deepfence_runtime_api.WorkloadProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))
body = deepfence_runtime_api.Body3() # Body3 | JSON parameters. (optional)

try:
    # Delete multiple node network protection policies
    api_instance.bulk_delete_workload_protection_policy(body=body)
except ApiException as e:
    print("Exception when calling WorkloadProtectionPolicyApi->bulk_delete_workload_protection_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| JSON parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workload_protection_policy**
> delete_workload_protection_policy(policy_id)

Delete a node network protection policy

 

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
api_instance = deepfence_runtime_api.WorkloadProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))
policy_id = 56 # int | 

try:
    # Delete a node network protection policy
    api_instance.delete_workload_protection_policy(policy_id)
except ApiException as e:
    print("Exception when calling WorkloadProtectionPolicyApi->delete_workload_protection_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workload_protection_policy**
> get_workload_protection_policy(node_policy_type)

Get all node network protection policies created by the user.

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
api_instance = deepfence_runtime_api.WorkloadProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))
node_policy_type = 'node_policy_type_example' # str | Policy type - whitelist or blacklist

try:
    # Get all node network protection policies created by the user.
    api_instance.get_workload_protection_policy(node_policy_type)
except ApiException as e:
    print("Exception when calling WorkloadProtectionPolicyApi->get_workload_protection_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_policy_type** | **str**| Policy type - whitelist or blacklist | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

