# swagger_client.CalculationApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculation_get_at_intervals**](CalculationApi.md#calculation_get_at_intervals) | **GET** /calculation/intervals | Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.
[**calculation_get_at_recorded**](CalculationApi.md#calculation_get_at_recorded) | **GET** /calculation/recorded | Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.
[**calculation_get_at_times**](CalculationApi.md#calculation_get_at_times) | **GET** /calculation/times | Returns the result of evaluating the expression at the specified timestamps.
[**calculation_get_summary**](CalculationApi.md#calculation_get_summary) | **GET** /calculation/summary | Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.


# **calculation_get_at_intervals**
> InlineResponse20033 calculation_get_at_intervals(end_time=end_time, expression=expression, sample_interval=sample_interval, selected_fields=selected_fields, start_time=start_time, web_id=web_id)

Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculationApi()
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
expression = 'expression_example' # str | A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. (optional)
sample_interval = 'sample_interval_example' # str | A time span specifies how often the filter expression is evaluated when computing the summary for an interval. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
web_id = 'web_id_example' # str | The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. (optional)

try: 
    # Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.
    api_response = api_instance.calculation_get_at_intervals(end_time=end_time, expression=expression, sample_interval=sample_interval, selected_fields=selected_fields, start_time=start_time, web_id=web_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculationApi->calculation_get_at_intervals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **expression** | **str**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. | [optional] 
 **sample_interval** | **str**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **web_id** | **str**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculation_get_at_recorded**
> InlineResponse20033 calculation_get_at_recorded(end_time=end_time, expression=expression, selected_fields=selected_fields, start_time=start_time, web_id=web_id)

Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculationApi()
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
expression = 'expression_example' # str | A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
web_id = 'web_id_example' # str | The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. (optional)

try: 
    # Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.
    api_response = api_instance.calculation_get_at_recorded(end_time=end_time, expression=expression, selected_fields=selected_fields, start_time=start_time, web_id=web_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculationApi->calculation_get_at_recorded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **expression** | **str**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **web_id** | **str**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculation_get_at_times**
> InlineResponse20033 calculation_get_at_times(expression=expression, selected_fields=selected_fields, sort_order=sort_order, time=time, web_id=web_id)

Returns the result of evaluating the expression at the specified timestamps.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculationApi()
expression = 'expression_example' # str | A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
sort_order = 'sort_order_example' # str | The order that the returned collection is sorted. The default is 'Ascending'. (optional)
time = ['time_example'] # list[str] | A list of timestamps at which to calculate the expression. (optional)
web_id = 'web_id_example' # str | The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. (optional)

try: 
    # Returns the result of evaluating the expression at the specified timestamps.
    api_response = api_instance.calculation_get_at_times(expression=expression, selected_fields=selected_fields, sort_order=sort_order, time=time, web_id=web_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculationApi->calculation_get_at_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sort_order** | **str**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **time** | [**list[str]**](str.md)| A list of timestamps at which to calculate the expression. | [optional] 
 **web_id** | **str**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculation_get_summary**
> InlineResponse20034 calculation_get_summary(calculation_basis=calculation_basis, end_time=end_time, expression=expression, sample_interval=sample_interval, sample_type=sample_type, selected_fields=selected_fields, start_time=start_time, summary_duration=summary_duration, summary_type=summary_type, time_type=time_type, web_id=web_id)

Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CalculationApi()
calculation_basis = 'calculation_basis_example' # str | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'. (optional)
end_time = 'end_time_example' # str | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. (optional)
expression = 'expression_example' # str | A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. (optional)
sample_interval = 'sample_interval_example' # str | A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'. (optional)
sample_type = 'sample_type_example' # str | A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'. (optional)
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)
start_time = 'start_time_example' # str | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set. (optional)
summary_duration = 'summary_duration_example' # str | The duration of each summary interval. (optional)
summary_type = ['summary_type_example'] # list[str] | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType. (optional)
time_type = 'time_type_example' # str | Specifies how to calculate the timestamp for each interval. The default is 'Auto'. (optional)
web_id = 'web_id_example' # str | The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. (optional)

try: 
    # Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.
    api_response = api_instance.calculation_get_summary(calculation_basis=calculation_basis, end_time=end_time, expression=expression, sample_interval=sample_interval, sample_type=sample_type, selected_fields=selected_fields, start_time=start_time, summary_duration=summary_duration, summary_type=summary_type, time_type=time_type, web_id=web_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculationApi->calculation_get_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_basis** | **str**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] 
 **end_time** | **str**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **expression** | **str**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. | [optional] 
 **sample_interval** | **str**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;. | [optional] 
 **sample_type** | **str**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **start_time** | **str**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **summary_duration** | **str**| The duration of each summary interval. | [optional] 
 **summary_type** | [**list[str]**](str.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] 
 **time_type** | **str**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] 
 **web_id** | **str**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

