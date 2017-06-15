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


class EventFrame1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, description=None, path=None, template_name=None, has_children=None, category_names=None, extended_properties=None, start_time=None, end_time=None, severity=None, acknowledged_by=None, acknowledged_date=None, can_be_acknowledged=None, is_acknowledged=None, is_annotated=None, is_locked=None, are_values_captured=None, ref_element_web_ids=None, security=None, links=None):
        """
        EventFrame1 - a model defined in Swagger

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
            'template_name': 'str',
            'has_children': 'bool',
            'category_names': 'list[str]',
            'extended_properties': 'dict(str, InlineResponse2009ExtendedProperties)',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'severity': 'str',
            'acknowledged_by': 'str',
            'acknowledged_date': 'datetime',
            'can_be_acknowledged': 'bool',
            'is_acknowledged': 'bool',
            'is_annotated': 'bool',
            'is_locked': 'bool',
            'are_values_captured': 'bool',
            'ref_element_web_ids': 'list[str]',
            'security': 'InlineResponse20018Security',
            'links': 'InlineResponse20018Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'path': 'Path',
            'template_name': 'TemplateName',
            'has_children': 'HasChildren',
            'category_names': 'CategoryNames',
            'extended_properties': 'ExtendedProperties',
            'start_time': 'StartTime',
            'end_time': 'EndTime',
            'severity': 'Severity',
            'acknowledged_by': 'AcknowledgedBy',
            'acknowledged_date': 'AcknowledgedDate',
            'can_be_acknowledged': 'CanBeAcknowledged',
            'is_acknowledged': 'IsAcknowledged',
            'is_annotated': 'IsAnnotated',
            'is_locked': 'IsLocked',
            'are_values_captured': 'AreValuesCaptured',
            'ref_element_web_ids': 'RefElementWebIds',
            'security': 'Security',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._description = description
        self._path = path
        self._template_name = template_name
        self._has_children = has_children
        self._category_names = category_names
        self._extended_properties = extended_properties
        self._start_time = start_time
        self._end_time = end_time
        self._severity = severity
        self._acknowledged_by = acknowledged_by
        self._acknowledged_date = acknowledged_date
        self._can_be_acknowledged = can_be_acknowledged
        self._is_acknowledged = is_acknowledged
        self._is_annotated = is_annotated
        self._is_locked = is_locked
        self._are_values_captured = are_values_captured
        self._ref_element_web_ids = ref_element_web_ids
        self._security = security
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this EventFrame1.

        :return: The web_id of this EventFrame1.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this EventFrame1.

        :param web_id: The web_id of this EventFrame1.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this EventFrame1.

        :return: The id of this EventFrame1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EventFrame1.

        :param id: The id of this EventFrame1.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this EventFrame1.

        :return: The name of this EventFrame1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EventFrame1.

        :param name: The name of this EventFrame1.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this EventFrame1.

        :return: The description of this EventFrame1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EventFrame1.

        :param description: The description of this EventFrame1.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this EventFrame1.

        :return: The path of this EventFrame1.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this EventFrame1.

        :param path: The path of this EventFrame1.
        :type: str
        """

        self._path = path

    @property
    def template_name(self):
        """
        Gets the template_name of this EventFrame1.

        :return: The template_name of this EventFrame1.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """
        Sets the template_name of this EventFrame1.

        :param template_name: The template_name of this EventFrame1.
        :type: str
        """

        self._template_name = template_name

    @property
    def has_children(self):
        """
        Gets the has_children of this EventFrame1.

        :return: The has_children of this EventFrame1.
        :rtype: bool
        """
        return self._has_children

    @has_children.setter
    def has_children(self, has_children):
        """
        Sets the has_children of this EventFrame1.

        :param has_children: The has_children of this EventFrame1.
        :type: bool
        """

        self._has_children = has_children

    @property
    def category_names(self):
        """
        Gets the category_names of this EventFrame1.

        :return: The category_names of this EventFrame1.
        :rtype: list[str]
        """
        return self._category_names

    @category_names.setter
    def category_names(self, category_names):
        """
        Sets the category_names of this EventFrame1.

        :param category_names: The category_names of this EventFrame1.
        :type: list[str]
        """

        self._category_names = category_names

    @property
    def extended_properties(self):
        """
        Gets the extended_properties of this EventFrame1.

        :return: The extended_properties of this EventFrame1.
        :rtype: dict(str, InlineResponse2009ExtendedProperties)
        """
        return self._extended_properties

    @extended_properties.setter
    def extended_properties(self, extended_properties):
        """
        Sets the extended_properties of this EventFrame1.

        :param extended_properties: The extended_properties of this EventFrame1.
        :type: dict(str, InlineResponse2009ExtendedProperties)
        """

        self._extended_properties = extended_properties

    @property
    def start_time(self):
        """
        Gets the start_time of this EventFrame1.

        :return: The start_time of this EventFrame1.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this EventFrame1.

        :param start_time: The start_time of this EventFrame1.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this EventFrame1.

        :return: The end_time of this EventFrame1.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this EventFrame1.

        :param end_time: The end_time of this EventFrame1.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def severity(self):
        """
        Gets the severity of this EventFrame1.

        :return: The severity of this EventFrame1.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this EventFrame1.

        :param severity: The severity of this EventFrame1.
        :type: str
        """

        self._severity = severity

    @property
    def acknowledged_by(self):
        """
        Gets the acknowledged_by of this EventFrame1.

        :return: The acknowledged_by of this EventFrame1.
        :rtype: str
        """
        return self._acknowledged_by

    @acknowledged_by.setter
    def acknowledged_by(self, acknowledged_by):
        """
        Sets the acknowledged_by of this EventFrame1.

        :param acknowledged_by: The acknowledged_by of this EventFrame1.
        :type: str
        """

        self._acknowledged_by = acknowledged_by

    @property
    def acknowledged_date(self):
        """
        Gets the acknowledged_date of this EventFrame1.

        :return: The acknowledged_date of this EventFrame1.
        :rtype: datetime
        """
        return self._acknowledged_date

    @acknowledged_date.setter
    def acknowledged_date(self, acknowledged_date):
        """
        Sets the acknowledged_date of this EventFrame1.

        :param acknowledged_date: The acknowledged_date of this EventFrame1.
        :type: datetime
        """

        self._acknowledged_date = acknowledged_date

    @property
    def can_be_acknowledged(self):
        """
        Gets the can_be_acknowledged of this EventFrame1.

        :return: The can_be_acknowledged of this EventFrame1.
        :rtype: bool
        """
        return self._can_be_acknowledged

    @can_be_acknowledged.setter
    def can_be_acknowledged(self, can_be_acknowledged):
        """
        Sets the can_be_acknowledged of this EventFrame1.

        :param can_be_acknowledged: The can_be_acknowledged of this EventFrame1.
        :type: bool
        """

        self._can_be_acknowledged = can_be_acknowledged

    @property
    def is_acknowledged(self):
        """
        Gets the is_acknowledged of this EventFrame1.

        :return: The is_acknowledged of this EventFrame1.
        :rtype: bool
        """
        return self._is_acknowledged

    @is_acknowledged.setter
    def is_acknowledged(self, is_acknowledged):
        """
        Sets the is_acknowledged of this EventFrame1.

        :param is_acknowledged: The is_acknowledged of this EventFrame1.
        :type: bool
        """

        self._is_acknowledged = is_acknowledged

    @property
    def is_annotated(self):
        """
        Gets the is_annotated of this EventFrame1.

        :return: The is_annotated of this EventFrame1.
        :rtype: bool
        """
        return self._is_annotated

    @is_annotated.setter
    def is_annotated(self, is_annotated):
        """
        Sets the is_annotated of this EventFrame1.

        :param is_annotated: The is_annotated of this EventFrame1.
        :type: bool
        """

        self._is_annotated = is_annotated

    @property
    def is_locked(self):
        """
        Gets the is_locked of this EventFrame1.

        :return: The is_locked of this EventFrame1.
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """
        Sets the is_locked of this EventFrame1.

        :param is_locked: The is_locked of this EventFrame1.
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def are_values_captured(self):
        """
        Gets the are_values_captured of this EventFrame1.

        :return: The are_values_captured of this EventFrame1.
        :rtype: bool
        """
        return self._are_values_captured

    @are_values_captured.setter
    def are_values_captured(self, are_values_captured):
        """
        Sets the are_values_captured of this EventFrame1.

        :param are_values_captured: The are_values_captured of this EventFrame1.
        :type: bool
        """

        self._are_values_captured = are_values_captured

    @property
    def ref_element_web_ids(self):
        """
        Gets the ref_element_web_ids of this EventFrame1.

        :return: The ref_element_web_ids of this EventFrame1.
        :rtype: list[str]
        """
        return self._ref_element_web_ids

    @ref_element_web_ids.setter
    def ref_element_web_ids(self, ref_element_web_ids):
        """
        Sets the ref_element_web_ids of this EventFrame1.

        :param ref_element_web_ids: The ref_element_web_ids of this EventFrame1.
        :type: list[str]
        """

        self._ref_element_web_ids = ref_element_web_ids

    @property
    def security(self):
        """
        Gets the security of this EventFrame1.

        :return: The security of this EventFrame1.
        :rtype: InlineResponse20018Security
        """
        return self._security

    @security.setter
    def security(self, security):
        """
        Sets the security of this EventFrame1.

        :param security: The security of this EventFrame1.
        :type: InlineResponse20018Security
        """

        self._security = security

    @property
    def links(self):
        """
        Gets the links of this EventFrame1.

        :return: The links of this EventFrame1.
        :rtype: InlineResponse20018Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this EventFrame1.

        :param links: The links of this EventFrame1.
        :type: InlineResponse20018Links
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
        if not isinstance(other, EventFrame1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
