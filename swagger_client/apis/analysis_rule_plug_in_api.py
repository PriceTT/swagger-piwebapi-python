# coding: utf-8

"""
    PI Web API 2017 Swagger Spec

    Swagger Spec file that describes PI Web API

    OpenAPI spec version: 1.9.0.266
    Contact: techsupport@osisoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AnalysisRulePlugInApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def analysis_rule_plug_in_get(self, web_id, **kwargs):
        """
        Retrieve an Analysis Rule Plug-in.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analysis_rule_plug_in_get(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the Analysis Rule Plug-in. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analysis_rule_plug_in_get_with_http_info(web_id, **kwargs)
        else:
            (data) = self.analysis_rule_plug_in_get_with_http_info(web_id, **kwargs)
            return data

    def analysis_rule_plug_in_get_with_http_info(self, web_id, **kwargs):
        """
        Retrieve an Analysis Rule Plug-in.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analysis_rule_plug_in_get_with_http_info(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the Analysis Rule Plug-in. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['web_id', 'selected_fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analysis_rule_plug_in_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'web_id' is set
        if ('web_id' not in params) or (params['web_id'] is None):
            raise ValueError("Missing the required parameter `web_id` when calling `analysis_rule_plug_in_get`")


        collection_formats = {}

        resource_path = '/analysisruleplugins/{webId}'.replace('{format}', 'json')
        path_params = {}
        if 'web_id' in params:
            path_params['webId'] = params['web_id']

        query_params = {}
        if 'selected_fields' in params:
            query_params['selectedFields'] = params['selected_fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2005',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def analysis_rule_plug_in_get_by_path(self, path, **kwargs):
        """
        Retrieve an Analysis Rule Plug-in by path.
        This method returns an Analysis Rule Plug-in based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analysis_rule_plug_in_get_by_path(path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str path: The path to the Analysis Rule Plug-in. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analysis_rule_plug_in_get_by_path_with_http_info(path, **kwargs)
        else:
            (data) = self.analysis_rule_plug_in_get_by_path_with_http_info(path, **kwargs)
            return data

    def analysis_rule_plug_in_get_by_path_with_http_info(self, path, **kwargs):
        """
        Retrieve an Analysis Rule Plug-in by path.
        This method returns an Analysis Rule Plug-in based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analysis_rule_plug_in_get_by_path_with_http_info(path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str path: The path to the Analysis Rule Plug-in. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['path', 'selected_fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analysis_rule_plug_in_get_by_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `analysis_rule_plug_in_get_by_path`")


        collection_formats = {}

        resource_path = '/analysisruleplugins'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'path' in params:
            query_params['path'] = params['path']
        if 'selected_fields' in params:
            query_params['selectedFields'] = params['selected_fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2005',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
