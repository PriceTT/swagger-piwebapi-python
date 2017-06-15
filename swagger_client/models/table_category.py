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


class TableCategory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, description=None, path=None, links=None):
        """
        TableCategory - a model defined in Swagger

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
            'links': 'InlineResponse20019Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'path': 'Path',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._description = description
        self._path = path
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this TableCategory.

        :return: The web_id of this TableCategory.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this TableCategory.

        :param web_id: The web_id of this TableCategory.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this TableCategory.

        :return: The id of this TableCategory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TableCategory.

        :param id: The id of this TableCategory.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this TableCategory.

        :return: The name of this TableCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TableCategory.

        :param name: The name of this TableCategory.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TableCategory.

        :return: The description of this TableCategory.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TableCategory.

        :param description: The description of this TableCategory.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this TableCategory.

        :return: The path of this TableCategory.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this TableCategory.

        :param path: The path of this TableCategory.
        :type: str
        """

        self._path = path

    @property
    def links(self):
        """
        Gets the links of this TableCategory.

        :return: The links of this TableCategory.
        :rtype: InlineResponse20019Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this TableCategory.

        :param links: The links of this TableCategory.
        :type: InlineResponse20019Links
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
        if not isinstance(other, TableCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
