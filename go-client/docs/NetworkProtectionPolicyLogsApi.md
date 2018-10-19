# \NetworkProtectionPolicyLogsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteNetworkProtectionPolicyLog**](NetworkProtectionPolicyLogsApi.md#DeleteNetworkProtectionPolicyLog) | **Delete** /deepfence/v1.5/users/network_protection_policy_log/{policy_log_id} | Delete network protection policy log by policy_log_id
[**FindNetworkProtectionPolicyLogs**](NetworkProtectionPolicyLogsApi.md#FindNetworkProtectionPolicyLogs) | **Post** /deepfence/v1.5/users/network_protection_policy_log | Get/Delete network protection policy logs by filter
[**GetNetworkProtectionPolicyLog**](NetworkProtectionPolicyLogsApi.md#GetNetworkProtectionPolicyLog) | **Get** /deepfence/v1.5/users/network_protection_policy_log/{policy_log_id} | Get network protection policy log by given policy_log_id


# **DeleteNetworkProtectionPolicyLog**
> DeleteNetworkProtectionPolicyLog(ctx, policyLogId)
Delete network protection policy log by policy_log_id

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **policyLogId** | **string**|  | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **FindNetworkProtectionPolicyLogs**
> FindNetworkProtectionPolicyLogs(ctx, optional)
Get/Delete network protection policy logs by filter

Get/Delete network protection policy logs by filter

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options7**](Options7.md)| Options to get or delete policy logs | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetNetworkProtectionPolicyLog**
> GetNetworkProtectionPolicyLog(ctx, policyLogId)
Get network protection policy log by given policy_log_id

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **policyLogId** | **string**| Policy log ID | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

