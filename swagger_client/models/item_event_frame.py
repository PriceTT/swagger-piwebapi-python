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


class ItemEventFrame(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, identifier=None, identifier_type=None, object=None, exception=None):
        """
        ItemEventFrame - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'identifier': 'str',
            'identifier_type': 'str',
            'object': 'InlineResponse20018Items',
            'exception': 'InlineResponse400'
        }

        self.attribute_map = {
            'identifier': 'Identifier',
            'identifier_type': 'IdentifierType',
            'object': 'Object',
            'exception': 'Exception'
        }

        self._identifier = identifier
        self._identifier_type = identifier_type
        self._object = object
        self._exception = exception

    @property
    def identifier(self):
        """
        Gets the identifier of this ItemEventFrame.

        :return: The identifier of this ItemEventFrame.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ItemEventFrame.

        :param identifier: The identifier of this ItemEventFrame.
        :type: str
        """

        self._identifier = identifier

    @property
    def identifier_type(self):
        """
        Gets the identifier_type of this ItemEventFrame.

        :return: The identifier_type of this ItemEventFrame.
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """
        Sets the identifier_type of this ItemEventFrame.

        :param identifier_type: The identifier_type of this ItemEventFrame.
        :type: str
        """

        self._identifier_type = identifier_type

    @property
    def object(self):
        """
        Gets the object of this ItemEventFrame.

        :return: The object of this ItemEventFrame.
        :rtype: InlineResponse20018Items
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this ItemEventFrame.

        :param object: The object of this ItemEventFrame.
        :type: InlineResponse20018Items
        """

        self._object = object

    @property
    def exception(self):
        """
        Gets the exception of this ItemEventFrame.

        :return: The exception of this ItemEventFrame.
        :rtype: InlineResponse400
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """
        Sets the exception of this ItemEventFrame.

        :param exception: The exception of this ItemEventFrame.
        :type: InlineResponse400
        """

        self._exception = exception

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
        if not isinstance(other, ItemEventFrame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
