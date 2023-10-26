# swagger_client.DirectorsApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_directors_director_name_status_get**](DirectorsApi.md#api_v2_directors_director_name_status_get) | **GET** /api/v2/directors/{director_name}/status | Get director status

# **api_v2_directors_director_name_status_get**
> InlineResponse20080 api_v2_directors_director_name_status_get(director_name, output=output, type=type)

Get director status

Get director status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DirectorsApi()
director_name = 'director_name_example' # str | Director name
output = 'output_example' # str | Output format (optional)
type = 'type_example' # str | Output type using together with output=json parameter. (optional)

try:
    # Get director status
    api_response = api_instance.api_v2_directors_director_name_status_get(director_name, output=output, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->api_v2_directors_director_name_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **director_name** | **str**| Director name | 
 **output** | **str**| Output format | [optional] 
 **type** | **str**| Output type using together with output&#x3D;json parameter. | [optional] 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

