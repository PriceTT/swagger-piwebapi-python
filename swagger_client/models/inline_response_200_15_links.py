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


class InlineResponse20015Links(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _self=None, analyses=None, attributes=None, elements=None, database=None, parent=None, template=None, categories=None, default_attribute=None, event_frames=None, interpolated_data=None, recorded_data=None, plot_data=None, summary_data=None, value=None, end_value=None, security=None, security_entries=None):
        """
        InlineResponse20015Links - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_self': 'str',
            'analyses': 'str',
            'attributes': 'str',
            'elements': 'str',
            'database': 'str',
            'parent': 'str',
            'template': 'str',
            'categories': 'str',
            'default_attribute': 'str',
            'event_frames': 'str',
            'interpolated_data': 'str',
            'recorded_data': 'str',
            'plot_data': 'str',
            'summary_data': 'str',
            'value': 'str',
            'end_value': 'str',
            'security': 'str',
            'security_entries': 'str'
        }

        self.attribute_map = {
            '_self': 'Self',
            'analyses': 'Analyses',
            'attributes': 'Attributes',
            'elements': 'Elements',
            'database': 'Database',
            'parent': 'Parent',
            'template': 'Template',
            'categories': 'Categories',
            'default_attribute': 'DefaultAttribute',
            'event_frames': 'EventFrames',
            'interpolated_data': 'InterpolatedData',
            'recorded_data': 'RecordedData',
            'plot_data': 'PlotData',
            'summary_data': 'SummaryData',
            'value': 'Value',
            'end_value': 'EndValue',
            'security': 'Security',
            'security_entries': 'SecurityEntries'
        }

        self.__self = _self
        self._analyses = analyses
        self._attributes = attributes
        self._elements = elements
        self._database = database
        self._parent = parent
        self._template = template
        self._categories = categories
        self._default_attribute = default_attribute
        self._event_frames = event_frames
        self._interpolated_data = interpolated_data
        self._recorded_data = recorded_data
        self._plot_data = plot_data
        self._summary_data = summary_data
        self._value = value
        self._end_value = end_value
        self._security = security
        self._security_entries = security_entries

    @property
    def _self(self):
        """
        Gets the _self of this InlineResponse20015Links.

        :return: The _self of this InlineResponse20015Links.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this InlineResponse20015Links.

        :param _self: The _self of this InlineResponse20015Links.
        :type: str
        """

        self.__self = _self

    @property
    def analyses(self):
        """
        Gets the analyses of this InlineResponse20015Links.

        :return: The analyses of this InlineResponse20015Links.
        :rtype: str
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        """
        Sets the analyses of this InlineResponse20015Links.

        :param analyses: The analyses of this InlineResponse20015Links.
        :type: str
        """

        self._analyses = analyses

    @property
    def attributes(self):
        """
        Gets the attributes of this InlineResponse20015Links.

        :return: The attributes of this InlineResponse20015Links.
        :rtype: str
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this InlineResponse20015Links.

        :param attributes: The attributes of this InlineResponse20015Links.
        :type: str
        """

        self._attributes = attributes

    @property
    def elements(self):
        """
        Gets the elements of this InlineResponse20015Links.

        :return: The elements of this InlineResponse20015Links.
        :rtype: str
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """
        Sets the elements of this InlineResponse20015Links.

        :param elements: The elements of this InlineResponse20015Links.
        :type: str
        """

        self._elements = elements

    @property
    def database(self):
        """
        Gets the database of this InlineResponse20015Links.

        :return: The database of this InlineResponse20015Links.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this InlineResponse20015Links.

        :param database: The database of this InlineResponse20015Links.
        :type: str
        """

        self._database = database

    @property
    def parent(self):
        """
        Gets the parent of this InlineResponse20015Links.

        :return: The parent of this InlineResponse20015Links.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this InlineResponse20015Links.

        :param parent: The parent of this InlineResponse20015Links.
        :type: str
        """

        self._parent = parent

    @property
    def template(self):
        """
        Gets the template of this InlineResponse20015Links.

        :return: The template of this InlineResponse20015Links.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this InlineResponse20015Links.

        :param template: The template of this InlineResponse20015Links.
        :type: str
        """

        self._template = template

    @property
    def categories(self):
        """
        Gets the categories of this InlineResponse20015Links.

        :return: The categories of this InlineResponse20015Links.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this InlineResponse20015Links.

        :param categories: The categories of this InlineResponse20015Links.
        :type: str
        """

        self._categories = categories

    @property
    def default_attribute(self):
        """
        Gets the default_attribute of this InlineResponse20015Links.

        :return: The default_attribute of this InlineResponse20015Links.
        :rtype: str
        """
        return self._default_attribute

    @default_attribute.setter
    def default_attribute(self, default_attribute):
        """
        Sets the default_attribute of this InlineResponse20015Links.

        :param default_attribute: The default_attribute of this InlineResponse20015Links.
        :type: str
        """

        self._default_attribute = default_attribute

    @property
    def event_frames(self):
        """
        Gets the event_frames of this InlineResponse20015Links.

        :return: The event_frames of this InlineResponse20015Links.
        :rtype: str
        """
        return self._event_frames

    @event_frames.setter
    def event_frames(self, event_frames):
        """
        Sets the event_frames of this InlineResponse20015Links.

        :param event_frames: The event_frames of this InlineResponse20015Links.
        :type: str
        """

        self._event_frames = event_frames

    @property
    def interpolated_data(self):
        """
        Gets the interpolated_data of this InlineResponse20015Links.

        :return: The interpolated_data of this InlineResponse20015Links.
        :rtype: str
        """
        return self._interpolated_data

    @interpolated_data.setter
    def interpolated_data(self, interpolated_data):
        """
        Sets the interpolated_data of this InlineResponse20015Links.

        :param interpolated_data: The interpolated_data of this InlineResponse20015Links.
        :type: str
        """

        self._interpolated_data = interpolated_data

    @property
    def recorded_data(self):
        """
        Gets the recorded_data of this InlineResponse20015Links.

        :return: The recorded_data of this InlineResponse20015Links.
        :rtype: str
        """
        return self._recorded_data

    @recorded_data.setter
    def recorded_data(self, recorded_data):
        """
        Sets the recorded_data of this InlineResponse20015Links.

        :param recorded_data: The recorded_data of this InlineResponse20015Links.
        :type: str
        """

        self._recorded_data = recorded_data

    @property
    def plot_data(self):
        """
        Gets the plot_data of this InlineResponse20015Links.

        :return: The plot_data of this InlineResponse20015Links.
        :rtype: str
        """
        return self._plot_data

    @plot_data.setter
    def plot_data(self, plot_data):
        """
        Sets the plot_data of this InlineResponse20015Links.

        :param plot_data: The plot_data of this InlineResponse20015Links.
        :type: str
        """

        self._plot_data = plot_data

    @property
    def summary_data(self):
        """
        Gets the summary_data of this InlineResponse20015Links.

        :return: The summary_data of this InlineResponse20015Links.
        :rtype: str
        """
        return self._summary_data

    @summary_data.setter
    def summary_data(self, summary_data):
        """
        Sets the summary_data of this InlineResponse20015Links.

        :param summary_data: The summary_data of this InlineResponse20015Links.
        :type: str
        """

        self._summary_data = summary_data

    @property
    def value(self):
        """
        Gets the value of this InlineResponse20015Links.

        :return: The value of this InlineResponse20015Links.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this InlineResponse20015Links.

        :param value: The value of this InlineResponse20015Links.
        :type: str
        """

        self._value = value

    @property
    def end_value(self):
        """
        Gets the end_value of this InlineResponse20015Links.

        :return: The end_value of this InlineResponse20015Links.
        :rtype: str
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value):
        """
        Sets the end_value of this InlineResponse20015Links.

        :param end_value: The end_value of this InlineResponse20015Links.
        :type: str
        """

        self._end_value = end_value

    @property
    def security(self):
        """
        Gets the security of this InlineResponse20015Links.

        :return: The security of this InlineResponse20015Links.
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """
        Sets the security of this InlineResponse20015Links.

        :param security: The security of this InlineResponse20015Links.
        :type: str
        """

        self._security = security

    @property
    def security_entries(self):
        """
        Gets the security_entries of this InlineResponse20015Links.

        :return: The security_entries of this InlineResponse20015Links.
        :rtype: str
        """
        return self._security_entries

    @security_entries.setter
    def security_entries(self, security_entries):
        """
        Sets the security_entries of this InlineResponse20015Links.

        :param security_entries: The security_entries of this InlineResponse20015Links.
        :type: str
        """

        self._security_entries = security_entries

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
        if not isinstance(other, InlineResponse20015Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
