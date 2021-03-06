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
from swagger_client.apis.asset_server_api import AssetServerApi


class TestAssetServerApi(unittest.TestCase):
    """ AssetServerApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.asset_server_api.AssetServerApi()

    def tearDown(self):
        pass

    def test_asset_server_create_asset_database(self):
        """
        Test case for asset_server_create_asset_database

        Create an asset database.
        """
        pass

    def test_asset_server_create_security_entry(self):
        """
        Test case for asset_server_create_security_entry

        Create a security entry owned by the asset server.
        """
        pass

    def test_asset_server_create_security_identity(self):
        """
        Test case for asset_server_create_security_identity

        Create a security identity.
        """
        pass

    def test_asset_server_create_security_mapping(self):
        """
        Test case for asset_server_create_security_mapping

        Create a security mapping.
        """
        pass

    def test_asset_server_create_unit_class(self):
        """
        Test case for asset_server_create_unit_class

        Create a unit class in the specified Asset Server.
        """
        pass

    def test_asset_server_delete_security_entry(self):
        """
        Test case for asset_server_delete_security_entry

        Delete a security entry owned by the asset server.
        """
        pass

    def test_asset_server_get(self):
        """
        Test case for asset_server_get

        Retrieve an Asset Server.
        """
        pass

    def test_asset_server_get_analysis_rule_plug_ins(self):
        """
        Test case for asset_server_get_analysis_rule_plug_ins

        Retrieve a list of all Analysis Rule Plug-in's.
        """
        pass

    def test_asset_server_get_by_name(self):
        """
        Test case for asset_server_get_by_name

        Retrieve an Asset Server by name.
        """
        pass

    def test_asset_server_get_by_path(self):
        """
        Test case for asset_server_get_by_path

        Retrieve an Asset Server by path.
        """
        pass

    def test_asset_server_get_databases(self):
        """
        Test case for asset_server_get_databases

        Retrieve a list of all Asset Databases on the specified Asset Server.
        """
        pass

    def test_asset_server_get_security(self):
        """
        Test case for asset_server_get_security

        Get the security information of the specified security item associated with the asset server for a specified user.
        """
        pass

    def test_asset_server_get_security_entries(self):
        """
        Test case for asset_server_get_security_entries

        Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.
        """
        pass

    def test_asset_server_get_security_entry_by_name(self):
        """
        Test case for asset_server_get_security_entry_by_name

        Retrieve the security entry of the specified security item associated with the asset server with the specified name.
        """
        pass

    def test_asset_server_get_security_identities(self):
        """
        Test case for asset_server_get_security_identities

        Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.
        """
        pass

    def test_asset_server_get_security_identities_for_user(self):
        """
        Test case for asset_server_get_security_identities_for_user

        Retrieve security identities for a specific user.
        """
        pass

    def test_asset_server_get_security_mappings(self):
        """
        Test case for asset_server_get_security_mappings

        Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.
        """
        pass

    def test_asset_server_get_time_rule_plug_ins(self):
        """
        Test case for asset_server_get_time_rule_plug_ins

        Retrieve a list of all Time Rule Plug-in's.
        """
        pass

    def test_asset_server_get_unit_classes(self):
        """
        Test case for asset_server_get_unit_classes

        Retrieve a list of all unit classes on the specified Asset Server.
        """
        pass

    def test_asset_server_list(self):
        """
        Test case for asset_server_list

        Retrieve a list of all Asset Servers known to this service.
        """
        pass

    def test_asset_server_update_security_entry(self):
        """
        Test case for asset_server_update_security_entry

        Update a security entry owned by the asset server.
        """
        pass


if __name__ == '__main__':
    unittest.main()
