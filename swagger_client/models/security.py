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


class Security(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, can_annotate=None, can_delete=None, can_execute=None, can_read=None, can_read_data=None, can_subscribe=None, can_subscribe_others=None, can_write=None, can_write_data=None, has_admin=None, rights=None):
        """
        Security - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'can_annotate': 'bool',
            'can_delete': 'bool',
            'can_execute': 'bool',
            'can_read': 'bool',
            'can_read_data': 'bool',
            'can_subscribe': 'bool',
            'can_subscribe_others': 'bool',
            'can_write': 'bool',
            'can_write_data': 'bool',
            'has_admin': 'bool',
            'rights': 'list[str]'
        }

        self.attribute_map = {
            'can_annotate': 'CanAnnotate',
            'can_delete': 'CanDelete',
            'can_execute': 'CanExecute',
            'can_read': 'CanRead',
            'can_read_data': 'CanReadData',
            'can_subscribe': 'CanSubscribe',
            'can_subscribe_others': 'CanSubscribeOthers',
            'can_write': 'CanWrite',
            'can_write_data': 'CanWriteData',
            'has_admin': 'HasAdmin',
            'rights': 'Rights'
        }

        self._can_annotate = can_annotate
        self._can_delete = can_delete
        self._can_execute = can_execute
        self._can_read = can_read
        self._can_read_data = can_read_data
        self._can_subscribe = can_subscribe
        self._can_subscribe_others = can_subscribe_others
        self._can_write = can_write
        self._can_write_data = can_write_data
        self._has_admin = has_admin
        self._rights = rights

    @property
    def can_annotate(self):
        """
        Gets the can_annotate of this Security.

        :return: The can_annotate of this Security.
        :rtype: bool
        """
        return self._can_annotate

    @can_annotate.setter
    def can_annotate(self, can_annotate):
        """
        Sets the can_annotate of this Security.

        :param can_annotate: The can_annotate of this Security.
        :type: bool
        """

        self._can_annotate = can_annotate

    @property
    def can_delete(self):
        """
        Gets the can_delete of this Security.

        :return: The can_delete of this Security.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """
        Sets the can_delete of this Security.

        :param can_delete: The can_delete of this Security.
        :type: bool
        """

        self._can_delete = can_delete

    @property
    def can_execute(self):
        """
        Gets the can_execute of this Security.

        :return: The can_execute of this Security.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        """
        Sets the can_execute of this Security.

        :param can_execute: The can_execute of this Security.
        :type: bool
        """

        self._can_execute = can_execute

    @property
    def can_read(self):
        """
        Gets the can_read of this Security.

        :return: The can_read of this Security.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        """
        Sets the can_read of this Security.

        :param can_read: The can_read of this Security.
        :type: bool
        """

        self._can_read = can_read

    @property
    def can_read_data(self):
        """
        Gets the can_read_data of this Security.

        :return: The can_read_data of this Security.
        :rtype: bool
        """
        return self._can_read_data

    @can_read_data.setter
    def can_read_data(self, can_read_data):
        """
        Sets the can_read_data of this Security.

        :param can_read_data: The can_read_data of this Security.
        :type: bool
        """

        self._can_read_data = can_read_data

    @property
    def can_subscribe(self):
        """
        Gets the can_subscribe of this Security.

        :return: The can_subscribe of this Security.
        :rtype: bool
        """
        return self._can_subscribe

    @can_subscribe.setter
    def can_subscribe(self, can_subscribe):
        """
        Sets the can_subscribe of this Security.

        :param can_subscribe: The can_subscribe of this Security.
        :type: bool
        """

        self._can_subscribe = can_subscribe

    @property
    def can_subscribe_others(self):
        """
        Gets the can_subscribe_others of this Security.

        :return: The can_subscribe_others of this Security.
        :rtype: bool
        """
        return self._can_subscribe_others

    @can_subscribe_others.setter
    def can_subscribe_others(self, can_subscribe_others):
        """
        Sets the can_subscribe_others of this Security.

        :param can_subscribe_others: The can_subscribe_others of this Security.
        :type: bool
        """

        self._can_subscribe_others = can_subscribe_others

    @property
    def can_write(self):
        """
        Gets the can_write of this Security.

        :return: The can_write of this Security.
        :rtype: bool
        """
        return self._can_write

    @can_write.setter
    def can_write(self, can_write):
        """
        Sets the can_write of this Security.

        :param can_write: The can_write of this Security.
        :type: bool
        """

        self._can_write = can_write

    @property
    def can_write_data(self):
        """
        Gets the can_write_data of this Security.

        :return: The can_write_data of this Security.
        :rtype: bool
        """
        return self._can_write_data

    @can_write_data.setter
    def can_write_data(self, can_write_data):
        """
        Sets the can_write_data of this Security.

        :param can_write_data: The can_write_data of this Security.
        :type: bool
        """

        self._can_write_data = can_write_data

    @property
    def has_admin(self):
        """
        Gets the has_admin of this Security.

        :return: The has_admin of this Security.
        :rtype: bool
        """
        return self._has_admin

    @has_admin.setter
    def has_admin(self, has_admin):
        """
        Sets the has_admin of this Security.

        :param has_admin: The has_admin of this Security.
        :type: bool
        """

        self._has_admin = has_admin

    @property
    def rights(self):
        """
        Gets the rights of this Security.

        :return: The rights of this Security.
        :rtype: list[str]
        """
        return self._rights

    @rights.setter
    def rights(self, rights):
        """
        Sets the rights of this Security.

        :param rights: The rights of this Security.
        :type: list[str]
        """

        self._rights = rights

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
        if not isinstance(other, Security):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
