# swagger_client.ChannelApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_instances**](ChannelApi.md#channel_instances) | **GET** /channels/instances | Retrieves a list of currently running channel instances.


# **channel_instances**
> channel_instances()

Retrieves a list of currently running channel instances.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApi()

try: 
    # Retrieves a list of currently running channel instances.
    api_instance.channel_instances()
except ApiException as e:
    print("Exception when calling ChannelApi->channel_instances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

