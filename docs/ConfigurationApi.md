# swagger_client.ConfigurationApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_delete**](ConfigurationApi.md#configuration_delete) | **DELETE** /system/configuration/{key} | Delete a configuration item.
[**configuration_get**](ConfigurationApi.md#configuration_get) | **GET** /system/configuration/{key} | Get the value of a configuration item.
[**configuration_list**](ConfigurationApi.md#configuration_list) | **GET** /system/configuration | Get the current system configuration.


# **configuration_delete**
> configuration_delete(key)

Delete a configuration item.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
key = 'key_example' # str | The key of the configuration item to remove.

try: 
    # Delete a configuration item.
    api_instance.configuration_delete(key)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the configuration item to remove. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_get**
> object configuration_get(key)

Get the value of a configuration item.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
key = 'key_example' # str | The key of the configuration item.

try: 
    # Get the value of a configuration item.
    api_response = api_instance.configuration_get(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the configuration item. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_list**
> dict(str, object) configuration_list()

Get the current system configuration.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try: 
    # Get the current system configuration.
    api_response = api_instance.configuration_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, object)**](dict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

