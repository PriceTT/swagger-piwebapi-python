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


class Table1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, description=None, path=None, category_names=None, time_zone=None, convert_to_local_time=None, links=None):
        """
        Table1 - a model defined in Swagger

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
            'category_names': 'list[str]',
            'time_zone': 'str',
            'convert_to_local_time': 'bool',
            'links': 'InlineResponse20020Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'path': 'Path',
            'category_names': 'CategoryNames',
            'time_zone': 'TimeZone',
            'convert_to_local_time': 'ConvertToLocalTime',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._description = description
        self._path = path
        self._category_names = category_names
        self._time_zone = time_zone
        self._convert_to_local_time = convert_to_local_time
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this Table1.

        :return: The web_id of this Table1.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this Table1.

        :param web_id: The web_id of this Table1.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this Table1.

        :return: The id of this Table1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Table1.

        :param id: The id of this Table1.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Table1.

        :return: The name of this Table1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Table1.

        :param name: The name of this Table1.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Table1.

        :return: The description of this Table1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Table1.

        :param description: The description of this Table1.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this Table1.

        :return: The path of this Table1.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Table1.

        :param path: The path of this Table1.
        :type: str
        """

        self._path = path

    @property
    def category_names(self):
        """
        Gets the category_names of this Table1.

        :return: The category_names of this Table1.
        :rtype: list[str]
        """
        return self._category_names

    @category_names.setter
    def category_names(self, category_names):
        """
        Sets the category_names of this Table1.

        :param category_names: The category_names of this Table1.
        :type: list[str]
        """

        self._category_names = category_names

    @property
    def time_zone(self):
        """
        Gets the time_zone of this Table1.

        :return: The time_zone of this Table1.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this Table1.

        :param time_zone: The time_zone of this Table1.
        :type: str
        """

        self._time_zone = time_zone

    @property
    def convert_to_local_time(self):
        """
        Gets the convert_to_local_time of this Table1.

        :return: The convert_to_local_time of this Table1.
        :rtype: bool
        """
        return self._convert_to_local_time

    @convert_to_local_time.setter
    def convert_to_local_time(self, convert_to_local_time):
        """
        Sets the convert_to_local_time of this Table1.

        :param convert_to_local_time: The convert_to_local_time of this Table1.
        :type: bool
        """

        self._convert_to_local_time = convert_to_local_time

    @property
    def links(self):
        """
        Gets the links of this Table1.

        :return: The links of this Table1.
        :rtype: InlineResponse20020Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Table1.

        :param links: The links of this Table1.
        :type: InlineResponse20020Links
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
        if not isinstance(other, Table1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
