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


class InlineResponse2002Links1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first=None, previous=None, next=None, last=None):
        """
        InlineResponse2002Links1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first': 'str',
            'previous': 'str',
            'next': 'str',
            'last': 'str'
        }

        self.attribute_map = {
            'first': 'First',
            'previous': 'Previous',
            'next': 'Next',
            'last': 'Last'
        }

        self._first = first
        self._previous = previous
        self._next = next
        self._last = last

    @property
    def first(self):
        """
        Gets the first of this InlineResponse2002Links1.

        :return: The first of this InlineResponse2002Links1.
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this InlineResponse2002Links1.

        :param first: The first of this InlineResponse2002Links1.
        :type: str
        """

        self._first = first

    @property
    def previous(self):
        """
        Gets the previous of this InlineResponse2002Links1.

        :return: The previous of this InlineResponse2002Links1.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """
        Sets the previous of this InlineResponse2002Links1.

        :param previous: The previous of this InlineResponse2002Links1.
        :type: str
        """

        self._previous = previous

    @property
    def next(self):
        """
        Gets the next of this InlineResponse2002Links1.

        :return: The next of this InlineResponse2002Links1.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this InlineResponse2002Links1.

        :param next: The next of this InlineResponse2002Links1.
        :type: str
        """

        self._next = next

    @property
    def last(self):
        """
        Gets the last of this InlineResponse2002Links1.

        :return: The last of this InlineResponse2002Links1.
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this InlineResponse2002Links1.

        :param last: The last of this InlineResponse2002Links1.
        :type: str
        """

        self._last = last

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
        if not isinstance(other, InlineResponse2002Links1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
