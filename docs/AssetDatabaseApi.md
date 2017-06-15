# swagger_client.AssetDatabaseApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_database_add_referenced_element**](AssetDatabaseApi.md#asset_database_add_referenced_element) | **POST** /assetdatabases/{webId}/referencedelements | Add a reference to an existing element to the specified database.
[**asset_database_create_analysis_category**](AssetDatabaseApi.md#asset_database_create_analysis_category) | **POST** /assetdatabases/{webId}/analysiscategories | Create an analysis category at the Asset Database root.
[**asset_database_create_analysis_template**](AssetDatabaseApi.md#asset_database_create_analysis_template) | **POST** /assetdatabases/{webId}/analysistemplates | Create an analysis template at the Asset Database root.
[**asset_database_create_attribute_category**](AssetDatabaseApi.md#asset_database_create_attribute_category) | **POST** /assetdatabases/{webId}/attributecategories | Create an attribute category at the Asset Database root.
[**asset_database_create_element**](AssetDatabaseApi.md#asset_database_create_element) | **POST** /assetdatabases/{webId}/elements | Create a child element.
[**asset_database_create_element_category**](AssetDatabaseApi.md#asset_database_create_element_category) | **POST** /assetdatabases/{webId}/elementcategories | Create an element category at the Asset Database root.
[**asset_database_create_element_template**](AssetDatabaseApi.md#asset_database_create_element_template) | **POST** /assetdatabases/{webId}/elementtemplates | Create a template at the Asset Database root. Specify InstanceType of \&quot;Element\&quot; or \&quot;EventFrame\&quot; to create element or event frame template respectively. Only these two types of templates can be created.
[**asset_database_create_enumeration_set**](AssetDatabaseApi.md#asset_database_create_enumeration_set) | **POST** /assetdatabases/{webId}/enumerationsets | Create an enumeration set at the Asset Database.
[**asset_database_create_event_frame**](AssetDatabaseApi.md#asset_database_create_event_frame) | **POST** /assetdatabases/{webId}/eventframes | Create an event frame.
[**asset_database_create_security_entry**](AssetDatabaseApi.md#asset_database_create_security_entry) | **POST** /assetdatabases/{webId}/securityentries | Create a security entry owned by the asset database.
[**asset_database_create_table**](AssetDatabaseApi.md#asset_database_create_table) | **POST** /assetdatabases/{webId}/tables | Create a table on the Asset Database.
[**asset_database_create_table_category**](AssetDatabaseApi.md#asset_database_create_table_category) | **POST** /assetdatabases/{webId}/tablecategories | Create a table category on the Asset Database.
[**asset_database_delete**](AssetDatabaseApi.md#asset_database_delete) | **DELETE** /assetdatabases/{webId} | Delete an asset database.
[**asset_database_delete_security_entry**](AssetDatabaseApi.md#asset_database_delete_security_entry) | **DELETE** /assetdatabases/{webId}/securityentries/{name} | Delete a security entry owned by the asset database.
[**asset_database_export**](AssetDatabaseApi.md#asset_database_export) | **GET** /assetdatabases/{webId}/export | Export the asset database.
[**asset_database_find_analyses**](AssetDatabaseApi.md#asset_database_find_analyses) | **GET** /assetdatabases/{webId}/analyses | Retrieve analyses based on the specified conditions.
[**asset_database_find_element_attributes**](AssetDatabaseApi.md#asset_database_find_element_attributes) | **GET** /assetdatabases/{webId}/elementattributes | Retrieves a list of element attributes matching the specified filters from the specified asset database.
[**asset_database_find_event_frame_attributes**](AssetDatabaseApi.md#asset_database_find_event_frame_attributes) | **GET** /assetdatabases/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified asset database.
[**asset_database_get**](AssetDatabaseApi.md#asset_database_get) | **GET** /assetdatabases/{webId} | Retrieve an Asset Database.
[**asset_database_get_analysis_categories**](AssetDatabaseApi.md#asset_database_get_analysis_categories) | **GET** /assetdatabases/{webId}/analysiscategories | Retrieve analysis categories for a given Asset Database.
[**asset_database_get_analysis_templates**](AssetDatabaseApi.md#asset_database_get_analysis_templates) | **GET** /assetdatabases/{webId}/analysistemplates | Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.
[**asset_database_get_attribute_categories**](AssetDatabaseApi.md#asset_database_get_attribute_categories) | **GET** /assetdatabases/{webId}/attributecategories | Retrieve attribute categories for a given Asset Database.
[**asset_database_get_by_path**](AssetDatabaseApi.md#asset_database_get_by_path) | **GET** /assetdatabases | Retrieve an Asset Database by path.
[**asset_database_get_element_categories**](AssetDatabaseApi.md#asset_database_get_element_categories) | **GET** /assetdatabases/{webId}/elementcategories | Retrieve element categories for a given Asset Database.
[**asset_database_get_element_templates**](AssetDatabaseApi.md#asset_database_get_element_templates) | **GET** /assetdatabases/{webId}/elementtemplates | Retrieve element templates based on the specified criteria. Only templates of instance type \&quot;Element\&quot; and \&quot;EventFrame\&quot; are returned. By default, all element and event frame templates in the specified Asset Database are returned.
[**asset_database_get_elements**](AssetDatabaseApi.md#asset_database_get_elements) | **GET** /assetdatabases/{webId}/elements | Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.
[**asset_database_get_enumeration_sets**](AssetDatabaseApi.md#asset_database_get_enumeration_sets) | **GET** /assetdatabases/{webId}/enumerationsets | Retrieve enumeration sets for given asset database.
[**asset_database_get_event_frames**](AssetDatabaseApi.md#asset_database_get_event_frames) | **GET** /assetdatabases/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource with a start time in the past 8 hours.
[**asset_database_get_referenced_elements**](AssetDatabaseApi.md#asset_database_get_referenced_elements) | **GET** /assetdatabases/{webId}/referencedelements | Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.
[**asset_database_get_security**](AssetDatabaseApi.md#asset_database_get_security) | **GET** /assetdatabases/{webId}/security | Get the security information of the specified security item associated with the asset database for a specified user.
[**asset_database_get_security_entries**](AssetDatabaseApi.md#asset_database_get_security_entries) | **GET** /assetdatabases/{webId}/securityentries | Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.
[**asset_database_get_security_entry_by_name**](AssetDatabaseApi.md#asset_database_get_security_entry_by_name) | **GET** /assetdatabases/{webId}/securityentries/{name} | Retrieve the security entry of the specified security item associated with the asset database with the specified name.
[**asset_database_get_table_categories**](AssetDatabaseApi.md#asset_database_get_table_categories) | **GET** /assetdatabases/{webId}/tablecategories | Retrieve table categories for a given Asset Database.
[**asset_database_get_tables**](AssetDatabaseApi.md#asset_database_get_tables) | **GET** /assetdatabases/{webId}/tables | Retrieve tables for given Asset Database.
[**asset_database_import**](AssetDatabaseApi.md#asset_database_import) | **POST** /assetdatabases/{webId}/import | Import an asset database.
[**asset_database_remove_referenced_element**](AssetDatabaseApi.md#asset_database_remove_referenced_element) | **DELETE** /assetdatabases/{webId}/referencedelements | Remove a reference to an existing element from the specified database.
[**asset_database_update**](AssetDatabaseApi.md#asset_database_update) | **PATCH** /assetdatabases/{webId} | Update an asset database by replacing items in its definition.
[**asset_database_update_security_entry**](AssetDatabaseApi.md#asset_database_update_security_entry) | **PUT** /assetdatabases/{webId}/securityentries/{name} | Update a security entry owned by the asset database.


# **asset_database_add_referenced_element**
> asset_database_add_referenced_element(web_id, referenced_element_web_id, reference_type=reference_type)

Add a reference to an existing element to the specified database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database which the referenced element will be added to.
referenced_element_web_id = ['referenced_element_web_id_example'] # list[str] | The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
reference_type = 'reference_type_example' # str | The name of the reference type between the parent and the referenced element. This must be a \"strong\" reference type. The default is \"parent-child\". (optional)

try: 
    # Add a reference to an existing element to the specified database.
    api_instance.asset_database_add_referenced_element(web_id, referenced_element_web_id, reference_type=reference_type)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_add_referenced_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database which the referenced element will be added to. | 
 **referenced_element_web_id** | [**list[str]**](str.md)| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter. | 
 **reference_type** | **str**| The name of the reference type between the parent and the referenced element. This must be a \&quot;strong\&quot; reference type. The default is \&quot;parent-child\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_analysis_category**
> asset_database_create_analysis_category(web_id, analysis_category)

Create an analysis category at the Asset Database root.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database in which to create the analysis category.
analysis_category = swagger_client.AnalysisCategory() # AnalysisCategory | The new analysis category definition.

try: 
    # Create an analysis category at the Asset Database root.
    api_instance.asset_database_create_analysis_category(web_id, analysis_category)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_analysis_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the analysis category. | 
 **analysis_category** | [**AnalysisCategory**](AnalysisCategory.md)| The new analysis category definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_analysis_template**
> asset_database_create_analysis_template(web_id, template)

Create an analysis template at the Asset Database root.

Analyses that are based on an analysis template will inherit characteristics defined in the template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database in which to create the analysis template.
template = swagger_client.Template1() # Template1 | The new analysis template definition.

try: 
    # Create an analysis template at the Asset Database root.
    api_instance.asset_database_create_analysis_template(web_id, template)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_analysis_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the analysis template. | 
 **template** | [**Template1**](Template1.md)| The new analysis template definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_attribute_category**
> asset_database_create_attribute_category(web_id, attribute_category)

Create an attribute category at the Asset Database root.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database in which to create the attribute category.
attribute_category = swagger_client.AttributeCategory() # AttributeCategory | The new attribute category definition.

try: 
    # Create an attribute category at the Asset Database root.
    api_instance.asset_database_create_attribute_category(web_id, attribute_category)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_attribute_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the attribute category. | 
 **attribute_category** | [**AttributeCategory**](AttributeCategory.md)| The new attribute category definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_element**
> asset_database_create_element(web_id, element)

Create a child element.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the asset database on which to create the element.
element = swagger_client.Element() # Element | The new element definition.

try: 
    # Create a child element.
    api_instance.asset_database_create_element(web_id, element)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database on which to create the element. | 
 **element** | [**Element**](Element.md)| The new element definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_element_category**
> asset_database_create_element_category(web_id, element_category)

Create an element category at the Asset Database root.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database in which to create the element category.
element_category = swagger_client.ElementCategory() # ElementCategory | The new element category definition.

try: 
    # Create an element category at the Asset Database root.
    api_instance.asset_database_create_element_category(web_id, element_category)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_element_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the element category. | 
 **element_category** | [**ElementCategory**](ElementCategory.md)| The new element category definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_element_template**
> asset_database_create_element_template(web_id, template)

Create a template at the Asset Database root. Specify InstanceType of \"Element\" or \"EventFrame\" to create element or event frame template respectively. Only these two types of templates can be created.

Elements and event frames that are based on an element template will inherit characteristics defined in the template.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database in which to create the element template.
template = swagger_client.Template2() # Template2 | The new element template definition.

try: 
    # Create a template at the Asset Database root. Specify InstanceType of \"Element\" or \"EventFrame\" to create element or event frame template respectively. Only these two types of templates can be created.
    api_instance.asset_database_create_element_template(web_id, template)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_element_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the element template. | 
 **template** | [**Template2**](Template2.md)| The new element template definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_enumeration_set**
> asset_database_create_enumeration_set(web_id, enumeration_set)

Create an enumeration set at the Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database in which to create the enumeration set.
enumeration_set = swagger_client.EnumerationSet() # EnumerationSet | The new enumeration set definition.

try: 
    # Create an enumeration set at the Asset Database.
    api_instance.asset_database_create_enumeration_set(web_id, enumeration_set)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_enumeration_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the enumeration set. | 
 **enumeration_set** | [**EnumerationSet**](EnumerationSet.md)| The new enumeration set definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_event_frame**
> asset_database_create_event_frame(web_id, event_frame)

Create an event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database on which to create the event frame.
event_frame = swagger_client.EventFrame() # EventFrame | The new event frame definition.

try: 
    # Create an event frame.
    api_instance.asset_database_create_event_frame(web_id, event_frame)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_event_frame: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database on which to create the event frame. | 
 **event_frame** | [**EventFrame**](EventFrame.md)| The new event frame definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_security_entry**
> asset_database_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children, security_item=security_item)

Create a security entry owned by the asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the asset database where the security entry will be created.
security_entry = swagger_client.SecurityEntry6() # SecurityEntry6 | The new security entry definition. The full list of allow and deny rights must be supplied.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)
security_item = 'security_item_example' # str | The security item of the desired security entries to be created. If the parameter is not specified, security entries of the 'Default' security item will be created. (optional)

try: 
    # Create a security entry owned by the asset database.
    api_instance.asset_database_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children, security_item=security_item)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database where the security entry will be created. | 
 **security_entry** | [**SecurityEntry6**](SecurityEntry6.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
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

# **asset_database_create_table**
> asset_database_create_table(web_id, table)

Create a table on the Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database in which to create the table.
table = swagger_client.Table() # Table | The new table definition.

try: 
    # Create a table on the Asset Database.
    api_instance.asset_database_create_table(web_id, table)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the table. | 
 **table** | [**Table**](Table.md)| The new table definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_create_table_category**
> asset_database_create_table_category(web_id, table_category)

Create a table category on the Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database in which to create the table category.
table_category = swagger_client.TableCategory() # TableCategory | The new table category definition.

try: 
    # Create a table category on the Asset Database.
    api_instance.asset_database_create_table_category(web_id, table_category)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_create_table_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the table category. | 
 **table_category** | [**TableCategory**](TableCategory.md)| The new table category definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_delete**
> asset_database_delete(web_id)

Delete an asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.

try: 
    # Delete an asset database.
    api_instance.asset_database_delete(web_id)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_delete_security_entry**
> asset_database_delete_security_entry(name, web_id, apply_to_children=apply_to_children, security_item=security_item)

Delete a security entry owned by the asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the asset database where the security entry will be deleted.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)
security_item = 'security_item_example' # str | The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the 'Default' security item will be deleted. (optional)

try: 
    # Delete a security entry owned by the asset database.
    api_instance.asset_database_delete_security_entry(name, web_id, apply_to_children=apply_to_children, security_item=security_item)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_delete_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the asset database where the security entry will be deleted. | 
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

# **asset_database_export**
> asset_database_export(web_id, end_time=end_time, export_mode=export_mode, start_time=start_time)

Export the asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
end_time = 'end_time_example' # str | The latest ending time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is '*'. (optional)
export_mode = ['export_mode_example'] # list[str] | Indicates the type of export to perform. The default is 'StrongReferences'. Multiple export modes may be specified by using multiple instances of exportMode. (optional)
start_time = 'start_time_example' # str | The earliest starting time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is '*-30d'. (optional)

try: 
    # Export the asset database.
    api_instance.asset_database_export(web_id, end_time=end_time, export_mode=export_mode, start_time=start_time)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **end_time** | **str**| The latest ending time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is &#39;*&#39;. | [optional] 
 **export_mode** | [**list[str]**](str.md)| Indicates the type of export to perform. The default is &#39;StrongReferences&#39;. Multiple export modes may be specified by using multiple instances of exportMode. | [optional] 
 **start_time** | **str**| The earliest starting time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is &#39;*-30d&#39;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_find_analyses**
> InlineResponse20010 asset_database_find_analyses(web_id, field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index)

Retrieve analyses based on the specified conditions.

Users can search for the analyses based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the analyses that match the default search.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database to search for the analyses.
field = ['field_example'] # list[str] | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
query = 'query_example' # str | The query string used for finding analyses. The default is null. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)

try: 
    # Retrieve analyses based on the specified conditions.
    api_response = api_instance.asset_database_find_analyses(web_id, field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_find_analyses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database to search for the analyses. | 
 **field** | [**list[str]**](str.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **str**| The query string used for finding analyses. The default is null. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_find_element_attributes**
> InlineResponse20013 asset_database_find_element_attributes(web_id, attribute_category=attribute_category, attribute_description_filter=attribute_description_filter, attribute_name_filter=attribute_name_filter, attribute_type=attribute_type, element_category=element_category, element_description_filter=element_description_filter, element_name_filter=element_name_filter, element_template=element_template, element_type=element_type, max_count=max_count, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index)

Retrieves a list of element attributes matching the specified filters from the specified asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the asset database to use as the root of the search.
attribute_category = 'attribute_category_example' # str | Specify that returned attributes must have this category. The default is no filter. (optional)
attribute_description_filter = 'attribute_description_filter_example' # str | The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. (optional)
attribute_name_filter = 'attribute_name_filter_example' # str | The attribute name filter string used for finding objects. The default is no filter. (optional)
attribute_type = 'attribute_type_example' # str | Specify that returned attributes' value type must be this value type. The default is no filter. (optional)
element_category = 'element_category_example' # str | Specify that the owner of the returned attributes must have this category. The default is no filter. (optional)
element_description_filter = 'element_description_filter_example' # str | The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. (optional)
element_name_filter = 'element_name_filter_example' # str | The element name filter string used for finding objects. The default is no filter. (optional)
element_template = 'element_template_example' # str | Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. (optional)
element_type = 'element_type_example' # str | Specify that the element of the returned attributes must have this AFElementType. The default is no filter. (optional)
max_count = 56 # int | The maximum number of objects to be returned (the page size). The default is 1000. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)

try: 
    # Retrieves a list of element attributes matching the specified filters from the specified asset database.
    api_response = api_instance.asset_database_find_element_attributes(web_id, attribute_category=attribute_category, attribute_description_filter=attribute_description_filter, attribute_name_filter=attribute_name_filter, attribute_type=attribute_type, element_category=element_category, element_description_filter=element_description_filter, element_name_filter=element_name_filter, element_template=element_template, element_type=element_type, max_count=max_count, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_find_element_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database to use as the root of the search. | 
 **attribute_category** | **str**| Specify that returned attributes must have this category. The default is no filter. | [optional] 
 **attribute_description_filter** | **str**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **attribute_name_filter** | **str**| The attribute name filter string used for finding objects. The default is no filter. | [optional] 
 **attribute_type** | **str**| Specify that returned attributes&#39; value type must be this value type. The default is no filter. | [optional] 
 **element_category** | **str**| Specify that the owner of the returned attributes must have this category. The default is no filter. | [optional] 
 **element_description_filter** | **str**| The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **element_name_filter** | **str**| The element name filter string used for finding objects. The default is no filter. | [optional] 
 **element_template** | **str**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. | [optional] 
 **element_type** | **str**| Specify that the element of the returned attributes must have this AFElementType. The default is no filter. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned (the page size). The default is 1000. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_find_event_frame_attributes**
> InlineResponse20013 asset_database_find_event_frame_attributes(web_id, attribute_category=attribute_category, attribute_description_filter=attribute_description_filter, attribute_name_filter=attribute_name_filter, attribute_type=attribute_type, end_time=end_time, event_frame_category=event_frame_category, event_frame_description_filter=event_frame_description_filter, event_frame_name_filter=event_frame_name_filter, event_frame_template=event_frame_template, max_count=max_count, referenced_element_name_filter=referenced_element_name_filter, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time)

Retrieves a list of event frame attributes matching the specified filters from the specified asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the asset database to use as the root of the search.
attribute_category = 'attribute_category_example' # str | Specify that returned attributes must have this category. The default is no filter. (optional)
attribute_description_filter = 'attribute_description_filter_example' # str | The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. (optional)
attribute_name_filter = 'attribute_name_filter_example' # str | The attribute name filter string used for finding objects. The default is no filter. (optional)
attribute_type = 'attribute_type_example' # str | Specify that returned attributes' value type must be this value type. The default is no filter. (optional)
end_time = 'end_time_example' # str | A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is '*'. (optional)
event_frame_category = 'event_frame_category_example' # str | Specify that the owner of the returned attributes must have this category. The default is no filter. (optional)
event_frame_description_filter = 'event_frame_description_filter_example' # str | The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. (optional)
event_frame_name_filter = 'event_frame_name_filter_example' # str | The event frame name filter string used for finding objects. The default is no filter. (optional)
event_frame_template = 'event_frame_template_example' # str | Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. (optional)
max_count = 56 # int | The maximum number of objects to be returned (the page size). The default is 1000. (optional)
referenced_element_name_filter = 'referenced_element_name_filter_example' # str | The name query string which must match the name of a referenced element. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'. (optional)
search_mode = 'search_mode_example' # str | Determines how the startTime and endTime parameters are treated when searching for event frames.     The default is 'Overlapped'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)
start_time = 'start_time_example' # str | A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is '*-8h'. (optional)

try: 
    # Retrieves a list of event frame attributes matching the specified filters from the specified asset database.
    api_response = api_instance.asset_database_find_event_frame_attributes(web_id, attribute_category=attribute_category, attribute_description_filter=attribute_description_filter, attribute_name_filter=attribute_name_filter, attribute_type=attribute_type, end_time=end_time, event_frame_category=event_frame_category, event_frame_description_filter=event_frame_description_filter, event_frame_name_filter=event_frame_name_filter, event_frame_template=event_frame_template, max_count=max_count, referenced_element_name_filter=referenced_element_name_filter, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_find_event_frame_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database to use as the root of the search. | 
 **attribute_category** | **str**| Specify that returned attributes must have this category. The default is no filter. | [optional] 
 **attribute_description_filter** | **str**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **attribute_name_filter** | **str**| The attribute name filter string used for finding objects. The default is no filter. | [optional] 
 **attribute_type** | **str**| Specify that returned attributes&#39; value type must be this value type. The default is no filter. | [optional] 
 **end_time** | **str**| A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is &#39;*&#39;. | [optional] 
 **event_frame_category** | **str**| Specify that the owner of the returned attributes must have this category. The default is no filter. | [optional] 
 **event_frame_description_filter** | **str**| The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **event_frame_name_filter** | **str**| The event frame name filter string used for finding objects. The default is no filter. | [optional] 
 **event_frame_template** | **str**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned (the page size). The default is 1000. | [optional] 
 **referenced_element_name_filter** | **str**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;. | [optional] 
 **search_mode** | **str**| Determines how the startTime and endTime parameters are treated when searching for event frames.     The default is &#39;Overlapped&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **start_time** | **str**| A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is &#39;*-8h&#39;. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get**
> InlineResponse2009 asset_database_get(web_id, selected_fields=selected_fields)

Retrieve an Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Asset Database.
    api_response = api_instance.asset_database_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_analysis_categories**
> InlineResponse2002 asset_database_get_analysis_categories(web_id, selected_fields=selected_fields)

Retrieve analysis categories for a given Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve analysis categories for a given Asset Database.
    api_response = api_instance.asset_database_get_analysis_categories(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_analysis_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_analysis_templates**
> InlineResponse20011 asset_database_get_analysis_templates(web_id, field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order)

Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.

Users can search for the analysis templates based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the templates that match the default search.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database to search.
field = ['field_example'] # list[str] | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
query = 'query_example' # str | The query string used for finding objects. The default is no query string. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)

try: 
    # Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.
    api_response = api_instance.asset_database_get_analysis_templates(web_id, field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_analysis_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database to search. | 
 **field** | [**list[str]**](str.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **str**| The query string used for finding objects. The default is no query string. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_attribute_categories**
> InlineResponse20012 asset_database_get_attribute_categories(web_id, selected_fields=selected_fields)

Retrieve attribute categories for a given Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve attribute categories for a given Asset Database.
    api_response = api_instance.asset_database_get_attribute_categories(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_attribute_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_by_path**
> InlineResponse2009 asset_database_get_by_path(path, selected_fields=selected_fields)

Retrieve an Asset Database by path.

This method returns an asset database based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
path = 'path_example' # str | The path to the database.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an Asset Database by path.
    api_response = api_instance.asset_database_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the database. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_element_categories**
> InlineResponse20014 asset_database_get_element_categories(web_id, selected_fields=selected_fields)

Retrieve element categories for a given Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve element categories for a given Asset Database.
    api_response = api_instance.asset_database_get_element_categories(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_element_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_element_templates**
> InlineResponse20016 asset_database_get_element_templates(web_id, field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order)

Retrieve element templates based on the specified criteria. Only templates of instance type \"Element\" and \"EventFrame\" are returned. By default, all element and event frame templates in the specified Asset Database are returned.

Users can search for the element and event frame template based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the templates that match the default search.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database to search.
field = ['field_example'] # list[str] | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
query = 'query_example' # str | The query string used for finding objects. The default is no query string. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)

try: 
    # Retrieve element templates based on the specified criteria. Only templates of instance type \"Element\" and \"EventFrame\" are returned. By default, all element and event frame templates in the specified Asset Database are returned.
    api_response = api_instance.asset_database_get_element_templates(web_id, field, max_count=max_count, query=query, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_element_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database to search. | 
 **field** | [**list[str]**](str.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **str**| The query string used for finding objects. The default is no query string. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_elements**
> InlineResponse20015 asset_database_get_elements(web_id, category_name=category_name, description_filter=description_filter, element_type=element_type, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index, template_name=template_name)

Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.

Users can search for the elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database to use as the root of the search.
category_name = 'category_name_example' # str | Specify that returned elements must have this category. The default is no category filter. (optional)
description_filter = 'description_filter_example' # str | Specify that returned elements must have this description. The default is no description filter. (optional)
element_type = 'element_type_example' # str | Specify that returned elements must have this type. The default type is 'Any'. (optional)
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
name_filter = 'name_filter_example' # str | The name query string used for finding objects. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)
template_name = 'template_name_example' # str | Specify that returned elements must have this template or a template derived from this template. The default is no template filter. (optional)

try: 
    # Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.
    api_response = api_instance.asset_database_get_elements(web_id, category_name=category_name, description_filter=description_filter, element_type=element_type, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index, template_name=template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database to use as the root of the search. | 
 **category_name** | **str**| Specify that returned elements must have this category. The default is no category filter. | [optional] 
 **description_filter** | **str**| Specify that returned elements must have this description. The default is no description filter. | [optional] 
 **element_type** | **str**| Specify that returned elements must have this type. The default type is &#39;Any&#39;. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **name_filter** | **str**| The name query string used for finding objects. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **template_name** | **str**| Specify that returned elements must have this template or a template derived from this template. The default is no template filter. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_enumeration_sets**
> InlineResponse20017 asset_database_get_enumeration_sets(web_id, selected_fields=selected_fields)

Retrieve enumeration sets for given asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve enumeration sets for given asset database.
    api_response = api_instance.asset_database_get_enumeration_sets(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_enumeration_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_event_frames**
> InlineResponse20018 asset_database_get_event_frames(web_id, can_be_acknowledged=can_be_acknowledged, category_name=category_name, end_time=end_time, is_acknowledged=is_acknowledged, max_count=max_count, name_filter=name_filter, referenced_element_name_filter=referenced_element_name_filter, referenced_element_template_name=referenced_element_template_name, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, severity=severity, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time, template_name=template_name)

Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource with a start time in the past 8 hours.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the asset database to use as the root of the search.
can_be_acknowledged = true # bool | Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter. (optional)
category_name = 'category_name_example' # str | Specify that returned event frames must have this category. The default is no category filter. (optional)
end_time = 'end_time_example' # str | The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*' if searchMode is not one of the 'Backward*' or 'Forward*' values. (optional)
is_acknowledged = true # bool | Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter. (optional)
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
name_filter = 'name_filter_example' # str | The name query string used for finding event frames. The default is no filter. (optional)
referenced_element_name_filter = 'referenced_element_name_filter_example' # str | The name query string which must match the name of a referenced element. The default is no filter. (optional)
referenced_element_template_name = 'referenced_element_template_name_example' # str | Specify that returned event frames must have an element in the event frame's referenced elements collection that derives from the template. Specify this parameter by name. (optional)
search_full_hierarchy = true # bool | Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'. (optional)
search_mode = 'search_mode_example' # str | Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the 'Backward*' or 'Forward*' values, none of endTime, sortField, or sortOrder may be specified. The default is 'Overlapped'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
severity = ['severity_example'] # list[str] | Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name' if searchMode is not one of the 'Backward*' or 'Forward*' values. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending' if searchMode is not one of the 'Backward*' or 'Forward*' values. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)
start_time = 'start_time_example' # str | The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'. (optional)
template_name = 'template_name_example' # str | Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name. (optional)

try: 
    # Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource with a start time in the past 8 hours.
    api_response = api_instance.asset_database_get_event_frames(web_id, can_be_acknowledged=can_be_acknowledged, category_name=category_name, end_time=end_time, is_acknowledged=is_acknowledged, max_count=max_count, name_filter=name_filter, referenced_element_name_filter=referenced_element_name_filter, referenced_element_template_name=referenced_element_template_name, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, severity=severity, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time, template_name=template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_event_frames: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database to use as the root of the search. | 
 **can_be_acknowledged** | **bool**| Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter. | [optional] 
 **category_name** | **str**| Specify that returned event frames must have this category. The default is no category filter. | [optional] 
 **end_time** | **str**| The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **is_acknowledged** | **bool**| Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **name_filter** | **str**| The name query string used for finding event frames. The default is no filter. | [optional] 
 **referenced_element_name_filter** | **str**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] 
 **referenced_element_template_name** | **str**| Specify that returned event frames must have an element in the event frame&#39;s referenced elements collection that derives from the template. Specify this parameter by name. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;. | [optional] 
 **search_mode** | **str**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the &#39;Backward*&#39; or &#39;Forward*&#39; values, none of endTime, sortField, or sortOrder may be specified. The default is &#39;Overlapped&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **severity** | [**list[str]**](str.md)| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **start_time** | **str**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;. | [optional] 
 **template_name** | **str**| Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_referenced_elements**
> InlineResponse20015 asset_database_get_referenced_elements(web_id, category_name=category_name, description_filter=description_filter, element_type=element_type, max_count=max_count, name_filter=name_filter, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index, template_name=template_name)

Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.

Users can search for the referenced elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the resource to use as the root of the search.
category_name = 'category_name_example' # str | Specify that returned elements must have this category. The default is no category filter. (optional)
description_filter = 'description_filter_example' # str | Specify that returned elements must have this description. The default is no description filter. (optional)
element_type = 'element_type_example' # str | Specify that returned elements must have this type. The default type is 'Any'. (optional)
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
name_filter = 'name_filter_example' # str | The name query string used for finding objects. The default is no filter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)
template_name = 'template_name_example' # str | Specify that returned elements must have this template or a template derived from this template. The default is no template filter. (optional)

try: 
    # Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.
    api_response = api_instance.asset_database_get_referenced_elements(web_id, category_name=category_name, description_filter=description_filter, element_type=element_type, max_count=max_count, name_filter=name_filter, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index, template_name=template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_referenced_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the resource to use as the root of the search. | 
 **category_name** | **str**| Specify that returned elements must have this category. The default is no category filter. | [optional] 
 **description_filter** | **str**| Specify that returned elements must have this description. The default is no description filter. | [optional] 
 **element_type** | **str**| Specify that returned elements must have this type. The default type is &#39;Any&#39;. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **name_filter** | **str**| The name query string used for finding objects. The default is no filter. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **template_name** | **str**| Specify that returned elements must have this template or a template derived from this template. The default is no template filter. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_security**
> InlineResponse2003 asset_database_get_security(web_id, security_item, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)

Get the security information of the specified security item associated with the asset database for a specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the asset database for the security to be checked.
security_item = ['security_item_example'] # list[str] | The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only 'Default' security item of the security information will be returned.
user_identity = ['user_identity_example'] # list[str] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
force_refresh = true # bool | Indicates if the security cache should be refreshed before getting security information. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the security information of the specified security item associated with the asset database for a specified user.
    api_response = api_instance.asset_database_get_security(web_id, security_item, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database for the security to be checked. | 
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

# **asset_database_get_security_entries**
> InlineResponse2004 asset_database_get_security_entries(web_id, name_filter=name_filter, security_item=security_item, selected_fields=selected_fields)

Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the asset database.
name_filter = 'name_filter_example' # str | The name query string used for filtering security entries. The default is no filter. (optional)
security_item = 'security_item_example' # str | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.
    api_response = api_instance.asset_database_get_security_entries(web_id, name_filter=name_filter, security_item=security_item, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_security_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database. | 
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

# **asset_database_get_security_entry_by_name**
> InlineResponse2004Items asset_database_get_security_entry_by_name(name, web_id, security_item=security_item, selected_fields=selected_fields)

Retrieve the security entry of the specified security item associated with the asset database with the specified name.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the asset database.
security_item = 'security_item_example' # str | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entry of the specified security item associated with the asset database with the specified name.
    api_response = api_instance.asset_database_get_security_entry_by_name(name, web_id, security_item=security_item, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_security_entry_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the asset database. | 
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

# **asset_database_get_table_categories**
> InlineResponse20019 asset_database_get_table_categories(web_id, selected_fields=selected_fields)

Retrieve table categories for a given Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve table categories for a given Asset Database.
    api_response = api_instance.asset_database_get_table_categories(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_table_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_get_tables**
> InlineResponse20020 asset_database_get_tables(web_id, selected_fields=selected_fields)

Retrieve tables for given Asset Database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve tables for given Asset Database.
    api_response = api_instance.asset_database_get_tables(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_get_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_import**
> asset_database_import(web_id, import_mode=import_mode)

Import an asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the asset database.
import_mode = ['import_mode_example'] # list[str] | Indicates the type of import to perform. The default is 'AllowCreate | AllowUpdate | AutoCheckIn'. Multiple import modes may be specified by using multiple instances of importMode. (optional)

try: 
    # Import an asset database.
    api_instance.asset_database_import(web_id, import_mode=import_mode)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database. | 
 **import_mode** | [**list[str]**](str.md)| Indicates the type of import to perform. The default is &#39;AllowCreate | AllowUpdate | AutoCheckIn&#39;. Multiple import modes may be specified by using multiple instances of importMode. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_remove_referenced_element**
> asset_database_remove_referenced_element(web_id, referenced_element_web_id)

Remove a reference to an existing element from the specified database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database which the referenced element will be removed from.
referenced_element_web_id = ['referenced_element_web_id_example'] # list[str] | The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.

try: 
    # Remove a reference to an existing element from the specified database.
    api_instance.asset_database_remove_referenced_element(web_id, referenced_element_web_id)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_remove_referenced_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database which the referenced element will be removed from. | 
 **referenced_element_web_id** | [**list[str]**](str.md)| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_update**
> asset_database_update(web_id, database)

Update an asset database by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
web_id = 'web_id_example' # str | The ID of the database.
database = swagger_client.Database() # Database | A partial database containing the desired changes.

try: 
    # Update an asset database by replacing items in its definition.
    api_instance.asset_database_update(web_id, database)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database. | 
 **database** | [**Database**](Database.md)| A partial database containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_database_update_security_entry**
> asset_database_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children, security_item=security_item)

Update a security entry owned by the asset database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetDatabaseApi()
name = 'name_example' # str | The name of the security entry.
web_id = 'web_id_example' # str | The ID of the asset database where the security entry will be updated.
security_entry = swagger_client.SecurityEntry7() # SecurityEntry7 | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)
security_item = 'security_item_example' # str | The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the 'Default' security item will be updated. (optional)

try: 
    # Update a security entry owned by the asset database.
    api_instance.asset_database_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children, security_item=security_item)
except ApiException as e:
    print("Exception when calling AssetDatabaseApi->asset_database_update_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. | 
 **web_id** | **str**| The ID of the asset database where the security entry will be updated. | 
 **security_entry** | [**SecurityEntry7**](SecurityEntry7.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
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

