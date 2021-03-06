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


class InlineResponse20024Items(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, description=None, path=None, is_enabled=None, links=None):
        """
        InlineResponse20024Items - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'web_id': 'str',
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'path': 'str',
            'is_enabled': 'bool',
            'links': 'InlineResponse20024Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'path': 'Path',
            'is_enabled': 'IsEnabled',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._description = description
        self._path = path
        self._is_enabled = is_enabled
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this InlineResponse20024Items.

        :return: The web_id of this InlineResponse20024Items.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this InlineResponse20024Items.

        :param web_id: The web_id of this InlineResponse20024Items.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this InlineResponse20024Items.

        :return: The id of this InlineResponse20024Items.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse20024Items.

        :param id: The id of this InlineResponse20024Items.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this InlineResponse20024Items.

        :return: The name of this InlineResponse20024Items.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse20024Items.

        :param name: The name of this InlineResponse20024Items.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this InlineResponse20024Items.

        :return: The description of this InlineResponse20024Items.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this InlineResponse20024Items.

        :param description: The description of this InlineResponse20024Items.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this InlineResponse20024Items.

        :return: The path of this InlineResponse20024Items.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this InlineResponse20024Items.

        :param path: The path of this InlineResponse20024Items.
        :type: str
        """

        self._path = path

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this InlineResponse20024Items.

        :return: The is_enabled of this InlineResponse20024Items.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this InlineResponse20024Items.

        :param is_enabled: The is_enabled of this InlineResponse20024Items.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def links(self):
        """
        Gets the links of this InlineResponse20024Items.

        :return: The links of this InlineResponse20024Items.
        :rtype: InlineResponse20024Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse20024Items.

        :param links: The links of this InlineResponse20024Items.
        :type: InlineResponse20024Links
        """

        self._links = links

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
        if not isinstance(other, InlineResponse20024Items):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
