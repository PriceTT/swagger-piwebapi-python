# coding: utf-8

"""
    PI Web API 2017 Swagger Spec

    Swagger Spec file that describes PI Web API

    OpenAPI spec version: 1.9.0.266
    Contact: techsupport@osisoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.channel_api import ChannelApi


class TestChannelApi(unittest.TestCase):
    """ ChannelApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.channel_api.ChannelApi()

    def tearDown(self):
        pass

    def test_channel_instances(self):
        """
        Test case for channel_instances

        Retrieves a list of currently running channel instances.
        """
        pass


if __name__ == '__main__':
    unittest.main()
