# swagger_client.SecurityMappingApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**security_mapping_delete**](SecurityMappingApi.md#security_mapping_delete) | **DELETE** /securitymappings/{webId} | Delete a security mapping.
[**security_mapping_get**](SecurityMappingApi.md#security_mapping_get) | **GET** /securitymappings/{webId} | Retrieve a security mapping.
[**security_mapping_get_by_path**](SecurityMappingApi.md#security_mapping_get_by_path) | **GET** /securitymappings | Retrieve a security mapping by path.
[**security_mapping_get_security**](SecurityMappingApi.md#security_mapping_get_security) | **GET** /securitymappings/{webId}/security | Get the security information of the specified security item associated with the security mapping for a specified user.
[**security_mapping_get_security_entries**](SecurityMappingApi.md#security_mapping_get_security_entries) | **GET** /securitymappings/{webId}/securityentries | Retrieve the security entries associated with the security mapping based on the specified criteria. By default, all security entries for this security mapping are returned.
[**security_mapping_get_security_entry_by_name**](SecurityMappingApi.md#security_mapping_get_security_entry_by_name) | **GET** /securitymappings/{webId}/securityentries/{name} | Retrieve the security entry associated with the security mapping with the specified name.
[**security_mapping_update**](SecurityMappingApi.md#security_mapping_update) | **PATCH** /securitymappings/{webId} | Update a security mapping by replacing items in its definition.


# **security_mapping_delete**
> security_mapping_delete(web_id)

Delete a security mapping.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityMappingApi()
web_id = 'web_id_example' # str | The ID of the security mapping.

try: 
    # Delete a security mapping.
    api_instance.security_mapping_delete(web_id)
except ApiException as e:
    print("Exception when calling SecurityMappingApi->security_mapping_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the security mapping. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_mapping_get**
> InlineResponse20025Items security_mapping_get(web_id, selected_fields=selected_fields)

Retrieve a security mapping.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityMappingApi()
web_id = 'web_id_example' # str | The ID of the security mapping.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a security mapping.
    api_response = api_instance.security_mapping_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityMappingApi->security_mapping_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the security mapping. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20025Items**](InlineResponse20025Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_mapping_get_by_path**
> InlineResponse20025Items security_mapping_get_by_path(path, selected_fields=selected_fields)

Retrieve a security mapping by path.

This method returns a security mapping based on the path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityMappingApi()
path = 'path_example' # str | The path to the security mapping.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a security mapping by path.
    api_response = api_instance.security_mapping_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityMappingApi->security_mapping_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the security mapping. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20025Items**](InlineResponse20025Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_mapping_get_security**
> InlineResponse2003 security_mapping_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)

Get the security information of the specified security item associated with the security mapping for a specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityMappingApi()
web_id = 'web_id_example' # str | The ID of the security mapping for the security to be checked.
user_identity = ['user_identity_example'] # list[str] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
force_refresh = true # bool | Indicates if the security cache should be refreshed before getting security information. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the security information of the specified security item associated with the security mapping for a specified user.
    api_response = api_instance.security_mapping_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityMappingApi->security_mapping_get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the security mapping for the security to be checked. | 
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

# **security_mapping_get_security_entries**
> InlineResponse2004 security_mapping_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)

Retrieve the security entries associated with the security mapping based on the specified criteria. By default, all security entries for this security mapping are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityMappingApi()
web_id = 'web_id_example' # str | The ID of the security mapping.
name_filter = 'name_filter_example' # str | The name query string used for filtering security entries. The default is no filter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entries associated with the security mapping based on the specified criteria. By default, all security entries for this security mapping are returned.
    api_response = api_instance.security_mapping_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityMappingApi->security_mapping_get_security_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the security mapping. | 
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

# **security_mapping_get_security_entry_by_name**
> InlineResponse2004Items security_mapping_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)

Retrieve the security entry associated with the security mapping with the specified name.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityMappingApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the security mapping.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entry associated with the security mapping with the specified name.
    api_response = api_instance.security_mapping_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityMappingApi->security_mapping_get_security_entry_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the security mapping. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2004Items**](InlineResponse2004Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_mapping_update**
> security_mapping_update(web_id, security_mapping)

Update a security mapping by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityMappingApi()
web_id = 'web_id_example' # str | The ID of the security mapping.
security_mapping = swagger_client.SecurityMapping1() # SecurityMapping1 | A partial security mapping containing the desired changes.

try: 
    # Update a security mapping by replacing items in its definition.
    api_instance.security_mapping_update(web_id, security_mapping)
except ApiException as e:
    print("Exception when calling SecurityMappingApi->security_mapping_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the security mapping. | 
 **security_mapping** | [**SecurityMapping1**](SecurityMapping1.md)| A partial security mapping containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

