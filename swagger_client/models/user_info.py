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


class UserInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, identity_type=None, name=None, is_authenticated=None, sid=None, impersonation_level=None):
        """
        UserInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'identity_type': 'str',
            'name': 'str',
            'is_authenticated': 'bool',
            'sid': 'str',
            'impersonation_level': 'str'
        }

        self.attribute_map = {
            'identity_type': 'IdentityType',
            'name': 'Name',
            'is_authenticated': 'IsAuthenticated',
            'sid': 'SID',
            'impersonation_level': 'ImpersonationLevel'
        }

        self._identity_type = identity_type
        self._name = name
        self._is_authenticated = is_authenticated
        self._sid = sid
        self._impersonation_level = impersonation_level

    @property
    def identity_type(self):
        """
        Gets the identity_type of this UserInfo.

        :return: The identity_type of this UserInfo.
        :rtype: str
        """
        return self._identity_type

    @identity_type.setter
    def identity_type(self, identity_type):
        """
        Sets the identity_type of this UserInfo.

        :param identity_type: The identity_type of this UserInfo.
        :type: str
        """

        self._identity_type = identity_type

    @property
    def name(self):
        """
        Gets the name of this UserInfo.

        :return: The name of this UserInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserInfo.

        :param name: The name of this UserInfo.
        :type: str
        """

        self._name = name

    @property
    def is_authenticated(self):
        """
        Gets the is_authenticated of this UserInfo.

        :return: The is_authenticated of this UserInfo.
        :rtype: bool
        """
        return self._is_authenticated

    @is_authenticated.setter
    def is_authenticated(self, is_authenticated):
        """
        Sets the is_authenticated of this UserInfo.

        :param is_authenticated: The is_authenticated of this UserInfo.
        :type: bool
        """

        self._is_authenticated = is_authenticated

    @property
    def sid(self):
        """
        Gets the sid of this UserInfo.

        :return: The sid of this UserInfo.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this UserInfo.

        :param sid: The sid of this UserInfo.
        :type: str
        """

        self._sid = sid

    @property
    def impersonation_level(self):
        """
        Gets the impersonation_level of this UserInfo.

        :return: The impersonation_level of this UserInfo.
        :rtype: str
        """
        return self._impersonation_level

    @impersonation_level.setter
    def impersonation_level(self, impersonation_level):
        """
        Sets the impersonation_level of this UserInfo.

        :param impersonation_level: The impersonation_level of this UserInfo.
        :type: str
        """

        self._impersonation_level = impersonation_level

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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
