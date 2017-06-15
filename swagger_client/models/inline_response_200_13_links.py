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


class InlineResponse20013Links(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _self=None, attributes=None, element=None, event_frame=None, parent=None, template=None, interpolated_data=None, recorded_data=None, plot_data=None, summary_data=None, value=None, end_value=None, point=None, categories=None, enumeration_set=None, trait=None):
        """
        InlineResponse20013Links - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_self': 'str',
            'attributes': 'str',
            'element': 'str',
            'event_frame': 'str',
            'parent': 'str',
            'template': 'str',
            'interpolated_data': 'str',
            'recorded_data': 'str',
            'plot_data': 'str',
            'summary_data': 'str',
            'value': 'str',
            'end_value': 'str',
            'point': 'str',
            'categories': 'str',
            'enumeration_set': 'str',
            'trait': 'str'
        }

        self.attribute_map = {
            '_self': 'Self',
            'attributes': 'Attributes',
            'element': 'Element',
            'event_frame': 'EventFrame',
            'parent': 'Parent',
            'template': 'Template',
            'interpolated_data': 'InterpolatedData',
            'recorded_data': 'RecordedData',
            'plot_data': 'PlotData',
            'summary_data': 'SummaryData',
            'value': 'Value',
            'end_value': 'EndValue',
            'point': 'Point',
            'categories': 'Categories',
            'enumeration_set': 'EnumerationSet',
            'trait': 'Trait'
        }

        self.__self = _self
        self._attributes = attributes
        self._element = element
        self._event_frame = event_frame
        self._parent = parent
        self._template = template
        self._interpolated_data = interpolated_data
        self._recorded_data = recorded_data
        self._plot_data = plot_data
        self._summary_data = summary_data
        self._value = value
        self._end_value = end_value
        self._point = point
        self._categories = categories
        self._enumeration_set = enumeration_set
        self._trait = trait

    @property
    def _self(self):
        """
        Gets the _self of this InlineResponse20013Links.

        :return: The _self of this InlineResponse20013Links.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this InlineResponse20013Links.

        :param _self: The _self of this InlineResponse20013Links.
        :type: str
        """

        self.__self = _self

    @property
    def attributes(self):
        """
        Gets the attributes of this InlineResponse20013Links.

        :return: The attributes of this InlineResponse20013Links.
        :rtype: str
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this InlineResponse20013Links.

        :param attributes: The attributes of this InlineResponse20013Links.
        :type: str
        """

        self._attributes = attributes

    @property
    def element(self):
        """
        Gets the element of this InlineResponse20013Links.

        :return: The element of this InlineResponse20013Links.
        :rtype: str
        """
        return self._element

    @element.setter
    def element(self, element):
        """
        Sets the element of this InlineResponse20013Links.

        :param element: The element of this InlineResponse20013Links.
        :type: str
        """

        self._element = element

    @property
    def event_frame(self):
        """
        Gets the event_frame of this InlineResponse20013Links.

        :return: The event_frame of this InlineResponse20013Links.
        :rtype: str
        """
        return self._event_frame

    @event_frame.setter
    def event_frame(self, event_frame):
        """
        Sets the event_frame of this InlineResponse20013Links.

        :param event_frame: The event_frame of this InlineResponse20013Links.
        :type: str
        """

        self._event_frame = event_frame

    @property
    def parent(self):
        """
        Gets the parent of this InlineResponse20013Links.

        :return: The parent of this InlineResponse20013Links.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this InlineResponse20013Links.

        :param parent: The parent of this InlineResponse20013Links.
        :type: str
        """

        self._parent = parent

    @property
    def template(self):
        """
        Gets the template of this InlineResponse20013Links.

        :return: The template of this InlineResponse20013Links.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this InlineResponse20013Links.

        :param template: The template of this InlineResponse20013Links.
        :type: str
        """

        self._template = template

    @property
    def interpolated_data(self):
        """
        Gets the interpolated_data of this InlineResponse20013Links.

        :return: The interpolated_data of this InlineResponse20013Links.
        :rtype: str
        """
        return self._interpolated_data

    @interpolated_data.setter
    def interpolated_data(self, interpolated_data):
        """
        Sets the interpolated_data of this InlineResponse20013Links.

        :param interpolated_data: The interpolated_data of this InlineResponse20013Links.
        :type: str
        """

        self._interpolated_data = interpolated_data

    @property
    def recorded_data(self):
        """
        Gets the recorded_data of this InlineResponse20013Links.

        :return: The recorded_data of this InlineResponse20013Links.
        :rtype: str
        """
        return self._recorded_data

    @recorded_data.setter
    def recorded_data(self, recorded_data):
        """
        Sets the recorded_data of this InlineResponse20013Links.

        :param recorded_data: The recorded_data of this InlineResponse20013Links.
        :type: str
        """

        self._recorded_data = recorded_data

    @property
    def plot_data(self):
        """
        Gets the plot_data of this InlineResponse20013Links.

        :return: The plot_data of this InlineResponse20013Links.
        :rtype: str
        """
        return self._plot_data

    @plot_data.setter
    def plot_data(self, plot_data):
        """
        Sets the plot_data of this InlineResponse20013Links.

        :param plot_data: The plot_data of this InlineResponse20013Links.
        :type: str
        """

        self._plot_data = plot_data

    @property
    def summary_data(self):
        """
        Gets the summary_data of this InlineResponse20013Links.

        :return: The summary_data of this InlineResponse20013Links.
        :rtype: str
        """
        return self._summary_data

    @summary_data.setter
    def summary_data(self, summary_data):
        """
        Sets the summary_data of this InlineResponse20013Links.

        :param summary_data: The summary_data of this InlineResponse20013Links.
        :type: str
        """

        self._summary_data = summary_data

    @property
    def value(self):
        """
        Gets the value of this InlineResponse20013Links.

        :return: The value of this InlineResponse20013Links.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this InlineResponse20013Links.

        :param value: The value of this InlineResponse20013Links.
        :type: str
        """

        self._value = value

    @property
    def end_value(self):
        """
        Gets the end_value of this InlineResponse20013Links.

        :return: The end_value of this InlineResponse20013Links.
        :rtype: str
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value):
        """
        Sets the end_value of this InlineResponse20013Links.

        :param end_value: The end_value of this InlineResponse20013Links.
        :type: str
        """

        self._end_value = end_value

    @property
    def point(self):
        """
        Gets the point of this InlineResponse20013Links.

        :return: The point of this InlineResponse20013Links.
        :rtype: str
        """
        return self._point

    @point.setter
    def point(self, point):
        """
        Sets the point of this InlineResponse20013Links.

        :param point: The point of this InlineResponse20013Links.
        :type: str
        """

        self._point = point

    @property
    def categories(self):
        """
        Gets the categories of this InlineResponse20013Links.

        :return: The categories of this InlineResponse20013Links.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this InlineResponse20013Links.

        :param categories: The categories of this InlineResponse20013Links.
        :type: str
        """

        self._categories = categories

    @property
    def enumeration_set(self):
        """
        Gets the enumeration_set of this InlineResponse20013Links.

        :return: The enumeration_set of this InlineResponse20013Links.
        :rtype: str
        """
        return self._enumeration_set

    @enumeration_set.setter
    def enumeration_set(self, enumeration_set):
        """
        Sets the enumeration_set of this InlineResponse20013Links.

        :param enumeration_set: The enumeration_set of this InlineResponse20013Links.
        :type: str
        """

        self._enumeration_set = enumeration_set

    @property
    def trait(self):
        """
        Gets the trait of this InlineResponse20013Links.

        :return: The trait of this InlineResponse20013Links.
        :rtype: str
        """
        return self._trait

    @trait.setter
    def trait(self, trait):
        """
        Sets the trait of this InlineResponse20013Links.

        :param trait: The trait of this InlineResponse20013Links.
        :type: str
        """

        self._trait = trait

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
        if not isinstance(other, InlineResponse20013Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
