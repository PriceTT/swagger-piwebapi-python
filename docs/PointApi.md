# swagger_client.PointApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**point_delete**](PointApi.md#point_delete) | **DELETE** /points/{webId} | Delete a point.
[**point_get**](PointApi.md#point_get) | **GET** /points/{webId} | Get a point.
[**point_get_attribute_by_name**](PointApi.md#point_get_attribute_by_name) | **GET** /points/{webId}/attributes/{name} | Get a point attribute by name.
[**point_get_attributes**](PointApi.md#point_get_attributes) | **GET** /points/{webId}/attributes | Get point attributes.
[**point_get_by_path**](PointApi.md#point_get_by_path) | **GET** /points | Get a point by path.
[**point_get_multiple**](PointApi.md#point_get_multiple) | **GET** /points/multiple | Retrieve multiple points by web id or path.
[**point_update**](PointApi.md#point_update) | **PATCH** /points/{webId} | Update a point.


# **point_delete**
> point_delete(web_id)

Delete a point.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PointApi()
web_id = 'web_id_example' # str | The ID of the point.

try: 
    # Delete a point.
    api_instance.point_delete(web_id)
except ApiException as e:
    print("Exception when calling PointApi->point_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the point. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **point_get**
> InlineResponse20036Items point_get(web_id, selected_fields=selected_fields)

Get a point.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PointApi()
web_id = 'web_id_example' # str | The ID of the point.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get a point.
    api_response = api_instance.point_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointApi->point_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the point. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20036Items**](InlineResponse20036Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **point_get_attribute_by_name**
> InlineResponse20041Items point_get_attribute_by_name(name, web_id, selected_fields=selected_fields)

Get a point attribute by name.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PointApi()
name = 'name_example' # str | The name of the attribute.
web_id = 'web_id_example' # str | The ID of the point.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get a point attribute by name.
    api_response = api_instance.point_get_attribute_by_name(name, web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointApi->point_get_attribute_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the attribute. | 
 **web_id** | **str**| The ID of the point. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20041Items**](InlineResponse20041Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **point_get_attributes**
> InlineResponse20041 point_get_attributes(web_id, name=name, name_filter=name_filter, selected_fields=selected_fields)

Get point attributes.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PointApi()
web_id = 'web_id_example' # str | The ID of the point.
name = ['name_example'] # list[str] | The name of a point attribute to be returned. Multiple attributes may be specified with multiple instances of the parameter. (optional)
name_filter = 'name_filter_example' # str | The filter to the names of the list of point attributes to be returned. The default is no filter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get point attributes.
    api_response = api_instance.point_get_attributes(web_id, name=name, name_filter=name_filter, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointApi->point_get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the point. | 
 **name** | [**list[str]**](str.md)| The name of a point attribute to be returned. Multiple attributes may be specified with multiple instances of the parameter. | [optional] 
 **name_filter** | **str**| The filter to the names of the list of point attributes to be returned. The default is no filter. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **point_get_by_path**
> InlineResponse20036Items point_get_by_path(path, selected_fields=selected_fields)

Get a point by path.

This method returns a PI Point based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PointApi()
path = 'path_example' # str | The path to the point.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get a point by path.
    api_response = api_instance.point_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointApi->point_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the point. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20036Items**](InlineResponse20036Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **point_get_multiple**
> InlineResponse20042 point_get_multiple(as_parallel=as_parallel, include_mode=include_mode, path=path, selected_fields=selected_fields, web_id=web_id)

Retrieve multiple points by web id or path.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PointApi()
as_parallel = true # bool | Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested points. The default is 'false'. (optional)
include_mode = 'include_mode_example' # str | The include mode for the return list. The default is 'All'. (optional)
path = ['path_example'] # list[str] | The path of a point. Multiple points may be specified with multiple instances of the parameter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
web_id = ['web_id_example'] # list[str] | The ID of a point. Multiple points may be specified with multiple instances of the parameter. (optional)

try: 
    # Retrieve multiple points by web id or path.
    api_response = api_instance.point_get_multiple(as_parallel=as_parallel, include_mode=include_mode, path=path, selected_fields=selected_fields, web_id=web_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointApi->point_get_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_parallel** | **bool**| Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested points. The default is &#39;false&#39;. | [optional] 
 **include_mode** | **str**| The include mode for the return list. The default is &#39;All&#39;. | [optional] 
 **path** | [**list[str]**](str.md)| The path of a point. Multiple points may be specified with multiple instances of the parameter. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **web_id** | [**list[str]**](str.md)| The ID of a point. Multiple points may be specified with multiple instances of the parameter. | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **point_update**
> point_update(web_id, point_dto)

Update a point.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PointApi()
web_id = 'web_id_example' # str | The ID of the point.
point_dto = swagger_client.PointDTO1() # PointDTO1 | A partial point containing the desired changes.

try: 
    # Update a point.
    api_instance.point_update(web_id, point_dto)
except ApiException as e:
    print("Exception when calling PointApi->point_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the point. | 
 **point_dto** | [**PointDTO1**](PointDTO1.md)| A partial point containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

