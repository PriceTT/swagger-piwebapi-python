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


class SecurityEntry17(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, security_identity_name=None, allow_rights=None, deny_rights=None, links=None):
        """
        SecurityEntry17 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'security_identity_name': 'str',
            'allow_rights': 'list[str]',
            'deny_rights': 'list[str]',
            'links': 'InlineResponse2004Links'
        }

        self.attribute_map = {
            'name': 'Name',
            'security_identity_name': 'SecurityIdentityName',
            'allow_rights': 'AllowRights',
            'deny_rights': 'DenyRights',
            'links': 'Links'
        }

        self._name = name
        self._security_identity_name = security_identity_name
        self._allow_rights = allow_rights
        self._deny_rights = deny_rights
        self._links = links

    @property
    def name(self):
        """
        Gets the name of this SecurityEntry17.

        :return: The name of this SecurityEntry17.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecurityEntry17.

        :param name: The name of this SecurityEntry17.
        :type: str
        """

        self._name = name

    @property
    def security_identity_name(self):
        """
        Gets the security_identity_name of this SecurityEntry17.

        :return: The security_identity_name of this SecurityEntry17.
        :rtype: str
        """
        return self._security_identity_name

    @security_identity_name.setter
    def security_identity_name(self, security_identity_name):
        """
        Sets the security_identity_name of this SecurityEntry17.

        :param security_identity_name: The security_identity_name of this SecurityEntry17.
        :type: str
        """

        self._security_identity_name = security_identity_name

    @property
    def allow_rights(self):
        """
        Gets the allow_rights of this SecurityEntry17.

        :return: The allow_rights of this SecurityEntry17.
        :rtype: list[str]
        """
        return self._allow_rights

    @allow_rights.setter
    def allow_rights(self, allow_rights):
        """
        Sets the allow_rights of this SecurityEntry17.

        :param allow_rights: The allow_rights of this SecurityEntry17.
        :type: list[str]
        """

        self._allow_rights = allow_rights

    @property
    def deny_rights(self):
        """
        Gets the deny_rights of this SecurityEntry17.

        :return: The deny_rights of this SecurityEntry17.
        :rtype: list[str]
        """
        return self._deny_rights

    @deny_rights.setter
    def deny_rights(self, deny_rights):
        """
        Sets the deny_rights of this SecurityEntry17.

        :param deny_rights: The deny_rights of this SecurityEntry17.
        :type: list[str]
        """

        self._deny_rights = deny_rights

    @property
    def links(self):
        """
        Gets the links of this SecurityEntry17.

        :return: The links of this SecurityEntry17.
        :rtype: InlineResponse2004Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this SecurityEntry17.

        :param links: The links of this SecurityEntry17.
        :type: InlineResponse2004Links
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
        if not isinstance(other, SecurityEntry17):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
