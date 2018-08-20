# \QuarantineProtectionPolicyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddQuarantineProtectionPolicy**](QuarantineProtectionPolicyApi.md#AddQuarantineProtectionPolicy) | **Post** /deepfence/v1.3/users/quarantine_protection_policy | Add a quarantine protection policy.
[**DeleteQuarantineProtectionPolicy**](QuarantineProtectionPolicyApi.md#DeleteQuarantineProtectionPolicy) | **Delete** /deepfence/v1.3/users/quarantine_protection_policy/{policy_id} | Delete a quarantine policy
[**GetQuarantineProtectionPolicy**](QuarantineProtectionPolicyApi.md#GetQuarantineProtectionPolicy) | **Get** /deepfence/v1.3/users/quarantine_protection_policy | Get all quarantine policies created by the user.


# **AddQuarantineProtectionPolicy**
> AddQuarantineProtectionPolicy(ctx, optional)
Add a quarantine protection policy.

 

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)| JSON parameters. | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteQuarantineProtectionPolicy**
> DeleteQuarantineProtectionPolicy(ctx, policyId)
Delete a quarantine policy

 

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

# **GetQuarantineProtectionPolicy**
> GetQuarantineProtectionPolicy(ctx, )
Get all quarantine policies created by the user.

 

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

