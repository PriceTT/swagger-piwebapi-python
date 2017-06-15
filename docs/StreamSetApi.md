# swagger_client.StreamSetApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stream_set_get_channel**](StreamSetApi.md#stream_set_get_channel) | **GET** /streamsets/{webId}/channel | Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.
[**stream_set_get_channel_ad_hoc**](StreamSetApi.md#stream_set_get_channel_ad_hoc) | **GET** /streamsets/channel | Opens a channel that will send messages about any value changes for the specified streams.
[**stream_set_get_end**](StreamSetApi.md#stream_set_get_end) | **GET** /streamsets/{webId}/end | Returns End of stream values of the attributes for an Element, Event Frame or Attribute
[**stream_set_get_end_ad_hoc**](StreamSetApi.md#stream_set_get_end_ad_hoc) | **GET** /streamsets/end | Returns End Of Stream values for attributes of the specified streams
[**stream_set_get_interpolated**](StreamSetApi.md#stream_set_get_interpolated) | **GET** /streamsets/{webId}/interpolated | Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.
[**stream_set_get_interpolated_ad_hoc**](StreamSetApi.md#stream_set_get_interpolated_ad_hoc) | **GET** /streamsets/interpolated | Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.
[**stream_set_get_interpolated_at_times**](StreamSetApi.md#stream_set_get_interpolated_at_times) | **GET** /streamsets/{webId}/interpolatedattimes | Returns interpolated values of attributes for an element, event frame or attribute at the specified times.
[**stream_set_get_interpolated_at_times_ad_hoc**](StreamSetApi.md#stream_set_get_interpolated_at_times_ad_hoc) | **GET** /streamsets/interpolatedattimes | Returns interpolated values of the specified streams at the specified times.
[**stream_set_get_plot**](StreamSetApi.md#stream_set_get_plot) | **GET** /streamsets/{webId}/plot | Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
[**stream_set_get_plot_ad_hoc**](StreamSetApi.md#stream_set_get_plot_ad_hoc) | **GET** /streamsets/plot | Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
[**stream_set_get_recorded**](StreamSetApi.md#stream_set_get_recorded) | **GET** /streamsets/{webId}/recorded | Returns recorded values of the attributes for an element, event frame, or attribute.
[**stream_set_get_recorded_ad_hoc**](StreamSetApi.md#stream_set_get_recorded_ad_hoc) | **GET** /streamsets/recorded | Returns recorded values of the specified streams.
[**stream_set_get_recorded_at_time**](StreamSetApi.md#stream_set_get_recorded_at_time) | **GET** /streamsets/{webId}/recordedattime | Returns recorded values of the attributes for an element, event frame, or attribute.
[**stream_set_get_recorded_at_time_ad_hoc**](StreamSetApi.md#stream_set_get_recorded_at_time_ad_hoc) | **GET** /streamsets/recordedattime | Returns recorded values based on the passed time and retrieval mode.
[**stream_set_get_recorded_at_times**](StreamSetApi.md#stream_set_get_recorded_at_times) | **GET** /streamsets/{webId}/recordedattimes | Returns recorded values of attributes for an element, event frame or attribute at the specified times.
[**stream_set_get_recorded_at_times_ad_hoc**](StreamSetApi.md#stream_set_get_recorded_at_times_ad_hoc) | **GET** /streamsets/recordedattimes | Returns recorded values of the specified streams at the specified times.
[**stream_set_get_summaries**](StreamSetApi.md#stream_set_get_summaries) | **GET** /streamsets/{webId}/summary | Returns summary values of the attributes for an element, event frame or attribute.
[**stream_set_get_summaries_ad_hoc**](StreamSetApi.md#stream_set_get_summaries_ad_hoc) | **GET** /streamsets/summary | Returns summary values of the specified streams.
[**stream_set_get_values**](StreamSetApi.md#stream_set_get_values) | **GET** /streamsets/{webId}/value | Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.
[**stream_set_get_values_ad_hoc**](StreamSetApi.md#stream_set_get_values_ad_hoc) | **GET** /streamsets/value | Returns values of the specified streams.
[**stream_set_update_value**](StreamSetApi.md#stream_set_update_value) | **POST** /streamsets/{webId}/value | Updates a single value for the specified streams.
[**stream_set_update_value_ad_hoc**](StreamSetApi.md#stream_set_update_value_ad_hoc) | **POST** /streamsets/value | Updates a single value for the specified streams.
[**stream_set_update_values**](StreamSetApi.md#stream_set_update_values) | **POST** /streamsets/{webId}/recorded | Updates multiple values for the specified streams.
[**stream_set_update_values_ad_hoc**](StreamSetApi.md#stream_set_update_values_ad_hoc) | **POST** /streamsets/recorded | Updates multiple values for the specified streams.


# **stream_set_get_channel**
> stream_set_get_channel(web_id, category_name=category_name, include_initial_values=include_initial_values, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, show_excluded=show_excluded, show_hidden=show_hidden, template_name=template_name)

Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
include_initial_values = true # bool | Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is 'false'. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)

try: 
    # Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.
    api_instance.stream_set_get_channel(web_id, category_name=category_name, include_initial_values=include_initial_values, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, show_excluded=show_excluded, show_hidden=show_hidden, template_name=template_name)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **include_initial_values** | **bool**| Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is &#39;false&#39;. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_channel_ad_hoc**
> stream_set_get_channel_ad_hoc(web_id, include_initial_values=include_initial_values)

Opens a channel that will send messages about any value changes for the specified streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = ['web_id_example'] # list[str] | The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.
include_initial_values = true # bool | Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is 'false'. (optional)

try: 
    # Opens a channel that will send messages about any value changes for the specified streams.
    api_instance.stream_set_get_channel_ad_hoc(web_id, include_initial_values=include_initial_values)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_channel_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | [**list[str]**](str.md)| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter. | 
 **include_initial_values** | **bool**| Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is &#39;false&#39;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_end**
> InlineResponse1011 stream_set_get_end(web_id, category_name=category_name, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, template_name=template_name)

Returns End of stream values of the attributes for an Element, Event Frame or Attribute

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)

try: 
    # Returns End of stream values of the attributes for an Element, Event Frame or Attribute
    api_response = api_instance.stream_set_get_end(web_id, category_name=category_name, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, template_name=template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_end: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 

### Return type

[**InlineResponse1011**](InlineResponse1011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_end_ad_hoc**
> InlineResponse101 stream_set_get_end_ad_hoc(web_id, selected_fields=selected_fields)

Returns End Of Stream values for attributes of the specified streams

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = ['web_id_example'] # list[str] | The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Returns End Of Stream values for attributes of the specified streams
    api_response = api_instance.stream_set_get_end_ad_hoc(web_id, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_end_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | [**list[str]**](str.md)| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_interpolated**
> InlineResponse101 stream_set_get_interpolated(web_id, category_name=category_name, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, interval=interval, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, start_time=start_time, template_name=template_name, time_zone=time_zone)

Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
interval = 'interval_example' # str | The sampling interval, in AFTimeSpan format. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.
    api_response = api_instance.stream_set_get_interpolated(web_id, category_name=category_name, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, interval=interval, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, start_time=start_time, template_name=template_name, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_interpolated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **interval** | **str**| The sampling interval, in AFTimeSpan format. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_interpolated_ad_hoc**
> InlineResponse101 stream_set_get_interpolated_ad_hoc(web_id, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, interval=interval, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)

Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = ['web_id_example'] # list[str] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
end_time = 'end_time_example' # str | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
interval = 'interval_example' # str | The sampling interval, in AFTimeSpan format. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d'. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.
    api_response = api_instance.stream_set_get_interpolated_ad_hoc(web_id, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, interval=interval, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_interpolated_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | [**list[str]**](str.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **interval** | **str**| The sampling interval, in AFTimeSpan format. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39;. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_interpolated_at_times**
> InlineResponse101 stream_set_get_interpolated_at_times(web_id, time, category_name=category_name, filter_expression=filter_expression, include_filtered_values=include_filtered_values, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, sort_order=sort_order, template_name=template_name, time_zone=time_zone)

Returns interpolated values of attributes for an element, event frame or attribute at the specified times.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
time = ['time_example'] # list[str] | The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns interpolated values of attributes for an element, event frame or attribute at the specified times.
    api_response = api_instance.stream_set_get_interpolated_at_times(web_id, time, category_name=category_name, filter_expression=filter_expression, include_filtered_values=include_filtered_values, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, sort_order=sort_order, template_name=template_name, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_interpolated_at_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **time** | [**list[str]**](str.md)| The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. | 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_interpolated_at_times_ad_hoc**
> InlineResponse101 stream_set_get_interpolated_at_times_ad_hoc(time, web_id, filter_expression=filter_expression, include_filtered_values=include_filtered_values, selected_fields=selected_fields, sort_order=sort_order, time_zone=time_zone)

Returns interpolated values of the specified streams at the specified times.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
time = ['time_example'] # list[str] | The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
web_id = ['web_id_example'] # list[str] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns interpolated values of the specified streams at the specified times.
    api_response = api_instance.stream_set_get_interpolated_at_times_ad_hoc(time, web_id, filter_expression=filter_expression, include_filtered_values=include_filtered_values, selected_fields=selected_fields, sort_order=sort_order, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_interpolated_at_times_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | [**list[str]**](str.md)| The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. | 
 **web_id** | [**list[str]**](str.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_plot**
> InlineResponse101 stream_set_get_plot(web_id, category_name=category_name, end_time=end_time, intervals=intervals, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, start_time=start_time, template_name=template_name, time_zone=time_zone)

Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
intervals = 56 # int | The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
    api_response = api_instance.stream_set_get_plot(web_id, category_name=category_name, end_time=end_time, intervals=intervals, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, start_time=start_time, template_name=template_name, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_plot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **intervals** | **int**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_plot_ad_hoc**
> InlineResponse101 stream_set_get_plot_ad_hoc(web_id, end_time=end_time, intervals=intervals, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)

Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = ['web_id_example'] # list[str] | The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.
end_time = 'end_time_example' # str | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
intervals = 56 # int | The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d'. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
    api_response = api_instance.stream_set_get_plot_ad_hoc(web_id, end_time=end_time, intervals=intervals, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_plot_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | [**list[str]**](str.md)| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter. | 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **intervals** | **int**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39;. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_recorded**
> InlineResponse101 stream_set_get_recorded(web_id, boundary_type=boundary_type, category_name=category_name, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, start_time=start_time, template_name=template_name, time_zone=time_zone)

Returns recorded values of the attributes for an element, event frame, or attribute.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
boundary_type = 'boundary_type_example' # str | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'. (optional)
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
max_count = 56 # int | The maximum number of values to be returned. The default is 1000. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns recorded values of the attributes for an element, event frame, or attribute.
    api_response = api_instance.stream_set_get_recorded(web_id, boundary_type=boundary_type, category_name=category_name, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, max_count=max_count, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, start_time=start_time, template_name=template_name, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_recorded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **boundary_type** | **str**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **max_count** | **int**| The maximum number of values to be returned. The default is 1000. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_recorded_ad_hoc**
> InlineResponse101 stream_set_get_recorded_ad_hoc(web_id, boundary_type=boundary_type, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, max_count=max_count, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)

Returns recorded values of the specified streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = ['web_id_example'] # list[str] | The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.
boundary_type = 'boundary_type_example' # str | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
max_count = 56 # int | The maximum number of values to be returned. The default is 1000. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d'. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns recorded values of the specified streams.
    api_response = api_instance.stream_set_get_recorded_ad_hoc(web_id, boundary_type=boundary_type, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, max_count=max_count, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_recorded_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | [**list[str]**](str.md)| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter. | 
 **boundary_type** | **str**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **max_count** | **int**| The maximum number of values to be returned. The default is 1000. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39;. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_recorded_at_time**
> InlineResponse101 stream_set_get_recorded_at_time(web_id, time, category_name=category_name, name_filter=name_filter, retrieval_mode=retrieval_mode, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, template_name=template_name, time_zone=time_zone)

Returns recorded values of the attributes for an element, event frame, or attribute.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
time = 'time_example' # str | The timestamp at which the values are desired.
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
retrieval_mode = 'retrieval_mode_example' # str | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns recorded values of the attributes for an element, event frame, or attribute.
    api_response = api_instance.stream_set_get_recorded_at_time(web_id, time, category_name=category_name, name_filter=name_filter, retrieval_mode=retrieval_mode, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, template_name=template_name, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_recorded_at_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **time** | **str**| The timestamp at which the values are desired. | 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **retrieval_mode** | **str**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_recorded_at_time_ad_hoc**
> InlineResponse1011 stream_set_get_recorded_at_time_ad_hoc(time, web_id, retrieval_mode=retrieval_mode, selected_fields=selected_fields, time_zone=time_zone)

Returns recorded values based on the passed time and retrieval mode.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
time = 'time_example' # str | The timestamp at which the values are desired.
web_id = ['web_id_example'] # list[str] | The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.
retrieval_mode = 'retrieval_mode_example' # str | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns recorded values based on the passed time and retrieval mode.
    api_response = api_instance.stream_set_get_recorded_at_time_ad_hoc(time, web_id, retrieval_mode=retrieval_mode, selected_fields=selected_fields, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_recorded_at_time_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | **str**| The timestamp at which the values are desired. | 
 **web_id** | [**list[str]**](str.md)| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter. | 
 **retrieval_mode** | **str**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse1011**](InlineResponse1011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_recorded_at_times**
> InlineResponse101 stream_set_get_recorded_at_times(web_id, time, category_name=category_name, name_filter=name_filter, retrieval_mode=retrieval_mode, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, sort_order=sort_order, template_name=template_name, time_zone=time_zone)

Returns recorded values of attributes for an element, event frame or attribute at the specified times.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
time = ['time_example'] # list[str] | The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
retrieval_mode = 'retrieval_mode_example' # str | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns recorded values of attributes for an element, event frame or attribute at the specified times.
    api_response = api_instance.stream_set_get_recorded_at_times(web_id, time, category_name=category_name, name_filter=name_filter, retrieval_mode=retrieval_mode, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, sort_order=sort_order, template_name=template_name, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_recorded_at_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **time** | [**list[str]**](str.md)| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. | 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **retrieval_mode** | **str**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_recorded_at_times_ad_hoc**
> InlineResponse101 stream_set_get_recorded_at_times_ad_hoc(time, web_id, retrieval_mode=retrieval_mode, selected_fields=selected_fields, sort_order=sort_order, time_zone=time_zone)

Returns recorded values of the specified streams at the specified times.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
time = ['time_example'] # list[str] | The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
web_id = ['web_id_example'] # list[str] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
retrieval_mode = 'retrieval_mode_example' # str | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns recorded values of the specified streams at the specified times.
    api_response = api_instance.stream_set_get_recorded_at_times_ad_hoc(time, web_id, retrieval_mode=retrieval_mode, selected_fields=selected_fields, sort_order=sort_order, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_recorded_at_times_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | [**list[str]**](str.md)| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. | 
 **web_id** | [**list[str]**](str.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **retrieval_mode** | **str**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse101**](InlineResponse101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_summaries**
> InlineResponse20044 stream_set_get_summaries(web_id, calculation_basis=calculation_basis, category_name=category_name, end_time=end_time, filter_expression=filter_expression, name_filter=name_filter, sample_interval=sample_interval, sample_type=sample_type, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, start_time=start_time, summary_duration=summary_duration, summary_type=summary_type, template_name=template_name, time_type=time_type, time_zone=time_zone)

Returns summary values of the attributes for an element, event frame or attribute.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
calculation_basis = 'calculation_basis_example' # str | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'. (optional)
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. The default is no filtering. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
sample_interval = 'sample_interval_example' # str | A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'. (optional)
sample_type = 'sample_type_example' # str | A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
summary_duration = 'summary_duration_example' # str | The duration of each summary interval. (optional)
summary_type = ['summary_type_example'] # list[str] | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)
time_type = 'time_type_example' # str | Specifies how to calculate the timestamp for each interval. The default is 'Auto'. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns summary values of the attributes for an element, event frame or attribute.
    api_response = api_instance.stream_set_get_summaries(web_id, calculation_basis=calculation_basis, category_name=category_name, end_time=end_time, filter_expression=filter_expression, name_filter=name_filter, sample_interval=sample_interval, sample_type=sample_type, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, start_time=start_time, summary_duration=summary_duration, summary_type=summary_type, template_name=template_name, time_type=time_type, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **calculation_basis** | **str**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **sample_interval** | **str**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;. | [optional] 
 **sample_type** | **str**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **summary_duration** | **str**| The duration of each summary interval. | [optional] 
 **summary_type** | [**list[str]**](str.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time_type** | **str**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_summaries_ad_hoc**
> InlineResponse20044 stream_set_get_summaries_ad_hoc(web_id, calculation_basis=calculation_basis, end_time=end_time, filter_expression=filter_expression, sample_interval=sample_interval, sample_type=sample_type, selected_fields=selected_fields, start_time=start_time, summary_duration=summary_duration, summary_type=summary_type, time_type=time_type, time_zone=time_zone)

Returns summary values of the specified streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = ['web_id_example'] # list[str] | The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.
calculation_basis = 'calculation_basis_example' # str | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. The default is no filtering. (optional)
sample_interval = 'sample_interval_example' # str | A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'. (optional)
sample_type = 'sample_type_example' # str | A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d'. (optional)
summary_duration = 'summary_duration_example' # str | The duration of each summary interval. (optional)
summary_type = ['summary_type_example'] # list[str] | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType. (optional)
time_type = 'time_type_example' # str | Specifies how to calculate the timestamp for each interval. The default is 'Auto'. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns summary values of the specified streams.
    api_response = api_instance.stream_set_get_summaries_ad_hoc(web_id, calculation_basis=calculation_basis, end_time=end_time, filter_expression=filter_expression, sample_interval=sample_interval, sample_type=sample_type, selected_fields=selected_fields, start_time=start_time, summary_duration=summary_duration, summary_type=summary_type, time_type=time_type, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_summaries_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | [**list[str]**](str.md)| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter. | 
 **calculation_basis** | **str**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **sample_interval** | **str**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;. | [optional] 
 **sample_type** | **str**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39;. | [optional] 
 **summary_duration** | **str**| The duration of each summary interval. | [optional] 
 **summary_type** | [**list[str]**](str.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] 
 **time_type** | **str**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_values**
> InlineResponse1011 stream_set_get_values(web_id, category_name=category_name, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, template_name=template_name, time=time, time_zone=time_zone)

Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
category_name = 'category_name_example' # str | Specify that included attributes must have this category. The default is no category filter. (optional)
name_filter = 'name_filter_example' # str | The name query string used for filtering attributes. The default is no filter. (optional)
search_full_hierarchy = true # bool | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
show_excluded = true # bool | Specified if the search should include attributes with the Excluded property set. The default is 'false'. (optional)
show_hidden = true # bool | Specified if the search should include attributes with the Hidden property set. The default is 'false'. (optional)
template_name = 'template_name_example' # str | Specify that included attributes must be members of this template. The default is no template filter. (optional)
time = 'time_example' # str | An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.
    api_response = api_instance.stream_set_get_values(web_id, category_name=category_name, name_filter=name_filter, search_full_hierarchy=search_full_hierarchy, selected_fields=selected_fields, show_excluded=show_excluded, show_hidden=show_hidden, template_name=template_name, time=time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | 
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time** | **str**| An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse1011**](InlineResponse1011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_get_values_ad_hoc**
> InlineResponse1011 stream_set_get_values_ad_hoc(web_id, selected_fields=selected_fields, time=time, time_zone=time_zone)

Returns values of the specified streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = ['web_id_example'] # list[str] | The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
time = 'time_example' # str | An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns values of the specified streams.
    api_response = api_instance.stream_set_get_values_ad_hoc(web_id, selected_fields=selected_fields, time=time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_get_values_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | [**list[str]**](str.md)| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **time** | **str**| An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse1011**](InlineResponse1011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_update_value**
> InlineResponse204 stream_set_update_value(web_id, values, buffer_option=buffer_option, update_option=update_option)

Updates a single value for the specified streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.
values = [swagger_client.InlineResponse1011Items()] # list[InlineResponse1011Items] | The values to add or update.
buffer_option = 'buffer_option_example' # str | The desired AFBufferOption. The default is 'BufferIfPossible'. (optional)
update_option = 'update_option_example' # str | The desired AFUpdateOption. The default is 'Replace'. (optional)

try: 
    # Updates a single value for the specified streams.
    api_response = api_instance.stream_set_update_value(web_id, values, buffer_option=buffer_option, update_option=update_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_update_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object. | 
 **values** | [**list[InlineResponse1011Items]**](InlineResponse1011Items.md)| The values to add or update. | 
 **buffer_option** | **str**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **update_option** | **str**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_update_value_ad_hoc**
> InlineResponse204 stream_set_update_value_ad_hoc(values, buffer_option=buffer_option, update_option=update_option)

Updates a single value for the specified streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
values = [swagger_client.InlineResponse101Items()] # list[InlineResponse101Items] | The values to add or update.
buffer_option = 'buffer_option_example' # str | The desired AFBufferOption. The default is 'BufferIfPossible'. (optional)
update_option = 'update_option_example' # str | The desired AFUpdateOption. The default is 'Replace'. (optional)

try: 
    # Updates a single value for the specified streams.
    api_response = api_instance.stream_set_update_value_ad_hoc(values, buffer_option=buffer_option, update_option=update_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_update_value_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **values** | [**list[InlineResponse101Items]**](InlineResponse101Items.md)| The values to add or update. | 
 **buffer_option** | **str**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **update_option** | **str**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_update_values**
> InlineResponse20043 stream_set_update_values(web_id, values, buffer_option=buffer_option, update_option=update_option)

Updates multiple values for the specified streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
web_id = 'web_id_example' # str | The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.
values = [swagger_client.InlineResponse101Items()] # list[InlineResponse101Items] | The values to add or update.
buffer_option = 'buffer_option_example' # str | The desired AFBufferOption. The default is 'BufferIfPossible'. (optional)
update_option = 'update_option_example' # str | The desired AFUpdateOption. The default is 'Replace'. (optional)

try: 
    # Updates multiple values for the specified streams.
    api_response = api_instance.stream_set_update_values(web_id, values, buffer_option=buffer_option, update_option=update_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_update_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object. | 
 **values** | [**list[InlineResponse101Items]**](InlineResponse101Items.md)| The values to add or update. | 
 **buffer_option** | **str**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **update_option** | **str**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_update_values_ad_hoc**
> InlineResponse20043 stream_set_update_values_ad_hoc(values, buffer_option=buffer_option, update_option=update_option)

Updates multiple values for the specified streams.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamSetApi()
values = [swagger_client.InlineResponse101Items()] # list[InlineResponse101Items] | The values to add or update.
buffer_option = 'buffer_option_example' # str | The desired AFBufferOption. The default is 'BufferIfPossible'. (optional)
update_option = 'update_option_example' # str | The desired AFUpdateOption. The default is 'Replace'. (optional)

try: 
    # Updates multiple values for the specified streams.
    api_response = api_instance.stream_set_update_values_ad_hoc(values, buffer_option=buffer_option, update_option=update_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamSetApi->stream_set_update_values_ad_hoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **values** | [**list[InlineResponse101Items]**](InlineResponse101Items.md)| The values to add or update. | 
 **buffer_option** | **str**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **update_option** | **str**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

