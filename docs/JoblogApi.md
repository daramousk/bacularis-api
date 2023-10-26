# swagger_client.JoblogApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_joblog_jobid_get**](JoblogApi.md#api_v2_joblog_jobid_get) | **GET** /api/v2/joblog/{jobid} | Get job log for jobid
[**api_v2_joblog_messages_get**](JoblogApi.md#api_v2_joblog_messages_get) | **GET** /api/v2/joblog/messages | Get console messages log.

# **api_v2_joblog_jobid_get**
> InlineResponse20078 api_v2_joblog_jobid_get(jobid, show_time=show_time)

Get job log for jobid

Get job log for jobid

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JoblogApi()
jobid = 56 # int | Job identifier
show_time = true # bool | Show time in job log. (optional)

try:
    # Get job log for jobid
    api_response = api_instance.api_v2_joblog_jobid_get(jobid, show_time=show_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JoblogApi->api_v2_joblog_jobid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 
 **show_time** | **bool**| Show time in job log. | [optional] 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_joblog_messages_get**
> InlineResponse20079 api_v2_joblog_messages_get(limit=limit)

Get console messages log.

Get messages log. Note, because there are returned all current Bacula messages, this endpoint should not be shared non-admin users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JoblogApi()
limit = 56 # int | Set messages log Limit. (optional)

try:
    # Get console messages log.
    api_response = api_instance.api_v2_joblog_messages_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JoblogApi->api_v2_joblog_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Set messages log Limit. | [optional] 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

