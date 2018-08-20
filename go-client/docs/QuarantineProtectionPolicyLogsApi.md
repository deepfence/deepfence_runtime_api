# \QuarantineProtectionPolicyLogsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteQuarantineProtectionPolicyLog**](QuarantineProtectionPolicyLogsApi.md#DeleteQuarantineProtectionPolicyLog) | **Delete** /deepfence/v1.3/users/quarantine_protection_policy_log/{policy_log_id} | Delete quarantine protection policy log by policy_log_id
[**FindQuarantineProtectionPolicyLogs**](QuarantineProtectionPolicyLogsApi.md#FindQuarantineProtectionPolicyLogs) | **Post** /deepfence/v1.3/users/quarantine_protection_policy_log | Get/Delete quarantine protection policy logs by filter
[**GetQuarantineProtectionPolicyLog**](QuarantineProtectionPolicyLogsApi.md#GetQuarantineProtectionPolicyLog) | **Get** /deepfence/v1.3/users/quarantine_protection_policy_log/{policy_log_id} | Get quarantine protection policy log by given policy_log_id


# **DeleteQuarantineProtectionPolicyLog**
> DeleteQuarantineProtectionPolicyLog(ctx, policyLogId)
Delete quarantine protection policy log by policy_log_id

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

# **FindQuarantineProtectionPolicyLogs**
> FindQuarantineProtectionPolicyLogs(ctx, optional)
Get/Delete quarantine protection policy logs by filter

Get/Delete quarantine protection policy logs by filter

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options6**](Options6.md)| Options to get or delete policy logs | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetQuarantineProtectionPolicyLog**
> GetQuarantineProtectionPolicyLog(ctx, policyLogId)
Get quarantine protection policy log by given policy_log_id

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

