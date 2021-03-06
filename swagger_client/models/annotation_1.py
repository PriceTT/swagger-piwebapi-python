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


class Annotation1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, description=None, value=None, creator=None, creation_date=None, modifier=None, modify_date=None, links=None):
        """
        Annotation1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'value': 'object',
            'creator': 'str',
            'creation_date': 'datetime',
            'modifier': 'str',
            'modify_date': 'datetime',
            'links': 'InlineResponse2003Links'
        }

        self.attribute_map = {
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'value': 'Value',
            'creator': 'Creator',
            'creation_date': 'CreationDate',
            'modifier': 'Modifier',
            'modify_date': 'ModifyDate',
            'links': 'Links'
        }

        self._id = id
        self._name = name
        self._description = description
        self._value = value
        self._creator = creator
        self._creation_date = creation_date
        self._modifier = modifier
        self._modify_date = modify_date
        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Annotation1.

        :return: The id of this Annotation1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Annotation1.

        :param id: The id of this Annotation1.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Annotation1.

        :return: The name of this Annotation1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Annotation1.

        :param name: The name of this Annotation1.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Annotation1.

        :return: The description of this Annotation1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Annotation1.

        :param description: The description of this Annotation1.
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """
        Gets the value of this Annotation1.

        :return: The value of this Annotation1.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Annotation1.

        :param value: The value of this Annotation1.
        :type: object
        """

        self._value = value

    @property
    def creator(self):
        """
        Gets the creator of this Annotation1.

        :return: The creator of this Annotation1.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this Annotation1.

        :param creator: The creator of this Annotation1.
        :type: str
        """

        self._creator = creator

    @property
    def creation_date(self):
        """
        Gets the creation_date of this Annotation1.

        :return: The creation_date of this Annotation1.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this Annotation1.

        :param creation_date: The creation_date of this Annotation1.
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modifier(self):
        """
        Gets the modifier of this Annotation1.

        :return: The modifier of this Annotation1.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """
        Sets the modifier of this Annotation1.

        :param modifier: The modifier of this Annotation1.
        :type: str
        """

        self._modifier = modifier

    @property
    def modify_date(self):
        """
        Gets the modify_date of this Annotation1.

        :return: The modify_date of this Annotation1.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this Annotation1.

        :param modify_date: The modify_date of this Annotation1.
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def links(self):
        """
        Gets the links of this Annotation1.

        :return: The links of this Annotation1.
        :rtype: InlineResponse2003Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Annotation1.

        :param links: The links of this Annotation1.
        :type: InlineResponse2003Links
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
        if not isinstance(other, Annotation1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
