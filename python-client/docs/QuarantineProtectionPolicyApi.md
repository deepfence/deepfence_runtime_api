# deepfence_runtime_api.QuarantineProtectionPolicyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_quarantine_protection_policy**](QuarantineProtectionPolicyApi.md#add_quarantine_protection_policy) | **POST** /deepfence/v1.3/users/quarantine_protection_policy | Add a quarantine protection policy.
[**delete_quarantine_protection_policy**](QuarantineProtectionPolicyApi.md#delete_quarantine_protection_policy) | **DELETE** /deepfence/v1.3/users/quarantine_protection_policy/{policy_id} | Delete a quarantine policy
[**get_quarantine_protection_policy**](QuarantineProtectionPolicyApi.md#get_quarantine_protection_policy) | **GET** /deepfence/v1.3/users/quarantine_protection_policy | Get all quarantine policies created by the user.


# **add_quarantine_protection_policy**
> add_quarantine_protection_policy(body=body)

Add a quarantine protection policy.

 

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
api_instance = deepfence_runtime_api.QuarantineProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))
body = deepfence_runtime_api.Body4() # Body4 | JSON parameters. (optional)

try:
    # Add a quarantine protection policy.
    api_instance.add_quarantine_protection_policy(body=body)
except ApiException as e:
    print("Exception when calling QuarantineProtectionPolicyApi->add_quarantine_protection_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)| JSON parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quarantine_protection_policy**
> delete_quarantine_protection_policy(policy_id)

Delete a quarantine policy

 

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
api_instance = deepfence_runtime_api.QuarantineProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))
policy_id = 56 # int | 

try:
    # Delete a quarantine policy
    api_instance.delete_quarantine_protection_policy(policy_id)
except ApiException as e:
    print("Exception when calling QuarantineProtectionPolicyApi->delete_quarantine_protection_policy: %s\n" % e)
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

# **get_quarantine_protection_policy**
> get_quarantine_protection_policy()

Get all quarantine policies created by the user.

 

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
api_instance = deepfence_runtime_api.QuarantineProtectionPolicyApi(deepfence_runtime_api.ApiClient(configuration))

try:
    # Get all quarantine policies created by the user.
    api_instance.get_quarantine_protection_policy()
except ApiException as e:
    print("Exception when calling QuarantineProtectionPolicyApi->get_quarantine_protection_policy: %s\n" % e)
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

