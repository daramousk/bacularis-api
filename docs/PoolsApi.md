# swagger_client.PoolsApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_pools_get**](PoolsApi.md#api_v2_pools_get) | **GET** /api/v2/pools | Pool list
[**api_v2_pools_poolid_get**](PoolsApi.md#api_v2_pools_poolid_get) | **GET** /api/v2/pools/{poolid} | Find pool by PoolId
[**api_v2_pools_poolid_show_get**](PoolsApi.md#api_v2_pools_poolid_show_get) | **GET** /api/v2/pools/{poolid}/show | Show pool
[**api_v2_pools_poolid_update_put**](PoolsApi.md#api_v2_pools_poolid_update_put) | **PUT** /api/v2/pools/{poolid}/update | Update pool properties
[**api_v2_pools_poolid_update_volumes_put**](PoolsApi.md#api_v2_pools_poolid_update_volumes_put) | **PUT** /api/v2/pools/{poolid}/update/volumes | Update properties all volumes in pool
[**api_v2_pools_poolid_volumes_get**](PoolsApi.md#api_v2_pools_poolid_volumes_get) | **GET** /api/v2/pools/{poolid}/volumes | Get all volumes in pool
[**api_v2_pools_show_get**](PoolsApi.md#api_v2_pools_show_get) | **GET** /api/v2/pools/show | Show pools

# **api_v2_pools_get**
> InlineResponse20032 api_v2_pools_get(limit=limit)

Pool list

Get pool list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
limit = 56 # int | Item limit (optional)

try:
    # Pool list
    api_response = api_instance.api_v2_pools_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->api_v2_pools_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Item limit | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pools_poolid_get**
> InlineResponse20033 api_v2_pools_poolid_get(poolid)

Find pool by PoolId

Get pool by specific Pool identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
poolid = 56 # int | Pool identifier

try:
    # Find pool by PoolId
    api_response = api_instance.api_v2_pools_poolid_get(poolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->api_v2_pools_poolid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolid** | **int**| Pool identifier | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pools_poolid_show_get**
> InlineResponse20035 api_v2_pools_poolid_show_get(poolid, output=output)

Show pool

Get 'show pools' bconsole command output for specific pool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
poolid = 56 # int | Pool identifier
output = 'output_example' # str | Output format (optional)

try:
    # Show pool
    api_response = api_instance.api_v2_pools_poolid_show_get(poolid, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->api_v2_pools_poolid_show_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolid** | **int**| Pool identifier | 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pools_poolid_update_put**
> InlineResponse20036 api_v2_pools_poolid_update_put(poolid)

Update pool properties

Update properties in specific pool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
poolid = 56 # int | Pool identifier

try:
    # Update pool properties
    api_response = api_instance.api_v2_pools_poolid_update_put(poolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->api_v2_pools_poolid_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolid** | **int**| Pool identifier | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pools_poolid_update_volumes_put**
> InlineResponse20037 api_v2_pools_poolid_update_volumes_put(poolid)

Update properties all volumes in pool

Update properties all volumes in specific pool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
poolid = 56 # int | Pool identifier

try:
    # Update properties all volumes in pool
    api_response = api_instance.api_v2_pools_poolid_update_volumes_put(poolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->api_v2_pools_poolid_update_volumes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolid** | **int**| Pool identifier | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pools_poolid_volumes_get**
> InlineResponse20034 api_v2_pools_poolid_volumes_get(poolid)

Get all volumes in pool

Get all volumes in specific pool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
poolid = 56 # int | Pool identifier

try:
    # Get all volumes in pool
    api_response = api_instance.api_v2_pools_poolid_volumes_get(poolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->api_v2_pools_poolid_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolid** | **int**| Pool identifier | 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pools_show_get**
> InlineResponse20038 api_v2_pools_show_get(name=name)

Show pools

Get 'show pools' bconsole command output

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
name = 'name_example' # str | Pool name (optional)

try:
    # Show pools
    api_response = api_instance.api_v2_pools_show_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->api_v2_pools_show_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Pool name | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

