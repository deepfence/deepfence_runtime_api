# \AuthenticationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AuthenticateApi**](AuthenticationApi.md#AuthenticateApi) | **Post** /deepfence/v1.5/users/auth | Authentication for API access
[**GetUserDetails**](AuthenticationApi.md#GetUserDetails) | **Get** /deepfence/v1.5/users/me | User details.
[**RefreshJwtToken**](AuthenticationApi.md#RefreshJwtToken) | **Post** /deepfence/v1.5/users/refresh/token | Generate a new access token using refresh token
[**ResetApiKey**](AuthenticationApi.md#ResetApiKey) | **Post** /deepfence/v1.5/users/reset-api-key | Reset API Key


# **AuthenticateApi**
> AuthenticateApi(ctx, optional)
Authentication for API access

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| JSON parameters. | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetUserDetails**
> InlineResponse200 GetUserDetails(ctx, )
User details.

 Permission: ALL 

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](inline_response_200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **RefreshJwtToken**
> RefreshJwtToken(ctx, )
Generate a new access token using refresh token

Generate a new access token using refresh token. Usage (In header): Authorization: Bearer <refresh_token>

### Required Parameters
This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ResetApiKey**
> ResetApiKey(ctx, )
Reset API Key

 Permission: ALL 

### Required Parameters
This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

