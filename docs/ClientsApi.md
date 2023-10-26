# swagger_client.ClientsApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_clients_clientid_bandwidth_put**](ClientsApi.md#api_v2_clients_clientid_bandwidth_put) | **PUT** /api/v2/clients/{clientid}/bandwidth | Set Client bandwidth limit
[**api_v2_clients_clientid_get**](ClientsApi.md#api_v2_clients_clientid_get) | **GET** /api/v2/clients/{clientid} | Find client by ClientId
[**api_v2_clients_clientid_jobs_get**](ClientsApi.md#api_v2_clients_clientid_jobs_get) | **GET** /api/v2/clients/{clientid}/jobs | Jobs for client
[**api_v2_clients_clientid_ls_get**](ClientsApi.md#api_v2_clients_clientid_ls_get) | **GET** /api/v2/clients/{clientid}/ls | List Client files/directories
[**api_v2_clients_clientid_show_get**](ClientsApi.md#api_v2_clients_clientid_show_get) | **GET** /api/v2/clients/{clientid}/show | Show client
[**api_v2_clients_clientid_status_get**](ClientsApi.md#api_v2_clients_clientid_status_get) | **GET** /api/v2/clients/{clientid}/status | Client status
[**api_v2_clients_get**](ClientsApi.md#api_v2_clients_get) | **GET** /api/v2/clients | Client list
[**api_v2_clients_show_get**](ClientsApi.md#api_v2_clients_show_get) | **GET** /api/v2/clients/show | Show clients

# **api_v2_clients_clientid_bandwidth_put**
> InlineResponse2006 api_v2_clients_clientid_bandwidth_put(clientid, limit=limit)

Set Client bandwidth limit

Set Client bandwidth limit in bytes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
clientid = 56 # int | Client identifier
limit = 56 # int | Bandwidth limit in bytes (optional)

try:
    # Set Client bandwidth limit
    api_response = api_instance.api_v2_clients_clientid_bandwidth_put(clientid, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->api_v2_clients_clientid_bandwidth_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier | 
 **limit** | **int**| Bandwidth limit in bytes | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_clients_clientid_get**
> InlineResponse2001 api_v2_clients_clientid_get(clientid)

Find client by ClientId

Get client by specific Client identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
clientid = 56 # int | Client identifier

try:
    # Find client by ClientId
    api_response = api_instance.api_v2_clients_clientid_get(clientid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->api_v2_clients_clientid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_clients_clientid_jobs_get**
> InlineResponse2004 api_v2_clients_clientid_jobs_get(clientid)

Jobs for client

Get jobs done by specific client

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
clientid = 56 # int | Client identifier

try:
    # Jobs for client
    api_response = api_instance.api_v2_clients_clientid_jobs_get(clientid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->api_v2_clients_clientid_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_clients_clientid_ls_get**
> InlineResponse2005 api_v2_clients_clientid_ls_get(clientid, path)

List Client files/directories

Get list Client files/directories for specific path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
clientid = 56 # int | Client identifier
path = 'path_example' # str | Path on Client

try:
    # List Client files/directories
    api_response = api_instance.api_v2_clients_clientid_ls_get(clientid, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->api_v2_clients_clientid_ls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier | 
 **path** | **str**| Path on Client | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_clients_clientid_show_get**
> InlineResponse2002 api_v2_clients_clientid_show_get(clientid, output=output)

Show client

Get 'show clients' bconsole command output for specific client

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
clientid = 56 # int | Client identifier
output = 'output_example' # str | Output format (optional)

try:
    # Show client
    api_response = api_instance.api_v2_clients_clientid_show_get(clientid, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->api_v2_clients_clientid_show_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier | 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_clients_clientid_status_get**
> InlineResponse2003 api_v2_clients_clientid_status_get(clientid, output=output, type=type)

Client status

Get client status for specific client

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
clientid = 56 # int | Client identifier
output = 'output_example' # str | Output format (optional)
type = 'type_example' # str | Output type using together with output=json parameter. (optional)

try:
    # Client status
    api_response = api_instance.api_v2_clients_clientid_status_get(clientid, output=output, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->api_v2_clients_clientid_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| Client identifier | 
 **output** | **str**| Output format | [optional] 
 **type** | **str**| Output type using together with output&#x3D;json parameter. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_clients_get**
> InlineResponse200 api_v2_clients_get(limit=limit)

Client list

Get client list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
limit = 56 # int | Item limit (optional)

try:
    # Client list
    api_response = api_instance.api_v2_clients_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->api_v2_clients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Item limit | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_clients_show_get**
> InlineResponse2007 api_v2_clients_show_get(name=name, output=output)

Show clients

Get 'show clients' bconsole command output

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
name = 'name_example' # str | Client name (optional)
output = 'output_example' # str | Output format (optional)

try:
    # Show clients
    api_response = api_instance.api_v2_clients_show_get(name=name, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->api_v2_clients_show_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Client name | [optional] 
 **output** | **str**| Output format | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

