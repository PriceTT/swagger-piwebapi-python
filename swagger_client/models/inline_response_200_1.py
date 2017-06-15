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


class InlineResponse2001(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, description=None, path=None, analysis_rule_plug_in_name=None, auto_created=None, category_names=None, group_id=None, has_notification=None, has_target=None, has_template=None, is_configured=None, is_time_rule_defined_by_template=None, maximum_queue_size=None, output_time=None, priority=None, publish_results=None, status=None, target_web_id=None, template_name=None, time_rule_plug_in_name=None, links=None):
        """
        InlineResponse2001 - a model defined in Swagger

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
            'analysis_rule_plug_in_name': 'str',
            'auto_created': 'bool',
            'category_names': 'list[str]',
            'group_id': 'int',
            'has_notification': 'bool',
            'has_target': 'bool',
            'has_template': 'bool',
            'is_configured': 'bool',
            'is_time_rule_defined_by_template': 'bool',
            'maximum_queue_size': 'int',
            'output_time': 'str',
            'priority': 'str',
            'publish_results': 'bool',
            'status': 'str',
            'target_web_id': 'str',
            'template_name': 'str',
            'time_rule_plug_in_name': 'str',
            'links': 'InlineResponse2001Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'path': 'Path',
            'analysis_rule_plug_in_name': 'AnalysisRulePlugInName',
            'auto_created': 'AutoCreated',
            'category_names': 'CategoryNames',
            'group_id': 'GroupId',
            'has_notification': 'HasNotification',
            'has_target': 'HasTarget',
            'has_template': 'HasTemplate',
            'is_configured': 'IsConfigured',
            'is_time_rule_defined_by_template': 'IsTimeRuleDefinedByTemplate',
            'maximum_queue_size': 'MaximumQueueSize',
            'output_time': 'OutputTime',
            'priority': 'Priority',
            'publish_results': 'PublishResults',
            'status': 'Status',
            'target_web_id': 'TargetWebId',
            'template_name': 'TemplateName',
            'time_rule_plug_in_name': 'TimeRulePlugInName',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._description = description
        self._path = path
        self._analysis_rule_plug_in_name = analysis_rule_plug_in_name
        self._auto_created = auto_created
        self._category_names = category_names
        self._group_id = group_id
        self._has_notification = has_notification
        self._has_target = has_target
        self._has_template = has_template
        self._is_configured = is_configured
        self._is_time_rule_defined_by_template = is_time_rule_defined_by_template
        self._maximum_queue_size = maximum_queue_size
        self._output_time = output_time
        self._priority = priority
        self._publish_results = publish_results
        self._status = status
        self._target_web_id = target_web_id
        self._template_name = template_name
        self._time_rule_plug_in_name = time_rule_plug_in_name
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this InlineResponse2001.

        :return: The web_id of this InlineResponse2001.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this InlineResponse2001.

        :param web_id: The web_id of this InlineResponse2001.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this InlineResponse2001.

        :return: The id of this InlineResponse2001.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse2001.

        :param id: The id of this InlineResponse2001.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this InlineResponse2001.

        :return: The name of this InlineResponse2001.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse2001.

        :param name: The name of this InlineResponse2001.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this InlineResponse2001.

        :return: The description of this InlineResponse2001.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this InlineResponse2001.

        :param description: The description of this InlineResponse2001.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this InlineResponse2001.

        :return: The path of this InlineResponse2001.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this InlineResponse2001.

        :param path: The path of this InlineResponse2001.
        :type: str
        """

        self._path = path

    @property
    def analysis_rule_plug_in_name(self):
        """
        Gets the analysis_rule_plug_in_name of this InlineResponse2001.

        :return: The analysis_rule_plug_in_name of this InlineResponse2001.
        :rtype: str
        """
        return self._analysis_rule_plug_in_name

    @analysis_rule_plug_in_name.setter
    def analysis_rule_plug_in_name(self, analysis_rule_plug_in_name):
        """
        Sets the analysis_rule_plug_in_name of this InlineResponse2001.

        :param analysis_rule_plug_in_name: The analysis_rule_plug_in_name of this InlineResponse2001.
        :type: str
        """

        self._analysis_rule_plug_in_name = analysis_rule_plug_in_name

    @property
    def auto_created(self):
        """
        Gets the auto_created of this InlineResponse2001.

        :return: The auto_created of this InlineResponse2001.
        :rtype: bool
        """
        return self._auto_created

    @auto_created.setter
    def auto_created(self, auto_created):
        """
        Sets the auto_created of this InlineResponse2001.

        :param auto_created: The auto_created of this InlineResponse2001.
        :type: bool
        """

        self._auto_created = auto_created

    @property
    def category_names(self):
        """
        Gets the category_names of this InlineResponse2001.

        :return: The category_names of this InlineResponse2001.
        :rtype: list[str]
        """
        return self._category_names

    @category_names.setter
    def category_names(self, category_names):
        """
        Sets the category_names of this InlineResponse2001.

        :param category_names: The category_names of this InlineResponse2001.
        :type: list[str]
        """

        self._category_names = category_names

    @property
    def group_id(self):
        """
        Gets the group_id of this InlineResponse2001.

        :return: The group_id of this InlineResponse2001.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this InlineResponse2001.

        :param group_id: The group_id of this InlineResponse2001.
        :type: int
        """

        self._group_id = group_id

    @property
    def has_notification(self):
        """
        Gets the has_notification of this InlineResponse2001.

        :return: The has_notification of this InlineResponse2001.
        :rtype: bool
        """
        return self._has_notification

    @has_notification.setter
    def has_notification(self, has_notification):
        """
        Sets the has_notification of this InlineResponse2001.

        :param has_notification: The has_notification of this InlineResponse2001.
        :type: bool
        """

        self._has_notification = has_notification

    @property
    def has_target(self):
        """
        Gets the has_target of this InlineResponse2001.

        :return: The has_target of this InlineResponse2001.
        :rtype: bool
        """
        return self._has_target

    @has_target.setter
    def has_target(self, has_target):
        """
        Sets the has_target of this InlineResponse2001.

        :param has_target: The has_target of this InlineResponse2001.
        :type: bool
        """

        self._has_target = has_target

    @property
    def has_template(self):
        """
        Gets the has_template of this InlineResponse2001.

        :return: The has_template of this InlineResponse2001.
        :rtype: bool
        """
        return self._has_template

    @has_template.setter
    def has_template(self, has_template):
        """
        Sets the has_template of this InlineResponse2001.

        :param has_template: The has_template of this InlineResponse2001.
        :type: bool
        """

        self._has_template = has_template

    @property
    def is_configured(self):
        """
        Gets the is_configured of this InlineResponse2001.

        :return: The is_configured of this InlineResponse2001.
        :rtype: bool
        """
        return self._is_configured

    @is_configured.setter
    def is_configured(self, is_configured):
        """
        Sets the is_configured of this InlineResponse2001.

        :param is_configured: The is_configured of this InlineResponse2001.
        :type: bool
        """

        self._is_configured = is_configured

    @property
    def is_time_rule_defined_by_template(self):
        """
        Gets the is_time_rule_defined_by_template of this InlineResponse2001.

        :return: The is_time_rule_defined_by_template of this InlineResponse2001.
        :rtype: bool
        """
        return self._is_time_rule_defined_by_template

    @is_time_rule_defined_by_template.setter
    def is_time_rule_defined_by_template(self, is_time_rule_defined_by_template):
        """
        Sets the is_time_rule_defined_by_template of this InlineResponse2001.

        :param is_time_rule_defined_by_template: The is_time_rule_defined_by_template of this InlineResponse2001.
        :type: bool
        """

        self._is_time_rule_defined_by_template = is_time_rule_defined_by_template

    @property
    def maximum_queue_size(self):
        """
        Gets the maximum_queue_size of this InlineResponse2001.

        :return: The maximum_queue_size of this InlineResponse2001.
        :rtype: int
        """
        return self._maximum_queue_size

    @maximum_queue_size.setter
    def maximum_queue_size(self, maximum_queue_size):
        """
        Sets the maximum_queue_size of this InlineResponse2001.

        :param maximum_queue_size: The maximum_queue_size of this InlineResponse2001.
        :type: int
        """

        self._maximum_queue_size = maximum_queue_size

    @property
    def output_time(self):
        """
        Gets the output_time of this InlineResponse2001.

        :return: The output_time of this InlineResponse2001.
        :rtype: str
        """
        return self._output_time

    @output_time.setter
    def output_time(self, output_time):
        """
        Sets the output_time of this InlineResponse2001.

        :param output_time: The output_time of this InlineResponse2001.
        :type: str
        """

        self._output_time = output_time

    @property
    def priority(self):
        """
        Gets the priority of this InlineResponse2001.

        :return: The priority of this InlineResponse2001.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this InlineResponse2001.

        :param priority: The priority of this InlineResponse2001.
        :type: str
        """

        self._priority = priority

    @property
    def publish_results(self):
        """
        Gets the publish_results of this InlineResponse2001.

        :return: The publish_results of this InlineResponse2001.
        :rtype: bool
        """
        return self._publish_results

    @publish_results.setter
    def publish_results(self, publish_results):
        """
        Sets the publish_results of this InlineResponse2001.

        :param publish_results: The publish_results of this InlineResponse2001.
        :type: bool
        """

        self._publish_results = publish_results

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2001.

        :return: The status of this InlineResponse2001.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2001.

        :param status: The status of this InlineResponse2001.
        :type: str
        """

        self._status = status

    @property
    def target_web_id(self):
        """
        Gets the target_web_id of this InlineResponse2001.

        :return: The target_web_id of this InlineResponse2001.
        :rtype: str
        """
        return self._target_web_id

    @target_web_id.setter
    def target_web_id(self, target_web_id):
        """
        Sets the target_web_id of this InlineResponse2001.

        :param target_web_id: The target_web_id of this InlineResponse2001.
        :type: str
        """

        self._target_web_id = target_web_id

    @property
    def template_name(self):
        """
        Gets the template_name of this InlineResponse2001.

        :return: The template_name of this InlineResponse2001.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """
        Sets the template_name of this InlineResponse2001.

        :param template_name: The template_name of this InlineResponse2001.
        :type: str
        """

        self._template_name = template_name

    @property
    def time_rule_plug_in_name(self):
        """
        Gets the time_rule_plug_in_name of this InlineResponse2001.

        :return: The time_rule_plug_in_name of this InlineResponse2001.
        :rtype: str
        """
        return self._time_rule_plug_in_name

    @time_rule_plug_in_name.setter
    def time_rule_plug_in_name(self, time_rule_plug_in_name):
        """
        Sets the time_rule_plug_in_name of this InlineResponse2001.

        :param time_rule_plug_in_name: The time_rule_plug_in_name of this InlineResponse2001.
        :type: str
        """

        self._time_rule_plug_in_name = time_rule_plug_in_name

    @property
    def links(self):
        """
        Gets the links of this InlineResponse2001.

        :return: The links of this InlineResponse2001.
        :rtype: InlineResponse2001Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse2001.

        :param links: The links of this InlineResponse2001.
        :type: InlineResponse2001Links
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
