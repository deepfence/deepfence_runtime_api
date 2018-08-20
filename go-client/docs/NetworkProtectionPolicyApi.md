# \NetworkProtectionPolicyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddNetworkProtectionPolicy**](NetworkProtectionPolicyApi.md#AddNetworkProtectionPolicy) | **Post** /deepfence/v1.3/users/network_protection_policy | Add a network protection policy.
[**DeleteNetworkProtectionPolicy**](NetworkProtectionPolicyApi.md#DeleteNetworkProtectionPolicy) | **Delete** /deepfence/v1.3/users/network_protection_policy/{policy_id} | Delete a network policy
[**GetNetworkProtectionPolicy**](NetworkProtectionPolicyApi.md#GetNetworkProtectionPolicy) | **Get** /deepfence/v1.3/users/network_protection_policy | Get all network policies created by the user.


# **AddNetworkProtectionPolicy**
> AddNetworkProtectionPolicy(ctx, optional)
Add a network protection policy.

 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| JSON parameters. | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteNetworkProtectionPolicy**
> DeleteNetworkProtectionPolicy(ctx, policyId)
Delete a network policy

 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **policyId** | **int32**|  | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetNetworkProtectionPolicy**
> GetNetworkProtectionPolicy(ctx, )
Get all network policies created by the user.

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

