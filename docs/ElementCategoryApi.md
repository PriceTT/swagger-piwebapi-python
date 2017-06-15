# swagger_client.ElementCategoryApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**element_category_create_security_entry**](ElementCategoryApi.md#element_category_create_security_entry) | **POST** /elementcategories/{webId}/securityentries | Create a security entry owned by the element category.
[**element_category_delete**](ElementCategoryApi.md#element_category_delete) | **DELETE** /elementcategories/{webId} | Delete an element category.
[**element_category_delete_security_entry**](ElementCategoryApi.md#element_category_delete_security_entry) | **DELETE** /elementcategories/{webId}/securityentries/{name} | Delete a security entry owned by the element category.
[**element_category_get**](ElementCategoryApi.md#element_category_get) | **GET** /elementcategories/{webId} | Retrieve an element category.
[**element_category_get_by_path**](ElementCategoryApi.md#element_category_get_by_path) | **GET** /elementcategories | Retrieve an element category by path.
[**element_category_get_security**](ElementCategoryApi.md#element_category_get_security) | **GET** /elementcategories/{webId}/security | Get the security information of the specified security item associated with the element category for a specified user.
[**element_category_get_security_entries**](ElementCategoryApi.md#element_category_get_security_entries) | **GET** /elementcategories/{webId}/securityentries | Retrieve the security entries associated with the element category based on the specified criteria. By default, all security entries for this element category are returned.
[**element_category_get_security_entry_by_name**](ElementCategoryApi.md#element_category_get_security_entry_by_name) | **GET** /elementcategories/{webId}/securityentries/{name} | Retrieve the security entry associated with the element category with the specified name.
[**element_category_update**](ElementCategoryApi.md#element_category_update) | **PATCH** /elementcategories/{webId} | Update an element category by replacing items in its definition.
[**element_category_update_security_entry**](ElementCategoryApi.md#element_category_update_security_entry) | **PUT** /elementcategories/{webId}/securityentries/{name} | Update a security entry owned by the element category.


# **element_category_create_security_entry**
> element_category_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children)

Create a security entry owned by the element category.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
web_id = 'web_id_example' # str | The ID of the element category where the security entry will be created.
security_entry = swagger_client.SecurityEntry12() # SecurityEntry12 | The new security entry definition. The full list of allow and deny rights must be supplied.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Create a security entry owned by the element category.
    api_instance.element_category_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_create_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element category where the security entry will be created. | 
 **security_entry** | [**SecurityEntry12**](SecurityEntry12.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_category_delete**
> element_category_delete(web_id)

Delete an element category.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
web_id = 'web_id_example' # str | The ID of the element category to delete.

try: 
    # Delete an element category.
    api_instance.element_category_delete(web_id)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element category to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_category_delete_security_entry**
> element_category_delete_security_entry(name, web_id, apply_to_children=apply_to_children)

Delete a security entry owned by the element category.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the element category where the security entry will be deleted.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Delete a security entry owned by the element category.
    api_instance.element_category_delete_security_entry(name, web_id, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_delete_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the element category where the security entry will be deleted. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_category_get**
> InlineResponse20014Items element_category_get(web_id, selected_fields=selected_fields)

Retrieve an element category.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
web_id = 'web_id_example' # str | The id of the element category.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an element category.
    api_response = api_instance.element_category_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The id of the element category. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20014Items**](InlineResponse20014Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_category_get_by_path**
> InlineResponse20014Items element_category_get_by_path(path, selected_fields=selected_fields)

Retrieve an element category by path.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
path = 'path_example' # str | The path to the target element category.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an element category by path.
    api_response = api_instance.element_category_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the target element category. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20014Items**](InlineResponse20014Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_category_get_security**
> InlineResponse2003 element_category_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)

Get the security information of the specified security item associated with the element category for a specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
web_id = 'web_id_example' # str | The ID of the element category for the security to be checked.
user_identity = ['user_identity_example'] # list[str] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
force_refresh = true # bool | Indicates if the security cache should be refreshed before getting security information. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the security information of the specified security item associated with the element category for a specified user.
    api_response = api_instance.element_category_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element category for the security to be checked. | 
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

# **element_category_get_security_entries**
> InlineResponse2004 element_category_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)

Retrieve the security entries associated with the element category based on the specified criteria. By default, all security entries for this element category are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
web_id = 'web_id_example' # str | The ID of the element category.
name_filter = 'name_filter_example' # str | The name query string used for filtering security entries. The default is no filter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entries associated with the element category based on the specified criteria. By default, all security entries for this element category are returned.
    api_response = api_instance.element_category_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_get_security_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element category. | 
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

# **element_category_get_security_entry_by_name**
> InlineResponse2004Items element_category_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)

Retrieve the security entry associated with the element category with the specified name.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the element category.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entry associated with the element category with the specified name.
    api_response = api_instance.element_category_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_get_security_entry_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the element category. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2004Items**](InlineResponse2004Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_category_update**
> element_category_update(web_id, element_category)

Update an element category by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
web_id = 'web_id_example' # str | The ID of the element category to update.
element_category = swagger_client.ElementCategory1() # ElementCategory1 | A partial element category containing the desired changes.

try: 
    # Update an element category by replacing items in its definition.
    api_instance.element_category_update(web_id, element_category)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element category to update. | 
 **element_category** | [**ElementCategory1**](ElementCategory1.md)| A partial element category containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_category_update_security_entry**
> element_category_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children)

Update a security entry owned by the element category.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementCategoryApi()
name = 'name_example' # str | The name of the security entry.
web_id = 'web_id_example' # str | The ID of the element category where the security entry will be updated.
security_entry = swagger_client.SecurityEntry13() # SecurityEntry13 | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Update a security entry owned by the element category.
    api_instance.element_category_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling ElementCategoryApi->element_category_update_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. | 
 **web_id** | **str**| The ID of the element category where the security entry will be updated. | 
 **security_entry** | [**SecurityEntry13**](SecurityEntry13.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

