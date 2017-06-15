# swagger_client.AssetServerApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_server_create_asset_database**](AssetServerApi.md#asset_server_create_asset_database) | **POST** /assetservers/{webId}/assetdatabases | Create an asset database.
[**asset_server_create_security_entry**](AssetServerApi.md#asset_server_create_security_entry) | **POST** /assetservers/{webId}/securityentries | Create a security entry owned by the asset server.
[**asset_server_create_security_identity**](AssetServerApi.md#asset_server_create_security_identity) | **POST** /assetservers/{webId}/securityidentities | Create a security identity.
[**asset_server_create_security_mapping**](AssetServerApi.md#asset_server_create_security_mapping) | **POST** /assetservers/{webId}/securitymappings | Create a security mapping.
[**asset_server_create_unit_class**](AssetServerApi.md#asset_server_create_unit_class) | **POST** /assetservers/{webId}/unitclasses | Create a unit class in the specified Asset Server.
[**asset_server_delete_security_entry**](AssetServerApi.md#asset_server_delete_security_entry) | **DELETE** /assetservers/{webId}/securityentries/{name} | Delete a security entry owned by the asset server.
[**asset_server_get**](AssetServerApi.md#asset_server_get) | **GET** /assetservers/{webId} | Retrieve an Asset Server.
[**asset_server_get_analysis_rule_plug_ins**](AssetServerApi.md#asset_server_get_analysis_rule_plug_ins) | **GET** /assetservers/{webId}/analysisruleplugins | Retrieve a list of all Analysis Rule Plug-in&#39;s.
[**asset_server_get_by_name**](AssetServerApi.md#asset_server_get_by_name) | **GET** /assetservers#name | Retrieve an Asset Server by name.
[**asset_server_get_by_path**](AssetServerApi.md#asset_server_get_by_path) | **GET** /assetservers#path | Retrieve an Asset Server by path.
[**asset_server_get_databases**](AssetServerApi.md#asset_server_get_databases) | **GET** /assetservers/{webId}/assetdatabases | Retrieve a list of all Asset Databases on the specified Asset Server.
[**asset_server_get_security**](AssetServerApi.md#asset_server_get_security) | **GET** /assetservers/{webId}/security | Get the security information of the specified security item associated with the asset server for a specified user.
[**asset_server_get_security_entries**](AssetServerApi.md#asset_server_get_security_entries) | **GET** /assetservers/{webId}/securityentries | Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.
[**asset_server_get_security_entry_by_name**](AssetServerApi.md#asset_server_get_security_entry_by_name) | **GET** /assetservers/{webId}/securityentries/{name} | Retrieve the security entry of the specified security item associated with the asset server with the specified name.
[**asset_server_get_security_identities**](AssetServerApi.md#asset_server_get_security_identities) | **GET** /assetservers/{webId}/securityidentities | Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.
[**asset_server_get_security_identities_for_user**](AssetServerApi.md#asset_server_get_security_identities_for_user) | **GET** /assetservers/{webId}/securityidentities#userIdentity | Retrieve security identities for a specific user.
[**asset_server_get_security_mappings**](AssetServerApi.md#asset_server_get_security_mappings) | **GET** /assetservers/{webId}/securitymappings | Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.
[**asset_server_get_time_rule_plug_ins**](AssetServerApi.md#asset_server_get_time_rule_plug_ins) | **GET** /assetservers/{webId}/timeruleplugins | Retrieve a list of all Time Rule Plug-in&#39;s.
[**asset_server_get_unit_classes**](AssetServerApi.md#asset_server_get_unit_classes) | **GET** /assetservers/{webId}/unitclasses | Retrieve a list of all unit classes on the specified Asset Server.
[**asset_server_list**](AssetServerApi.md#asset_server_list) | **GET** /assetservers | Retrieve a list of all Asset Servers known to this service.
[**asset_server_update_security_entry**](AssetServerApi.md#asset_server_update_security_entry) | **PUT** /assetservers/{webId}/securityentries/{name} | Update a security entry owned by the asset server.


# **asset_server_create_asset_database**
> asset_server_create_asset_database(web_id, database)

Create an asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server on which to create the database.
database = swagger_client.Database1() # Database1 | The new database definition.

try: 
    # Create an asset database.
    api_instance.asset_server_create_asset_database(web_id, database)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_create_asset_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server on which to create the database. | 
 **database** | [**Database1**](Database1.md)| The new database definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_create_security_entry**
> asset_server_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children, security_item=security_item)

Create a security entry owned by the asset server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server where the security entry will be created.
security_entry = swagger_client.SecurityEntry8() # SecurityEntry8 | The new security entry definition. The full list of allow and deny rights must be supplied.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)
security_item = 'security_item_example' # str | The security item of the desired security entries to be created. If the parameter is not specified, security entries of the 'Default' security item will be created. (optional)

try: 
    # Create a security entry owned by the asset server.
    api_instance.asset_server_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children, security_item=security_item)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_create_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server where the security entry will be created. | 
 **security_entry** | [**SecurityEntry8**](SecurityEntry8.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **security_item** | **str**| The security item of the desired security entries to be created. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be created. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_create_security_identity**
> asset_server_create_security_identity(web_id, security_identity)

Create a security identity.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server on which to create the security identity.
security_identity = swagger_client.SecurityIdentity() # SecurityIdentity | The new security identity definition.

try: 
    # Create a security identity.
    api_instance.asset_server_create_security_identity(web_id, security_identity)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_create_security_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server on which to create the security identity. | 
 **security_identity** | [**SecurityIdentity**](SecurityIdentity.md)| The new security identity definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_create_security_mapping**
> asset_server_create_security_mapping(web_id, security_mapping)

Create a security mapping.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server on which to create the security mapping.
security_mapping = swagger_client.SecurityMapping() # SecurityMapping | The new security mapping definition.

try: 
    # Create a security mapping.
    api_instance.asset_server_create_security_mapping(web_id, security_mapping)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_create_security_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server on which to create the security mapping. | 
 **security_mapping** | [**SecurityMapping**](SecurityMapping.md)| The new security mapping definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_create_unit_class**
> asset_server_create_unit_class(web_id, unit_class)

Create a unit class in the specified Asset Server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the server.
unit_class = swagger_client.UnitClass() # UnitClass | The new unit class definition.

try: 
    # Create a unit class in the specified Asset Server.
    api_instance.asset_server_create_unit_class(web_id, unit_class)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_create_unit_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **unit_class** | [**UnitClass**](UnitClass.md)| The new unit class definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_delete_security_entry**
> asset_server_delete_security_entry(name, web_id, apply_to_children=apply_to_children, security_item=security_item)

Delete a security entry owned by the asset server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the asset server where the security entry will be deleted.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)
security_item = 'security_item_example' # str | The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the 'Default' security item will be deleted. (optional)

try: 
    # Delete a security entry owned by the asset server.
    api_instance.asset_server_delete_security_entry(name, web_id, apply_to_children=apply_to_children, security_item=security_item)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_delete_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the asset server where the security entry will be deleted. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **security_item** | **str**| The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be deleted. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get**
> InlineResponse20021Items asset_server_get(web_id, selected_fields=selected_fields)

Retrieve an Asset Server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the server.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Asset Server.
    api_response = api_instance.asset_server_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20021Items**](InlineResponse20021Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_analysis_rule_plug_ins**
> InlineResponse20022 asset_server_get_analysis_rule_plug_ins(web_id, selected_fields=selected_fields)

Retrieve a list of all Analysis Rule Plug-in's.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server, where the Analysis Rule Plug-in's are installed.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a list of all Analysis Rule Plug-in's.
    api_response = api_instance.asset_server_get_analysis_rule_plug_ins(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_analysis_rule_plug_ins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server, where the Analysis Rule Plug-in&#39;s are installed. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_by_name**
> InlineResponse20021Items asset_server_get_by_name(name, selected_fields=selected_fields)

Retrieve an Asset Server by name.

This method returns an asset server based on the name associated with it. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
name = 'name_example' # str | The name of the server.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Asset Server by name.
    api_response = api_instance.asset_server_get_by_name(name, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the server. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20021Items**](InlineResponse20021Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_by_path**
> InlineResponse20021Items asset_server_get_by_path(path, selected_fields=selected_fields)

Retrieve an Asset Server by path.

This method returns an asset server based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
path = 'path_example' # str | The path to the server.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Asset Server by path.
    api_response = api_instance.asset_server_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the server. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20021Items**](InlineResponse20021Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_databases**
> InlineResponse20023 asset_server_get_databases(web_id, selected_fields=selected_fields)

Retrieve a list of all Asset Databases on the specified Asset Server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the server.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a list of all Asset Databases on the specified Asset Server.
    api_response = api_instance.asset_server_get_databases(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_databases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_security**
> InlineResponse2003 asset_server_get_security(web_id, security_item, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)

Get the security information of the specified security item associated with the asset server for a specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server for the security to be checked.
security_item = ['security_item_example'] # list[str] | The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only 'Default' security item of the security information will be returned.
user_identity = ['user_identity_example'] # list[str] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
force_refresh = true # bool | Indicates if the security cache should be refreshed before getting security information. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the security information of the specified security item associated with the asset server for a specified user.
    api_response = api_instance.asset_server_get_security(web_id, security_item, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server for the security to be checked. | 
 **security_item** | [**list[str]**](str.md)| The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only &#39;Default&#39; security item of the security information will be returned. | 
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

# **asset_server_get_security_entries**
> InlineResponse2004 asset_server_get_security_entries(web_id, name_filter=name_filter, security_item=security_item, selected_fields=selected_fields)

Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server.
name_filter = 'name_filter_example' # str | The name query string used for filtering security entries. The default is no filter. (optional)
security_item = 'security_item_example' # str | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.
    api_response = api_instance.asset_server_get_security_entries(web_id, name_filter=name_filter, security_item=security_item, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_security_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server. | 
 **name_filter** | **str**| The name query string used for filtering security entries. The default is no filter. | [optional] 
 **security_item** | **str**| The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_security_entry_by_name**
> InlineResponse2004Items asset_server_get_security_entry_by_name(name, web_id, security_item=security_item, selected_fields=selected_fields)

Retrieve the security entry of the specified security item associated with the asset server with the specified name.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the asset server.
security_item = 'security_item_example' # str | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entry of the specified security item associated with the asset server with the specified name.
    api_response = api_instance.asset_server_get_security_entry_by_name(name, web_id, security_item=security_item, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_security_entry_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the asset server. | 
 **security_item** | **str**| The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2004Items**](InlineResponse2004Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_security_identities**
> InlineResponse20024 asset_server_get_security_identities(web_id, field=field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order)

Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server to search.
field = 'field_example' # str | Specifies which of the object's properties are searched. The default is 'Name'. (optional)
max_count = 56 # int | The maximum number of objects to be returned. The default is 1000. (optional)
query = 'query_example' # str | The query string used for finding objects. The default is no query string. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)

try: 
    # Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.
    api_response = api_instance.asset_server_get_security_identities(web_id, field=field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_security_identities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server to search. | 
 **field** | **str**| Specifies which of the object&#39;s properties are searched. The default is &#39;Name&#39;. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned. The default is 1000. | [optional] 
 **query** | **str**| The query string used for finding objects. The default is no query string. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_security_identities_for_user**
> InlineResponse20024 asset_server_get_security_identities_for_user(web_id, user_identity, selected_fields=selected_fields)

Retrieve security identities for a specific user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the server.
user_identity = 'user_identity_example' # str | The user identity to search for.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve security identities for a specific user.
    api_response = api_instance.asset_server_get_security_identities_for_user(web_id, user_identity, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_security_identities_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **user_identity** | **str**| The user identity to search for. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_security_mappings**
> InlineResponse20025 asset_server_get_security_mappings(web_id, field=field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order)

Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server to search.
field = 'field_example' # str | Specifies which of the object's properties are searched. The default is 'Name'. (optional)
max_count = 56 # int | The maximum number of objects to be returned. The default is 1000. (optional)
query = 'query_example' # str | The query string used for finding objects. The default is no query string. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)

try: 
    # Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.
    api_response = api_instance.asset_server_get_security_mappings(web_id, field=field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_security_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server to search. | 
 **field** | **str**| Specifies which of the object&#39;s properties are searched. The default is &#39;Name&#39;. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned. The default is 1000. | [optional] 
 **query** | **str**| The query string used for finding objects. The default is no query string. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_time_rule_plug_ins**
> InlineResponse20026 asset_server_get_time_rule_plug_ins(web_id, selected_fields=selected_fields)

Retrieve a list of all Time Rule Plug-in's.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the asset server, where the Time Rule Plug-in's are installed.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a list of all Time Rule Plug-in's.
    api_response = api_instance.asset_server_get_time_rule_plug_ins(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_time_rule_plug_ins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset server, where the Time Rule Plug-in&#39;s are installed. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_get_unit_classes**
> InlineResponse20027 asset_server_get_unit_classes(web_id, selected_fields=selected_fields)

Retrieve a list of all unit classes on the specified Asset Server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
web_id = 'web_id_example' # str | The ID of the server.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a list of all unit classes on the specified Asset Server.
    api_response = api_instance.asset_server_get_unit_classes(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_get_unit_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_list**
> InlineResponse20021 asset_server_list(selected_fields=selected_fields)

Retrieve a list of all Asset Servers known to this service.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve a list of all Asset Servers known to this service.
    api_response = api_instance.asset_server_list(selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_server_update_security_entry**
> asset_server_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children, security_item=security_item)

Update a security entry owned by the asset server.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServerApi()
name = 'name_example' # str | The name of the security entry.
web_id = 'web_id_example' # str | The ID of the asset server where the security entry will be updated.
security_entry = swagger_client.SecurityEntry9() # SecurityEntry9 | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)
security_item = 'security_item_example' # str | The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the 'Default' security item will be updated. (optional)

try: 
    # Update a security entry owned by the asset server.
    api_instance.asset_server_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children, security_item=security_item)
except ApiException as e:
    print("Exception when calling AssetServerApi->asset_server_update_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. | 
 **web_id** | **str**| The ID of the asset server where the security entry will be updated. | 
 **security_entry** | [**SecurityEntry9**](SecurityEntry9.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **security_item** | **str**| The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

