# swagger_client.AttributeTraitApi

All URIs are relative to *https://dev.dstcontrols.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attribute_trait_get**](AttributeTraitApi.md#attribute_trait_get) | **GET** /attributetraits/{name} | Retrieve an attribute trait.
[**attribute_trait_get_by_category**](AttributeTraitApi.md#attribute_trait_get_by_category) | **GET** /attributetraits | Retrieve all attribute traits of the specified category/categories.


# **attribute_trait_get**
> InlineResponse20032Items attribute_trait_get(name, selected_fields=selected_fields)

Retrieve an attribute trait.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTraitApi()
name = 'name_example' # str | The name or abbreviation of the attribute trait.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve an attribute trait.
    api_response = api_instance.attribute_trait_get(name, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTraitApi->attribute_trait_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name or abbreviation of the attribute trait. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20032Items**](InlineResponse20032Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_trait_get_by_category**
> InlineResponse20032 attribute_trait_get_by_category(category, selected_fields=selected_fields)

Retrieve all attribute traits of the specified category/categories.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTraitApi()
category = ['category_example'] # list[str] | The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \"all\", then all attribute traits of all categories will be returned.
selected_fields = 'selected_fields_example' # str | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. (optional)

try: 
    # Retrieve all attribute traits of the specified category/categories.
    api_response = api_instance.attribute_trait_get_by_category(category, selected_fields=selected_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTraitApi->attribute_trait_get_by_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**list[str]**](str.md)| The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \&quot;all\&quot;, then all attribute traits of all categories will be returned. | 
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

