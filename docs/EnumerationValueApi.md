# swagger_client.EnumerationValueApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enumeration_value_delete_enumeration_value**](EnumerationValueApi.md#enumeration_value_delete_enumeration_value) | **DELETE** /enumerationvalues/{webId} | Delete an enumeration value from an enumeration set.
[**enumeration_value_get**](EnumerationValueApi.md#enumeration_value_get) | **GET** /enumerationvalues/{webId} | Retrieve an enumeration value mapping
[**enumeration_value_get_by_path**](EnumerationValueApi.md#enumeration_value_get_by_path) | **GET** /enumerationvalues | Retrieve an enumeration value by path.
[**enumeration_value_update_enumeration_value**](EnumerationValueApi.md#enumeration_value_update_enumeration_value) | **PATCH** /enumerationvalues/{webId} | Update an enumeration value by replacing items in its definition.


# **enumeration_value_delete_enumeration_value**
> enumeration_value_delete_enumeration_value(web_id)

Delete an enumeration value from an enumeration set.

Deleting a value will remove it from the enumeration set along with any value references within the PI Web API system.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationValueApi()
web_id = 'web_id_example' # str | The ID of the enumeration value.

try: 
    # Delete an enumeration value from an enumeration set.
    api_instance.enumeration_value_delete_enumeration_value(web_id)
except ApiException as e:
    print("Exception when calling EnumerationValueApi->enumeration_value_delete_enumeration_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration value. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_value_get**
> InlineResponse20038Items enumeration_value_get(web_id, selected_fields=selected_fields)

Retrieve an enumeration value mapping

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationValueApi()
web_id = 'web_id_example' # str | The ID of the enumeration value.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an enumeration value mapping
    api_response = api_instance.enumeration_value_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnumerationValueApi->enumeration_value_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration value. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20038Items**](InlineResponse20038Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_value_get_by_path**
> InlineResponse20038Items enumeration_value_get_by_path(path, selected_fields=selected_fields)

Retrieve an enumeration value by path.

This method returns a enumeration value based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationValueApi()
path = 'path_example' # str | The path to the target enumeration value.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an enumeration value by path.
    api_response = api_instance.enumeration_value_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnumerationValueApi->enumeration_value_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the target enumeration value. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20038Items**](InlineResponse20038Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_value_update_enumeration_value**
> enumeration_value_update_enumeration_value(web_id, enumeration_value)

Update an enumeration value by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationValueApi()
web_id = 'web_id_example' # str | The ID of the enumeration value to update.
enumeration_value = swagger_client.EnumerationValue1() # EnumerationValue1 | A partial enumeration value containing the desired changes.

try: 
    # Update an enumeration value by replacing items in its definition.
    api_instance.enumeration_value_update_enumeration_value(web_id, enumeration_value)
except ApiException as e:
    print("Exception when calling EnumerationValueApi->enumeration_value_update_enumeration_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration value to update. | 
 **enumeration_value** | [**EnumerationValue1**](EnumerationValue1.md)| A partial enumeration value containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

