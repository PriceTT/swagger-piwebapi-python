# coding: utf-8

"""
    PI Web API 2017 Swagger Spec

    Swagger Spec file that describes PI Web API

    OpenAPI spec version: 1.9.0.266
    Contact: techsupport@osisoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20020Links(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _self=None, database=None, data=None, categories=None, security=None, security_entries=None):
        """
        InlineResponse20020Links - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_self': 'str',
            'database': 'str',
            'data': 'str',
            'categories': 'str',
            'security': 'str',
            'security_entries': 'str'
        }

        self.attribute_map = {
            '_self': 'Self',
            'database': 'Database',
            'data': 'Data',
            'categories': 'Categories',
            'security': 'Security',
            'security_entries': 'SecurityEntries'
        }

        self.__self = _self
        self._database = database
        self._data = data
        self._categories = categories
        self._security = security
        self._security_entries = security_entries

    @property
    def _self(self):
        """
        Gets the _self of this InlineResponse20020Links.

        :return: The _self of this InlineResponse20020Links.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this InlineResponse20020Links.

        :param _self: The _self of this InlineResponse20020Links.
        :type: str
        """

        self.__self = _self

    @property
    def database(self):
        """
        Gets the database of this InlineResponse20020Links.

        :return: The database of this InlineResponse20020Links.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this InlineResponse20020Links.

        :param database: The database of this InlineResponse20020Links.
        :type: str
        """

        self._database = database

    @property
    def data(self):
        """
        Gets the data of this InlineResponse20020Links.

        :return: The data of this InlineResponse20020Links.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this InlineResponse20020Links.

        :param data: The data of this InlineResponse20020Links.
        :type: str
        """

        self._data = data

    @property
    def categories(self):
        """
        Gets the categories of this InlineResponse20020Links.

        :return: The categories of this InlineResponse20020Links.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this InlineResponse20020Links.

        :param categories: The categories of this InlineResponse20020Links.
        :type: str
        """

        self._categories = categories

    @property
    def security(self):
        """
        Gets the security of this InlineResponse20020Links.

        :return: The security of this InlineResponse20020Links.
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """
        Sets the security of this InlineResponse20020Links.

        :param security: The security of this InlineResponse20020Links.
        :type: str
        """

        self._security = security

    @property
    def security_entries(self):
        """
        Gets the security_entries of this InlineResponse20020Links.

        :return: The security_entries of this InlineResponse20020Links.
        :rtype: str
        """
        return self._security_entries

    @security_entries.setter
    def security_entries(self, security_entries):
        """
        Sets the security_entries of this InlineResponse20020Links.

        :param security_entries: The security_entries of this InlineResponse20020Links.
        :type: str
        """

        self._security_entries = security_entries

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse20020Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
