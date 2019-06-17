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


class RobotAccount(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'project_id': 'int',
        'disabled': 'bool',
        'creation_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'disabled': 'disabled',
        'creation_time': 'creation_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, disabled=None, creation_time=None, update_time=None):  # noqa: E501
        """RobotAccount - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._disabled = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if disabled is not None:
            self.disabled = disabled
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this RobotAccount.  # noqa: E501

        The id of robot account  # noqa: E501

        :return: The id of this RobotAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RobotAccount.

        The id of robot account  # noqa: E501

        :param id: The id of this RobotAccount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RobotAccount.  # noqa: E501

        The name of robot account  # noqa: E501

        :return: The name of this RobotAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RobotAccount.

        The name of robot account  # noqa: E501

        :param name: The name of this RobotAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RobotAccount.  # noqa: E501

        The description of robot account  # noqa: E501

        :return: The description of this RobotAccount.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RobotAccount.

        The description of robot account  # noqa: E501

        :param description: The description of this RobotAccount.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this RobotAccount.  # noqa: E501

        The project id of robot account  # noqa: E501

        :return: The project_id of this RobotAccount.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RobotAccount.

        The project id of robot account  # noqa: E501

        :param project_id: The project_id of this RobotAccount.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def disabled(self):
        """Gets the disabled of this RobotAccount.  # noqa: E501

        The robot account is disable or enable  # noqa: E501

        :return: The disabled of this RobotAccount.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this RobotAccount.

        The robot account is disable or enable  # noqa: E501

        :param disabled: The disabled of this RobotAccount.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def creation_time(self):
        """Gets the creation_time of this RobotAccount.  # noqa: E501

        The creation time of the robot account  # noqa: E501

        :return: The creation_time of this RobotAccount.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this RobotAccount.

        The creation time of the robot account  # noqa: E501

        :param creation_time: The creation_time of this RobotAccount.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this RobotAccount.  # noqa: E501

        The update time of the robot account  # noqa: E501

        :return: The update_time of this RobotAccount.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RobotAccount.

        The update time of the robot account  # noqa: E501

        :param update_time: The update_time of this RobotAccount.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(RobotAccount, dict):
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
        if not isinstance(other, RobotAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other