# swagger_client.AnalysisRulePlugInApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analysis_rule_plug_in_get**](AnalysisRulePlugInApi.md#analysis_rule_plug_in_get) | **GET** /analysisruleplugins/{webId} | Retrieve an Analysis Rule Plug-in.
[**analysis_rule_plug_in_get_by_path**](AnalysisRulePlugInApi.md#analysis_rule_plug_in_get_by_path) | **GET** /analysisruleplugins | Retrieve an Analysis Rule Plug-in by path.


# **analysis_rule_plug_in_get**
> InlineResponse2005 analysis_rule_plug_in_get(web_id, selected_fields=selected_fields)

Retrieve an Analysis Rule Plug-in.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisRulePlugInApi()
web_id = 'web_id_example' # str | The ID of the Analysis Rule Plug-in.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Analysis Rule Plug-in.
    api_response = api_instance.analysis_rule_plug_in_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisRulePlugInApi->analysis_rule_plug_in_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Analysis Rule Plug-in. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_rule_plug_in_get_by_path**
> InlineResponse2005 analysis_rule_plug_in_get_by_path(path, selected_fields=selected_fields)

Retrieve an Analysis Rule Plug-in by path.

This method returns an Analysis Rule Plug-in based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisRulePlugInApi()
path = 'path_example' # str | The path to the Analysis Rule Plug-in.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Analysis Rule Plug-in by path.
    api_response = api_instance.analysis_rule_plug_in_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisRulePlugInApi->analysis_rule_plug_in_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the Analysis Rule Plug-in. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

