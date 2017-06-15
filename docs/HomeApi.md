# swagger_client.HomeApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**home_get**](HomeApi.md#home_get) | **GET** / | Get top level links for this PI System Web API instance.


# **home_get**
> InlineResponse200 home_get()

Get top level links for this PI System Web API instance.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomeApi()

try: 
    # Get top level links for this PI System Web API instance.
    api_response = api_instance.home_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomeApi->home_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

