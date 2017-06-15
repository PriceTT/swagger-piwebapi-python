# swagger_client.DataServerApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_server_create_enumeration_set**](DataServerApi.md#data_server_create_enumeration_set) | **POST** /dataservers/{webId}/enumerationsets | Create an enumeration set on the Data Server.
[**data_server_create_point**](DataServerApi.md#data_server_create_point) | **POST** /dataservers/{webId}/points | Create a point in the specified Data Server.
[**data_server_get**](DataServerApi.md#data_server_get) | **GET** /dataservers/{webId} | Retrieve a Data Server.
[**data_server_get_by_name**](DataServerApi.md#data_server_get_by_name) | **GET** /dataservers#name | Retrieve a Data Server by name.
[**data_server_get_by_path**](DataServerApi.md#data_server_get_by_path) | **GET** /dataservers#path | Retrieve a Data Server by path.
[**data_server_get_enumeration_sets**](DataServerApi.md#data_server_get_enumeration_sets) | **GET** /dataservers/{webId}/enumerationsets | Retrieve enumeration sets for given Data Server.
[**data_server_get_points**](DataServerApi.md#data_server_get_points) | **GET** /dataservers/{webId}/points | Retrieve a list of points on a specified Data Server.
[**data_server_list**](DataServerApi.md#data_server_list) | **GET** /dataservers | Retrieve a list of Data Servers known to this service.


# **data_server_create_enumeration_set**
> data_server_create_enumeration_set(web_id, enumeration_set)

Create an enumeration set on the Data Server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataServerApi()
web_id = 'web_id_example' # str | The ID of the server on which to create the enumeration set.
enumeration_set = swagger_client.EnumerationSet1() # EnumerationSet1 | The new enumeration set definition.

try: 
    # Create an enumeration set on the Data Server.
    api_instance.data_server_create_enumeration_set(web_id, enumeration_set)
except ApiException as e:
    print("Exception when calling DataServerApi->data_server_create_enumeration_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server on which to create the enumeration set. | 
 **enumeration_set** | [**EnumerationSet1**](EnumerationSet1.md)| The new enumeration set definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_server_create_point**
> data_server_create_point(web_id, point_dto)

Create a point in the specified Data Server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataServerApi()
web_id = 'web_id_example' # str | The ID of the server.
point_dto = swagger_client.PointDTO() # PointDTO | The new point definition.

try: 
    # Create a point in the specified Data Server.
    api_instance.data_server_create_point(web_id, point_dto)
except ApiException as e:
    print("Exception when calling DataServerApi->data_server_create_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **point_dto** | [**PointDTO**](PointDTO.md)| The new point definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_server_get**
> InlineResponse20035Items data_server_get(web_id, selected_fields=selected_fields)

Retrieve a Data Server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataServerApi()
web_id = 'web_id_example' # str | The ID of the server.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a Data Server.
    api_response = api_instance.data_server_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServerApi->data_server_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20035Items**](InlineResponse20035Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_server_get_by_name**
> InlineResponse20035Items data_server_get_by_name(name, selected_fields=selected_fields)

Retrieve a Data Server by name.

This method returns a data server based on the name. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataServerApi()
name = 'name_example' # str | The name of the server.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a Data Server by name.
    api_response = api_instance.data_server_get_by_name(name, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServerApi->data_server_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the server. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20035Items**](InlineResponse20035Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_server_get_by_path**
> InlineResponse20035Items data_server_get_by_path(path, selected_fields=selected_fields)

Retrieve a Data Server by path.

This method returns a data server based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataServerApi()
path = 'path_example' # str | The path to the server. Note that the path supplied to this method must be of the form '\\\\servername'.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a Data Server by path.
    api_response = api_instance.data_server_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServerApi->data_server_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the server. Note that the path supplied to this method must be of the form &#39;\\\\servername&#39;. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20035Items**](InlineResponse20035Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_server_get_enumeration_sets**
> InlineResponse20017 data_server_get_enumeration_sets(web_id, selected_fields=selected_fields)

Retrieve enumeration sets for given Data Server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataServerApi()
web_id = 'web_id_example' # str | The ID of the server.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve enumeration sets for given Data Server.
    api_response = api_instance.data_server_get_enumeration_sets(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServerApi->data_server_get_enumeration_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_server_get_points**
> InlineResponse20036 data_server_get_points(web_id, max_count=max_count, name_filter=name_filter, selected_fields=selected_fields, start_index=start_index)

Retrieve a list of points on a specified Data Server.

Users can search for the data servers based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the data servers that match the default search.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataServerApi()
web_id = 'web_id_example' # str | The ID of the server.
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
name_filter = 'name_filter_example' # str | A query string for filtering by point name. The default is no filter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is '0'. (optional)

try: 
    # Retrieve a list of points on a specified Data Server.
    api_response = api_instance.data_server_get_points(web_id, max_count=max_count, name_filter=name_filter, selected_fields=selected_fields, start_index=start_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServerApi->data_server_get_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **name_filter** | **str**| A query string for filtering by point name. The default is no filter. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is &#39;0&#39;. | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_server_list**
> InlineResponse20035 data_server_list(selected_fields=selected_fields)

Retrieve a list of Data Servers known to this service.

This method returns a list of all available known Data Servers that the user can connect to. Even though a server may be returned in the list, the user may not have permission to access it.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataServerApi()
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a list of Data Servers known to this service.
    api_response = api_instance.data_server_list(selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataServerApi->data_server_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

