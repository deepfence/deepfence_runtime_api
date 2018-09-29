# deepfence_runtime_api.ComplianceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicable_compliance_scans**](ComplianceApi.md#applicable_compliance_scans) | **GET** /deepfence/v1.3/node/{node_id}/applicable_compliance_scans | Compliance API - Get Applicable Compliance Scans
[**check_compliance_scan_status**](ComplianceApi.md#check_compliance_scan_status) | **GET** /deepfence/v1.3/compliance/{node_id}/{compliance_check_type}/scan_status | Compliance API - Check Compliance Scan Status
[**find_compliance_scan_results**](ComplianceApi.md#find_compliance_scan_results) | **POST** /deepfence/v1.3/compliance/scan_results | Compliance API - Get/Delete Compliance Scan Results with filters
[**start_compliance_scan**](ComplianceApi.md#start_compliance_scan) | **POST** /deepfence/v1.3/node/{node_id}/start_compliance_scan | Compliance API - Start Compliance Scan


# **applicable_compliance_scans**
> applicable_compliance_scans(node_id)

Compliance API - Get Applicable Compliance Scans

Get list of applicable compliance scans for this node (Applicable node type - `host`, `container`)

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
api_instance = deepfence_runtime_api.ComplianceApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)

try:
    # Compliance API - Get Applicable Compliance Scans
    api_instance.applicable_compliance_scans(node_id)
except ApiException as e:
    print("Exception when calling ComplianceApi->applicable_compliance_scans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_compliance_scan_status**
> check_compliance_scan_status(node_id, compliance_check_type)

Compliance API - Check Compliance Scan Status

Check status of compliance scan on this node (Applicable node type - `host`, `container`)

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
api_instance = deepfence_runtime_api.ComplianceApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
compliance_check_type = 'compliance_check_type_example' # str | Compliance check type. Not all options are available. Check applicable compliance scans first.

try:
    # Compliance API - Check Compliance Scan Status
    api_instance.check_compliance_scan_status(node_id, compliance_check_type)
except ApiException as e:
    print("Exception when calling ComplianceApi->check_compliance_scan_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **compliance_check_type** | **str**| Compliance check type. Not all options are available. Check applicable compliance scans first. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_compliance_scan_results**
> find_compliance_scan_results(options=options)

Compliance API - Get/Delete Compliance Scan Results with filters

Get/Delete compliance scan results with filters for node_id, compliance_check_type, etc

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
api_instance = deepfence_runtime_api.ComplianceApi(deepfence_runtime_api.ApiClient(configuration))
options = deepfence_runtime_api.Options1() # Options1 | Options to get or delete compliance scan results (optional)

try:
    # Compliance API - Get/Delete Compliance Scan Results with filters
    api_instance.find_compliance_scan_results(options=options)
except ApiException as e:
    print("Exception when calling ComplianceApi->find_compliance_scan_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options1**](Options1.md)| Options to get or delete compliance scan results | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_compliance_scan**
> start_compliance_scan(node_id, options=options)

Compliance API - Start Compliance Scan

Start compliance scan on this node (Applicable node type - `host`, `container`)

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
api_instance = deepfence_runtime_api.ComplianceApi(deepfence_runtime_api.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID (refer enumerate api)
options = deepfence_runtime_api.Options5() # Options5 | Options to start compliance scan (optional)

try:
    # Compliance API - Start Compliance Scan
    api_instance.start_compliance_scan(node_id, options=options)
except ApiException as e:
    print("Exception when calling ComplianceApi->start_compliance_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID (refer enumerate api) | 
 **options** | [**Options5**](Options5.md)| Options to start compliance scan | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

