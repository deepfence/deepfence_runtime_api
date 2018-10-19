# deepfence_runtime_api.AuthenticationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_api**](AuthenticationApi.md#authenticate_api) | **POST** /deepfence/v1.5/users/auth | Authentication for API access
[**get_user_details**](AuthenticationApi.md#get_user_details) | **GET** /deepfence/v1.5/users/me | User details.
[**refresh_jwt_token**](AuthenticationApi.md#refresh_jwt_token) | **POST** /deepfence/v1.5/users/refresh/token | Generate a new access token using refresh token
[**reset_api_key**](AuthenticationApi.md#reset_api_key) | **POST** /deepfence/v1.5/users/reset-api-key | Reset API Key


# **authenticate_api**
> authenticate_api(body=body)

Authentication for API access

### Example
```python
from __future__ import print_function
import time
import deepfence_runtime_api
from deepfence_runtime_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = deepfence_runtime_api.AuthenticationApi()
body = deepfence_runtime_api.Body() # Body | JSON parameters. (optional)

try:
    # Authentication for API access
    api_instance.authenticate_api(body=body)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authenticate_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| JSON parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_details**
> InlineResponse200 get_user_details()

User details.

 Permission: ALL 

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
api_instance = deepfence_runtime_api.AuthenticationApi(deepfence_runtime_api.ApiClient(configuration))

try:
    # User details.
    api_response = api_instance.get_user_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_user_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_jwt_token**
> refresh_jwt_token()

Generate a new access token using refresh token

Generate a new access token using refresh token. Usage (In header): Authorization: Bearer <refresh_token>

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
api_instance = deepfence_runtime_api.AuthenticationApi(deepfence_runtime_api.ApiClient(configuration))

try:
    # Generate a new access token using refresh token
    api_instance.refresh_jwt_token()
except ApiException as e:
    print("Exception when calling AuthenticationApi->refresh_jwt_token: %s\n" % e)
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

# **reset_api_key**
> reset_api_key()

Reset API Key

 Permission: ALL 

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
api_instance = deepfence_runtime_api.AuthenticationApi(deepfence_runtime_api.ApiClient(configuration))

try:
    # Reset API Key
    api_instance.reset_api_key()
except ApiException as e:
    print("Exception when calling AuthenticationApi->reset_api_key: %s\n" % e)
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

