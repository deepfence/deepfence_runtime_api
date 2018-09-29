# \ComplianceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApplicableComplianceScans**](ComplianceApi.md#ApplicableComplianceScans) | **Get** /deepfence/v1.3/node/{node_id}/applicable_compliance_scans | Compliance API - Get Applicable Compliance Scans
[**CheckComplianceScanStatus**](ComplianceApi.md#CheckComplianceScanStatus) | **Get** /deepfence/v1.3/compliance/{node_id}/{compliance_check_type}/scan_status | Compliance API - Check Compliance Scan Status
[**FindComplianceScanResults**](ComplianceApi.md#FindComplianceScanResults) | **Post** /deepfence/v1.3/compliance/scan_results | Compliance API - Get/Delete Compliance Scan Results with filters
[**StartComplianceScan**](ComplianceApi.md#StartComplianceScan) | **Post** /deepfence/v1.3/node/{node_id}/start_compliance_scan | Compliance API - Start Compliance Scan


# **ApplicableComplianceScans**
> ApplicableComplianceScans(ctx, nodeId)
Compliance API - Get Applicable Compliance Scans

Get list of applicable compliance scans for this node (Applicable node type - `host`, `container`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CheckComplianceScanStatus**
> CheckComplianceScanStatus(ctx, nodeId, complianceCheckType)
Compliance API - Check Compliance Scan Status

Check status of compliance scan on this node (Applicable node type - `host`, `container`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
  **complianceCheckType** | **string**| Compliance check type. Not all options are available. Check applicable compliance scans first. | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **FindComplianceScanResults**
> FindComplianceScanResults(ctx, optional)
Compliance API - Get/Delete Compliance Scan Results with filters

Get/Delete compliance scan results with filters for node_id, compliance_check_type, etc

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options1**](Options1.md)| Options to get or delete compliance scan results | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StartComplianceScan**
> StartComplianceScan(ctx, nodeId, optional)
Compliance API - Start Compliance Scan

Start compliance scan on this node (Applicable node type - `host`, `container`)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for logging, tracing, authentication, etc.
  **nodeId** | **string**| Node ID (refer enumerate api) | 
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeId** | **string**| Node ID (refer enumerate api) | 
 **options** | [**Options5**](Options5.md)| Options to start compliance scan | 

### Return type

 (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

