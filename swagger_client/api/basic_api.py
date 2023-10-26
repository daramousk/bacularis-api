# coding: utf-8

"""
    Bacularis API

    This is the Bacularis API documentation.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: marcin.haba@bacula.pl
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BasicApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_basic_users_get(self, **kwargs):  # noqa: E501
        """Basic user list  # noqa: E501

        Get Basic user list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20086
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_basic_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_basic_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v2_basic_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """Basic user list  # noqa: E501

        Get Basic user list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20086
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_basic_users_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/basic/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20086',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_basic_users_username_delete(self, username, **kwargs):  # noqa: E501
        """Delete Basic user account  # noqa: E501

        Delete Basic user account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_username_delete(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Basic user name (required)
        :return: InlineResponse20090
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_basic_users_username_delete_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_basic_users_username_delete_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def api_v2_basic_users_username_delete_with_http_info(self, username, **kwargs):  # noqa: E501
        """Delete Basic user account  # noqa: E501

        Delete Basic user account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_username_delete_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Basic user name (required)
        :return: InlineResponse20090
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_basic_users_username_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `api_v2_basic_users_username_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/basic/users/{username}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20090',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_basic_users_username_get(self, username, **kwargs):  # noqa: E501
        """Specific Basic user config  # noqa: E501

        Get specific Basic user config  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_username_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Basic user name (required)
        :return: InlineResponse20087
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_basic_users_username_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_basic_users_username_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def api_v2_basic_users_username_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """Specific Basic user config  # noqa: E501

        Get specific Basic user config  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_username_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Basic user name (required)
        :return: InlineResponse20087
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_basic_users_username_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `api_v2_basic_users_username_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/basic/users/{username}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20087',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_basic_users_username_post(self, username, password, **kwargs):  # noqa: E501
        """Create Basic user account  # noqa: E501

        Create specific Basic user account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_username_post(username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Basic user name (required)
        :param str password: Basic user password (required)
        :param str bconsole_cfg_path: Dedicated Bconsole configuration file path
        :param str console: Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'director' parameter.
        :param str director: Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'console' parameter.
        :return: InlineResponse20089
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_basic_users_username_post_with_http_info(username, password, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_basic_users_username_post_with_http_info(username, password, **kwargs)  # noqa: E501
            return data

    def api_v2_basic_users_username_post_with_http_info(self, username, password, **kwargs):  # noqa: E501
        """Create Basic user account  # noqa: E501

        Create specific Basic user account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_username_post_with_http_info(username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Basic user name (required)
        :param str password: Basic user password (required)
        :param str bconsole_cfg_path: Dedicated Bconsole configuration file path
        :param str console: Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'director' parameter.
        :param str director: Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'console' parameter.
        :return: InlineResponse20089
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'password', 'bconsole_cfg_path', 'console', 'director']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_basic_users_username_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `api_v2_basic_users_username_post`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in params or
                params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `api_v2_basic_users_username_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []

        header_params = {}
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501
        if 'bconsole_cfg_path' in params:
            header_params['bconsole_cfg_path'] = params['bconsole_cfg_path']  # noqa: E501
        if 'console' in params:
            header_params['console'] = params['console']  # noqa: E501
        if 'director' in params:
            header_params['director'] = params['director']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/basic/users/{username}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20089',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_basic_users_username_put(self, username, **kwargs):  # noqa: E501
        """Set Basic user settings  # noqa: E501

        Set specific Basic user settings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_username_put(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Basic user name (required)
        :param str password: Basic user password
        :param str bconsole_cfg_path: Dedicated Bconsole configuration file path
        :param str console: Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'director' parameter.
        :param str director: Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'console' parameter.
        :return: InlineResponse20088
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_basic_users_username_put_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_basic_users_username_put_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def api_v2_basic_users_username_put_with_http_info(self, username, **kwargs):  # noqa: E501
        """Set Basic user settings  # noqa: E501

        Set specific Basic user settings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_basic_users_username_put_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Basic user name (required)
        :param str password: Basic user password
        :param str bconsole_cfg_path: Dedicated Bconsole configuration file path
        :param str console: Director Console name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'director' parameter.
        :param str director: Director Name to create dedicated bconsole.conf that is assigned to account. Parameter must be used together with 'console' parameter.
        :return: InlineResponse20088
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'password', 'bconsole_cfg_path', 'console', 'director']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_basic_users_username_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `api_v2_basic_users_username_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []

        header_params = {}
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501
        if 'bconsole_cfg_path' in params:
            header_params['bconsole_cfg_path'] = params['bconsole_cfg_path']  # noqa: E501
        if 'console' in params:
            header_params['console'] = params['console']  # noqa: E501
        if 'director' in params:
            header_params['director'] = params['director']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/basic/users/{username}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20088',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)