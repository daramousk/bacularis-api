# swagger_client.ConfigApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_config_component_type_get**](ConfigApi.md#api_v2_config_component_type_get) | **GET** /api/v2/config/{component_type} | Get component config
[**api_v2_config_component_type_put**](ConfigApi.md#api_v2_config_component_type_put) | **PUT** /api/v2/config/{component_type} | Set component config
[**api_v2_config_component_type_resource_type_get**](ConfigApi.md#api_v2_config_component_type_resource_type_get) | **GET** /api/v2/config/{component_type}/{resource_type} | Get component resources config
[**api_v2_config_component_type_resource_type_put**](ConfigApi.md#api_v2_config_component_type_resource_type_put) | **PUT** /api/v2/config/{component_type}/{resource_type} | Set component resources config
[**api_v2_config_component_type_resource_type_resource_name_get**](ConfigApi.md#api_v2_config_component_type_resource_type_resource_name_get) | **GET** /api/v2/config/{component_type}/{resource_type}/{resource_name} | Get component resource config
[**api_v2_config_component_type_resource_type_resource_name_put**](ConfigApi.md#api_v2_config_component_type_resource_type_resource_name_put) | **PUT** /api/v2/config/{component_type}/{resource_type}/{resource_name} | Set component resource config
[**api_v2_config_get**](ConfigApi.md#api_v2_config_get) | **GET** /api/v2/config | Get components information

# **api_v2_config_component_type_get**
> InlineResponse20064 api_v2_config_component_type_get(component_type, apply_jobdefs=apply_jobdefs)

Get component config

Get specific component config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
component_type = 'component_type_example' # str | Component type: dir, sd, fd or bcons
apply_jobdefs = true # bool | Apply JobDefs in results (this parameter is taken into account only for Job resources) (optional)

try:
    # Get component config
    api_response = api_instance.api_v2_config_component_type_get(component_type, apply_jobdefs=apply_jobdefs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v2_config_component_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type: dir, sd, fd or bcons | 
 **apply_jobdefs** | **bool**| Apply JobDefs in results (this parameter is taken into account only for Job resources) | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_config_component_type_put**
> InlineResponse20065 api_v2_config_component_type_put(component_type, config)

Set component config

Set specific component config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
component_type = 'component_type_example' # str | Component type: dir, sd, fd or bcons
config = 'config_example' # str | Config in JSON form to set

try:
    # Set component config
    api_response = api_instance.api_v2_config_component_type_put(component_type, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v2_config_component_type_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type: dir, sd, fd or bcons | 
 **config** | **str**| Config in JSON form to set | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_config_component_type_resource_type_get**
> InlineResponse20066 api_v2_config_component_type_resource_type_get(component_type, resource_type, apply_jobdefs=apply_jobdefs)

Get component resources config

Get component resources config by type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
component_type = 'component_type_example' # str | Component type: dir, sd, fd or bcons
resource_type = 'resource_type_example' # str | Resource type: Client, Pool, Job...etc.
apply_jobdefs = true # bool | Apply JobDefs in results (this parameter is taken into account only for Job resources) (optional)

try:
    # Get component resources config
    api_response = api_instance.api_v2_config_component_type_resource_type_get(component_type, resource_type, apply_jobdefs=apply_jobdefs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v2_config_component_type_resource_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type: dir, sd, fd or bcons | 
 **resource_type** | **str**| Resource type: Client, Pool, Job...etc. | 
 **apply_jobdefs** | **bool**| Apply JobDefs in results (this parameter is taken into account only for Job resources) | [optional] 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_config_component_type_resource_type_put**
> InlineResponse20067 api_v2_config_component_type_resource_type_put(component_type, resource_type, config)

Set component resources config

Set specific component resources config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
component_type = 'component_type_example' # str | Component type: dir, sd, fd or bcons
resource_type = 'resource_type_example' # str | Resource type: Client, Pool, Job...etc.
config = 'config_example' # str | Config in JSON form to set

try:
    # Set component resources config
    api_response = api_instance.api_v2_config_component_type_resource_type_put(component_type, resource_type, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v2_config_component_type_resource_type_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type: dir, sd, fd or bcons | 
 **resource_type** | **str**| Resource type: Client, Pool, Job...etc. | 
 **config** | **str**| Config in JSON form to set | 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_config_component_type_resource_type_resource_name_get**
> InlineResponse20068 api_v2_config_component_type_resource_type_resource_name_get(component_type, resource_type, resource_name, apply_jobdefs=apply_jobdefs)

Get component resource config

Get component resource config by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
component_type = 'component_type_example' # str | Component type: dir, sd, fd or bcons
resource_type = 'resource_type_example' # str | Resource type: Client, Pool, Job...etc.
resource_name = 'resource_name_example' # str | Resource name
apply_jobdefs = true # bool | Apply JobDefs in results (this parameter is taken into account only for Job resources) (optional)

try:
    # Get component resource config
    api_response = api_instance.api_v2_config_component_type_resource_type_resource_name_get(component_type, resource_type, resource_name, apply_jobdefs=apply_jobdefs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v2_config_component_type_resource_type_resource_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type: dir, sd, fd or bcons | 
 **resource_type** | **str**| Resource type: Client, Pool, Job...etc. | 
 **resource_name** | **str**| Resource name | 
 **apply_jobdefs** | **bool**| Apply JobDefs in results (this parameter is taken into account only for Job resources) | [optional] 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_config_component_type_resource_type_resource_name_put**
> InlineResponse20069 api_v2_config_component_type_resource_type_resource_name_put(component_type, resource_type, resource_name, config)

Set component resource config

Set specific component resource config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
component_type = 'component_type_example' # str | Component type: dir, sd, fd or bcons
resource_type = 'resource_type_example' # str | Resource type: Client, Pool, Job...etc.
resource_name = 'resource_name_example' # str | Resource name
config = 'config_example' # str | Config in JSON form to set

try:
    # Set component resource config
    api_response = api_instance.api_v2_config_component_type_resource_type_resource_name_put(component_type, resource_type, resource_name, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v2_config_component_type_resource_type_resource_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type: dir, sd, fd or bcons | 
 **resource_type** | **str**| Resource type: Client, Pool, Job...etc. | 
 **resource_name** | **str**| Resource name | 
 **config** | **str**| Config in JSON form to set | 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_config_get**
> InlineResponse20063 api_v2_config_get()

Get components information

Get components information such as component types and component names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()

try:
    # Get components information
    api_response = api_instance.api_v2_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v2_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

