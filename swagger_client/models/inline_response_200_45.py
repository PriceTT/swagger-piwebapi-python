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


class InlineResponse20045(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_title=None, product_version=None, links=None):
        """
        InlineResponse20045 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_title': 'str',
            'product_version': 'str',
            'links': 'InlineResponse20045Links'
        }

        self.attribute_map = {
            'product_title': 'ProductTitle',
            'product_version': 'ProductVersion',
            'links': 'Links'
        }

        self._product_title = product_title
        self._product_version = product_version
        self._links = links

    @property
    def product_title(self):
        """
        Gets the product_title of this InlineResponse20045.

        :return: The product_title of this InlineResponse20045.
        :rtype: str
        """
        return self._product_title

    @product_title.setter
    def product_title(self, product_title):
        """
        Sets the product_title of this InlineResponse20045.

        :param product_title: The product_title of this InlineResponse20045.
        :type: str
        """

        self._product_title = product_title

    @property
    def product_version(self):
        """
        Gets the product_version of this InlineResponse20045.

        :return: The product_version of this InlineResponse20045.
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """
        Sets the product_version of this InlineResponse20045.

        :param product_version: The product_version of this InlineResponse20045.
        :type: str
        """

        self._product_version = product_version

    @property
    def links(self):
        """
        Gets the links of this InlineResponse20045.

        :return: The links of this InlineResponse20045.
        :rtype: InlineResponse20045Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse20045.

        :param links: The links of this InlineResponse20045.
        :type: InlineResponse20045Links
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
        if not isinstance(other, InlineResponse20045):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
