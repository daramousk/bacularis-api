# swagger_client.FilesetsApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_filesets_filesetid_get**](FilesetsApi.md#api_v2_filesets_filesetid_get) | **GET** /api/v2/filesets/{filesetid} | Find FileSet by FileSetId
[**api_v2_filesets_get**](FilesetsApi.md#api_v2_filesets_get) | **GET** /api/v2/filesets | FileSet list
[**api_v2_filesets_resnames_get**](FilesetsApi.md#api_v2_filesets_resnames_get) | **GET** /api/v2/filesets/resnames | FileSet resource names

# **api_v2_filesets_filesetid_get**
> InlineResponse20051 api_v2_filesets_filesetid_get(filesetid)

Find FileSet by FileSetId

Get FileSet by specific FileSet identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesetsApi()
filesetid = 56 # int | FileSet identifier

try:
    # Find FileSet by FileSetId
    api_response = api_instance.api_v2_filesets_filesetid_get(filesetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesetsApi->api_v2_filesets_filesetid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filesetid** | **int**| FileSet identifier | 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_filesets_get**
> InlineResponse20050 api_v2_filesets_get(limit=limit)

FileSet list

Get fileset list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesetsApi()
limit = 56 # int | Item limit (optional)

try:
    # FileSet list
    api_response = api_instance.api_v2_filesets_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesetsApi->api_v2_filesets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Item limit | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_filesets_resnames_get**
> InlineResponse20052 api_v2_filesets_resnames_get()

FileSet resource names

Get FileSet resource names (after applying console ACL)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesetsApi()

try:
    # FileSet resource names
    api_response = api_instance.api_v2_filesets_resnames_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesetsApi->api_v2_filesets_resnames_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

