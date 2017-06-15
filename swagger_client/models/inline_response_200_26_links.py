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


class InlineResponse20026Links(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _self=None, asset_server=None):
        """
        InlineResponse20026Links - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_self': 'str',
            'asset_server': 'str'
        }

        self.attribute_map = {
            '_self': 'Self',
            'asset_server': 'AssetServer'
        }

        self.__self = _self
        self._asset_server = asset_server

    @property
    def _self(self):
        """
        Gets the _self of this InlineResponse20026Links.

        :return: The _self of this InlineResponse20026Links.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this InlineResponse20026Links.

        :param _self: The _self of this InlineResponse20026Links.
        :type: str
        """

        self.__self = _self

    @property
    def asset_server(self):
        """
        Gets the asset_server of this InlineResponse20026Links.

        :return: The asset_server of this InlineResponse20026Links.
        :rtype: str
        """
        return self._asset_server

    @asset_server.setter
    def asset_server(self, asset_server):
        """
        Sets the asset_server of this InlineResponse20026Links.

        :param asset_server: The asset_server of this InlineResponse20026Links.
        :type: str
        """

        self._asset_server = asset_server

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
        if not isinstance(other, InlineResponse20026Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
