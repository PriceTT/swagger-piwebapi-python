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


class UnitDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, abbreviation=None, description=None, path=None, factor=None, offset=None, reference_factor=None, reference_offset=None, reference_unit_abbreviation=None, links=None):
        """
        UnitDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'web_id': 'str',
            'id': 'str',
            'name': 'str',
            'abbreviation': 'str',
            'description': 'str',
            'path': 'str',
            'factor': 'float',
            'offset': 'float',
            'reference_factor': 'float',
            'reference_offset': 'float',
            'reference_unit_abbreviation': 'str',
            'links': 'InlineResponse20051Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'abbreviation': 'Abbreviation',
            'description': 'Description',
            'path': 'Path',
            'factor': 'Factor',
            'offset': 'Offset',
            'reference_factor': 'ReferenceFactor',
            'reference_offset': 'ReferenceOffset',
            'reference_unit_abbreviation': 'ReferenceUnitAbbreviation',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._abbreviation = abbreviation
        self._description = description
        self._path = path
        self._factor = factor
        self._offset = offset
        self._reference_factor = reference_factor
        self._reference_offset = reference_offset
        self._reference_unit_abbreviation = reference_unit_abbreviation
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this UnitDTO.

        :return: The web_id of this UnitDTO.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this UnitDTO.

        :param web_id: The web_id of this UnitDTO.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this UnitDTO.

        :return: The id of this UnitDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UnitDTO.

        :param id: The id of this UnitDTO.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UnitDTO.

        :return: The name of this UnitDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UnitDTO.

        :param name: The name of this UnitDTO.
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """
        Gets the abbreviation of this UnitDTO.

        :return: The abbreviation of this UnitDTO.
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """
        Sets the abbreviation of this UnitDTO.

        :param abbreviation: The abbreviation of this UnitDTO.
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def description(self):
        """
        Gets the description of this UnitDTO.

        :return: The description of this UnitDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UnitDTO.

        :param description: The description of this UnitDTO.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this UnitDTO.

        :return: The path of this UnitDTO.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this UnitDTO.

        :param path: The path of this UnitDTO.
        :type: str
        """

        self._path = path

    @property
    def factor(self):
        """
        Gets the factor of this UnitDTO.

        :return: The factor of this UnitDTO.
        :rtype: float
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """
        Sets the factor of this UnitDTO.

        :param factor: The factor of this UnitDTO.
        :type: float
        """

        self._factor = factor

    @property
    def offset(self):
        """
        Gets the offset of this UnitDTO.

        :return: The offset of this UnitDTO.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this UnitDTO.

        :param offset: The offset of this UnitDTO.
        :type: float
        """

        self._offset = offset

    @property
    def reference_factor(self):
        """
        Gets the reference_factor of this UnitDTO.

        :return: The reference_factor of this UnitDTO.
        :rtype: float
        """
        return self._reference_factor

    @reference_factor.setter
    def reference_factor(self, reference_factor):
        """
        Sets the reference_factor of this UnitDTO.

        :param reference_factor: The reference_factor of this UnitDTO.
        :type: float
        """

        self._reference_factor = reference_factor

    @property
    def reference_offset(self):
        """
        Gets the reference_offset of this UnitDTO.

        :return: The reference_offset of this UnitDTO.
        :rtype: float
        """
        return self._reference_offset

    @reference_offset.setter
    def reference_offset(self, reference_offset):
        """
        Sets the reference_offset of this UnitDTO.

        :param reference_offset: The reference_offset of this UnitDTO.
        :type: float
        """

        self._reference_offset = reference_offset

    @property
    def reference_unit_abbreviation(self):
        """
        Gets the reference_unit_abbreviation of this UnitDTO.

        :return: The reference_unit_abbreviation of this UnitDTO.
        :rtype: str
        """
        return self._reference_unit_abbreviation

    @reference_unit_abbreviation.setter
    def reference_unit_abbreviation(self, reference_unit_abbreviation):
        """
        Sets the reference_unit_abbreviation of this UnitDTO.

        :param reference_unit_abbreviation: The reference_unit_abbreviation of this UnitDTO.
        :type: str
        """

        self._reference_unit_abbreviation = reference_unit_abbreviation

    @property
    def links(self):
        """
        Gets the links of this UnitDTO.

        :return: The links of this UnitDTO.
        :rtype: InlineResponse20051Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this UnitDTO.

        :param links: The links of this UnitDTO.
        :type: InlineResponse20051Links
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
        if not isinstance(other, UnitDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
