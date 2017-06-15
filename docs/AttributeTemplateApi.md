# swagger_client.AttributeTemplateApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attribute_template_create_attribute_template**](AttributeTemplateApi.md#attribute_template_create_attribute_template) | **POST** /attributetemplates/{webId}/attributetemplates | Create an attribute template as a child of another attribute template.
[**attribute_template_delete**](AttributeTemplateApi.md#attribute_template_delete) | **DELETE** /attributetemplates/{webId} | Delete an attribute template.
[**attribute_template_get**](AttributeTemplateApi.md#attribute_template_get) | **GET** /attributetemplates/{webId} | Retrieve an attribute template.
[**attribute_template_get_attribute_templates**](AttributeTemplateApi.md#attribute_template_get_attribute_templates) | **GET** /attributetemplates/{webId}/attributetemplates | Retrieve an attribute template&#39;s child attribute templates.
[**attribute_template_get_by_path**](AttributeTemplateApi.md#attribute_template_get_by_path) | **GET** /attributetemplates | Retrieve an attribute template by path.
[**attribute_template_get_categories**](AttributeTemplateApi.md#attribute_template_get_categories) | **GET** /attributetemplates/{webId}/categories | Get an attribute template&#39;s categories.
[**attribute_template_update**](AttributeTemplateApi.md#attribute_template_update) | **PATCH** /attributetemplates/{webId} | Update an existing attribute template by replacing items in its definition.


# **attribute_template_create_attribute_template**
> attribute_template_create_attribute_template(web_id, template)

Create an attribute template as a child of another attribute template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTemplateApi()
web_id = 'web_id_example' # str | The ID of the parent attribute template on which to create the attribute template.
template = swagger_client.Template4() # Template4 | The attribute template definition.

try: 
    # Create an attribute template as a child of another attribute template.
    api_instance.attribute_template_create_attribute_template(web_id, template)
except ApiException as e:
    print("Exception when calling AttributeTemplateApi->attribute_template_create_attribute_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent attribute template on which to create the attribute template. | 
 **template** | [**Template4**](Template4.md)| The attribute template definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_template_delete**
> attribute_template_delete(web_id)

Delete an attribute template.

Deleting an attribute template will delete the attributes that were created based on the template

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTemplateApi()
web_id = 'web_id_example' # str | The ID of the attribute template.

try: 
    # Delete an attribute template.
    api_instance.attribute_template_delete(web_id)
except ApiException as e:
    print("Exception when calling AttributeTemplateApi->attribute_template_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_template_get**
> InlineResponse20030 attribute_template_get(web_id, selected_fields=selected_fields)

Retrieve an attribute template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTemplateApi()
web_id = 'web_id_example' # str | The ID of the attribute template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an attribute template.
    api_response = api_instance.attribute_template_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTemplateApi->attribute_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_template_get_attribute_templates**
> InlineResponse20031 attribute_template_get_attribute_templates(web_id, selected_fields=selected_fields)

Retrieve an attribute template's child attribute templates.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTemplateApi()
web_id = 'web_id_example' # str | The ID of the attribute template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an attribute template's child attribute templates.
    api_response = api_instance.attribute_template_get_attribute_templates(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTemplateApi->attribute_template_get_attribute_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_template_get_by_path**
> InlineResponse20030 attribute_template_get_by_path(path, selected_fields=selected_fields)

Retrieve an attribute template by path.

This method returns an attribute template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTemplateApi()
path = 'path_example' # str | The path to the attribute template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an attribute template by path.
    api_response = api_instance.attribute_template_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTemplateApi->attribute_template_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the attribute template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_template_get_categories**
> InlineResponse20012 attribute_template_get_categories(web_id, selected_fields=selected_fields)

Get an attribute template's categories.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTemplateApi()
web_id = 'web_id_example' # str | The ID of the attribute template.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get an attribute template's categories.
    api_response = api_instance.attribute_template_get_categories(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTemplateApi->attribute_template_get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_template_update**
> attribute_template_update(web_id, template)

Update an existing attribute template by replacing items in its definition.

Updating an attribute template will propagate changes to the attributes that were created based on the template

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTemplateApi()
web_id = 'web_id_example' # str | The ID of the attribute template.
template = swagger_client.Template3() # Template3 | A partial attribute template containing the desired changes.

try: 
    # Update an existing attribute template by replacing items in its definition.
    api_instance.attribute_template_update(web_id, template)
except ApiException as e:
    print("Exception when calling AttributeTemplateApi->attribute_template_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template. | 
 **template** | [**Template3**](Template3.md)| A partial attribute template containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

