# swagger_client.AnalysisRuleApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analysis_rule_create_analysis_rule**](AnalysisRuleApi.md#analysis_rule_create_analysis_rule) | **POST** /analysisrules/{webId}/analysisrules | Create a new Analysis Rule as a child of an existing Analysis Rule.
[**analysis_rule_delete**](AnalysisRuleApi.md#analysis_rule_delete) | **DELETE** /analysisrules/{webId} | Delete an Analysis Rule.
[**analysis_rule_get**](AnalysisRuleApi.md#analysis_rule_get) | **GET** /analysisrules/{webId} | Retrieve an Analysis Rule.
[**analysis_rule_get_analysis_rules**](AnalysisRuleApi.md#analysis_rule_get_analysis_rules) | **GET** /analysisrules/{webId}/analysisrules | Get the child Analysis Rules of the Analysis Rule.
[**analysis_rule_get_by_path**](AnalysisRuleApi.md#analysis_rule_get_by_path) | **GET** /analysisrules | Retrieve an Analysis Rule by path.
[**analysis_rule_update**](AnalysisRuleApi.md#analysis_rule_update) | **PATCH** /analysisrules/{webId} | Update an Analysis Rule by replacing items in its definition.


# **analysis_rule_create_analysis_rule**
> analysis_rule_create_analysis_rule(web_id, analysis_rule)

Create a new Analysis Rule as a child of an existing Analysis Rule.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisRuleApi()
web_id = 'web_id_example' # str | The ID of the parent Analysis Rule, on which to create the child Analysis Rule.
analysis_rule = swagger_client.AnalysisRule1() # AnalysisRule1 | The definition of the new Analysis Rule.

try: 
    # Create a new Analysis Rule as a child of an existing Analysis Rule.
    api_instance.analysis_rule_create_analysis_rule(web_id, analysis_rule)
except ApiException as e:
    print("Exception when calling AnalysisRuleApi->analysis_rule_create_analysis_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent Analysis Rule, on which to create the child Analysis Rule. | 
 **analysis_rule** | [**AnalysisRule1**](AnalysisRule1.md)| The definition of the new Analysis Rule. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_rule_delete**
> analysis_rule_delete(web_id)

Delete an Analysis Rule.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisRuleApi()
web_id = 'web_id_example' # str | The ID of the Analysis Rule.

try: 
    # Delete an Analysis Rule.
    api_instance.analysis_rule_delete(web_id)
except ApiException as e:
    print("Exception when calling AnalysisRuleApi->analysis_rule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Analysis Rule. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_rule_get**
> InlineResponse2006 analysis_rule_get(web_id, selected_fields=selected_fields)

Retrieve an Analysis Rule.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisRuleApi()
web_id = 'web_id_example' # str | The ID of the Analysis Rule.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Analysis Rule.
    api_response = api_instance.analysis_rule_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisRuleApi->analysis_rule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Analysis Rule. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_rule_get_analysis_rules**
> InlineResponse2007 analysis_rule_get_analysis_rules(web_id, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index)

Get the child Analysis Rules of the Analysis Rule.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisRuleApi()
web_id = 'web_id_example' # str | The ID of the parent Analysis Rule.
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
name_filter = 'name_filter_example' # str | The name query string used for finding Analysis Rules. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include Analysis Rules nested further than the immediate children of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)

try: 
    # Get the child Analysis Rules of the Analysis Rule.
    api_response = api_instance.analysis_rule_get_analysis_rules(web_id, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisRuleApi->analysis_rule_get_analysis_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent Analysis Rule. | 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **name_filter** | **str**| The name query string used for finding Analysis Rules. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include Analysis Rules nested further than the immediate children of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_rule_get_by_path**
> InlineResponse2006 analysis_rule_get_by_path(path, selected_fields=selected_fields)

Retrieve an Analysis Rule by path.

This method returns an Analysis Rule based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisRuleApi()
path = 'path_example' # str | The path to the Analysis Rule.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Analysis Rule by path.
    api_response = api_instance.analysis_rule_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisRuleApi->analysis_rule_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the Analysis Rule. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_rule_update**
> analysis_rule_update(web_id, analysis_rule)

Update an Analysis Rule by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisRuleApi()
web_id = 'web_id_example' # str | The ID of the Analysis Rule.
analysis_rule = swagger_client.AnalysisRule() # AnalysisRule | A partial Analysis Rule containing the desired changes.

try: 
    # Update an Analysis Rule by replacing items in its definition.
    api_instance.analysis_rule_update(web_id, analysis_rule)
except ApiException as e:
    print("Exception when calling AnalysisRuleApi->analysis_rule_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Analysis Rule. | 
 **analysis_rule** | [**AnalysisRule**](AnalysisRule.md)| A partial Analysis Rule containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

