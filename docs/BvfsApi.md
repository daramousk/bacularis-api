# swagger_client.BvfsApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_bvfs_cleanup_put**](BvfsApi.md#api_v2_bvfs_cleanup_put) | **PUT** /api/v2/bvfs/cleanup | Cleanup BVFS (remove temporary table)
[**api_v2_bvfs_clear_put**](BvfsApi.md#api_v2_bvfs_clear_put) | **PUT** /api/v2/bvfs/clear | Clear BVFS cache
[**api_v2_bvfs_getjobids_get**](BvfsApi.md#api_v2_bvfs_getjobids_get) | **GET** /api/v2/bvfs/getjobids | BVFS get particular jobids to restore
[**api_v2_bvfs_lsdirs_get**](BvfsApi.md#api_v2_bvfs_lsdirs_get) | **GET** /api/v2/bvfs/lsdirs | BVFS list directories
[**api_v2_bvfs_lsfiles_get**](BvfsApi.md#api_v2_bvfs_lsfiles_get) | **GET** /api/v2/bvfs/lsfiles | BVFS list files
[**api_v2_bvfs_restore_post**](BvfsApi.md#api_v2_bvfs_restore_post) | **POST** /api/v2/bvfs/restore | Prepare BVFS restore
[**api_v2_bvfs_update_put**](BvfsApi.md#api_v2_bvfs_update_put) | **PUT** /api/v2/bvfs/update | Update BVFS cache
[**api_v2_bvfs_versions_get**](BvfsApi.md#api_v2_bvfs_versions_get) | **GET** /api/v2/bvfs/versions | BVFS list file versions

# **api_v2_bvfs_cleanup_put**
> InlineResponse20062 api_v2_bvfs_cleanup_put(path)

Cleanup BVFS (remove temporary table)

Cleanup BVFS

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BvfsApi()
path = 56 # int | Path in format b2[0-9]+

try:
    # Cleanup BVFS (remove temporary table)
    api_response = api_instance.api_v2_bvfs_cleanup_put(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BvfsApi->api_v2_bvfs_cleanup_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **int**| Path in format b2[0-9]+ | 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bvfs_clear_put**
> InlineResponse20061 api_v2_bvfs_clear_put()

Clear BVFS cache

Clear BVFS cache

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BvfsApi()

try:
    # Clear BVFS cache
    api_response = api_instance.api_v2_bvfs_clear_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BvfsApi->api_v2_bvfs_clear_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bvfs_getjobids_get**
> InlineResponse20059 api_v2_bvfs_getjobids_get(jobid)

BVFS get particular jobids to restore

BVFS get particular jobids to restore job with given jobid

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BvfsApi()
jobid = 56 # int | Job identifier

try:
    # BVFS get particular jobids to restore
    api_response = api_instance.api_v2_bvfs_getjobids_get(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BvfsApi->api_v2_bvfs_getjobids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bvfs_lsdirs_get**
> InlineResponse20056 api_v2_bvfs_lsdirs_get(jobids, path, pathid, offset=offset, limit=limit, output=output)

BVFS list directories

BVFS list directories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BvfsApi()
jobids = 'jobids_example' # str | Comma separated job identifiers
path = 'path_example' # str | Path to list (used instead of pathid parameter)
pathid = 56 # int | Path identifier to list path (used instead of path parameter)
offset = 'offset_example' # str | Offset (optional)
limit = 'limit_example' # str | Limit (optional)
output = 'output_example' # str | Output format (optional)

try:
    # BVFS list directories
    api_response = api_instance.api_v2_bvfs_lsdirs_get(jobids, path, pathid, offset=offset, limit=limit, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BvfsApi->api_v2_bvfs_lsdirs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobids** | **str**| Comma separated job identifiers | 
 **path** | **str**| Path to list (used instead of pathid parameter) | 
 **pathid** | **int**| Path identifier to list path (used instead of path parameter) | 
 **offset** | **str**| Offset | [optional] 
 **limit** | **str**| Limit | [optional] 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bvfs_lsfiles_get**
> InlineResponse20057 api_v2_bvfs_lsfiles_get(jobids, path, pathid, offset=offset, limit=limit, output=output)

BVFS list files

BVFS list files

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BvfsApi()
jobids = 'jobids_example' # str | Comma separated job identifiers
path = 'path_example' # str | Path to list (used instead of pathid parameter)
pathid = 56 # int | Path identifier to list path (used instead of path parameter)
offset = 'offset_example' # str | Offset (optional)
limit = 'limit_example' # str | Limit (optional)
output = 'output_example' # str | Output format (optional)

try:
    # BVFS list files
    api_response = api_instance.api_v2_bvfs_lsfiles_get(jobids, path, pathid, offset=offset, limit=limit, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BvfsApi->api_v2_bvfs_lsfiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobids** | **str**| Comma separated job identifiers | 
 **path** | **str**| Path to list (used instead of pathid parameter) | 
 **pathid** | **int**| Path identifier to list path (used instead of path parameter) | 
 **offset** | **str**| Offset | [optional] 
 **limit** | **str**| Limit | [optional] 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bvfs_restore_post**
> InlineResponse20060 api_v2_bvfs_restore_post(path, jobids, fileid=fileid, dirid=dirid, findex=findex)

Prepare BVFS restore

Prepare BVFS restore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BvfsApi()
path = 56 # int | Path in format b2[0-9]+
jobids = 56 # int | Comma separated job identifiers
fileid = 'fileid_example' # str | Comma seprated file identifiers (optional)
dirid = 'dirid_example' # str | Comma seprated directory identifiers (optional)
findex = 'findex_example' # str | Comma seprated directory file indexes (optional)

try:
    # Prepare BVFS restore
    api_response = api_instance.api_v2_bvfs_restore_post(path, jobids, fileid=fileid, dirid=dirid, findex=findex)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BvfsApi->api_v2_bvfs_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **int**| Path in format b2[0-9]+ | 
 **jobids** | **int**| Comma separated job identifiers | 
 **fileid** | **str**| Comma seprated file identifiers | [optional] 
 **dirid** | **str**| Comma seprated directory identifiers | [optional] 
 **findex** | **str**| Comma seprated directory file indexes | [optional] 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bvfs_update_put**
> InlineResponse20055 api_v2_bvfs_update_put()

Update BVFS cache

Update BVFS cache for specific jobs identifiers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BvfsApi()

try:
    # Update BVFS cache
    api_response = api_instance.api_v2_bvfs_update_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BvfsApi->api_v2_bvfs_update_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bvfs_versions_get**
> InlineResponse20058 api_v2_bvfs_versions_get(clientid, client, jobid, pathid, filenameid, copies=copies, output=output)

BVFS list file versions

BVFS list file versions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BvfsApi()
clientid = 56 # int | Client identifier (can be used instead of client value)
client = 'client_example' # str | Client name (can be used instead clientid)
jobid = 56 # int | Job identifier
pathid = 56 # int | Path identifier
filenameid = 56 # int | Filename identifier
copies = 0 # int | If set to 1, lists copy job file versions together with backup job file versions (optional) (default to 0)
output = 'output_example' # str | Output format (optional)

try:
    # BVFS list file versions
    api_response = api_instance.api_v2_bvfs_versions_get(clientid, client, jobid, pathid, filenameid, copies=copies, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BvfsApi->api_v2_bvfs_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier (can be used instead of client value) | 
 **client** | **str**| Client name (can be used instead clientid) | 
 **jobid** | **int**| Job identifier | 
 **pathid** | **int**| Path identifier | 
 **filenameid** | **int**| Filename identifier | 
 **copies** | **int**| If set to 1, lists copy job file versions together with backup job file versions | [optional] [default to 0]
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

