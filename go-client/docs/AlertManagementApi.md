# \AlertManagementApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteAlert**](AlertManagementApi.md#DeleteAlert) | **Delete** /deepfence/v1.3/alerts/{alert_id} | Delete an alert by alert_id
[**FindAlerts**](AlertManagementApi.md#FindAlerts) | **Post** /deepfence/v1.3/alerts | Get/Delete alerts by filter
[**GetAlert**](AlertManagementApi.md#GetAlert) | **Get** /deepfence/v1.3/alerts/{alert_id} | Get alert by given alert_id
[**GetNodeSeverity**](AlertManagementApi.md#GetNodeSeverity) | **Get** /deepfence/v1.3/node-severities | Get the severity of all nodes


# **DeleteAlert**
> DeleteAlert(ctx, alertId)
Delete an alert by alert_id

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **alertId** | **string**|  | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **FindAlerts**
> FindAlerts(ctx, optional)
Get/Delete alerts by filter

Get/Delete alerts by filter

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options**](Options.md)| Options to get or delete alerts | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAlert**
> GetAlert(ctx, alertId)
Get alert by given alert_id

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **alertId** | **string**| Alert ID | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetNodeSeverity**
> GetNodeSeverity(ctx, )
Get the severity of all nodes

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

