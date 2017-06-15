# swagger_client.TimeRuleApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**time_rule_delete**](TimeRuleApi.md#time_rule_delete) | **DELETE** /timerules/{webId} | Delete a Time Rule.
[**time_rule_get**](TimeRuleApi.md#time_rule_get) | **GET** /timerules/{webId} | Retrieve a Time Rule.
[**time_rule_get_by_path**](TimeRuleApi.md#time_rule_get_by_path) | **GET** /timerules | Retrieve a Time Rule by path.
[**time_rule_update**](TimeRuleApi.md#time_rule_update) | **PATCH** /timerules/{webId} | Update a Time Rule by replacing items in its definition.


# **time_rule_delete**
> time_rule_delete(web_id)

Delete a Time Rule.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeRuleApi()
web_id = 'web_id_example' # str | The ID of the Time Rule.

try: 
    # Delete a Time Rule.
    api_instance.time_rule_delete(web_id)
except ApiException as e:
    print("Exception when calling TimeRuleApi->time_rule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Time Rule. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_rule_get**
> InlineResponse20050 time_rule_get(web_id, selected_fields=selected_fields)

Retrieve a Time Rule.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeRuleApi()
web_id = 'web_id_example' # str | The ID of the Time Rule.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a Time Rule.
    api_response = api_instance.time_rule_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeRuleApi->time_rule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Time Rule. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_rule_get_by_path**
> InlineResponse20050 time_rule_get_by_path(path, selected_fields=selected_fields)

Retrieve a Time Rule by path.

This method returns a Time Rule based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeRuleApi()
path = 'path_example' # str | The path to the Time Rule.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a Time Rule by path.
    api_response = api_instance.time_rule_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeRuleApi->time_rule_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the Time Rule. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_rule_update**
> time_rule_update(web_id, time_rule)

Update a Time Rule by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeRuleApi()
web_id = 'web_id_example' # str | The ID of the Time Rule.
time_rule = swagger_client.TimeRule() # TimeRule | A partial Time Rule containing the desired changes.

try: 
    # Update a Time Rule by replacing items in its definition.
    api_instance.time_rule_update(web_id, time_rule)
except ApiException as e:
    print("Exception when calling TimeRuleApi->time_rule_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Time Rule. | 
 **time_rule** | [**TimeRule**](TimeRule.md)| A partial Time Rule containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

