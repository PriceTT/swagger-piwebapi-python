# swagger_client.ElementTemplateApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**element_template_create_attribute_template**](ElementTemplateApi.md#element_template_create_attribute_template) | **POST** /elementtemplates/{webId}/attributetemplates | Create an attribute template.
[**element_template_create_security_entry**](ElementTemplateApi.md#element_template_create_security_entry) | **POST** /elementtemplates/{webId}/securityentries | Create a security entry owned by the element template.
[**element_template_delete**](ElementTemplateApi.md#element_template_delete) | **DELETE** /elementtemplates/{webId} | Delete an element template.
[**element_template_delete_security_entry**](ElementTemplateApi.md#element_template_delete_security_entry) | **DELETE** /elementtemplates/{webId}/securityentries/{name} | Delete a security entry owned by the element template.
[**element_template_get**](ElementTemplateApi.md#element_template_get) | **GET** /elementtemplates/{webId} | Retrieve an element template.
[**element_template_get_analysis_templates**](ElementTemplateApi.md#element_template_get_analysis_templates) | **GET** /elementtemplates/{webId}/analysistemplates | Get analysis templates for an element template.
[**element_template_get_attribute_templates**](ElementTemplateApi.md#element_template_get_attribute_templates) | **GET** /elementtemplates/{webId}/attributetemplates | Get child attribute templates for an element template.
[**element_template_get_by_path**](ElementTemplateApi.md#element_template_get_by_path) | **GET** /elementtemplates | Retrieve an element template by path.
[**element_template_get_categories**](ElementTemplateApi.md#element_template_get_categories) | **GET** /elementtemplates/{webId}/categories | Get an element template&#39;s categories.
[**element_template_get_security**](ElementTemplateApi.md#element_template_get_security) | **GET** /elementtemplates/{webId}/security | Get the security information of the specified security item associated with the element template for a specified user.
[**element_template_get_security_entries**](ElementTemplateApi.md#element_template_get_security_entries) | **GET** /elementtemplates/{webId}/securityentries | Retrieve the security entries associated with the element template based on the specified criteria. By default, all security entries for this element template are returned.
[**element_template_get_security_entry_by_name**](ElementTemplateApi.md#element_template_get_security_entry_by_name) | **GET** /elementtemplates/{webId}/securityentries/{name} | Retrieve the security entry associated with the element template with the specified name.
[**element_template_update**](ElementTemplateApi.md#element_template_update) | **PATCH** /elementtemplates/{webId} | Update an element template by replacing items in its definition.
[**element_template_update_security_entry**](ElementTemplateApi.md#element_template_update_security_entry) | **PUT** /elementtemplates/{webId}/securityentries/{name} | Update a security entry owned by the element template.


# **element_template_create_attribute_template**
> element_template_create_attribute_template(web_id, template)

Create an attribute template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template on which to create the attribute template.
template = swagger_client.Template6() # Template6 | The attribute template definition.

try: 
    # Create an attribute template.
    api_instance.element_template_create_attribute_template(web_id, template)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_create_attribute_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template on which to create the attribute template. | 
 **template** | [**Template6**](Template6.md)| The attribute template definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_create_security_entry**
> element_template_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children)

Create a security entry owned by the element template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template where the security entry will be created.
security_entry = swagger_client.SecurityEntry16() # SecurityEntry16 | The new security entry definition. The full list of allow and deny rights must be supplied.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Create a security entry owned by the element template.
    api_instance.element_template_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_create_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template where the security entry will be created. | 
 **security_entry** | [**SecurityEntry16**](SecurityEntry16.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_delete**
> element_template_delete(web_id)

Delete an element template.

Deleting an element template will delete all associated templated data from elements which were created from it.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template to update.

try: 
    # Delete an element template.
    api_instance.element_template_delete(web_id)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template to update. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_delete_security_entry**
> element_template_delete_security_entry(name, web_id, apply_to_children=apply_to_children)

Delete a security entry owned by the element template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the element template where the security entry will be deleted.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Delete a security entry owned by the element template.
    api_instance.element_template_delete_security_entry(name, web_id, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_delete_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the element template where the security entry will be deleted. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_get**
> InlineResponse20016Items element_template_get(web_id, selected_fields=selected_fields)

Retrieve an element template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an element template.
    api_response = api_instance.element_template_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20016Items**](InlineResponse20016Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_get_analysis_templates**
> InlineResponse20011 element_template_get_analysis_templates(web_id, selected_fields=selected_fields)

Get analysis templates for an element template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get analysis templates for an element template.
    api_response = api_instance.element_template_get_analysis_templates(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_get_analysis_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_get_attribute_templates**
> InlineResponse20031 element_template_get_attribute_templates(web_id, selected_fields=selected_fields, show_inherited=show_inherited)

Get child attribute templates for an element template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_inherited = true # bool | Specifies if the result should include attribute templates inherited from base element templates. The default is 'false'. (optional)

try: 
    # Get child attribute templates for an element template.
    api_response = api_instance.element_template_get_attribute_templates(web_id, selected_fields=selected_fields, show_inherited=show_inherited)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_get_attribute_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_inherited** | **bool**| Specifies if the result should include attribute templates inherited from base element templates. The default is &#39;false&#39;. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_get_by_path**
> InlineResponse20016Items element_template_get_by_path(path, selected_fields=selected_fields)

Retrieve an element template by path.

This method returns an element template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
path = 'path_example' # str | The path to the element template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an element template by path.
    api_response = api_instance.element_template_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the element template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20016Items**](InlineResponse20016Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_get_categories**
> InlineResponse20014 element_template_get_categories(web_id, selected_fields=selected_fields, show_inherited=show_inherited)

Get an element template's categories.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_inherited = true # bool | Specifies if the result should include categories inherited from base element templates. The default is 'false'. (optional)

try: 
    # Get an element template's categories.
    api_response = api_instance.element_template_get_categories(web_id, selected_fields=selected_fields, show_inherited=show_inherited)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_inherited** | **bool**| Specifies if the result should include categories inherited from base element templates. The default is &#39;false&#39;. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_get_security**
> InlineResponse2003 element_template_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)

Get the security information of the specified security item associated with the element template for a specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template for the security to be checked.
user_identity = ['user_identity_example'] # list[str] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
force_refresh = true # bool | Indicates if the security cache should be refreshed before getting security information. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the security information of the specified security item associated with the element template for a specified user.
    api_response = api_instance.element_template_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template for the security to be checked. | 
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

# **element_template_get_security_entries**
> InlineResponse2004 element_template_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)

Retrieve the security entries associated with the element template based on the specified criteria. By default, all security entries for this element template are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template.
name_filter = 'name_filter_example' # str | The name query string used for filtering security entries. The default is no filter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entries associated with the element template based on the specified criteria. By default, all security entries for this element template are returned.
    api_response = api_instance.element_template_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_get_security_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template. | 
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

# **element_template_get_security_entry_by_name**
> InlineResponse2004 element_template_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)

Retrieve the security entry associated with the element template with the specified name.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the element template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entry associated with the element template with the specified name.
    api_response = api_instance.element_template_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_get_security_entry_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the element template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_update**
> element_template_update(web_id, template)

Update an element template by replacing items in its definition.

Updating the InstanceType property of an element template will not affect any elements that have already been created from this template; it will only affect any future elements created from this template. All other changes will be propagated to elements based on this template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
web_id = 'web_id_example' # str | The ID of the element template to update.
template = swagger_client.Template5() # Template5 | A partial element template containing the desired changes.

try: 
    # Update an element template by replacing items in its definition.
    api_instance.element_template_update(web_id, template)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element template to update. | 
 **template** | [**Template5**](Template5.md)| A partial element template containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **element_template_update_security_entry**
> element_template_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children)

Update a security entry owned by the element template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementTemplateApi()
name = 'name_example' # str | The name of the security entry.
web_id = 'web_id_example' # str | The ID of the element template where the security entry will be updated.
security_entry = swagger_client.SecurityEntry17() # SecurityEntry17 | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Update a security entry owned by the element template.
    api_instance.element_template_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling ElementTemplateApi->element_template_update_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. | 
 **web_id** | **str**| The ID of the element template where the security entry will be updated. | 
 **security_entry** | [**SecurityEntry17**](SecurityEntry17.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

