# swagger_client.DevicesApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_devices_device_name_list_get**](DevicesApi.md#api_v2_devices_device_name_list_get) | **GET** /api/v2/devices/{device_name}/list | List autochanger volume names (requires barcode reader)
[**api_v2_devices_device_name_listall_get**](DevicesApi.md#api_v2_devices_device_name_listall_get) | **GET** /api/v2/devices/{device_name}/listall | List all autochanger slots and drives
[**api_v2_devices_device_name_load_get**](DevicesApi.md#api_v2_devices_device_name_load_get) | **GET** /api/v2/devices/{device_name}/load | Get autochanger tape drive load output
[**api_v2_devices_device_name_load_put**](DevicesApi.md#api_v2_devices_device_name_load_put) | **PUT** /api/v2/devices/{device_name}/load | Load device
[**api_v2_devices_device_name_loaded_get**](DevicesApi.md#api_v2_devices_device_name_loaded_get) | **GET** /api/v2/devices/{device_name}/loaded | Get loaded slot in given tape drive
[**api_v2_devices_device_name_slots_get**](DevicesApi.md#api_v2_devices_device_name_slots_get) | **GET** /api/v2/devices/{device_name}/slots | Get how many slots has autochanger
[**api_v2_devices_device_name_transfer_get**](DevicesApi.md#api_v2_devices_device_name_transfer_get) | **GET** /api/v2/devices/{device_name}/transfer | Get output from transfering tape from source slot to destination slot
[**api_v2_devices_device_name_transfer_put**](DevicesApi.md#api_v2_devices_device_name_transfer_put) | **PUT** /api/v2/devices/{device_name}/transfer | Transfer tape from source slot to destination slot
[**api_v2_devices_device_name_unload_get**](DevicesApi.md#api_v2_devices_device_name_unload_get) | **GET** /api/v2/devices/{device_name}/unload | Get autochanger tape drive unload output
[**api_v2_devices_device_name_unload_put**](DevicesApi.md#api_v2_devices_device_name_unload_put) | **PUT** /api/v2/devices/{device_name}/unload | Unload device

# **api_v2_devices_device_name_list_get**
> InlineResponse20074 api_v2_devices_device_name_list_get(device_name)

List autochanger volume names (requires barcode reader)

List autochanger volume names (requires barcode reader)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name

try:
    # List autochanger volume names (requires barcode reader)
    api_response = api_instance.api_v2_devices_device_name_list_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_listall_get**
> InlineResponse20075 api_v2_devices_device_name_listall_get(device_name)

List all autochanger slots and drives

List all autochanger slots and drives

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name

try:
    # List all autochanger slots and drives
    api_response = api_instance.api_v2_devices_device_name_listall_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_listall_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_load_get**
> InlineResponse20070 api_v2_devices_device_name_load_get(device_name, out_id)

Get autochanger tape drive load output

Get autochanger tape drive load output by output identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name
out_id = 'out_id_example' # str | Output identifier acquired during load drive start.

try:
    # Get autochanger tape drive load output
    api_response = api_instance.api_v2_devices_device_name_load_get(device_name, out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_load_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 
 **out_id** | **str**| Output identifier acquired during load drive start. | 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_load_put**
> InlineResponse20071 api_v2_devices_device_name_load_put(device_name, drive, slot)

Load device

Load autochanger tape drive device.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name
drive = 'drive_example' # str | Drive name
slot = 56 # int | Slot number

try:
    # Load device
    api_response = api_instance.api_v2_devices_device_name_load_put(device_name, drive, slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_load_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 
 **drive** | **str**| Drive name | 
 **slot** | **int**| Slot number | 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_loaded_get**
> InlineResponse20073 api_v2_devices_device_name_loaded_get(device_name, drive)

Get loaded slot in given tape drive

Get loaded slot in given autochanger tape drive

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name
drive = 'drive_example' # str | Drive name

try:
    # Get loaded slot in given tape drive
    api_response = api_instance.api_v2_devices_device_name_loaded_get(device_name, drive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_loaded_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 
 **drive** | **str**| Drive name | 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_slots_get**
> InlineResponse20076 api_v2_devices_device_name_slots_get(device_name)

Get how many slots has autochanger

Get how many slots has autochanger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name

try:
    # Get how many slots has autochanger
    api_response = api_instance.api_v2_devices_device_name_slots_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_slots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_transfer_get**
> InlineResponse20077 api_v2_devices_device_name_transfer_get(device_name, out_id)

Get output from transfering tape from source slot to destination slot

Get output from ransfering tape from source slot to destination slot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name
out_id = 'out_id_example' # str | Output identifier acquired during transfer tape start.

try:
    # Get output from transfering tape from source slot to destination slot
    api_response = api_instance.api_v2_devices_device_name_transfer_get(device_name, out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_transfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 
 **out_id** | **str**| Output identifier acquired during transfer tape start. | 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_transfer_put**
> InlineResponse20071 api_v2_devices_device_name_transfer_put(device_name, drive, slotsrc, destsrc)

Transfer tape from source slot to destination slot

Transfer tape from source slot to destination slot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name
drive = 'drive_example' # str | Drive name
slotsrc = 56 # int | Source slot number
destsrc = 56 # int | Destination slot number

try:
    # Transfer tape from source slot to destination slot
    api_response = api_instance.api_v2_devices_device_name_transfer_put(device_name, drive, slotsrc, destsrc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_transfer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 
 **drive** | **str**| Drive name | 
 **slotsrc** | **int**| Source slot number | 
 **destsrc** | **int**| Destination slot number | 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_unload_get**
> InlineResponse20072 api_v2_devices_device_name_unload_get(device_name, out_id)

Get autochanger tape drive unload output

Get autochanger tape drive unload output by output identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name
out_id = 'out_id_example' # str | Output identifier acquired during unload drive start.

try:
    # Get autochanger tape drive unload output
    api_response = api_instance.api_v2_devices_device_name_unload_get(device_name, out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_unload_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 
 **out_id** | **str**| Output identifier acquired during unload drive start. | 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_devices_device_name_unload_put**
> InlineResponse20071 api_v2_devices_device_name_unload_put(device_name, drive, slot)

Unload device

Unload autochanger tape drive device.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_name = 'device_name_example' # str | Autochanger tape drive device name
drive = 'drive_example' # str | Drive name
slot = 56 # int | Slot number

try:
    # Unload device
    api_response = api_instance.api_v2_devices_device_name_unload_put(device_name, drive, slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->api_v2_devices_device_name_unload_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Autochanger tape drive device name | 
 **drive** | **str**| Drive name | 
 **slot** | **int**| Slot number | 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

