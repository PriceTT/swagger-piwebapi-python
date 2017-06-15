# swagger_client.UnitClassApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**unit_class_create_unit**](UnitClassApi.md#unit_class_create_unit) | **POST** /unitclasses/{webId}/units | Create a unit in the specified Unit Class.
[**unit_class_delete**](UnitClassApi.md#unit_class_delete) | **DELETE** /unitclasses/{webId} | Delete a unit class.
[**unit_class_get**](UnitClassApi.md#unit_class_get) | **GET** /unitclasses/{webId} | Retrieve a unit class.
[**unit_class_get_by_path**](UnitClassApi.md#unit_class_get_by_path) | **GET** /unitclasses | Retrieve a unit class by path.
[**unit_class_get_canonical_unit**](UnitClassApi.md#unit_class_get_canonical_unit) | **GET** /unitclasses/{webId}/canonicalunit | Get the canonical unit of a unit class.
[**unit_class_get_units**](UnitClassApi.md#unit_class_get_units) | **GET** /unitclasses/{webId}/units | Get a list of all units belonging to the unit class.
[**unit_class_update**](UnitClassApi.md#unit_class_update) | **PATCH** /unitclasses/{webId} | Update a unit class.


# **unit_class_create_unit**
> unit_class_create_unit(web_id, unit_dto)

Create a unit in the specified Unit Class.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitClassApi()
web_id = 'web_id_example' # str | The ID of the server.
unit_dto = swagger_client.UnitDTO() # UnitDTO | The new unit definition.

try: 
    # Create a unit in the specified Unit Class.
    api_instance.unit_class_create_unit(web_id, unit_dto)
except ApiException as e:
    print("Exception when calling UnitClassApi->unit_class_create_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **unit_dto** | [**UnitDTO**](UnitDTO.md)| The new unit definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unit_class_delete**
> unit_class_delete(web_id)

Delete a unit class.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitClassApi()
web_id = 'web_id_example' # str | The ID of the unit class.

try: 
    # Delete a unit class.
    api_instance.unit_class_delete(web_id)
except ApiException as e:
    print("Exception when calling UnitClassApi->unit_class_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the unit class. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unit_class_get**
> InlineResponse20027Items unit_class_get(web_id, selected_fields=selected_fields)

Retrieve a unit class.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitClassApi()
web_id = 'web_id_example' # str | The ID of the unit class.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a unit class.
    api_response = api_instance.unit_class_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitClassApi->unit_class_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the unit class. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20027Items**](InlineResponse20027Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unit_class_get_by_path**
> InlineResponse20027Items unit_class_get_by_path(path, selected_fields=selected_fields)

Retrieve a unit class by path.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitClassApi()
path = 'path_example' # str | The path to the unit class.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a unit class by path.
    api_response = api_instance.unit_class_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitClassApi->unit_class_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the unit class. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20027Items**](InlineResponse20027Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unit_class_get_canonical_unit**
> InlineResponse20051 unit_class_get_canonical_unit(web_id, selected_fields=selected_fields)

Get the canonical unit of a unit class.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitClassApi()
web_id = 'web_id_example' # str | The ID of unit class.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the canonical unit of a unit class.
    api_response = api_instance.unit_class_get_canonical_unit(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitClassApi->unit_class_get_canonical_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of unit class. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unit_class_get_units**
> InlineResponse20051 unit_class_get_units(web_id, selected_fields=selected_fields)

Get a list of all units belonging to the unit class.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitClassApi()
web_id = 'web_id_example' # str | The ID of unit class.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get a list of all units belonging to the unit class.
    api_response = api_instance.unit_class_get_units(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitClassApi->unit_class_get_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of unit class. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unit_class_update**
> unit_class_update(web_id, unit_class_dto)

Update a unit class.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitClassApi()
web_id = 'web_id_example' # str | The ID of the unit class.
unit_class_dto = swagger_client.UnitClassDTO() # UnitClassDTO | A partial unit class containing the desired changes.

try: 
    # Update a unit class.
    api_instance.unit_class_update(web_id, unit_class_dto)
except ApiException as e:
    print("Exception when calling UnitClassApi->unit_class_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the unit class. | 
 **unit_class_dto** | [**UnitClassDTO**](UnitClassDTO.md)| A partial unit class containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

