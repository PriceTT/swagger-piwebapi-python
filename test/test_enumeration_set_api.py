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
from swagger_client.apis.enumeration_set_api import EnumerationSetApi


class TestEnumerationSetApi(unittest.TestCase):
    """ EnumerationSetApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.enumeration_set_api.EnumerationSetApi()

    def tearDown(self):
        pass

    def test_enumeration_set_create_security_entry(self):
        """
        Test case for enumeration_set_create_security_entry

        Create a security entry owned by the enumeration set.
        """
        pass

    def test_enumeration_set_create_value(self):
        """
        Test case for enumeration_set_create_value

        Create an enumeration value for a enumeration set.
        """
        pass

    def test_enumeration_set_delete(self):
        """
        Test case for enumeration_set_delete

        Delete an enumeration set.
        """
        pass

    def test_enumeration_set_delete_security_entry(self):
        """
        Test case for enumeration_set_delete_security_entry

        Delete a security entry owned by the enumeration set.
        """
        pass

    def test_enumeration_set_get(self):
        """
        Test case for enumeration_set_get

        Retrieve an enumeration set.
        """
        pass

    def test_enumeration_set_get_by_path(self):
        """
        Test case for enumeration_set_get_by_path

        Retrieve an enumeration set by path.
        """
        pass

    def test_enumeration_set_get_security(self):
        """
        Test case for enumeration_set_get_security

        Get the security information of the specified security item associated with the enumeration set for a specified user.
        """
        pass

    def test_enumeration_set_get_security_entries(self):
        """
        Test case for enumeration_set_get_security_entries

        Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.
        """
        pass

    def test_enumeration_set_get_security_entry_by_name(self):
        """
        Test case for enumeration_set_get_security_entry_by_name

        Retrieve the security entry associated with the enumeration set with the specified name.
        """
        pass

    def test_enumeration_set_get_values(self):
        """
        Test case for enumeration_set_get_values

        Retrieve an enumeration set's values.
        """
        pass

    def test_enumeration_set_update(self):
        """
        Test case for enumeration_set_update

        Update an enumeration set by replacing items in its definition.
        """
        pass

    def test_enumeration_set_update_security_entry(self):
        """
        Test case for enumeration_set_update_security_entry

        Update a security entry owned by the enumeration set.
        """
        pass


if __name__ == '__main__':
    unittest.main()
