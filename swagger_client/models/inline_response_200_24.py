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


class InlineResponse20024(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, items=None, links=None):
        """
        InlineResponse20024 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'items': 'list[InlineResponse20024Items]',
            'links': 'InlineResponse2002Links1'
        }

        self.attribute_map = {
            'items': 'Items',
            'links': 'Links'
        }

        self._items = items
        self._links = links

    @property
    def items(self):
        """
        Gets the items of this InlineResponse20024.

        :return: The items of this InlineResponse20024.
        :rtype: list[InlineResponse20024Items]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this InlineResponse20024.

        :param items: The items of this InlineResponse20024.
        :type: list[InlineResponse20024Items]
        """

        self._items = items

    @property
    def links(self):
        """
        Gets the links of this InlineResponse20024.

        :return: The links of this InlineResponse20024.
        :rtype: InlineResponse2002Links1
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse20024.

        :param links: The links of this InlineResponse20024.
        :type: InlineResponse2002Links1
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
        if not isinstance(other, InlineResponse20024):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
