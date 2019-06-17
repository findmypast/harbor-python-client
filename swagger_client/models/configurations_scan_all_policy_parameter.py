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


class ConfigurationsScanAllPolicyParameter(object):
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
        'daily_time': 'int'
    }

    attribute_map = {
        'daily_time': 'daily_time'
    }

    def __init__(self, daily_time=None):  # noqa: E501
        """ConfigurationsScanAllPolicyParameter - a model defined in Swagger"""  # noqa: E501

        self._daily_time = None
        self.discriminator = None

        if daily_time is not None:
            self.daily_time = daily_time

    @property
    def daily_time(self):
        """Gets the daily_time of this ConfigurationsScanAllPolicyParameter.  # noqa: E501

        The offest in seconds of UTC 0 o'clock, only valid when the policy type is \"daily\"  # noqa: E501

        :return: The daily_time of this ConfigurationsScanAllPolicyParameter.  # noqa: E501
        :rtype: int
        """
        return self._daily_time

    @daily_time.setter
    def daily_time(self, daily_time):
        """Sets the daily_time of this ConfigurationsScanAllPolicyParameter.

        The offest in seconds of UTC 0 o'clock, only valid when the policy type is \"daily\"  # noqa: E501

        :param daily_time: The daily_time of this ConfigurationsScanAllPolicyParameter.  # noqa: E501
        :type: int
        """

        self._daily_time = daily_time

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
        if issubclass(ConfigurationsScanAllPolicyParameter, dict):
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
        if not isinstance(other, ConfigurationsScanAllPolicyParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
