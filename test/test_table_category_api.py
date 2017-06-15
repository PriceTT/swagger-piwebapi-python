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
from swagger_client.apis.table_category_api import TableCategoryApi


class TestTableCategoryApi(unittest.TestCase):
    """ TableCategoryApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.table_category_api.TableCategoryApi()

    def tearDown(self):
        pass

    def test_table_category_create_security_entry(self):
        """
        Test case for table_category_create_security_entry

        Create a security entry owned by the table category.
        """
        pass

    def test_table_category_delete(self):
        """
        Test case for table_category_delete

        Delete a table category.
        """
        pass

    def test_table_category_delete_security_entry(self):
        """
        Test case for table_category_delete_security_entry

        Delete a security entry owned by the table category.
        """
        pass

    def test_table_category_get(self):
        """
        Test case for table_category_get

        Retrieve a table category.
        """
        pass

    def test_table_category_get_by_path(self):
        """
        Test case for table_category_get_by_path

        Retrieve a table category by path.
        """
        pass

    def test_table_category_get_security(self):
        """
        Test case for table_category_get_security

        Get the security information of the specified security item associated with the table category for a specified user.
        """
        pass

    def test_table_category_get_security_entries(self):
        """
        Test case for table_category_get_security_entries

        Retrieve the security entries associated with the table category based on the specified criteria. By default, all security entries for this table category are returned.
        """
        pass

    def test_table_category_get_security_entry_by_name(self):
        """
        Test case for table_category_get_security_entry_by_name

        Retrieve the security entry associated with the table category with the specified name.
        """
        pass

    def test_table_category_update(self):
        """
        Test case for table_category_update

        Update a table category by replacing items in its definition.
        """
        pass

    def test_table_category_update_security_entry(self):
        """
        Test case for table_category_update_security_entry

        Update a security entry owned by the table category.
        """
        pass


if __name__ == '__main__':
    unittest.main()
