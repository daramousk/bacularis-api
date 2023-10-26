# swagger_client.JobsApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_jobs_estimate_get**](JobsApi.md#api_v2_jobs_estimate_get) | **GET** /api/v2/jobs/estimate | Get estimate output
[**api_v2_jobs_estimate_post**](JobsApi.md#api_v2_jobs_estimate_post) | **POST** /api/v2/jobs/estimate | Estimate job bytes and files
[**api_v2_jobs_files_get**](JobsApi.md#api_v2_jobs_files_get) | **GET** /api/v2/jobs/files | Search jobs by file criteria
[**api_v2_jobs_get**](JobsApi.md#api_v2_jobs_get) | **GET** /api/v2/jobs | Job list
[**api_v2_jobs_jobid_bandwidth_put**](JobsApi.md#api_v2_jobs_jobid_bandwidth_put) | **PUT** /api/v2/jobs/{jobid}/bandwidth | Set Job bandwidth limit
[**api_v2_jobs_jobid_cancel_put**](JobsApi.md#api_v2_jobs_jobid_cancel_put) | **PUT** /api/v2/jobs/{jobid}/cancel | Cancel job
[**api_v2_jobs_jobid_delete**](JobsApi.md#api_v2_jobs_jobid_delete) | **DELETE** /api/v2/jobs/{jobid} | Delete job
[**api_v2_jobs_jobid_files_get**](JobsApi.md#api_v2_jobs_jobid_files_get) | **GET** /api/v2/jobs/{jobid}/files | Show job files and directories
[**api_v2_jobs_jobid_get**](JobsApi.md#api_v2_jobs_jobid_get) | **GET** /api/v2/jobs/{jobid} | Find job by JobId
[**api_v2_jobs_jobid_show_get**](JobsApi.md#api_v2_jobs_jobid_show_get) | **GET** /api/v2/jobs/{jobid}/show | Show job
[**api_v2_jobs_recent_jobname_get**](JobsApi.md#api_v2_jobs_recent_jobname_get) | **GET** /api/v2/jobs/recent/{jobname} | Get most recent jobids for job to restore
[**api_v2_jobs_resnames_get**](JobsApi.md#api_v2_jobs_resnames_get) | **GET** /api/v2/jobs/resnames | Job resource names
[**api_v2_jobs_restore_post**](JobsApi.md#api_v2_jobs_restore_post) | **POST** /api/v2/jobs/restore | Restore job
[**api_v2_jobs_run_post**](JobsApi.md#api_v2_jobs_run_post) | **POST** /api/v2/jobs/run | Run job
[**api_v2_jobs_show_get**](JobsApi.md#api_v2_jobs_show_get) | **GET** /api/v2/jobs/show | Show jobs
[**api_v2_jobs_totals_get**](JobsApi.md#api_v2_jobs_totals_get) | **GET** /api/v2/jobs/totals | Show job total bytes and files

# **api_v2_jobs_estimate_get**
> InlineResponse20018 api_v2_jobs_estimate_get(out_id)

Get estimate output

Get estimate output by output identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
out_id = 'out_id_example' # str | Output identifier acquired during estimate start.

try:
    # Get estimate output
    api_response = api_instance.api_v2_jobs_estimate_get(out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_estimate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_id** | **str**| Output identifier acquired during estimate start. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_estimate_post**
> InlineResponse20019 api_v2_jobs_estimate_post(id, name, clientid, client, fileset, accurate=accurate)

Estimate job bytes and files

Estimate job bytes and files before real job run. There can be used (id OR name) and (clientid OR client)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
id = 56 # int | Job identifier
name = 'name_example' # str | Job name (can be used instead id)
clientid = 56 # int | Client identifier
client = 'client_example' # str | Client name (can be used instead clientid)
fileset = 'fileset_example' # str | FileSet name
accurate = 56 # int | Accurate mode, 1 if enabled, otherwise 0 (optional)

try:
    # Estimate job bytes and files
    api_response = api_instance.api_v2_jobs_estimate_post(id, name, clientid, client, fileset, accurate=accurate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_estimate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job identifier | 
 **name** | **str**| Job name (can be used instead id) | 
 **clientid** | **int**| Client identifier | 
 **client** | **str**| Client name (can be used instead clientid) | 
 **fileset** | **str**| FileSet name | 
 **accurate** | **int**| Accurate mode, 1 if enabled, otherwise 0 | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_files_get**
> InlineResponse20015 api_v2_jobs_files_get(clientid, client, filename, strict=strict, path=path)

Search jobs by file criteria

Get job list by file criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
clientid = 56 # int | Client identifier (used instead of 'client' parameter)
client = 'client_example' # str | Client name (used instead of 'clientid' parameter)
filename = 'filename_example' # str | Filename to find jobs containing the file. Normally it searches for files which have given 'filename' in name, like \\*filename\\*. If strict mode is used then is done equal matching filename == name.
strict = true # bool | Enables strict file matching filename == name (optional)
path = 'path_example' # str | Path to narrow down the results to files from one specific path. The path must be finished with a slash. (optional)

try:
    # Search jobs by file criteria
    api_response = api_instance.api_v2_jobs_files_get(clientid, client, filename, strict=strict, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier (used instead of &#x27;client&#x27; parameter) | 
 **client** | **str**| Client name (used instead of &#x27;clientid&#x27; parameter) | 
 **filename** | **str**| Filename to find jobs containing the file. Normally it searches for files which have given &#x27;filename&#x27; in name, like \\*filename\\*. If strict mode is used then is done equal matching filename &#x3D;&#x3D; name. | 
 **strict** | **bool**| Enables strict file matching filename &#x3D;&#x3D; name | [optional] 
 **path** | **str**| Path to narrow down the results to files from one specific path. The path must be finished with a slash. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_get**
> InlineResponse2008 api_v2_jobs_get(limit=limit, name=name, jobstatus=jobstatus, clientid=clientid, client=client, type=type, level=level, age=age)

Job list

Get job list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
limit = 56 # int | Item limit (optional)
name = 'name_example' # str | Job name (optional)
jobstatus = 'jobstatus_example' # str | Job status letter (optional)
clientid = 56 # int | Client identifier (optional)
client = 'client_example' # str | Client name (optional)
type = 'type_example' # str | Job type letter (optional)
level = 'level_example' # str | Job level letter (optional)
age = 56 # int | Time in seconds to determine how old jobs will be returned. Age uses startime in the following way: starttime >= now - age. (optional)

try:
    # Job list
    api_response = api_instance.api_v2_jobs_get(limit=limit, name=name, jobstatus=jobstatus, clientid=clientid, client=client, type=type, level=level, age=age)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Item limit | [optional] 
 **name** | **str**| Job name | [optional] 
 **jobstatus** | **str**| Job status letter | [optional] 
 **clientid** | **int**| Client identifier | [optional] 
 **client** | **str**| Client name | [optional] 
 **type** | **str**| Job type letter | [optional] 
 **level** | **str**| Job level letter | [optional] 
 **age** | **int**| Time in seconds to determine how old jobs will be returned. Age uses startime in the following way: starttime &gt;&#x3D; now - age. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_jobid_bandwidth_put**
> InlineResponse20013 api_v2_jobs_jobid_bandwidth_put(jobid, limit=limit)

Set Job bandwidth limit

Set Job bandwidth limit in bytes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
jobid = 56 # int | Job identifier
limit = 56 # int | Bandwidth limit in bytes (optional)

try:
    # Set Job bandwidth limit
    api_response = api_instance.api_v2_jobs_jobid_bandwidth_put(jobid, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_jobid_bandwidth_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 
 **limit** | **int**| Bandwidth limit in bytes | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_jobid_cancel_put**
> InlineResponse20011 api_v2_jobs_jobid_cancel_put(jobid)

Cancel job

Cancel running job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
jobid = 56 # int | Job identifier

try:
    # Cancel job
    api_response = api_instance.api_v2_jobs_jobid_cancel_put(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_jobid_cancel_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_jobid_delete**
> InlineResponse20010 api_v2_jobs_jobid_delete(jobid)

Delete job

Delete job by specific Job identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
jobid = 56 # int | Job identifier

try:
    # Delete job
    api_response = api_instance.api_v2_jobs_jobid_delete(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_jobid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_jobid_files_get**
> InlineResponse20014 api_v2_jobs_jobid_files_get(jobid, type=type, offset=offset, limit=limit, search=search, details=details)

Show job files and directories

Get job file and directory list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
jobid = 56 # int | Job identifier
type = 'type_example' # str | List item type (optional)
offset = 56 # int | Result items offset (optional)
limit = 56 # int | Result items limit (optional)
search = 'search_example' # str | Search keyword in item list (optional)
details = true # bool | Show more details (including LStat value) (optional)

try:
    # Show job files and directories
    api_response = api_instance.api_v2_jobs_jobid_files_get(jobid, type=type, offset=offset, limit=limit, search=search, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_jobid_files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 
 **type** | **str**| List item type | [optional] 
 **offset** | **int**| Result items offset | [optional] 
 **limit** | **int**| Result items limit | [optional] 
 **search** | **str**| Search keyword in item list | [optional] 
 **details** | **bool**| Show more details (including LStat value) | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_jobid_get**
> InlineResponse2009 api_v2_jobs_jobid_get(jobid)

Find job by JobId

Get job by specific Job identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
jobid = 56 # int | Job identifier

try:
    # Find job by JobId
    api_response = api_instance.api_v2_jobs_jobid_get(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_jobid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_jobid_show_get**
> InlineResponse20012 api_v2_jobs_jobid_show_get(jobid, output=output)

Show job

Get 'show jobs' bconsole command output for specific job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
jobid = 56 # int | Job identifier
output = 'output_example' # str | Output format (optional)

try:
    # Show job
    api_response = api_instance.api_v2_jobs_jobid_show_get(jobid, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_jobid_show_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **int**| Job identifier | 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_recent_jobname_get**
> InlineResponse20017 api_v2_jobs_recent_jobname_get(jobname, clientid, client, filesetid, fileset)

Get most recent jobids for job to restore

Useful for restore. Determines all single jobids required to restore job given in jobname. Besides jobname there are required only two parameters (client OR clientid) AND (fileset OR filesetid)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
jobname = 'jobname_example' # str | Job name
clientid = 56 # int | Client identifier
client = 'client_example' # str | Client name (can be used instead clientid)
filesetid = 56 # int | FileSet identifier
fileset = 'fileset_example' # str | FileSet name (can be used instead filesetid)

try:
    # Get most recent jobids for job to restore
    api_response = api_instance.api_v2_jobs_recent_jobname_get(jobname, clientid, client, filesetid, fileset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_recent_jobname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobname** | **str**| Job name | 
 **clientid** | **int**| Client identifier | 
 **client** | **str**| Client name (can be used instead clientid) | 
 **filesetid** | **int**| FileSet identifier | 
 **fileset** | **str**| FileSet name (can be used instead filesetid) | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_resnames_get**
> InlineResponse20016 api_v2_jobs_resnames_get(limit=limit, type=type)

Job resource names

Get job resource names (after applying console ACL)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
limit = 56 # int | Item limit (optional)
type = 'type_example' # str | Job type (B - backup, R - restore, V - verify ...etc.) (optional)

try:
    # Job resource names
    api_response = api_instance.api_v2_jobs_resnames_get(limit=limit, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_resnames_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Item limit | [optional] 
 **type** | **str**| Job type (B - backup, R - restore, V - verify ...etc.) | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_restore_post**
> InlineResponse20023 api_v2_jobs_restore_post(clientid, client, where, id=id, rpath=rpath, full=full, filesetid=filesetid, fileset=fileset, restoreclientid=restoreclientid, restoreclient=restoreclient, restorejob=restorejob, strip_prefix=strip_prefix, add_prefix=add_prefix, add_suffix=add_suffix, regex_where=regex_where)

Restore job

Restore backup job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
clientid = 56 # int | Client identifier
client = 'client_example' # str | Client name (can be used instead clientid)
where = 'where_example' # str | Where to restore files
id = 56 # int | Job identifier (for full restore) (optional)
rpath = 'rpath_example' # str | Rpath (restore path) (optional)
full = true # bool | Full restore all files (optional)
filesetid = 'filesetid_example' # str | FileSet identifier (for full restore) (optional)
fileset = 'fileset_example' # str | FileSet (can be used instead of filesetid) (for full restore) (optional)
restoreclientid = 56 # int | Restore client identifier (can be used instead of restoreclient) (optional)
restoreclient = 'restoreclient_example' # str | Restore client name (can be used instead of restoreclientid) (optional)
restorejob = 'restorejob_example' # str | Restore job name (optional)
strip_prefix = 'strip_prefix_example' # str | Strip prefix in restored paths (optional)
add_prefix = 'add_prefix_example' # str | Add prefix to restored paths (optional)
add_suffix = 'add_suffix_example' # str | Add suffix to restored paths (optional)
regex_where = 'regex_where_example' # str | Use regex to file relocation (optional)

try:
    # Restore job
    api_response = api_instance.api_v2_jobs_restore_post(clientid, client, where, id=id, rpath=rpath, full=full, filesetid=filesetid, fileset=fileset, restoreclientid=restoreclientid, restoreclient=restoreclient, restorejob=restorejob, strip_prefix=strip_prefix, add_prefix=add_prefix, add_suffix=add_suffix, regex_where=regex_where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier | 
 **client** | **str**| Client name (can be used instead clientid) | 
 **where** | **str**| Where to restore files | 
 **id** | **int**| Job identifier (for full restore) | [optional] 
 **rpath** | **str**| Rpath (restore path) | [optional] 
 **full** | **bool**| Full restore all files | [optional] 
 **filesetid** | **str**| FileSet identifier (for full restore) | [optional] 
 **fileset** | **str**| FileSet (can be used instead of filesetid) (for full restore) | [optional] 
 **restoreclientid** | **int**| Restore client identifier (can be used instead of restoreclient) | [optional] 
 **restoreclient** | **str**| Restore client name (can be used instead of restoreclientid) | [optional] 
 **restorejob** | **str**| Restore job name | [optional] 
 **strip_prefix** | **str**| Strip prefix in restored paths | [optional] 
 **add_prefix** | **str**| Add prefix to restored paths | [optional] 
 **add_suffix** | **str**| Add suffix to restored paths | [optional] 
 **regex_where** | **str**| Use regex to file relocation | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_run_post**
> InlineResponse20020 api_v2_jobs_run_post(id, name, level, clientid, client, storageid, storage, poolid, pool, filesetid, fileset, priority=priority, accurate=accurate, jobid=jobid, verifyjob=verifyjob)

Run job

Run job with specific parameters. There can be used (id OR name) and (clientid OR client)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
id = 56 # int | Job identifier
name = 'name_example' # str | Job name (can be used instead id)
level = 'level_example' # str | Job level
clientid = 56 # int | Client identifier
client = 'client_example' # str | Client name (can be used instead clientid)
storageid = 56 # int | Storage identifier
storage = 'storage_example' # str | Storage name (can be used instead storageid)
poolid = 56 # int | Pool identifier
pool = 'pool_example' # str | Pool name (can be used instead poolid)
filesetid = 56 # int | FileSet identifier
fileset = 'fileset_example' # str | FileSet name (can be used instead filesetid)
priority = 56 # int | Job priority (optional)
accurate = 56 # int | Accurate mode, 1 if enabled, otherwise 0 (optional)
jobid = 56 # int | Job identifier for verify job (optional)
verifyjob = 'verifyjob_example' # str | Verify job name (optional)

try:
    # Run job
    api_response = api_instance.api_v2_jobs_run_post(id, name, level, clientid, client, storageid, storage, poolid, pool, filesetid, fileset, priority=priority, accurate=accurate, jobid=jobid, verifyjob=verifyjob)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_run_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job identifier | 
 **name** | **str**| Job name (can be used instead id) | 
 **level** | **str**| Job level | 
 **clientid** | **int**| Client identifier | 
 **client** | **str**| Client name (can be used instead clientid) | 
 **storageid** | **int**| Storage identifier | 
 **storage** | **str**| Storage name (can be used instead storageid) | 
 **poolid** | **int**| Pool identifier | 
 **pool** | **str**| Pool name (can be used instead poolid) | 
 **filesetid** | **int**| FileSet identifier | 
 **fileset** | **str**| FileSet name (can be used instead filesetid) | 
 **priority** | **int**| Job priority | [optional] 
 **accurate** | **int**| Accurate mode, 1 if enabled, otherwise 0 | [optional] 
 **jobid** | **int**| Job identifier for verify job | [optional] 
 **verifyjob** | **str**| Verify job name | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_show_get**
> InlineResponse20021 api_v2_jobs_show_get(name=name, output=output)

Show jobs

Get 'show jobs' bconsole command output

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
name = 'name_example' # str | Job name (optional)
output = 'output_example' # str | Output format (optional)

try:
    # Show jobs
    api_response = api_instance.api_v2_jobs_show_get(name=name, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_show_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Job name | [optional] 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_totals_get**
> InlineResponse20022 api_v2_jobs_totals_get()

Show job total bytes and files

Get total number backed up bytes and files from all jobs. It works also with Console ACL.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()

try:
    # Show job total bytes and files
    api_response = api_instance.api_v2_jobs_totals_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->api_v2_jobs_totals_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

