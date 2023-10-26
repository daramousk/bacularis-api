# swagger_client.Oauth2Api

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_oauth2_clients_client_id_delete**](Oauth2Api.md#api_v2_oauth2_clients_client_id_delete) | **DELETE** /api/v2/oauth2/clients/{client_id} | Delete OAuth2 client account
[**api_v2_oauth2_clients_client_id_get**](Oauth2Api.md#api_v2_oauth2_clients_client_id_get) | **GET** /api/v2/oauth2/clients/{client_id} | Specific OAuth2 client account config
[**api_v2_oauth2_clients_client_id_post**](Oauth2Api.md#api_v2_oauth2_clients_client_id_post) | **POST** /api/v2/oauth2/clients/{client_id} | Create OAuth2 client settings
[**api_v2_oauth2_clients_client_id_put**](Oauth2Api.md#api_v2_oauth2_clients_client_id_put) | **PUT** /api/v2/oauth2/clients/{client_id} | Set OAuth2 client settings
[**api_v2_oauth2_clients_get**](Oauth2Api.md#api_v2_oauth2_clients_get) | **GET** /api/v2/oauth2/clients | OAuth2 client account list

# **api_v2_oauth2_clients_client_id_delete**
> InlineResponse20085 api_v2_oauth2_clients_client_id_delete(client_id)

Delete OAuth2 client account

Delete OAuth2 client account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Oauth2Api()
client_id = 'client_id_example' # str | Client identifier (OAuth2 Client ID)

try:
    # Delete OAuth2 client account
    api_response = api_instance.api_v2_oauth2_clients_client_id_delete(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Oauth2Api->api_v2_oauth2_clients_client_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client identifier (OAuth2 Client ID) | 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_oauth2_clients_client_id_get**
> InlineResponse20082 api_v2_oauth2_clients_client_id_get(client_id)

Specific OAuth2 client account config

Get specific OAuth2 client account config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Oauth2Api()
client_id = 'client_id_example' # str | Client identifier (OAuth2 Client ID)

try:
    # Specific OAuth2 client account config
    api_response = api_instance.api_v2_oauth2_clients_client_id_get(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Oauth2Api->api_v2_oauth2_clients_client_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client identifier (OAuth2 Client ID) | 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_oauth2_clients_client_id_post**
> InlineResponse20084 api_v2_oauth2_clients_client_id_post(client_id, client_secret, redirect_uri, scope, bconsole_cfg_path, console=console, director=director, name=name)

Create OAuth2 client settings

Create specific OAuth2 client settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Oauth2Api()
client_id = 'client_id_example' # str | Client identifier (OAuth2 Client ID)
client_secret = 'client_secret_example' # str | OAuth2 client secret
redirect_uri = 'redirect_uri_example' # str | OAuth2 redirect URI (OAuth2 callback)
scope = 'scope_example' # str | Comma separated OAuth2 scopes
bconsole_cfg_path = 'bconsole_cfg_path_example' # str | Bconsole config file path
console = 'console_example' # str | Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'director' parameter. (optional)
director = 'director_example' # str | Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'console' parameter. (optional)
name = 'name_example' # str | OAuth2 client account name (optional)

try:
    # Create OAuth2 client settings
    api_response = api_instance.api_v2_oauth2_clients_client_id_post(client_id, client_secret, redirect_uri, scope, bconsole_cfg_path, console=console, director=director, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Oauth2Api->api_v2_oauth2_clients_client_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client identifier (OAuth2 Client ID) | 
 **client_secret** | **str**| OAuth2 client secret | 
 **redirect_uri** | **str**| OAuth2 redirect URI (OAuth2 callback) | 
 **scope** | **str**| Comma separated OAuth2 scopes | 
 **bconsole_cfg_path** | **str**| Bconsole config file path | 
 **console** | **str**| Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with &#x27;director&#x27; parameter. | [optional] 
 **director** | **str**| Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with &#x27;console&#x27; parameter. | [optional] 
 **name** | **str**| OAuth2 client account name | [optional] 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_oauth2_clients_client_id_put**
> InlineResponse20083 api_v2_oauth2_clients_client_id_put(client_id, client_secret, redirect_uri, scope, bconsole_cfg_path, console=console, director=director, name=name)

Set OAuth2 client settings

Set specific OAuth2 client settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Oauth2Api()
client_id = 'client_id_example' # str | Client identifier (OAuth2 Client ID)
client_secret = 'client_secret_example' # str | OAuth2 client secret
redirect_uri = 'redirect_uri_example' # str | OAuth2 redirect URI (OAuth2 callback)
scope = 'scope_example' # str | Comma separated OAuth2 scopes
bconsole_cfg_path = 'bconsole_cfg_path_example' # str | Bconsole config file path
console = 'console_example' # str | Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'director' parameter. (optional)
director = 'director_example' # str | Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'console' parameter. (optional)
name = 'name_example' # str | OAuth2 client account name (optional)

try:
    # Set OAuth2 client settings
    api_response = api_instance.api_v2_oauth2_clients_client_id_put(client_id, client_secret, redirect_uri, scope, bconsole_cfg_path, console=console, director=director, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Oauth2Api->api_v2_oauth2_clients_client_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client identifier (OAuth2 Client ID) | 
 **client_secret** | **str**| OAuth2 client secret | 
 **redirect_uri** | **str**| OAuth2 redirect URI (OAuth2 callback) | 
 **scope** | **str**| Comma separated OAuth2 scopes | 
 **bconsole_cfg_path** | **str**| Bconsole config file path | 
 **console** | **str**| Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with &#x27;director&#x27; parameter. | [optional] 
 **director** | **str**| Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with &#x27;console&#x27; parameter. | [optional] 
 **name** | **str**| OAuth2 client account name | [optional] 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_oauth2_clients_get**
> InlineResponse20081 api_v2_oauth2_clients_get()

OAuth2 client account list

Get OAuth2 client account list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Oauth2Api()

try:
    # OAuth2 client account list
    api_response = api_instance.api_v2_oauth2_clients_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Oauth2Api->api_v2_oauth2_clients_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

