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


class InlineResponse2006Links(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _self=None, analysis_rules=None, analysis=None, analysis_template=None, parent=None, plug_in=None):
        """
        InlineResponse2006Links - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_self': 'str',
            'analysis_rules': 'str',
            'analysis': 'str',
            'analysis_template': 'str',
            'parent': 'str',
            'plug_in': 'str'
        }

        self.attribute_map = {
            '_self': 'Self',
            'analysis_rules': 'AnalysisRules',
            'analysis': 'Analysis',
            'analysis_template': 'AnalysisTemplate',
            'parent': 'Parent',
            'plug_in': 'PlugIn'
        }

        self.__self = _self
        self._analysis_rules = analysis_rules
        self._analysis = analysis
        self._analysis_template = analysis_template
        self._parent = parent
        self._plug_in = plug_in

    @property
    def _self(self):
        """
        Gets the _self of this InlineResponse2006Links.

        :return: The _self of this InlineResponse2006Links.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this InlineResponse2006Links.

        :param _self: The _self of this InlineResponse2006Links.
        :type: str
        """

        self.__self = _self

    @property
    def analysis_rules(self):
        """
        Gets the analysis_rules of this InlineResponse2006Links.

        :return: The analysis_rules of this InlineResponse2006Links.
        :rtype: str
        """
        return self._analysis_rules

    @analysis_rules.setter
    def analysis_rules(self, analysis_rules):
        """
        Sets the analysis_rules of this InlineResponse2006Links.

        :param analysis_rules: The analysis_rules of this InlineResponse2006Links.
        :type: str
        """

        self._analysis_rules = analysis_rules

    @property
    def analysis(self):
        """
        Gets the analysis of this InlineResponse2006Links.

        :return: The analysis of this InlineResponse2006Links.
        :rtype: str
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """
        Sets the analysis of this InlineResponse2006Links.

        :param analysis: The analysis of this InlineResponse2006Links.
        :type: str
        """

        self._analysis = analysis

    @property
    def analysis_template(self):
        """
        Gets the analysis_template of this InlineResponse2006Links.

        :return: The analysis_template of this InlineResponse2006Links.
        :rtype: str
        """
        return self._analysis_template

    @analysis_template.setter
    def analysis_template(self, analysis_template):
        """
        Sets the analysis_template of this InlineResponse2006Links.

        :param analysis_template: The analysis_template of this InlineResponse2006Links.
        :type: str
        """

        self._analysis_template = analysis_template

    @property
    def parent(self):
        """
        Gets the parent of this InlineResponse2006Links.

        :return: The parent of this InlineResponse2006Links.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this InlineResponse2006Links.

        :param parent: The parent of this InlineResponse2006Links.
        :type: str
        """

        self._parent = parent

    @property
    def plug_in(self):
        """
        Gets the plug_in of this InlineResponse2006Links.

        :return: The plug_in of this InlineResponse2006Links.
        :rtype: str
        """
        return self._plug_in

    @plug_in.setter
    def plug_in(self, plug_in):
        """
        Sets the plug_in of this InlineResponse2006Links.

        :param plug_in: The plug_in of this InlineResponse2006Links.
        :type: str
        """

        self._plug_in = plug_in

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
        if not isinstance(other, InlineResponse2006Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
