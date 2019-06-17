# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.component_overview_entry import ComponentOverviewEntry  # noqa: F401,E501


class DetailedTagScanOverviewComponents(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total': 'int',
        'summary': 'list[ComponentOverviewEntry]'
    }

    attribute_map = {
        'total': 'total',
        'summary': 'summary'
    }

    def __init__(self, total=None, summary=None):  # noqa: E501
        """DetailedTagScanOverviewComponents - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._summary = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if summary is not None:
            self.summary = summary

    @property
    def total(self):
        """Gets the total of this DetailedTagScanOverviewComponents.  # noqa: E501

        Total number of the components in this image.  # noqa: E501

        :return: The total of this DetailedTagScanOverviewComponents.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DetailedTagScanOverviewComponents.

        Total number of the components in this image.  # noqa: E501

        :param total: The total of this DetailedTagScanOverviewComponents.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def summary(self):
        """Gets the summary of this DetailedTagScanOverviewComponents.  # noqa: E501

        List of number of components of different severities.  # noqa: E501

        :return: The summary of this DetailedTagScanOverviewComponents.  # noqa: E501
        :rtype: list[ComponentOverviewEntry]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this DetailedTagScanOverviewComponents.

        List of number of components of different severities.  # noqa: E501

        :param summary: The summary of this DetailedTagScanOverviewComponents.  # noqa: E501
        :type: list[ComponentOverviewEntry]
        """

        self._summary = summary

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DetailedTagScanOverviewComponents, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DetailedTagScanOverviewComponents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
