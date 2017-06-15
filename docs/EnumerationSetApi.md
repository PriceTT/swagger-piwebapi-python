# swagger_client.EnumerationSetApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enumeration_set_create_security_entry**](EnumerationSetApi.md#enumeration_set_create_security_entry) | **POST** /enumerationsets/{webId}/securityentries | Create a security entry owned by the enumeration set.
[**enumeration_set_create_value**](EnumerationSetApi.md#enumeration_set_create_value) | **POST** /enumerationsets/{webId}/enumerationvalues | Create an enumeration value for a enumeration set.
[**enumeration_set_delete**](EnumerationSetApi.md#enumeration_set_delete) | **DELETE** /enumerationsets/{webId} | Delete an enumeration set.
[**enumeration_set_delete_security_entry**](EnumerationSetApi.md#enumeration_set_delete_security_entry) | **DELETE** /enumerationsets/{webId}/securityentries/{name} | Delete a security entry owned by the enumeration set.
[**enumeration_set_get**](EnumerationSetApi.md#enumeration_set_get) | **GET** /enumerationsets/{webId} | Retrieve an enumeration set.
[**enumeration_set_get_by_path**](EnumerationSetApi.md#enumeration_set_get_by_path) | **GET** /enumerationsets | Retrieve an enumeration set by path.
[**enumeration_set_get_security**](EnumerationSetApi.md#enumeration_set_get_security) | **GET** /enumerationsets/{webId}/security | Get the security information of the specified security item associated with the enumeration set for a specified user.
[**enumeration_set_get_security_entries**](EnumerationSetApi.md#enumeration_set_get_security_entries) | **GET** /enumerationsets/{webId}/securityentries | Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.
[**enumeration_set_get_security_entry_by_name**](EnumerationSetApi.md#enumeration_set_get_security_entry_by_name) | **GET** /enumerationsets/{webId}/securityentries/{name} | Retrieve the security entry associated with the enumeration set with the specified name.
[**enumeration_set_get_values**](EnumerationSetApi.md#enumeration_set_get_values) | **GET** /enumerationsets/{webId}/enumerationvalues | Retrieve an enumeration set&#39;s values.
[**enumeration_set_update**](EnumerationSetApi.md#enumeration_set_update) | **PATCH** /enumerationsets/{webId} | Update an enumeration set by replacing items in its definition.
[**enumeration_set_update_security_entry**](EnumerationSetApi.md#enumeration_set_update_security_entry) | **PUT** /enumerationsets/{webId}/securityentries/{name} | Update a security entry owned by the enumeration set.


# **enumeration_set_create_security_entry**
> enumeration_set_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children)

Create a security entry owned by the enumeration set.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
web_id = 'web_id_example' # str | The ID of the enumeration set where the security entry will be created.
security_entry = swagger_client.SecurityEntry18() # SecurityEntry18 | The new security entry definition. The full list of allow and deny rights must be supplied.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Create a security entry owned by the enumeration set.
    api_instance.enumeration_set_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_create_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set where the security entry will be created. | 
 **security_entry** | [**SecurityEntry18**](SecurityEntry18.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_create_value**
> enumeration_set_create_value(web_id, enumeration_value)

Create an enumeration value for a enumeration set.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
web_id = 'web_id_example' # str | The ID of the enumeration set on which to create the enumeration value.
enumeration_value = swagger_client.EnumerationValue() # EnumerationValue | The new enumeration value definition.

try: 
    # Create an enumeration value for a enumeration set.
    api_instance.enumeration_set_create_value(web_id, enumeration_value)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_create_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set on which to create the enumeration value. | 
 **enumeration_value** | [**EnumerationValue**](EnumerationValue.md)| The new enumeration value definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_delete**
> enumeration_set_delete(web_id)

Delete an enumeration set.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
web_id = 'web_id_example' # str | The ID of the enumeration set to delete.

try: 
    # Delete an enumeration set.
    api_instance.enumeration_set_delete(web_id)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_delete_security_entry**
> enumeration_set_delete_security_entry(name, web_id, apply_to_children=apply_to_children)

Delete a security entry owned by the enumeration set.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the enumeration set where the security entry will be deleted.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Delete a security entry owned by the enumeration set.
    api_instance.enumeration_set_delete_security_entry(name, web_id, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_delete_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the enumeration set where the security entry will be deleted. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_get**
> InlineResponse20017Items enumeration_set_get(web_id, selected_fields=selected_fields)

Retrieve an enumeration set.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
web_id = 'web_id_example' # str | The ID of the enumeration set.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an enumeration set.
    api_response = api_instance.enumeration_set_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20017Items**](InlineResponse20017Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_get_by_path**
> InlineResponse20017Items enumeration_set_get_by_path(path, selected_fields=selected_fields)

Retrieve an enumeration set by path.

This method returns an enumeration set based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
path = 'path_example' # str | The path to the target enumeration set.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an enumeration set by path.
    api_response = api_instance.enumeration_set_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the target enumeration set. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20017Items**](InlineResponse20017Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_get_security**
> InlineResponse2003 enumeration_set_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)

Get the security information of the specified security item associated with the enumeration set for a specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
web_id = 'web_id_example' # str | The ID of the enumeration set for the security to be checked.
user_identity = ['user_identity_example'] # list[str] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
force_refresh = true # bool | Indicates if the security cache should be refreshed before getting security information. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the security information of the specified security item associated with the enumeration set for a specified user.
    api_response = api_instance.enumeration_set_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set for the security to be checked. | 
 **user_identity** | [**list[str]**](str.md)| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user&#39;s security rights will be returned. | 
 **force_refresh** | **bool**| Indicates if the security cache should be refreshed before getting security information. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_get_security_entries**
> InlineResponse2004 enumeration_set_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)

Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
web_id = 'web_id_example' # str | The ID of the enumeration set.
name_filter = 'name_filter_example' # str | The name query string used for filtering security entries. The default is no filter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.
    api_response = api_instance.enumeration_set_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_get_security_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set. | 
 **name_filter** | **str**| The name query string used for filtering security entries. The default is no filter. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_get_security_entry_by_name**
> InlineResponse2004Items enumeration_set_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)

Retrieve the security entry associated with the enumeration set with the specified name.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the enumeration set.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entry associated with the enumeration set with the specified name.
    api_response = api_instance.enumeration_set_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_get_security_entry_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the enumeration set. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2004Items**](InlineResponse2004Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_get_values**
> InlineResponse20038 enumeration_set_get_values(web_id, selected_fields=selected_fields)

Retrieve an enumeration set's values.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
web_id = 'web_id_example' # str | The ID of the enumeration set.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an enumeration set's values.
    api_response = api_instance.enumeration_set_get_values(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_get_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_update**
> enumeration_set_update(web_id, enumeration_set)

Update an enumeration set by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
web_id = 'web_id_example' # str | The ID of the enumeration set to update.
enumeration_set = swagger_client.EnumerationSet2() # EnumerationSet2 | A partial enumeration set containing the desired changes.

try: 
    # Update an enumeration set by replacing items in its definition.
    api_instance.enumeration_set_update(web_id, enumeration_set)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set to update. | 
 **enumeration_set** | [**EnumerationSet2**](EnumerationSet2.md)| A partial enumeration set containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumeration_set_update_security_entry**
> enumeration_set_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children)

Update a security entry owned by the enumeration set.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnumerationSetApi()
name = 'name_example' # str | The name of the security entry.
web_id = 'web_id_example' # str | The ID of the enumeration set where the security entry will be updated.
security_entry = swagger_client.SecurityEntry19() # SecurityEntry19 | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Update a security entry owned by the enumeration set.
    api_instance.enumeration_set_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling EnumerationSetApi->enumeration_set_update_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. | 
 **web_id** | **str**| The ID of the enumeration set where the security entry will be updated. | 
 **security_entry** | [**SecurityEntry19**](SecurityEntry19.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

