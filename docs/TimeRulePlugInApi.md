# swagger_client.TimeRulePlugInApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**time_rule_plug_in_get**](TimeRulePlugInApi.md#time_rule_plug_in_get) | **GET** /timeruleplugins/{webId} | Retrieve a Time Rule Plug-in.
[**time_rule_plug_in_get_by_path**](TimeRulePlugInApi.md#time_rule_plug_in_get_by_path) | **GET** /timeruleplugins | Retrieve a Time Rule Plug-in by path.


# **time_rule_plug_in_get**
> InlineResponse20026Items time_rule_plug_in_get(web_id, selected_fields=selected_fields)

Retrieve a Time Rule Plug-in.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeRulePlugInApi()
web_id = 'web_id_example' # str | The ID of the Time Rule Plug-in.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a Time Rule Plug-in.
    api_response = api_instance.time_rule_plug_in_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeRulePlugInApi->time_rule_plug_in_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Time Rule Plug-in. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20026Items**](InlineResponse20026Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_rule_plug_in_get_by_path**
> InlineResponse20026Items time_rule_plug_in_get_by_path(path, selected_fields=selected_fields)

Retrieve a Time Rule Plug-in by path.

This method returns a Time Rule Plug-in based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeRulePlugInApi()
path = 'path_example' # str | The path to the Time Rule Plug-in.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a Time Rule Plug-in by path.
    api_response = api_instance.time_rule_plug_in_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeRulePlugInApi->time_rule_plug_in_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the Time Rule Plug-in. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20026Items**](InlineResponse20026Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

