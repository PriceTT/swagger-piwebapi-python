# swagger_client.AttributeApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attribute_create_attribute**](AttributeApi.md#attribute_create_attribute) | **POST** /attributes/{webId}/attributes | Create a new attribute as a child of the specified attribute.
[**attribute_create_config**](AttributeApi.md#attribute_create_config) | **POST** /attributes/{webId}/config | Create or update an attribute&#39;s DataReference configuration (Create/Update PI point for PI Point DataReference).
[**attribute_delete**](AttributeApi.md#attribute_delete) | **DELETE** /attributes/{webId} | Delete an attribute.
[**attribute_get**](AttributeApi.md#attribute_get) | **GET** /attributes/{webId} | Retrieve an attribute.
[**attribute_get_attributes**](AttributeApi.md#attribute_get_attributes) | **GET** /attributes/{webId}/attributes | Get the child attributes of the specified attribute.
[**attribute_get_by_path**](AttributeApi.md#attribute_get_by_path) | **GET** /attributes | Retrieve an attribute by path.
[**attribute_get_categories**](AttributeApi.md#attribute_get_categories) | **GET** /attributes/{webId}/categories | Get an attribute&#39;s categories.
[**attribute_get_multiple**](AttributeApi.md#attribute_get_multiple) | **GET** /attributes/multiple | Retrieve multiple attributes by web id or path.
[**attribute_get_value**](AttributeApi.md#attribute_get_value) | **GET** /attributes/{webId}/value | Get the attribute&#39;s value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.
[**attribute_set_value**](AttributeApi.md#attribute_set_value) | **PUT** /attributes/{webId}/value | Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.
[**attribute_update**](AttributeApi.md#attribute_update) | **PATCH** /attributes/{webId} | Update an attribute by replacing items in its definition.


# **attribute_create_attribute**
> attribute_create_attribute(web_id, attribute)

Create a new attribute as a child of the specified attribute.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the parent attribute on which to create the attribute.
attribute = swagger_client.Attribute1() # Attribute1 | The definition of the new attribute.

try: 
    # Create a new attribute as a child of the specified attribute.
    api_instance.attribute_create_attribute(web_id, attribute)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent attribute on which to create the attribute. | 
 **attribute** | [**Attribute1**](Attribute1.md)| The definition of the new attribute. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_create_config**
> attribute_create_config(web_id)

Create or update an attribute's DataReference configuration (Create/Update PI point for PI Point DataReference).

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the attribute.

try: 
    # Create or update an attribute's DataReference configuration (Create/Update PI point for PI Point DataReference).
    api_instance.attribute_create_config(web_id)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_create_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_delete**
> attribute_delete(web_id)

Delete an attribute.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the attribute.

try: 
    # Delete an attribute.
    api_instance.attribute_delete(web_id)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_get**
> InlineResponse20013Items attribute_get(web_id, selected_fields=selected_fields)

Retrieve an attribute.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the attribute.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an attribute.
    api_response = api_instance.attribute_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20013Items**](InlineResponse20013Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_get_attributes**
> InlineResponse20013 attribute_get_attributes(web_id, category_name=category_name, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, sort_field=sort_field, sort_order=sort_order, start_index=start_index, template_name=template_name, value_type=value_type)

Get the child attributes of the specified attribute.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the parent attribute.
category_name = 'category_name_example' # str | Specify that returned attributes must have this category. The default is no category filter. (optional)
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
name_filter = 'name_filter_example' # str | The name query string used for finding attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)
template_name = 'template_name_example' # str | Specify that returned attributes must be members of this template. The default is no template filter. (optional)
value_type = 'value_type_example' # str | Specify that returned attributes' value type must be the given value type. The default is no value type filter. (optional)

try: 
    # Get the child attributes of the specified attribute.
    api_response = api_instance.attribute_get_attributes(web_id, category_name=category_name, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, sort_field=sort_field, sort_order=sort_order, start_index=start_index, template_name=template_name, value_type=value_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent attribute. | 
 **category_name** | **str**| Specify that returned attributes must have this category. The default is no category filter. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **name_filter** | **str**| The name query string used for finding attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **template_name** | **str**| Specify that returned attributes must be members of this template. The default is no template filter. | [optional] 
 **value_type** | **str**| Specify that returned attributes&#39; value type must be the given value type. The default is no value type filter. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_get_by_path**
> InlineResponse20013Items attribute_get_by_path(path, selected_fields=selected_fields)

Retrieve an attribute by path.

This method returns an attribute based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
path = 'path_example' # str | The path to the attribute.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an attribute by path.
    api_response = api_instance.attribute_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the attribute. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20013Items**](InlineResponse20013Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_get_categories**
> InlineResponse20012 attribute_get_categories(web_id, selected_fields=selected_fields)

Get an attribute's categories.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the attribute.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get an attribute's categories.
    api_response = api_instance.attribute_get_categories(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_get_multiple**
> InlineResponse20029 attribute_get_multiple(as_parallel=as_parallel, include_mode=include_mode, path=path, selected_fields=selected_fields, web_id=web_id)

Retrieve multiple attributes by web id or path.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
as_parallel = true # bool | Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is 'false'. (optional)
include_mode = 'include_mode_example' # str | The include mode for the return list. The default is 'All'. (optional)
path = ['path_example'] # list[str] | The path of an attribute. Multiple attributes may be specified with multiple instances of the parameter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
web_id = ['web_id_example'] # list[str] | The ID of an attribute. Multiple attributes may be specified with multiple instances of the parameter. (optional)

try: 
    # Retrieve multiple attributes by web id or path.
    api_response = api_instance.attribute_get_multiple(as_parallel=as_parallel, include_mode=include_mode, path=path, selected_fields=selected_fields, web_id=web_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_get_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_parallel** | **bool**| Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is &#39;false&#39;. | [optional] 
 **include_mode** | **str**| The include mode for the return list. The default is &#39;All&#39;. | [optional] 
 **path** | [**list[str]**](str.md)| The path of an attribute. Multiple attributes may be specified with multiple instances of the parameter. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **web_id** | [**list[str]**](str.md)| The ID of an attribute. Multiple attributes may be specified with multiple instances of the parameter. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_get_value**
> InlineResponse20028 attribute_get_value(web_id, selected_fields=selected_fields)

Get the attribute's value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the attribute.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the attribute's value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.
    api_response = api_instance.attribute_get_value(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_get_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_set_value**
> attribute_set_value(web_id, value)

Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.

Users must be aware of the value type that the attribute takes before changing the value. If a value entered by the user does not match the value type expressed in the attribute, it will not work or it will return an error. Users should also be careful of what the value type means, for instance, if a value type accepts strings and the user enters a number, the attribute will interpret it as a string of characters and not as the integer value that the user may have wanted.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the attribute.
value = swagger_client.Value() # Value | The value to write.

try: 
    # Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.
    api_instance.attribute_set_value(web_id, value)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_set_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute. | 
 **value** | [**Value**](Value.md)| The value to write. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_update**
> attribute_update(web_id, attribute)

Update an attribute by replacing items in its definition.

If an attribute is based on a template, the user must make sure to update the attribute appropriately so that it does not conflict with the template's design. Once a template is applied to an attribute, it can not be changed.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeApi()
web_id = 'web_id_example' # str | The ID of the attribute.
attribute = swagger_client.Attribute() # Attribute | A partial attribute containing the desired changes.

try: 
    # Update an attribute by replacing items in its definition.
    api_instance.attribute_update(web_id, attribute)
except ApiException as e:
    print("Exception when calling AttributeApi->attribute_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute. | 
 **attribute** | [**Attribute**](Attribute.md)| A partial attribute containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

