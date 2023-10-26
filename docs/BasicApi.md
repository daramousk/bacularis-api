# swagger_client.BasicApi

All URIs are relative to *https://{username}:{password}@localhost:{port}/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_basic_users_get**](BasicApi.md#api_v2_basic_users_get) | **GET** /api/v2/basic/users | Basic user list
[**api_v2_basic_users_username_delete**](BasicApi.md#api_v2_basic_users_username_delete) | **DELETE** /api/v2/basic/users/{username} | Delete Basic user account
[**api_v2_basic_users_username_get**](BasicApi.md#api_v2_basic_users_username_get) | **GET** /api/v2/basic/users/{username} | Specific Basic user config
[**api_v2_basic_users_username_post**](BasicApi.md#api_v2_basic_users_username_post) | **POST** /api/v2/basic/users/{username} | Create Basic user account
[**api_v2_basic_users_username_put**](BasicApi.md#api_v2_basic_users_username_put) | **PUT** /api/v2/basic/users/{username} | Set Basic user settings

# **api_v2_basic_users_get**
> InlineResponse20086 api_v2_basic_users_get()

Basic user list

Get Basic user list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BasicApi()

try:
    # Basic user list
    api_response = api_instance.api_v2_basic_users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicApi->api_v2_basic_users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_basic_users_username_delete**
> InlineResponse20090 api_v2_basic_users_username_delete(username)

Delete Basic user account

Delete Basic user account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BasicApi()
username = 'username_example' # str | Basic user name

try:
    # Delete Basic user account
    api_response = api_instance.api_v2_basic_users_username_delete(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicApi->api_v2_basic_users_username_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Basic user name | 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_basic_users_username_get**
> InlineResponse20087 api_v2_basic_users_username_get(username)

Specific Basic user config

Get specific Basic user config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BasicApi()
username = 'username_example' # str | Basic user name

try:
    # Specific Basic user config
    api_response = api_instance.api_v2_basic_users_username_get(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicApi->api_v2_basic_users_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Basic user name | 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_basic_users_username_post**
> InlineResponse20089 api_v2_basic_users_username_post(username, password, bconsole_cfg_path=bconsole_cfg_path, console=console, director=director)

Create Basic user account

Create specific Basic user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BasicApi()
username = 'username_example' # str | Basic user name
password = 'password_example' # str | Basic user password
bconsole_cfg_path = 'bconsole_cfg_path_example' # str | Dedicated Bconsole configuration file path (optional)
console = 'console_example' # str | Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'director' parameter. (optional)
director = 'director_example' # str | Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'console' parameter. (optional)

try:
    # Create Basic user account
    api_response = api_instance.api_v2_basic_users_username_post(username, password, bconsole_cfg_path=bconsole_cfg_path, console=console, director=director)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicApi->api_v2_basic_users_username_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Basic user name | 
 **password** | **str**| Basic user password | 
 **bconsole_cfg_path** | **str**| Dedicated Bconsole configuration file path | [optional] 
 **console** | **str**| Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with &#x27;director&#x27; parameter. | [optional] 
 **director** | **str**| Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with &#x27;console&#x27; parameter. | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_basic_users_username_put**
> InlineResponse20088 api_v2_basic_users_username_put(username, password=password, bconsole_cfg_path=bconsole_cfg_path, console=console, director=director)

Set Basic user settings

Set specific Basic user settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BasicApi()
username = 'username_example' # str | Basic user name
password = 'password_example' # str | Basic user password (optional)
bconsole_cfg_path = 'bconsole_cfg_path_example' # str | Dedicated Bconsole configuration file path (optional)
console = 'console_example' # str | Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'director' parameter. (optional)
director = 'director_example' # str | Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'console' parameter. (optional)

try:
    # Set Basic user settings
    api_response = api_instance.api_v2_basic_users_username_put(username, password=password, bconsole_cfg_path=bconsole_cfg_path, console=console, director=director)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicApi->api_v2_basic_users_username_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Basic user name | 
 **password** | **str**| Basic user password | [optional] 
 **bconsole_cfg_path** | **str**| Dedicated Bconsole configuration file path | [optional] 
 **console** | **str**| Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with &#x27;director&#x27; parameter. | [optional] 
 **director** | **str**| Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with &#x27;console&#x27; parameter. | [optional] 

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

