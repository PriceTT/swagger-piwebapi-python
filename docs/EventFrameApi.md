# swagger_client.EventFrameApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_frame_acknowledge**](EventFrameApi.md#event_frame_acknowledge) | **PATCH** /eventframes/{webId}/acknowledge | Calls the EventFrame&#39;s Acknowledge method.
[**event_frame_capture_values**](EventFrameApi.md#event_frame_capture_values) | **POST** /eventframes/{webId}/attributes/capture | Calls the EventFrame&#39;s CaptureValues method.
[**event_frame_create_annotation**](EventFrameApi.md#event_frame_create_annotation) | **POST** /eventframes/{webId}/annotations | Create an annotation on an event frame.
[**event_frame_create_attribute**](EventFrameApi.md#event_frame_create_attribute) | **POST** /eventframes/{webId}/attributes | Create a new attribute of the specified event frame.
[**event_frame_create_config**](EventFrameApi.md#event_frame_create_config) | **POST** /eventframes/{webId}/config | Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.
[**event_frame_create_event_frame**](EventFrameApi.md#event_frame_create_event_frame) | **POST** /eventframes/{webId}/eventframes | Create an event frame as a child of the specified event frame.
[**event_frame_create_search_by_attribute**](EventFrameApi.md#event_frame_create_search_by_attribute) | **POST** /eventframes/searchbyattribute | Create a link for a \&quot;Search EventFrames By Attribute Value\&quot; operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.
[**event_frame_create_security_entry**](EventFrameApi.md#event_frame_create_security_entry) | **POST** /eventframes/{webId}/securityentries | Create a security entry owned by the event frame.
[**event_frame_delete**](EventFrameApi.md#event_frame_delete) | **DELETE** /eventframes/{webId} | Delete an event frame.
[**event_frame_delete_annotation**](EventFrameApi.md#event_frame_delete_annotation) | **DELETE** /eventframes/{webId}/annotations/{id} | Delete an annotation on an event frame.
[**event_frame_delete_security_entry**](EventFrameApi.md#event_frame_delete_security_entry) | **DELETE** /eventframes/{webId}/securityentries/{name} | Delete a security entry owned by the event frame.
[**event_frame_execute_search_by_attribute**](EventFrameApi.md#event_frame_execute_search_by_attribute) | **GET** /eventframes/searchbyattribute/{searchId} | Execute a \&quot;Search EventFrames By Attribute Value\&quot; operation.
[**event_frame_find_event_frame_attributes**](EventFrameApi.md#event_frame_find_event_frame_attributes) | **GET** /eventframes/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified event frame.
[**event_frame_get**](EventFrameApi.md#event_frame_get) | **GET** /eventframes/{webId} | Retrieve an event frame.
[**event_frame_get_annotation_by_id**](EventFrameApi.md#event_frame_get_annotation_by_id) | **GET** /eventframes/{webId}/annotations/{id} | Get a specific annotation on an event frame.
[**event_frame_get_annotations**](EventFrameApi.md#event_frame_get_annotations) | **GET** /eventframes/{webId}/annotations | Get an event frame&#39;s annotations.
[**event_frame_get_attributes**](EventFrameApi.md#event_frame_get_attributes) | **GET** /eventframes/{webId}/attributes | Get the attributes of the specified event frame.
[**event_frame_get_by_path**](EventFrameApi.md#event_frame_get_by_path) | **GET** /eventframes | Retrieve an event frame by path.
[**event_frame_get_categories**](EventFrameApi.md#event_frame_get_categories) | **GET** /eventframes/{webId}/categories | Get an event frame&#39;s categories.
[**event_frame_get_event_frames**](EventFrameApi.md#event_frame_get_event_frames) | **GET** /eventframes/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame with a start time in the past 8 hours.
[**event_frame_get_multiple**](EventFrameApi.md#event_frame_get_multiple) | **GET** /eventframes/multiple | Retrieve multiple event frames by web ids or paths.
[**event_frame_get_referenced_elements**](EventFrameApi.md#event_frame_get_referenced_elements) | **GET** /eventframes/{webId}/referencedelements | Retrieve the event frame&#39;s referenced elements.
[**event_frame_get_security**](EventFrameApi.md#event_frame_get_security) | **GET** /eventframes/{webId}/security | Get the security information of the specified security item associated with the event frame for a specified user.
[**event_frame_get_security_entries**](EventFrameApi.md#event_frame_get_security_entries) | **GET** /eventframes/{webId}/securityentries | Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.
[**event_frame_get_security_entry_by_name**](EventFrameApi.md#event_frame_get_security_entry_by_name) | **GET** /eventframes/{webId}/securityentries/{name} | Retrieve the security entry associated with the event frame with the specified name.
[**event_frame_update**](EventFrameApi.md#event_frame_update) | **PATCH** /eventframes/{webId} | Update an event frame by replacing items in its definition.
[**event_frame_update_annotation**](EventFrameApi.md#event_frame_update_annotation) | **PATCH** /eventframes/{webId}/annotations/{id} | Update an annotation on an event frame by replacing items in its definition.
[**event_frame_update_security_entry**](EventFrameApi.md#event_frame_update_security_entry) | **PUT** /eventframes/{webId}/securityentries/{name} | Update a security entry owned by the event frame.


# **event_frame_acknowledge**
> event_frame_acknowledge(web_id)

Calls the EventFrame's Acknowledge method.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame.

try: 
    # Calls the EventFrame's Acknowledge method.
    api_instance.event_frame_acknowledge(web_id)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_acknowledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_capture_values**
> event_frame_capture_values(web_id)

Calls the EventFrame's CaptureValues method.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame.

try: 
    # Calls the EventFrame's CaptureValues method.
    api_instance.event_frame_capture_values(web_id)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_capture_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_create_annotation**
> event_frame_create_annotation(web_id, annotation)

Create an annotation on an event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the owner event frame on which to create the annotation.
annotation = swagger_client.Annotation() # Annotation | The new annotation definition.

try: 
    # Create an annotation on an event frame.
    api_instance.event_frame_create_annotation(web_id, annotation)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_create_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the owner event frame on which to create the annotation. | 
 **annotation** | [**Annotation**](Annotation.md)| The new annotation definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_create_attribute**
> event_frame_create_attribute(web_id, attribute)

Create a new attribute of the specified event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame on which to create the attribute.
attribute = swagger_client.Attribute3() # Attribute3 | The definition of the new attribute.

try: 
    # Create a new attribute of the specified event frame.
    api_instance.event_frame_create_attribute(web_id, attribute)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame on which to create the attribute. | 
 **attribute** | [**Attribute3**](Attribute3.md)| The definition of the new attribute. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_create_config**
> event_frame_create_config(web_id, include_child_elements=include_child_elements)

Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame.
include_child_elements = true # bool | If true, includes the child event frames of the specified event frame. (optional)

try: 
    # Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.
    api_instance.event_frame_create_config(web_id, include_child_elements=include_child_elements)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_create_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame. | 
 **include_child_elements** | **bool**| If true, includes the child event frames of the specified event frame. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_create_event_frame**
> event_frame_create_event_frame(web_id, event_frame)

Create an event frame as a child of the specified event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the parent event frame on which to create the event frame.
event_frame = swagger_client.EventFrame2() # EventFrame2 | The new event frame definition.

try: 
    # Create an event frame as a child of the specified event frame.
    api_instance.event_frame_create_event_frame(web_id, event_frame)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_create_event_frame: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent event frame on which to create the event frame. | 
 **event_frame** | [**EventFrame2**](EventFrame2.md)| The new event frame definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_create_search_by_attribute**
> event_frame_create_search_by_attribute()

Create a link for a \"Search EventFrames By Attribute Value\" operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()

try: 
    # Create a link for a \"Search EventFrames By Attribute Value\" operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.
    api_instance.event_frame_create_search_by_attribute()
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_create_search_by_attribute: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_create_security_entry**
> event_frame_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children)

Create a security entry owned by the event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame where the security entry will be created.
security_entry = swagger_client.SecurityEntry20() # SecurityEntry20 | The new security entry definition. The full list of allow and deny rights must be supplied.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Create a security entry owned by the event frame.
    api_instance.event_frame_create_security_entry(web_id, security_entry, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_create_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame where the security entry will be created. | 
 **security_entry** | [**SecurityEntry20**](SecurityEntry20.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_delete**
> event_frame_delete(web_id)

Delete an event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame to delete.

try: 
    # Delete an event frame.
    api_instance.event_frame_delete(web_id)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_delete_annotation**
> event_frame_delete_annotation(id, web_id)

Delete an annotation on an event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
id = 'id_example' # str | The Annotation identifier of the annotation to be deleted.
web_id = 'web_id_example' # str | The ID of the owner event frame of the annotation to delete.

try: 
    # Delete an annotation on an event frame.
    api_instance.event_frame_delete_annotation(id, web_id)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_delete_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Annotation identifier of the annotation to be deleted. | 
 **web_id** | **str**| The ID of the owner event frame of the annotation to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_delete_security_entry**
> event_frame_delete_security_entry(name, web_id, apply_to_children=apply_to_children)

Delete a security entry owned by the event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the event frame where the security entry will be deleted.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Delete a security entry owned by the event frame.
    api_instance.event_frame_delete_security_entry(name, web_id, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_delete_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the event frame where the security entry will be deleted. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_execute_search_by_attribute**
> event_frame_execute_search_by_attribute(search_id, can_be_acknowledged=can_be_acknowledged, end_time=end_time, is_acknowledged=is_acknowledged, max_count=max_count, name_filter=name_filter, referenced_element_name_filter=referenced_element_name_filter, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, severity=severity, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time)

Execute a \"Search EventFrames By Attribute Value\" operation.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
search_id = 'search_id_example' # str | The encoded search Id of the \"Search EventFrames By Attribute Value\" operation.
can_be_acknowledged = true # bool | Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter. (optional)
end_time = 'end_time_example' # str | The ending time for the search. endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*'. (optional)
is_acknowledged = true # bool | Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter. (optional)
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
name_filter = 'name_filter_example' # str | The name query string used for finding event frames. The default is no filter. (optional)
referenced_element_name_filter = 'referenced_element_name_filter_example' # str | The name query string which must match the name of a referenced element. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'. (optional)
search_mode = 'search_mode_example' # str | Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. The default is 'Overlapped'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
severity = ['severity_example'] # list[str] | Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)
start_time = 'start_time_example' # str | The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'. (optional)

try: 
    # Execute a \"Search EventFrames By Attribute Value\" operation.
    api_instance.event_frame_execute_search_by_attribute(search_id, can_be_acknowledged=can_be_acknowledged, end_time=end_time, is_acknowledged=is_acknowledged, max_count=max_count, name_filter=name_filter, referenced_element_name_filter=referenced_element_name_filter, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, severity=severity, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_execute_search_by_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| The encoded search Id of the \&quot;Search EventFrames By Attribute Value\&quot; operation. | 
 **can_be_acknowledged** | **bool**| Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter. | [optional] 
 **end_time** | **str**| The ending time for the search. endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39;. | [optional] 
 **is_acknowledged** | **bool**| Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **name_filter** | **str**| The name query string used for finding event frames. The default is no filter. | [optional] 
 **referenced_element_name_filter** | **str**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;. | [optional] 
 **search_mode** | **str**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. The default is &#39;Overlapped&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **severity** | [**list[str]**](str.md)| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **start_time** | **str**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_find_event_frame_attributes**
> InlineResponse20013 event_frame_find_event_frame_attributes(web_id, attribute_category=attribute_category, attribute_description_filter=attribute_description_filter, attribute_name_filter=attribute_name_filter, attribute_type=attribute_type, end_time=end_time, event_frame_category=event_frame_category, event_frame_description_filter=event_frame_description_filter, event_frame_name_filter=event_frame_name_filter, event_frame_template=event_frame_template, max_count=max_count, referenced_element_name_filter=referenced_element_name_filter, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time)

Retrieves a list of event frame attributes matching the specified filters from the specified event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame to use as the root of the search.
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
    # Retrieves a list of event frame attributes matching the specified filters from the specified event frame.
    api_response = api_instance.event_frame_find_event_frame_attributes(web_id, attribute_category=attribute_category, attribute_description_filter=attribute_description_filter, attribute_name_filter=attribute_name_filter, attribute_type=attribute_type, end_time=end_time, event_frame_category=event_frame_category, event_frame_description_filter=event_frame_description_filter, event_frame_name_filter=event_frame_name_filter, event_frame_template=event_frame_template, max_count=max_count, referenced_element_name_filter=referenced_element_name_filter, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_find_event_frame_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame to use as the root of the search. | 
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

# **event_frame_get**
> InlineResponse20018Items event_frame_get(web_id, selected_fields=selected_fields)

Retrieve an event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an event frame.
    api_response = api_instance.event_frame_get(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20018Items**](InlineResponse20018Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_get_annotation_by_id**
> InlineResponse20039Items event_frame_get_annotation_by_id(id, web_id, selected_fields=selected_fields)

Get a specific annotation on an event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
id = 'id_example' # str | The Annotation identifier of the specific annotation.
web_id = 'web_id_example' # str | The ID of the owner event frame.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get a specific annotation on an event frame.
    api_response = api_instance.event_frame_get_annotation_by_id(id, web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_annotation_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Annotation identifier of the specific annotation. | 
 **web_id** | **str**| The ID of the owner event frame. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20039Items**](InlineResponse20039Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_get_annotations**
> InlineResponse20039 event_frame_get_annotations(web_id, selected_fields=selected_fields)

Get an event frame's annotations.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the owner event frame.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get an event frame's annotations.
    api_response = api_instance.event_frame_get_annotations(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the owner event frame. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_get_attributes**
> InlineResponse20013 event_frame_get_attributes(web_id, category_name=category_name, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, sort_field=sort_field, sort_order=sort_order, start_index=start_index, template_name=template_name, value_type=value_type)

Get the attributes of the specified event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame.
category_name = 'category_name_example' # str | Specify that returned attributes must have this category. The default is no category filter. (optional)
max_count = 56 # int | The maximum number of objects to be returned per call (page size). The default is 1000. (optional)
name_filter = 'name_filter_example' # str | The name query string used for finding attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
sort_field = 'sort_field_example' # str | The field or property of the object used to sort the returned collection. The default is 'Name'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
start_index = 56 # int | The starting index (zero based) of the items to be returned. The default is 0. (optional)
template_name = 'template_name_example' # str | Specify that returned attributes must be members of this template. The default is no template filter. (optional)
value_type = 'value_type_example' # str | Specify that returned attributes' value type must be the given value type. The default is no value type filter. (optional)

try: 
    # Get the attributes of the specified event frame.
    api_response = api_instance.event_frame_get_attributes(web_id, category_name=category_name, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, sort_field=sort_field, sort_order=sort_order, start_index=start_index, template_name=template_name, value_type=value_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame. | 
 **category_name** | **str**| Specify that returned attributes must have this category. The default is no category filter. | [optional] 
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **name_filter** | **str**| The name query string used for finding attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **template_name** | **str**| Specify that returned attributes must be members of this template. The default is no template filter. | [optional] 
 **value_type** | **str**| Specify that returned attributes&#39; value type must be the given value type. The default is no value type filter. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_get_by_path**
> InlineResponse20018Items event_frame_get_by_path(path, selected_fields=selected_fields)

Retrieve an event frame by path.

This method returns an event frame based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
path = 'path_example' # str | The path to the event frame.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an event frame by path.
    api_response = api_instance.event_frame_get_by_path(path, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the event frame. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20018Items**](InlineResponse20018Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_get_categories**
> InlineResponse20014 event_frame_get_categories(web_id, selected_fields=selected_fields)

Get an event frame's categories.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get an event frame's categories.
    api_response = api_instance.event_frame_get_categories(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_get_event_frames**
> InlineResponse20018 event_frame_get_event_frames(web_id, can_be_acknowledged=can_be_acknowledged, category_name=category_name, end_time=end_time, is_acknowledged=is_acknowledged, max_count=max_count, name_filter=name_filter, referenced_element_name_filter=referenced_element_name_filter, referenced_element_template_name=referenced_element_template_name, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, severity=severity, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time, template_name=template_name)

Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame with a start time in the past 8 hours.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame to use as the root of the search.
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
    # Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame with a start time in the past 8 hours.
    api_response = api_instance.event_frame_get_event_frames(web_id, can_be_acknowledged=can_be_acknowledged, category_name=category_name, end_time=end_time, is_acknowledged=is_acknowledged, max_count=max_count, name_filter=name_filter, referenced_element_name_filter=referenced_element_name_filter, referenced_element_template_name=referenced_element_template_name, search_full_hierarchy=search_full_hierarchy, search_mode=search_mode, selected_fields=selected_fields, severity=severity, sort_field=sort_field, sort_order=sort_order, start_index=start_index, start_time=start_time, template_name=template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_event_frames: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame to use as the root of the search. | 
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

# **event_frame_get_multiple**
> InlineResponse20040 event_frame_get_multiple(as_parallel=as_parallel, include_mode=include_mode, path=path, selected_fields=selected_fields, web_id=web_id)

Retrieve multiple event frames by web ids or paths.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
as_parallel = true # bool | Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is 'false'. (optional)
include_mode = 'include_mode_example' # str | The include mode for the return list. The default is 'All'. (optional)
path = ['path_example'] # list[str] | The path of an event frame. Multiple event frames may be specified with multiple instances of the parameter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
web_id = ['web_id_example'] # list[str] | The ID of an event frame. Multiple event frames may be specified with multiple instances of the parameter. (optional)

try: 
    # Retrieve multiple event frames by web ids or paths.
    api_response = api_instance.event_frame_get_multiple(as_parallel=as_parallel, include_mode=include_mode, path=path, selected_fields=selected_fields, web_id=web_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_parallel** | **bool**| Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is &#39;false&#39;. | [optional] 
 **include_mode** | **str**| The include mode for the return list. The default is &#39;All&#39;. | [optional] 
 **path** | [**list[str]**](str.md)| The path of an event frame. Multiple event frames may be specified with multiple instances of the parameter. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **web_id** | [**list[str]**](str.md)| The ID of an event frame. Multiple event frames may be specified with multiple instances of the parameter. | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_get_referenced_elements**
> InlineResponse20015 event_frame_get_referenced_elements(web_id, selected_fields=selected_fields)

Retrieve the event frame's referenced elements.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame whose referenced elements should be retrieved.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the event frame's referenced elements.
    api_response = api_instance.event_frame_get_referenced_elements(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_referenced_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame whose referenced elements should be retrieved. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_get_security**
> InlineResponse2003 event_frame_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)

Get the security information of the specified security item associated with the event frame for a specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame for the security to be checked.
user_identity = ['user_identity_example'] # list[str] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
force_refresh = true # bool | Indicates if the security cache should be refreshed before getting security information. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Get the security information of the specified security item associated with the event frame for a specified user.
    api_response = api_instance.event_frame_get_security(web_id, user_identity, force_refresh=force_refresh, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame for the security to be checked. | 
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

# **event_frame_get_security_entries**
> InlineResponse2004 event_frame_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)

Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame.
name_filter = 'name_filter_example' # str | The name query string used for filtering security entries. The default is no filter. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.
    api_response = api_instance.event_frame_get_security_entries(web_id, name_filter=name_filter, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_security_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame. | 
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

# **event_frame_get_security_entry_by_name**
> InlineResponse2004Items event_frame_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)

Retrieve the security entry associated with the event frame with the specified name.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
name = 'name_example' # str | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
web_id = 'web_id_example' # str | The ID of the event frame.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve the security entry associated with the event frame with the specified name.
    api_response = api_instance.event_frame_get_security_entry_by_name(name, web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_get_security_entry_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **web_id** | **str**| The ID of the event frame. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse2004Items**](InlineResponse2004Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_update**
> event_frame_update(web_id, event_frame)

Update an event frame by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
web_id = 'web_id_example' # str | The ID of the event frame to update.
event_frame = swagger_client.EventFrame1() # EventFrame1 | A partial event frame containing the desired changes.

try: 
    # Update an event frame by replacing items in its definition.
    api_instance.event_frame_update(web_id, event_frame)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the event frame to update. | 
 **event_frame** | [**EventFrame1**](EventFrame1.md)| A partial event frame containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_update_annotation**
> event_frame_update_annotation(id, web_id, annotation)

Update an annotation on an event frame by replacing items in its definition.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
id = 'id_example' # str | The Annotation identifier of the annotation to be updated.
web_id = 'web_id_example' # str | The ID of the owner event frame of the annotation to update.
annotation = swagger_client.Annotation1() # Annotation1 | A partial annotation containing the desired changes.

try: 
    # Update an annotation on an event frame by replacing items in its definition.
    api_instance.event_frame_update_annotation(id, web_id, annotation)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_update_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Annotation identifier of the annotation to be updated. | 
 **web_id** | **str**| The ID of the owner event frame of the annotation to update. | 
 **annotation** | [**Annotation1**](Annotation1.md)| A partial annotation containing the desired changes. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_frame_update_security_entry**
> event_frame_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children)

Update a security entry owned by the event frame.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventFrameApi()
name = 'name_example' # str | The name of the security entry.
web_id = 'web_id_example' # str | The ID of the event frame where the security entry will be updated.
security_entry = swagger_client.SecurityEntry21() # SecurityEntry21 | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
apply_to_children = true # bool | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. (optional)

try: 
    # Update a security entry owned by the event frame.
    api_instance.event_frame_update_security_entry(name, web_id, security_entry, apply_to_children=apply_to_children)
except ApiException as e:
    print("Exception when calling EventFrameApi->event_frame_update_security_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. | 
 **web_id** | **str**| The ID of the event frame where the security entry will be updated. | 
 **security_entry** | [**SecurityEntry21**](SecurityEntry21.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

