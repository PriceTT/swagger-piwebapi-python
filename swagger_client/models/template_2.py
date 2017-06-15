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


class Template2(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, description=None, path=None, allow_element_to_extend=None, base_template=None, instance_type=None, naming_pattern=None, category_names=None, extended_properties=None, severity=None, can_be_acknowledged=None, links=None):
        """
        Template2 - a model defined in Swagger

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
            'allow_element_to_extend': 'bool',
            'base_template': 'str',
            'instance_type': 'str',
            'naming_pattern': 'str',
            'category_names': 'list[str]',
            'extended_properties': 'dict(str, InlineResponse2009ExtendedProperties)',
            'severity': 'str',
            'can_be_acknowledged': 'bool',
            'links': 'InlineResponse20016Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'path': 'Path',
            'allow_element_to_extend': 'AllowElementToExtend',
            'base_template': 'BaseTemplate',
            'instance_type': 'InstanceType',
            'naming_pattern': 'NamingPattern',
            'category_names': 'CategoryNames',
            'extended_properties': 'ExtendedProperties',
            'severity': 'Severity',
            'can_be_acknowledged': 'CanBeAcknowledged',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._description = description
        self._path = path
        self._allow_element_to_extend = allow_element_to_extend
        self._base_template = base_template
        self._instance_type = instance_type
        self._naming_pattern = naming_pattern
        self._category_names = category_names
        self._extended_properties = extended_properties
        self._severity = severity
        self._can_be_acknowledged = can_be_acknowledged
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this Template2.

        :return: The web_id of this Template2.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this Template2.

        :param web_id: The web_id of this Template2.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this Template2.

        :return: The id of this Template2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Template2.

        :param id: The id of this Template2.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Template2.

        :return: The name of this Template2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Template2.

        :param name: The name of this Template2.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Template2.

        :return: The description of this Template2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Template2.

        :param description: The description of this Template2.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this Template2.

        :return: The path of this Template2.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Template2.

        :param path: The path of this Template2.
        :type: str
        """

        self._path = path

    @property
    def allow_element_to_extend(self):
        """
        Gets the allow_element_to_extend of this Template2.

        :return: The allow_element_to_extend of this Template2.
        :rtype: bool
        """
        return self._allow_element_to_extend

    @allow_element_to_extend.setter
    def allow_element_to_extend(self, allow_element_to_extend):
        """
        Sets the allow_element_to_extend of this Template2.

        :param allow_element_to_extend: The allow_element_to_extend of this Template2.
        :type: bool
        """

        self._allow_element_to_extend = allow_element_to_extend

    @property
    def base_template(self):
        """
        Gets the base_template of this Template2.

        :return: The base_template of this Template2.
        :rtype: str
        """
        return self._base_template

    @base_template.setter
    def base_template(self, base_template):
        """
        Sets the base_template of this Template2.

        :param base_template: The base_template of this Template2.
        :type: str
        """

        self._base_template = base_template

    @property
    def instance_type(self):
        """
        Gets the instance_type of this Template2.

        :return: The instance_type of this Template2.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """
        Sets the instance_type of this Template2.

        :param instance_type: The instance_type of this Template2.
        :type: str
        """

        self._instance_type = instance_type

    @property
    def naming_pattern(self):
        """
        Gets the naming_pattern of this Template2.

        :return: The naming_pattern of this Template2.
        :rtype: str
        """
        return self._naming_pattern

    @naming_pattern.setter
    def naming_pattern(self, naming_pattern):
        """
        Sets the naming_pattern of this Template2.

        :param naming_pattern: The naming_pattern of this Template2.
        :type: str
        """

        self._naming_pattern = naming_pattern

    @property
    def category_names(self):
        """
        Gets the category_names of this Template2.

        :return: The category_names of this Template2.
        :rtype: list[str]
        """
        return self._category_names

    @category_names.setter
    def category_names(self, category_names):
        """
        Sets the category_names of this Template2.

        :param category_names: The category_names of this Template2.
        :type: list[str]
        """

        self._category_names = category_names

    @property
    def extended_properties(self):
        """
        Gets the extended_properties of this Template2.

        :return: The extended_properties of this Template2.
        :rtype: dict(str, InlineResponse2009ExtendedProperties)
        """
        return self._extended_properties

    @extended_properties.setter
    def extended_properties(self, extended_properties):
        """
        Sets the extended_properties of this Template2.

        :param extended_properties: The extended_properties of this Template2.
        :type: dict(str, InlineResponse2009ExtendedProperties)
        """

        self._extended_properties = extended_properties

    @property
    def severity(self):
        """
        Gets the severity of this Template2.

        :return: The severity of this Template2.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Template2.

        :param severity: The severity of this Template2.
        :type: str
        """

        self._severity = severity

    @property
    def can_be_acknowledged(self):
        """
        Gets the can_be_acknowledged of this Template2.

        :return: The can_be_acknowledged of this Template2.
        :rtype: bool
        """
        return self._can_be_acknowledged

    @can_be_acknowledged.setter
    def can_be_acknowledged(self, can_be_acknowledged):
        """
        Sets the can_be_acknowledged of this Template2.

        :param can_be_acknowledged: The can_be_acknowledged of this Template2.
        :type: bool
        """

        self._can_be_acknowledged = can_be_acknowledged

    @property
    def links(self):
        """
        Gets the links of this Template2.

        :return: The links of this Template2.
        :rtype: InlineResponse20016Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Template2.

        :param links: The links of this Template2.
        :type: InlineResponse20016Links
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
        if not isinstance(other, Template2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
