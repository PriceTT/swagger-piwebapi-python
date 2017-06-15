# swagger_client.StreamApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stream_get_channel**](StreamApi.md#stream_get_channel) | **GET** /streams/{webId}/channel | Opens a channel that will send messages about any value changes for the specified stream.
[**stream_get_end**](StreamApi.md#stream_get_end) | **GET** /streams/{webId}/end | Returns the end-of-stream value of the stream.
[**stream_get_interpolated**](StreamApi.md#stream_get_interpolated) | **GET** /streams/{webId}/interpolated | Retrieves interpolated values over the specified time range at the specified sampling interval.
[**stream_get_interpolated_at_times**](StreamApi.md#stream_get_interpolated_at_times) | **GET** /streams/{webId}/interpolatedattimes | Retrieves interpolated values over the specified time range at the specified sampling interval.
[**stream_get_plot**](StreamApi.md#stream_get_plot) | **GET** /streams/{webId}/plot | Retrieves values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
[**stream_get_recorded**](StreamApi.md#stream_get_recorded) | **GET** /streams/{webId}/recorded | Returns a list of compressed values for the requested time range from the source provider.
[**stream_get_recorded_at_time**](StreamApi.md#stream_get_recorded_at_time) | **GET** /streams/{webId}/recordedattime | Returns a single recorded value based on the passed time and retrieval mode from the stream.
[**stream_get_recorded_at_times**](StreamApi.md#stream_get_recorded_at_times) | **GET** /streams/{webId}/recordedattimes | Retrieves recorded values at the specified times.
[**stream_get_summary**](StreamApi.md#stream_get_summary) | **GET** /streams/{webId}/summary | Returns a summary over the specified time range for the stream.
[**stream_get_value**](StreamApi.md#stream_get_value) | **GET** /streams/{webId}/value | Returns the value of the stream at the specified time. By default, this is usually the current value.
[**stream_update_value**](StreamApi.md#stream_update_value) | **POST** /streams/{webId}/value | Updates a value for the specified stream.
[**stream_update_values**](StreamApi.md#stream_update_values) | **POST** /streams/{webId}/recorded | Updates multiple values for the specified stream.


# **stream_get_channel**
> stream_get_channel(web_id, include_initial_values=include_initial_values)

Opens a channel that will send messages about any value changes for the specified stream.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
include_initial_values = true # bool | Specified if the channel should send a message with the current value of the stream after the connection is opened. The default is 'false'. (optional)

try: 
    # Opens a channel that will send messages about any value changes for the specified stream.
    api_instance.stream_get_channel(web_id, include_initial_values=include_initial_values)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **include_initial_values** | **bool**| Specified if the channel should send a message with the current value of the stream after the connection is opened. The default is &#39;false&#39;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_end**
> InlineResponse20028 stream_get_end(web_id, desired_units=desired_units, selected_fields=selected_fields)

Returns the end-of-stream value of the stream.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
desired_units = 'desired_units_example' # str | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Returns the end-of-stream value of the stream.
    api_response = api_instance.stream_get_end(web_id, desired_units=desired_units, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_end: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_interpolated**
> InlineResponse20033 stream_get_interpolated(web_id, desired_units=desired_units, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, interval=interval, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)

Retrieves interpolated values over the specified time range at the specified sampling interval.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
desired_units = 'desired_units_example' # str | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
interval = 'interval_example' # str | The sampling interval, in AFTimeSpan format. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Retrieves interpolated values over the specified time range at the specified sampling interval.
    api_response = api_instance.stream_get_interpolated(web_id, desired_units=desired_units, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, interval=interval, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_interpolated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **interval** | **str**| The sampling interval, in AFTimeSpan format. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_interpolated_at_times**
> InlineResponse20033 stream_get_interpolated_at_times(web_id, desired_units=desired_units, filter_expression=filter_expression, include_filtered_values=include_filtered_values, selected_fields=selected_fields, sort_order=sort_order, time=time, time_zone=time_zone)

Retrieves interpolated values over the specified time range at the specified sampling interval.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
desired_units = 'desired_units_example' # str | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. (optional)
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
time = ['time_example'] # list[str] | The timestamp at which to retrieve an interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Retrieves interpolated values over the specified time range at the specified sampling interval.
    api_response = api_instance.stream_get_interpolated_at_times(web_id, desired_units=desired_units, filter_expression=filter_expression, include_filtered_values=include_filtered_values, selected_fields=selected_fields, sort_order=sort_order, time=time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_interpolated_at_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **time** | [**list[str]**](str.md)| The timestamp at which to retrieve an interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_plot**
> InlineResponse20033 stream_get_plot(web_id, desired_units=desired_units, end_time=end_time, intervals=intervals, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)

Retrieves values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
desired_units = 'desired_units_example' # str | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
intervals = 56 # int | The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Retrieves values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
    api_response = api_instance.stream_get_plot(web_id, desired_units=desired_units, end_time=end_time, intervals=intervals, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_plot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **intervals** | **int**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_recorded**
> InlineResponse20033 stream_get_recorded(web_id, boundary_type=boundary_type, desired_units=desired_units, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, max_count=max_count, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)

Returns a list of compressed values for the requested time range from the source provider.

Returned times are affected by the specified boundary type. If no values are found for the time range and conditions specified then the HTTP response will be success, with a body containing an empty array of Items. When specifying true for the includeFilteredValues parameter, consecutive filtered events are not returned. The first value that would be filtered out is returned with its time and the enumeration value \"Filtered\". The next value in the collection will be the next compressed value in the specified direction that passes the filter criteria - if any. When both boundaryType and a filterExpression are specified, the events returned for the boundary condition specified are passed through the filter. If the includeFilteredValues parameter is true, the boundary values will be reported at the proper timestamps with the enumeration value \"Filtered\" when the filter conditions are not met at the boundary time. If the includeFilteredValues parameter is false for this case, no event is returned for the boundary time.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
boundary_type = 'boundary_type_example' # str | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'. (optional)
desired_units = 'desired_units_example' # str | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering. (optional)
include_filtered_values = true # bool | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted. (optional)
max_count = 56 # int | The maximum number of values to be returned. The default is 1000. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns a list of compressed values for the requested time range from the source provider.
    api_response = api_instance.stream_get_recorded(web_id, boundary_type=boundary_type, desired_units=desired_units, end_time=end_time, filter_expression=filter_expression, include_filtered_values=include_filtered_values, max_count=max_count, selected_fields=selected_fields, start_time=start_time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_recorded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **boundary_type** | **str**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] 
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **include_filtered_values** | **bool**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **max_count** | **int**| The maximum number of values to be returned. The default is 1000. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_recorded_at_time**
> InlineResponse20028 stream_get_recorded_at_time(web_id, time, desired_units=desired_units, retrieval_mode=retrieval_mode, selected_fields=selected_fields, time_zone=time_zone)

Returns a single recorded value based on the passed time and retrieval mode from the stream.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
time = 'time_example' # str | The timestamp at which the value is desired.
desired_units = 'desired_units_example' # str | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. (optional)
retrieval_mode = 'retrieval_mode_example' # str | An optional value that determines the value to return when a value doesn't exist at the exact time specified. The default is 'Auto'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns a single recorded value based on the passed time and retrieval mode from the stream.
    api_response = api_instance.stream_get_recorded_at_time(web_id, time, desired_units=desired_units, retrieval_mode=retrieval_mode, selected_fields=selected_fields, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_recorded_at_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **time** | **str**| The timestamp at which the value is desired. | 
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] 
 **retrieval_mode** | **str**| An optional value that determines the value to return when a value doesn&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_recorded_at_times**
> InlineResponse20033 stream_get_recorded_at_times(web_id, desired_units=desired_units, retrieval_mode=retrieval_mode, selected_fields=selected_fields, sort_order=sort_order, time=time, time_zone=time_zone)

Retrieves recorded values at the specified times.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
desired_units = 'desired_units_example' # str | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. (optional)
retrieval_mode = 'retrieval_mode_example' # str | An optional value that determines the value to return when a value doesn't exist at the exact time specified. The default is 'Auto'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
time = ['time_example'] # list[str] | The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Retrieves recorded values at the specified times.
    api_response = api_instance.stream_get_recorded_at_times(web_id, desired_units=desired_units, retrieval_mode=retrieval_mode, selected_fields=selected_fields, sort_order=sort_order, time=time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_recorded_at_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] 
 **retrieval_mode** | **str**| An optional value that determines the value to return when a value doesn&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **time** | [**list[str]**](str.md)| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_summary**
> InlineResponse20034 stream_get_summary(web_id, calculation_basis=calculation_basis, end_time=end_time, filter_expression=filter_expression, sample_interval=sample_interval, sample_type=sample_type, selected_fields=selected_fields, start_time=start_time, summary_duration=summary_duration, summary_type=summary_type, time_type=time_type, time_zone=time_zone)

Returns a summary over the specified time range for the stream.

Count is the only summary type supported on non-numeric streams. Requesting a summary for any other type will generate an error. Time-weighted totals are computed by integrating the rate tag values over the requested time range. If some of the data are bad in the time range, the calculated total is divided by the fraction of the time period for which there are good values. This approach is equivalent to assuming that during the period of bad data, the tag takes on the average values for the entire calculation time range. The PercentGood summary may be used to determine if the calculation results are suitable for the application's purposes. For time-weighted totals, if the time unit rate of the stream cannot be determined, then the value will be totaled assuming a unit of \"per day\" and no unit of measure will be assigned to the value. If the measured time component of the tag is not based on a day, the user of the data must convert the totalized value to the correct units.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
calculation_basis = 'calculation_basis_example' # str | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
filter_expression = 'filter_expression_example' # str | A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. (optional)
sample_interval = 'sample_interval_example' # str | When the sampleType is Interval, sampleInterval specifies how often the filter expression is evaluated when computing the summary for an interval. (optional)
sample_type = 'sample_type_example' # str | Defines the evaluation of an expression over a time range. The default is 'ExpressionRecordedValues'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
summary_duration = 'summary_duration_example' # str | The duration of each summary interval. If specified in hours, minutes, seconds, or milliseconds, the summary durations will be evenly spaced UTC time intervals. Longer interval types are interpreted using wall clock rules and are time zone dependent. (optional)
summary_type = ['summary_type_example'] # list[str] | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType. (optional)
time_type = 'time_type_example' # str | Specifies how to calculate the timestamp for each interval. The default is 'Auto'. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns a summary over the specified time range for the stream.
    api_response = api_instance.stream_get_summary(web_id, calculation_basis=calculation_basis, end_time=end_time, filter_expression=filter_expression, sample_interval=sample_interval, sample_type=sample_type, selected_fields=selected_fields, start_time=start_time, summary_duration=summary_duration, summary_type=summary_type, time_type=time_type, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **calculation_basis** | **str**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filter_expression** | **str**| A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. | [optional] 
 **sample_interval** | **str**| When the sampleType is Interval, sampleInterval specifies how often the filter expression is evaluated when computing the summary for an interval. | [optional] 
 **sample_type** | **str**| Defines the evaluation of an expression over a time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **summary_duration** | **str**| The duration of each summary interval. If specified in hours, minutes, seconds, or milliseconds, the summary durations will be evenly spaced UTC time intervals. Longer interval types are interpreted using wall clock rules and are time zone dependent. | [optional] 
 **summary_type** | [**list[str]**](str.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] 
 **time_type** | **str**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_value**
> InlineResponse20028 stream_get_value(web_id, desired_units=desired_units, selected_fields=selected_fields, time=time, time_zone=time_zone)

Returns the value of the stream at the specified time. By default, this is usually the current value.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
desired_units = 'desired_units_example' # str | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
time = 'time_example' # str | An optional time. The default time context is determined from the owning object - for example, the time range of the event frame or transfer which holds this attribute. Otherwise, the implementation of the Data Reference determines the meaning of no context. For Points or simply configured PI Point Data References, this means the snapshot value of the PI Point on the Data Server. (optional)
time_zone = 'time_zone_example' # str | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. (optional)

try: 
    # Returns the value of the stream at the specified time. By default, this is usually the current value.
    api_response = api_instance.stream_get_value(web_id, desired_units=desired_units, selected_fields=selected_fields, time=time, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **time** | **str**| An optional time. The default time context is determined from the owning object - for example, the time range of the event frame or transfer which holds this attribute. Otherwise, the implementation of the Data Reference determines the meaning of no context. For Points or simply configured PI Point Data References, this means the snapshot value of the PI Point on the Data Server. | [optional] 
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_update_value**
> stream_update_value(web_id, value, buffer_option=buffer_option, update_option=update_option)

Updates a value for the specified stream.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
value = swagger_client.Value1() # Value1 | The value to add or update.
buffer_option = 'buffer_option_example' # str | The desired AFBufferOption. The default is 'BufferIfPossible'. (optional)
update_option = 'update_option_example' # str | The desired AFUpdateOption. The default is 'Replace'. This parameter is ignored if the attribute is a configuration item. (optional)

try: 
    # Updates a value for the specified stream.
    api_instance.stream_update_value(web_id, value, buffer_option=buffer_option, update_option=update_option)
except ApiException as e:
    print("Exception when calling StreamApi->stream_update_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **value** | [**Value1**](Value1.md)| The value to add or update. | 
 **buffer_option** | **str**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **update_option** | **str**| The desired AFUpdateOption. The default is &#39;Replace&#39;. This parameter is ignored if the attribute is a configuration item. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_update_values**
> InlineResponse204 stream_update_values(web_id, values, buffer_option=buffer_option, update_option=update_option)

Updates multiple values for the specified stream.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
web_id = 'web_id_example' # str | The ID of the stream.
values = [swagger_client.InlineResponse20028()] # list[InlineResponse20028] | The values to add or update.
buffer_option = 'buffer_option_example' # str | The desired AFBufferOption. The default is 'BufferIfPossible'. (optional)
update_option = 'update_option_example' # str | The desired AFUpdateOption. The default is 'Replace'. (optional)

try: 
    # Updates multiple values for the specified stream.
    api_response = api_instance.stream_update_values(web_id, values, buffer_option=buffer_option, update_option=update_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_update_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the stream. | 
 **values** | [**list[InlineResponse20028]**](InlineResponse20028.md)| The values to add or update. | 
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

