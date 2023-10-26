# swagger_client.VolumesApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_volumes_get**](VolumesApi.md#api_v2_volumes_get) | **GET** /api/v2/volumes | Volume list
[**api_v2_volumes_label_barcodes_get**](VolumesApi.md#api_v2_volumes_label_barcodes_get) | **GET** /api/v2/volumes/label/barcodes | Get label barcodes volume output
[**api_v2_volumes_label_barcodes_post**](VolumesApi.md#api_v2_volumes_label_barcodes_post) | **POST** /api/v2/volumes/label/barcodes | Label volume using barcodes
[**api_v2_volumes_label_get**](VolumesApi.md#api_v2_volumes_label_get) | **GET** /api/v2/volumes/label | Get label volume output
[**api_v2_volumes_label_post**](VolumesApi.md#api_v2_volumes_label_post) | **POST** /api/v2/volumes/label | Label volume
[**api_v2_volumes_mediaid_delete**](VolumesApi.md#api_v2_volumes_mediaid_delete) | **DELETE** /api/v2/volumes/{mediaid} | Delete volume by MediaId
[**api_v2_volumes_mediaid_get**](VolumesApi.md#api_v2_volumes_mediaid_get) | **GET** /api/v2/volumes/{mediaid} | Find volume by MediaId
[**api_v2_volumes_mediaid_jobs_get**](VolumesApi.md#api_v2_volumes_mediaid_jobs_get) | **GET** /api/v2/volumes/{mediaid}/jobs | Jobs on volume
[**api_v2_volumes_mediaid_prune_put**](VolumesApi.md#api_v2_volumes_mediaid_prune_put) | **PUT** /api/v2/volumes/{mediaid}/prune | Prune volume
[**api_v2_volumes_mediaid_purge_put**](VolumesApi.md#api_v2_volumes_mediaid_purge_put) | **PUT** /api/v2/volumes/{mediaid}/purge | Purge volume
[**api_v2_volumes_mediaid_put**](VolumesApi.md#api_v2_volumes_mediaid_put) | **PUT** /api/v2/volumes/{mediaid} | Update volume properties
[**api_v2_volumes_required_jobid_fileid_get**](VolumesApi.md#api_v2_volumes_required_jobid_fileid_get) | **GET** /api/v2/volumes/required/{jobid}/{fileid} | Get volumes required to restore file
[**api_v2_volumes_update_barcodes_get**](VolumesApi.md#api_v2_volumes_update_barcodes_get) | **GET** /api/v2/volumes/update/barcodes | Get update slots output using barcodes
[**api_v2_volumes_update_barcodes_put**](VolumesApi.md#api_v2_volumes_update_barcodes_put) | **PUT** /api/v2/volumes/update/barcodes | Update slots using barcodes
[**api_v2_volumes_update_get**](VolumesApi.md#api_v2_volumes_update_get) | **GET** /api/v2/volumes/update | Get update slots output
[**api_v2_volumes_update_put**](VolumesApi.md#api_v2_volumes_update_put) | **PUT** /api/v2/volumes/update | Update slots

# **api_v2_volumes_get**
> InlineResponse20039 api_v2_volumes_get(limit=limit)

Volume list

Get volume list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
limit = 56 # int | Item limit (optional)

try:
    # Volume list
    api_response = api_instance.api_v2_volumes_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Item limit | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_label_barcodes_get**
> InlineResponse20046 api_v2_volumes_label_barcodes_get(out_id)

Get label barcodes volume output

Get label barcodes volume output by output identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
out_id = 'out_id_example' # str | Output identifier acquired during label start.

try:
    # Get label barcodes volume output
    api_response = api_instance.api_v2_volumes_label_barcodes_get(out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_label_barcodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_id** | **str**| Output identifier acquired during label start. | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_label_barcodes_post**
> InlineResponse20047 api_v2_volumes_label_barcodes_post(slots, drive, storageid, storage, poolid, pool)

Label volume using barcodes

Label volume with specified name (with using barcode).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
slots = 'slots_example' # str | Slots numbers or slots range (ex. 1-3,5,10)
drive = 56 # int | Drive number
storageid = 56 # int | Storage identifier
storage = 'storage_example' # str | Storage name can be used instead of storageid
poolid = 56 # int | Pool identifier
pool = 'pool_example' # str | Pool name can be used instead of poolid

try:
    # Label volume using barcodes
    api_response = api_instance.api_v2_volumes_label_barcodes_post(slots, drive, storageid, storage, poolid, pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_label_barcodes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slots** | **str**| Slots numbers or slots range (ex. 1-3,5,10) | 
 **drive** | **int**| Drive number | 
 **storageid** | **int**| Storage identifier | 
 **storage** | **str**| Storage name can be used instead of storageid | 
 **poolid** | **int**| Pool identifier | 
 **pool** | **str**| Pool name can be used instead of poolid | 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_label_get**
> InlineResponse20046 api_v2_volumes_label_get(out_id)

Get label volume output

Get label volume output by output identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
out_id = 'out_id_example' # str | Output identifier acquired during label start.

try:
    # Get label volume output
    api_response = api_instance.api_v2_volumes_label_get(out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_label_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_id** | **str**| Output identifier acquired during label start. | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_label_post**
> InlineResponse20047 api_v2_volumes_label_post(volume, slot, drive, storageid, storage, poolid, pool)

Label volume

Label volume with specified name (without using barcode).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
volume = 'volume_example' # str | Volume name
slot = 56 # int | Slot number
drive = 56 # int | Drive number
storageid = 56 # int | Storage identifier
storage = 'storage_example' # str | Storage name can be used instead of storageid
poolid = 56 # int | Pool identifier
pool = 'pool_example' # str | Pool name can be used instead of poolid

try:
    # Label volume
    api_response = api_instance.api_v2_volumes_label_post(volume, slot, drive, storageid, storage, poolid, pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_label_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume** | **str**| Volume name | 
 **slot** | **int**| Slot number | 
 **drive** | **int**| Drive number | 
 **storageid** | **int**| Storage identifier | 
 **storage** | **str**| Storage name can be used instead of storageid | 
 **poolid** | **int**| Pool identifier | 
 **pool** | **str**| Pool name can be used instead of poolid | 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_mediaid_delete**
> InlineResponse20042 api_v2_volumes_mediaid_delete(mediaid)

Delete volume by MediaId

Delete volume from the Catalog by specific Volume/Media identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
mediaid = 56 # int | Media/volume identifier

try:
    # Delete volume by MediaId
    api_response = api_instance.api_v2_volumes_mediaid_delete(mediaid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_mediaid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaid** | **int**| Media/volume identifier | 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_mediaid_get**
> InlineResponse20040 api_v2_volumes_mediaid_get(mediaid)

Find volume by MediaId

Get volume by specific Volume/Media identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
mediaid = 56 # int | Media/volume identifier

try:
    # Find volume by MediaId
    api_response = api_instance.api_v2_volumes_mediaid_get(mediaid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_mediaid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaid** | **int**| Media/volume identifier | 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_mediaid_jobs_get**
> InlineResponse2004 api_v2_volumes_mediaid_jobs_get(mediaid)

Jobs on volume

Get jobs done on volume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
mediaid = 56 # int | Media/volume identifier

try:
    # Jobs on volume
    api_response = api_instance.api_v2_volumes_mediaid_jobs_get(mediaid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_mediaid_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaid** | **int**| Media/volume identifier | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_mediaid_prune_put**
> InlineResponse20043 api_v2_volumes_mediaid_prune_put(mediaid)

Prune volume

Do prunning on volume.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
mediaid = 56 # int | Media/volume identifier

try:
    # Prune volume
    api_response = api_instance.api_v2_volumes_mediaid_prune_put(mediaid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_mediaid_prune_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaid** | **int**| Media/volume identifier | 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_mediaid_purge_put**
> InlineResponse20044 api_v2_volumes_mediaid_purge_put(mediaid)

Purge volume

Do purging on volume.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
mediaid = 56 # int | Media/volume identifier

try:
    # Purge volume
    api_response = api_instance.api_v2_volumes_mediaid_purge_put(mediaid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_mediaid_purge_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaid** | **int**| Media/volume identifier | 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_mediaid_put**
> InlineResponse20041 api_v2_volumes_mediaid_put(mediaid, volstatus=volstatus, poolid=poolid, volretention=volretention, voluseduration=voluseduration, maxvoljobs=maxvoljobs, maxvolfiles=maxvolfiles, maxvolbytes=maxvolbytes, slot=slot, recycle=recycle, enabled=enabled, inchanger=inchanger)

Update volume properties

Update specific volume properties.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
mediaid = 56 # int | Media/volume identifier
volstatus = 'volstatus_example' # str | Volume status (optional)
poolid = 56 # int | Update Volume Pool by Pool identifier (optional)
volretention = 56 # int | Volume retention time (optional)
voluseduration = 56 # int | Volume use duration time (optional)
maxvoljobs = 56 # int | Maximum volume jobs (optional)
maxvolfiles = 56 # int | Maximum volume files (optional)
maxvolbytes = 56 # int | Maximum volume bytes (optional)
slot = 56 # int | Volume slot (optional)
recycle = 56 # int | Volume recycle flag (optional)
enabled = 56 # int | Volume enabled flag (optional)
inchanger = 56 # int | Volume InChanger flag (optional)

try:
    # Update volume properties
    api_response = api_instance.api_v2_volumes_mediaid_put(mediaid, volstatus=volstatus, poolid=poolid, volretention=volretention, voluseduration=voluseduration, maxvoljobs=maxvoljobs, maxvolfiles=maxvolfiles, maxvolbytes=maxvolbytes, slot=slot, recycle=recycle, enabled=enabled, inchanger=inchanger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_mediaid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaid** | **int**| Media/volume identifier | 
 **volstatus** | **str**| Volume status | [optional] 
 **poolid** | **int**| Update Volume Pool by Pool identifier | [optional] 
 **volretention** | **int**| Volume retention time | [optional] 
 **voluseduration** | **int**| Volume use duration time | [optional] 
 **maxvoljobs** | **int**| Maximum volume jobs | [optional] 
 **maxvolfiles** | **int**| Maximum volume files | [optional] 
 **maxvolbytes** | **int**| Maximum volume bytes | [optional] 
 **slot** | **int**| Volume slot | [optional] 
 **recycle** | **int**| Volume recycle flag | [optional] 
 **enabled** | **int**| Volume enabled flag | [optional] 
 **inchanger** | **int**| Volume InChanger flag | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_required_jobid_fileid_get**
> InlineResponse20045 api_v2_volumes_required_jobid_fileid_get(jobid, fileid)

Get volumes required to restore file

Get volumes required to restore a file from a job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
jobid = 56 # int | Job identifier
fileid = 56 # int | File identifier

try:
    # Get volumes required to restore file
    api_response = api_instance.api_v2_volumes_required_jobid_fileid_get(jobid, fileid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_required_jobid_fileid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 
 **fileid** | **int**| File identifier | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_update_barcodes_get**
> InlineResponse20048 api_v2_volumes_update_barcodes_get(out_id)

Get update slots output using barcodes

Get update barcodes slots output by output identifier (with barcodes)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
out_id = 'out_id_example' # str | Output identifier acquired during update barcodes slots start.

try:
    # Get update slots output using barcodes
    api_response = api_instance.api_v2_volumes_update_barcodes_get(out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_update_barcodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_id** | **str**| Output identifier acquired during update barcodes slots start. | 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_update_barcodes_put**
> InlineResponse20049 api_v2_volumes_update_barcodes_put(slots, drive, storageid, storage)

Update slots using barcodes

Update volume slots (with using barcode).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
slots = 'slots_example' # str | Slots numbers or slots range (ex. 1-3,5,10)
drive = 56 # int | Drive number
storageid = 56 # int | Storage identifier
storage = 'storage_example' # str | Storage name can be used instead of storageid

try:
    # Update slots using barcodes
    api_response = api_instance.api_v2_volumes_update_barcodes_put(slots, drive, storageid, storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_update_barcodes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slots** | **str**| Slots numbers or slots range (ex. 1-3,5,10) | 
 **drive** | **int**| Drive number | 
 **storageid** | **int**| Storage identifier | 
 **storage** | **str**| Storage name can be used instead of storageid | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_update_get**
> InlineResponse20048 api_v2_volumes_update_get(out_id)

Get update slots output

Get update slots output by output identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
out_id = 'out_id_example' # str | Output identifier acquired during update slots start.

try:
    # Get update slots output
    api_response = api_instance.api_v2_volumes_update_get(out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_update_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_id** | **str**| Output identifier acquired during update slots start. | 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_volumes_update_put**
> InlineResponse20049 api_v2_volumes_update_put(slots, drive, storageid, storage)

Update slots

Update volume slots (without using barcode).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VolumesApi()
slots = 'slots_example' # str | Slots numbers or slots range (ex. 1-3,5,10)
drive = 56 # int | Drive number
storageid = 56 # int | Storage identifier
storage = 'storage_example' # str | Storage name can be used instead of storageid

try:
    # Update slots
    api_response = api_instance.api_v2_volumes_update_put(slots, drive, storageid, storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->api_v2_volumes_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slots** | **str**| Slots numbers or slots range (ex. 1-3,5,10) | 
 **drive** | **int**| Drive number | 
 **storageid** | **int**| Storage identifier | 
 **storage** | **str**| Storage name can be used instead of storageid | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

