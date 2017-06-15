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


class SecurityMapping(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, description=None, path=None, account=None, security_identity_web_id=None, links=None):
        """
        SecurityMapping - a model defined in Swagger

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
            'account': 'str',
            'security_identity_web_id': 'str',
            'links': 'InlineResponse20025Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'path': 'Path',
            'account': 'Account',
            'security_identity_web_id': 'SecurityIdentityWebId',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._description = description
        self._path = path
        self._account = account
        self._security_identity_web_id = security_identity_web_id
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this SecurityMapping.

        :return: The web_id of this SecurityMapping.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this SecurityMapping.

        :param web_id: The web_id of this SecurityMapping.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this SecurityMapping.

        :return: The id of this SecurityMapping.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityMapping.

        :param id: The id of this SecurityMapping.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SecurityMapping.

        :return: The name of this SecurityMapping.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecurityMapping.

        :param name: The name of this SecurityMapping.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SecurityMapping.

        :return: The description of this SecurityMapping.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityMapping.

        :param description: The description of this SecurityMapping.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this SecurityMapping.

        :return: The path of this SecurityMapping.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this SecurityMapping.

        :param path: The path of this SecurityMapping.
        :type: str
        """

        self._path = path

    @property
    def account(self):
        """
        Gets the account of this SecurityMapping.

        :return: The account of this SecurityMapping.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this SecurityMapping.

        :param account: The account of this SecurityMapping.
        :type: str
        """

        self._account = account

    @property
    def security_identity_web_id(self):
        """
        Gets the security_identity_web_id of this SecurityMapping.

        :return: The security_identity_web_id of this SecurityMapping.
        :rtype: str
        """
        return self._security_identity_web_id

    @security_identity_web_id.setter
    def security_identity_web_id(self, security_identity_web_id):
        """
        Sets the security_identity_web_id of this SecurityMapping.

        :param security_identity_web_id: The security_identity_web_id of this SecurityMapping.
        :type: str
        """

        self._security_identity_web_id = security_identity_web_id

    @property
    def links(self):
        """
        Gets the links of this SecurityMapping.

        :return: The links of this SecurityMapping.
        :rtype: InlineResponse20025Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this SecurityMapping.

        :param links: The links of this SecurityMapping.
        :type: InlineResponse20025Links
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
        if not isinstance(other, SecurityMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
