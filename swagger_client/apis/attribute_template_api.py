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


class AttributeTemplateApi(object):
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

    def attribute_template_create_attribute_template(self, web_id, template, **kwargs):
        """
        Create an attribute template as a child of another attribute template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_create_attribute_template(web_id, template, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the parent attribute template on which to create the attribute template. (required)
        :param Template4 template: The attribute template definition. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attribute_template_create_attribute_template_with_http_info(web_id, template, **kwargs)
        else:
            (data) = self.attribute_template_create_attribute_template_with_http_info(web_id, template, **kwargs)
            return data

    def attribute_template_create_attribute_template_with_http_info(self, web_id, template, **kwargs):
        """
        Create an attribute template as a child of another attribute template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_create_attribute_template_with_http_info(web_id, template, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the parent attribute template on which to create the attribute template. (required)
        :param Template4 template: The attribute template definition. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['web_id', 'template']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attribute_template_create_attribute_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'web_id' is set
        if ('web_id' not in params) or (params['web_id'] is None):
            raise ValueError("Missing the required parameter `web_id` when calling `attribute_template_create_attribute_template`")
        # verify the required parameter 'template' is set
        if ('template' not in params) or (params['template'] is None):
            raise ValueError("Missing the required parameter `template` when calling `attribute_template_create_attribute_template`")


        collection_formats = {}

        resource_path = '/attributetemplates/{webId}/attributetemplates'.replace('{format}', 'json')
        path_params = {}
        if 'web_id' in params:
            path_params['webId'] = params['web_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'template' in params:
            body_params = params['template']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def attribute_template_delete(self, web_id, **kwargs):
        """
        Delete an attribute template.
        Deleting an attribute template will delete the attributes that were created based on the template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_delete(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attribute_template_delete_with_http_info(web_id, **kwargs)
        else:
            (data) = self.attribute_template_delete_with_http_info(web_id, **kwargs)
            return data

    def attribute_template_delete_with_http_info(self, web_id, **kwargs):
        """
        Delete an attribute template.
        Deleting an attribute template will delete the attributes that were created based on the template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_delete_with_http_info(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['web_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attribute_template_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'web_id' is set
        if ('web_id' not in params) or (params['web_id'] is None):
            raise ValueError("Missing the required parameter `web_id` when calling `attribute_template_delete`")


        collection_formats = {}

        resource_path = '/attributetemplates/{webId}'.replace('{format}', 'json')
        path_params = {}
        if 'web_id' in params:
            path_params['webId'] = params['web_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def attribute_template_get(self, web_id, **kwargs):
        """
        Retrieve an attribute template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_get(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse20030
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attribute_template_get_with_http_info(web_id, **kwargs)
        else:
            (data) = self.attribute_template_get_with_http_info(web_id, **kwargs)
            return data

    def attribute_template_get_with_http_info(self, web_id, **kwargs):
        """
        Retrieve an attribute template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_get_with_http_info(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse20030
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
                    " to method attribute_template_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'web_id' is set
        if ('web_id' not in params) or (params['web_id'] is None):
            raise ValueError("Missing the required parameter `web_id` when calling `attribute_template_get`")


        collection_formats = {}

        resource_path = '/attributetemplates/{webId}'.replace('{format}', 'json')
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
                                        response_type='InlineResponse20030',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def attribute_template_get_attribute_templates(self, web_id, **kwargs):
        """
        Retrieve an attribute template's child attribute templates.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_get_attribute_templates(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse20031
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attribute_template_get_attribute_templates_with_http_info(web_id, **kwargs)
        else:
            (data) = self.attribute_template_get_attribute_templates_with_http_info(web_id, **kwargs)
            return data

    def attribute_template_get_attribute_templates_with_http_info(self, web_id, **kwargs):
        """
        Retrieve an attribute template's child attribute templates.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_get_attribute_templates_with_http_info(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse20031
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
                    " to method attribute_template_get_attribute_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'web_id' is set
        if ('web_id' not in params) or (params['web_id'] is None):
            raise ValueError("Missing the required parameter `web_id` when calling `attribute_template_get_attribute_templates`")


        collection_formats = {}

        resource_path = '/attributetemplates/{webId}/attributetemplates'.replace('{format}', 'json')
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
                                        response_type='InlineResponse20031',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def attribute_template_get_by_path(self, path, **kwargs):
        """
        Retrieve an attribute template by path.
        This method returns an attribute template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_get_by_path(path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str path: The path to the attribute template. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse20030
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attribute_template_get_by_path_with_http_info(path, **kwargs)
        else:
            (data) = self.attribute_template_get_by_path_with_http_info(path, **kwargs)
            return data

    def attribute_template_get_by_path_with_http_info(self, path, **kwargs):
        """
        Retrieve an attribute template by path.
        This method returns an attribute template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_get_by_path_with_http_info(path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str path: The path to the attribute template. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse20030
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
                    " to method attribute_template_get_by_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `attribute_template_get_by_path`")


        collection_formats = {}

        resource_path = '/attributetemplates'.replace('{format}', 'json')
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
                                        response_type='InlineResponse20030',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def attribute_template_get_categories(self, web_id, **kwargs):
        """
        Get an attribute template's categories.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_get_categories(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attribute_template_get_categories_with_http_info(web_id, **kwargs)
        else:
            (data) = self.attribute_template_get_categories_with_http_info(web_id, **kwargs)
            return data

    def attribute_template_get_categories_with_http_info(self, web_id, **kwargs):
        """
        Get an attribute template's categories.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_get_categories_with_http_info(web_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :param str selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
        :return: InlineResponse20012
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
                    " to method attribute_template_get_categories" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'web_id' is set
        if ('web_id' not in params) or (params['web_id'] is None):
            raise ValueError("Missing the required parameter `web_id` when calling `attribute_template_get_categories`")


        collection_formats = {}

        resource_path = '/attributetemplates/{webId}/categories'.replace('{format}', 'json')
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
                                        response_type='InlineResponse20012',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def attribute_template_update(self, web_id, template, **kwargs):
        """
        Update an existing attribute template by replacing items in its definition.
        Updating an attribute template will propagate changes to the attributes that were created based on the template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_update(web_id, template, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :param Template3 template: A partial attribute template containing the desired changes. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attribute_template_update_with_http_info(web_id, template, **kwargs)
        else:
            (data) = self.attribute_template_update_with_http_info(web_id, template, **kwargs)
            return data

    def attribute_template_update_with_http_info(self, web_id, template, **kwargs):
        """
        Update an existing attribute template by replacing items in its definition.
        Updating an attribute template will propagate changes to the attributes that were created based on the template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attribute_template_update_with_http_info(web_id, template, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_id: The ID of the attribute template. (required)
        :param Template3 template: A partial attribute template containing the desired changes. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['web_id', 'template']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attribute_template_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'web_id' is set
        if ('web_id' not in params) or (params['web_id'] is None):
            raise ValueError("Missing the required parameter `web_id` when calling `attribute_template_update`")
        # verify the required parameter 'template' is set
        if ('template' not in params) or (params['template'] is None):
            raise ValueError("Missing the required parameter `template` when calling `attribute_template_update`")


        collection_formats = {}

        resource_path = '/attributetemplates/{webId}'.replace('{format}', 'json')
        path_params = {}
        if 'web_id' in params:
            path_params['webId'] = params['web_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'template' in params:
            body_params = params['template']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)