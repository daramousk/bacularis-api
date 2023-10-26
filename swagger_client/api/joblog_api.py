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


class JoblogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_joblog_jobid_get(self, jobid, **kwargs):  # noqa: E501
        """Get job log for jobid  # noqa: E501

        Get job log for jobid  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_joblog_jobid_get(jobid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int jobid: Job identifier (required)
        :param bool show_time: Show time in job log.
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_joblog_jobid_get_with_http_info(jobid, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_joblog_jobid_get_with_http_info(jobid, **kwargs)  # noqa: E501
            return data

    def api_v2_joblog_jobid_get_with_http_info(self, jobid, **kwargs):  # noqa: E501
        """Get job log for jobid  # noqa: E501

        Get job log for jobid  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_joblog_jobid_get_with_http_info(jobid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int jobid: Job identifier (required)
        :param bool show_time: Show time in job log.
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jobid', 'show_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_joblog_jobid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jobid' is set
        if ('jobid' not in params or
                params['jobid'] is None):
            raise ValueError("Missing the required parameter `jobid` when calling `api_v2_joblog_jobid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'jobid' in params:
            path_params['jobid'] = params['jobid']  # noqa: E501

        query_params = []
        if 'show_time' in params:
            query_params.append(('show_time', params['show_time']))  # noqa: E501

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
            '/api/v2/joblog/{jobid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20078',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_joblog_messages_get(self, **kwargs):  # noqa: E501
        """Get console messages log.  # noqa: E501

        Get messages log. Note, because there are returned all current Bacula messages, this endpoint should not be shared non-admin users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_joblog_messages_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Set messages log Limit.
        :return: InlineResponse20079
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_joblog_messages_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_joblog_messages_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v2_joblog_messages_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get console messages log.  # noqa: E501

        Get messages log. Note, because there are returned all current Bacula messages, this endpoint should not be shared non-admin users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_joblog_messages_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Set messages log Limit.
        :return: InlineResponse20079
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_joblog_messages_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/api/v2/joblog/messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20079',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
