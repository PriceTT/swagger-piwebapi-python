# swagger_client.SystemApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_cache_instances**](SystemApi.md#system_cache_instances) | **GET** /system/cacheinstances | Get AF cache instances currently in use by the system. These are caches from which user requests are serviced. The number of instances depends on the number of users connected to the service, the service&#39;s authentication method, and the cache instance configuration.
[**system_landing**](SystemApi.md#system_landing) | **GET** /system | Get system links for this PI System Web API instance.
[**system_status**](SystemApi.md#system_status) | **GET** /system/status | Get the system uptime, the system state and the number of cache instances for this PI System Web API instance.
[**system_user_info**](SystemApi.md#system_user_info) | **GET** /system/userinfo | Get information about the Windows identity used to fulfill the request. This depends on the service&#39;s authentication method and the credentials passed by the client. The impersonation level of the Windows identity is included.
[**system_versions**](SystemApi.md#system_versions) | **GET** /system/versions | Get the current versions of the PI Web API instance and all external plugins.


# **system_cache_instances**
> InlineResponse20046 system_cache_instances()

Get AF cache instances currently in use by the system. These are caches from which user requests are serviced. The number of instances depends on the number of users connected to the service, the service's authentication method, and the cache instance configuration.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try: 
    # Get AF cache instances currently in use by the system. These are caches from which user requests are serviced. The number of instances depends on the number of users connected to the service, the service's authentication method, and the cache instance configuration.
    api_response = api_instance.system_cache_instances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_cache_instances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_landing**
> InlineResponse20045 system_landing()

Get system links for this PI System Web API instance.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try: 
    # Get system links for this PI System Web API instance.
    api_response = api_instance.system_landing()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_landing: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_status**
> InlineResponse20047 system_status()

Get the system uptime, the system state and the number of cache instances for this PI System Web API instance.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try: 
    # Get the system uptime, the system state and the number of cache instances for this PI System Web API instance.
    api_response = api_instance.system_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_user_info**
> InlineResponse20048 system_user_info()

Get information about the Windows identity used to fulfill the request. This depends on the service's authentication method and the credentials passed by the client. The impersonation level of the Windows identity is included.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try: 
    # Get information about the Windows identity used to fulfill the request. This depends on the service's authentication method and the credentials passed by the client. The impersonation level of the Windows identity is included.
    api_response = api_instance.system_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_versions**
> dict(str, InlineResponse20049) system_versions()

Get the current versions of the PI Web API instance and all external plugins.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try: 
    # Get the current versions of the PI Web API instance and all external plugins.
    api_response = api_instance.system_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, InlineResponse20049)**](InlineResponse20049.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

