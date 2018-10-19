# deepfence_runtime_api.NetworkProtectionPolicyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_network_protection_policy**](NetworkProtectionPolicyApi.md#add_network_protection_policy) | **POST** /deepfence/v1.5/users/network_protection_policy | Add a network protection policy.
[**delete_network_protection_policy**](NetworkProtectionPolicyApi.md#delete_network_protection_policy) | **DELETE** /deepfence/v1.5/users/network_protection_policy/{policy_id} | Delete a network policy
[**get_network_protection_policy**](NetworkProtectionPolicyApi.md#get_network_protection_policy) | **GET** /deepfence/v1.5/users/network_protection_policy | Get all network policies created by the user.


# **add_network_protection_policy**
> add_network_protection_policy(body=body)

Add a network protection policy.

 

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
api_instance = deepfence_runtime_api.NetworkProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))
body = deepfence_runtime_api.Body1() # Body1 | JSON parameters. (optional)

try:
    # Add a network protection policy.
    api_instance.add_network_protection_policy(body=body)
except ApiException as e:
    print("Exception when calling NetworkProtectionPolicyApi->add_network_protection_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| JSON parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_protection_policy**
> delete_network_protection_policy(policy_id)

Delete a network policy

 

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
api_instance = deepfence_runtime_api.NetworkProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))
policy_id = 56 # int | 

try:
    # Delete a network policy
    api_instance.delete_network_protection_policy(policy_id)
except ApiException as e:
    print("Exception when calling NetworkProtectionPolicyApi->delete_network_protection_policy: %s\n" % e)
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

# **get_network_protection_policy**
> get_network_protection_policy()

Get all network policies created by the user.

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
api_instance = deepfence_runtime_api.NetworkProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))

try:
    # Get all network policies created by the user.
    api_instance.get_network_protection_policy()
except ApiException as e:
    print("Exception when calling NetworkProtectionPolicyApi->get_network_protection_policy: %s\n" % e)
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

