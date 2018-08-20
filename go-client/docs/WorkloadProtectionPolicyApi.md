# \WorkloadProtectionPolicyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddWorkloadProtectionPolicy**](WorkloadProtectionPolicyApi.md#AddWorkloadProtectionPolicy) | **Post** /deepfence/v1.3/users/node_network_protection_policy | Add a node network protection policy.
[**BulkDeleteWorkloadProtectionPolicy**](WorkloadProtectionPolicyApi.md#BulkDeleteWorkloadProtectionPolicy) | **Delete** /deepfence/v1.3/users/node_network_protection_policy | Delete multiple node network protection policies
[**DeleteWorkloadProtectionPolicy**](WorkloadProtectionPolicyApi.md#DeleteWorkloadProtectionPolicy) | **Delete** /deepfence/v1.3/users/node_network_protection_policy/{policy_id} | Delete a node network protection policy
[**GetWorkloadProtectionPolicy**](WorkloadProtectionPolicyApi.md#GetWorkloadProtectionPolicy) | **Get** /deepfence/v1.3/users/node_network_protection_policy | Get all node network protection policies created by the user.


# **AddWorkloadProtectionPolicy**
> AddWorkloadProtectionPolicy(ctx, optional)
Add a node network protection policy.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| JSON parameters. | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkDeleteWorkloadProtectionPolicy**
> BulkDeleteWorkloadProtectionPolicy(ctx, optional)
Delete multiple node network protection policies

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| JSON parameters. | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteWorkloadProtectionPolicy**
> DeleteWorkloadProtectionPolicy(ctx, policyId)
Delete a node network protection policy

 

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

# **GetWorkloadProtectionPolicy**
> GetWorkloadProtectionPolicy(ctx, nodePolicyType)
Get all node network protection policies created by the user.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodePolicyType** | **string**| Policy type - whitelist or blacklist | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

