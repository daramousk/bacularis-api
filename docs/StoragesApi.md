# swagger_client.StoragesApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_storages_get**](StoragesApi.md#api_v2_storages_get) | **GET** /api/v2/storages | Storage list
[**api_v2_storages_show_get**](StoragesApi.md#api_v2_storages_show_get) | **GET** /api/v2/storages/show | Show storages
[**api_v2_storages_storageid_get**](StoragesApi.md#api_v2_storages_storageid_get) | **GET** /api/v2/storages/{storageid} | Find storage by StorageId
[**api_v2_storages_storageid_mount_get**](StoragesApi.md#api_v2_storages_storageid_mount_get) | **GET** /api/v2/storages/{storageid}/mount | Mount storage
[**api_v2_storages_storageid_release_get**](StoragesApi.md#api_v2_storages_storageid_release_get) | **GET** /api/v2/storages/{storageid}/release | Release storage
[**api_v2_storages_storageid_show_get**](StoragesApi.md#api_v2_storages_storageid_show_get) | **GET** /api/v2/storages/{storageid}/show | Show storage
[**api_v2_storages_storageid_status_get**](StoragesApi.md#api_v2_storages_storageid_status_get) | **GET** /api/v2/storages/{storageid}/status | Storage status
[**api_v2_storages_storageid_umount_get**](StoragesApi.md#api_v2_storages_storageid_umount_get) | **GET** /api/v2/storages/{storageid}/umount | Umount storage

# **api_v2_storages_get**
> InlineResponse20024 api_v2_storages_get(limit=limit)

Storage list

Get storage list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoragesApi()
limit = 56 # int | Item limit (optional)

try:
    # Storage list
    api_response = api_instance.api_v2_storages_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->api_v2_storages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Item limit | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storages_show_get**
> InlineResponse20031 api_v2_storages_show_get(name=name, output=output)

Show storages

Get 'show storages' bconsole command output

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoragesApi()
name = 'name_example' # str | Storage name (optional)
output = 'output_example' # str | Output format (optional)

try:
    # Show storages
    api_response = api_instance.api_v2_storages_show_get(name=name, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->api_v2_storages_show_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Storage name | [optional] 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storages_storageid_get**
> InlineResponse20025 api_v2_storages_storageid_get(storageid)

Find storage by StorageId

Get storage by specific Storage identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoragesApi()
storageid = 56 # int | Storage identifier

try:
    # Find storage by StorageId
    api_response = api_instance.api_v2_storages_storageid_get(storageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->api_v2_storages_storageid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storageid** | **int**| Storage identifier | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storages_storageid_mount_get**
> InlineResponse20028 api_v2_storages_storageid_mount_get(storageid, drive, device, slot)

Mount storage

Mount storage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoragesApi()
storageid = 56 # int | Storage identifier
drive = 56 # int | Storage drive
device = 'device_example' # str | Storage device (can be used instead drive)
slot = 56 # int | Storage slot

try:
    # Mount storage
    api_response = api_instance.api_v2_storages_storageid_mount_get(storageid, drive, device, slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->api_v2_storages_storageid_mount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storageid** | **int**| Storage identifier | 
 **drive** | **int**| Storage drive | 
 **device** | **str**| Storage device (can be used instead drive) | 
 **slot** | **int**| Storage slot | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storages_storageid_release_get**
> InlineResponse20030 api_v2_storages_storageid_release_get(storageid, drive, device)

Release storage

Release storage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoragesApi()
storageid = 56 # int | Storage identifier
drive = 56 # int | Storage drive
device = 'device_example' # str | Storage device (can be used instead drive)

try:
    # Release storage
    api_response = api_instance.api_v2_storages_storageid_release_get(storageid, drive, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->api_v2_storages_storageid_release_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storageid** | **int**| Storage identifier | 
 **drive** | **int**| Storage drive | 
 **device** | **str**| Storage device (can be used instead drive) | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storages_storageid_show_get**
> InlineResponse20026 api_v2_storages_storageid_show_get(storageid, output=output)

Show storage

Get 'show storages' bconsole command output for specific storage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoragesApi()
storageid = 56 # int | Storage identifier
output = 'output_example' # str | Output format (optional)

try:
    # Show storage
    api_response = api_instance.api_v2_storages_storageid_show_get(storageid, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->api_v2_storages_storageid_show_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storageid** | **int**| Storage identifier | 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storages_storageid_status_get**
> InlineResponse20027 api_v2_storages_storageid_status_get(storageid, output=output, type=type)

Storage status

Get storage status for specific storage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoragesApi()
storageid = 56 # int | Storage identifier
output = 'output_example' # str | Output format (optional)
type = 'type_example' # str | Output type using together with output=json parameter. (optional)

try:
    # Storage status
    api_response = api_instance.api_v2_storages_storageid_status_get(storageid, output=output, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->api_v2_storages_storageid_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storageid** | **int**| Storage identifier | 
 **output** | **str**| Output format | [optional] 
 **type** | **str**| Output type using together with output&#x3D;json parameter. | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storages_storageid_umount_get**
> InlineResponse20029 api_v2_storages_storageid_umount_get(storageid, drive, device)

Umount storage

Umount storage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoragesApi()
storageid = 56 # int | Storage identifier
drive = 56 # int | Storage drive
device = 'device_example' # str | Storage device (can be used instead drive)

try:
    # Umount storage
    api_response = api_instance.api_v2_storages_storageid_umount_get(storageid, drive, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->api_v2_storages_storageid_umount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storageid** | **int**| Storage identifier | 
 **drive** | **int**| Storage drive | 
 **device** | **str**| Storage device (can be used instead drive) | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

