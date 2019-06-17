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


class GCScheduleSchedule(object):
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
        'type': 'str',
        'weekday': 'int',
        'offtime': 'int'
    }

    attribute_map = {
        'type': 'type',
        'weekday': 'weekday',
        'offtime': 'offtime'
    }

    def __init__(self, type=None, weekday=None, offtime=None):  # noqa: E501
        """GCScheduleSchedule - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._weekday = None
        self._offtime = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if weekday is not None:
            self.weekday = weekday
        if offtime is not None:
            self.offtime = offtime

    @property
    def type(self):
        """Gets the type of this GCScheduleSchedule.  # noqa: E501

        The schedule type. The valid values are daily， weekly and None. 'None' means to cancel the schedule.  # noqa: E501

        :return: The type of this GCScheduleSchedule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GCScheduleSchedule.

        The schedule type. The valid values are daily， weekly and None. 'None' means to cancel the schedule.  # noqa: E501

        :param type: The type of this GCScheduleSchedule.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def weekday(self):
        """Gets the weekday of this GCScheduleSchedule.  # noqa: E501

        Optional, only used when the type is weekly. The valid values are 1-7.  # noqa: E501

        :return: The weekday of this GCScheduleSchedule.  # noqa: E501
        :rtype: int
        """
        return self._weekday

    @weekday.setter
    def weekday(self, weekday):
        """Sets the weekday of this GCScheduleSchedule.

        Optional, only used when the type is weekly. The valid values are 1-7.  # noqa: E501

        :param weekday: The weekday of this GCScheduleSchedule.  # noqa: E501
        :type: int
        """

        self._weekday = weekday

    @property
    def offtime(self):
        """Gets the offtime of this GCScheduleSchedule.  # noqa: E501

        The time offset with the UTC 00:00 in seconds.  # noqa: E501

        :return: The offtime of this GCScheduleSchedule.  # noqa: E501
        :rtype: int
        """
        return self._offtime

    @offtime.setter
    def offtime(self, offtime):
        """Sets the offtime of this GCScheduleSchedule.

        The time offset with the UTC 00:00 in seconds.  # noqa: E501

        :param offtime: The offtime of this GCScheduleSchedule.  # noqa: E501
        :type: int
        """

        self._offtime = offtime

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
        if issubclass(GCScheduleSchedule, dict):
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
        if not isinstance(other, GCScheduleSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
