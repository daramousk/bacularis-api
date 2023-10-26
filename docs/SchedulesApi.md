# swagger_client.SchedulesApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_schedules_resnames_get**](SchedulesApi.md#api_v2_schedules_resnames_get) | **GET** /api/v2/schedules/resnames | Schedule resource names
[**api_v2_schedules_status_get**](SchedulesApi.md#api_v2_schedules_status_get) | **GET** /api/v2/schedules/status | Schedule status

# **api_v2_schedules_resnames_get**
> InlineResponse20053 api_v2_schedules_resnames_get()

Schedule resource names

Get Schedule resource names (after applying console ACL)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchedulesApi()

try:
    # Schedule resource names
    api_response = api_instance.api_v2_schedules_resnames_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->api_v2_schedules_resnames_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schedules_status_get**
> InlineResponse20054 api_v2_schedules_status_get(job=job, client=client, schedule=schedule, days=days, limit=limit, time=time)

Schedule status

Get Schedule status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchedulesApi()
job = 'job_example' # str | Job name (optional)
client = 'client_example' # str | Client name (optional)
schedule = 'schedule_example' # str | Schedule name (optional)
days = 30 # int | Days number to show schedule (optional) (default to 30)
limit = 30 # int | Schedule results limit. Setting zero disables the limit. Default value is taken into account only if the days parameter is not set. (optional) (default to 30)
time = 'time_example' # str | Schedule start time to show (YYYY-MM-DD HH:MM::SS) (optional)

try:
    # Schedule status
    api_response = api_instance.api_v2_schedules_status_get(job=job, client=client, schedule=schedule, days=days, limit=limit, time=time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->api_v2_schedules_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Job name | [optional] 
 **client** | **str**| Client name | [optional] 
 **schedule** | **str**| Schedule name | [optional] 
 **days** | **int**| Days number to show schedule | [optional] [default to 30]
 **limit** | **int**| Schedule results limit. Setting zero disables the limit. Default value is taken into account only if the days parameter is not set. | [optional] [default to 30]
 **time** | **str**| Schedule start time to show (YYYY-MM-DD HH:MM::SS) | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

