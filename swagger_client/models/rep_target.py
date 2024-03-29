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


class RepTarget(object):
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
        'endpoint': 'str',
        'name': 'str',
        'username': 'str',
        'password': 'str',
        'type': 'int',
        'insecure': 'bool',
        'creation_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'endpoint': 'endpoint',
        'name': 'name',
        'username': 'username',
        'password': 'password',
        'type': 'type',
        'insecure': 'insecure',
        'creation_time': 'creation_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, endpoint=None, name=None, username=None, password=None, type=None, insecure=None, creation_time=None, update_time=None):  # noqa: E501
        """RepTarget - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._endpoint = None
        self._name = None
        self._username = None
        self._password = None
        self._type = None
        self._insecure = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if endpoint is not None:
            self.endpoint = endpoint
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if type is not None:
            self.type = type
        if insecure is not None:
            self.insecure = insecure
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this RepTarget.  # noqa: E501

        The target ID.  # noqa: E501

        :return: The id of this RepTarget.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepTarget.

        The target ID.  # noqa: E501

        :param id: The id of this RepTarget.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def endpoint(self):
        """Gets the endpoint of this RepTarget.  # noqa: E501

        The target address URL string.  # noqa: E501

        :return: The endpoint of this RepTarget.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this RepTarget.

        The target address URL string.  # noqa: E501

        :param endpoint: The endpoint of this RepTarget.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def name(self):
        """Gets the name of this RepTarget.  # noqa: E501

        The target name.  # noqa: E501

        :return: The name of this RepTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepTarget.

        The target name.  # noqa: E501

        :param name: The name of this RepTarget.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def username(self):
        """Gets the username of this RepTarget.  # noqa: E501

        The target server username.  # noqa: E501

        :return: The username of this RepTarget.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RepTarget.

        The target server username.  # noqa: E501

        :param username: The username of this RepTarget.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this RepTarget.  # noqa: E501

        The target server password.  # noqa: E501

        :return: The password of this RepTarget.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RepTarget.

        The target server password.  # noqa: E501

        :param password: The password of this RepTarget.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def type(self):
        """Gets the type of this RepTarget.  # noqa: E501

        Reserved field.  # noqa: E501

        :return: The type of this RepTarget.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RepTarget.

        Reserved field.  # noqa: E501

        :param type: The type of this RepTarget.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def insecure(self):
        """Gets the insecure of this RepTarget.  # noqa: E501

        Whether or not the certificate will be verified when Harbor tries to access the server.  # noqa: E501

        :return: The insecure of this RepTarget.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this RepTarget.

        Whether or not the certificate will be verified when Harbor tries to access the server.  # noqa: E501

        :param insecure: The insecure of this RepTarget.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def creation_time(self):
        """Gets the creation_time of this RepTarget.  # noqa: E501

        The create time of the policy.  # noqa: E501

        :return: The creation_time of this RepTarget.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this RepTarget.

        The create time of the policy.  # noqa: E501

        :param creation_time: The creation_time of this RepTarget.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this RepTarget.  # noqa: E501

        The update time of the policy.  # noqa: E501

        :return: The update_time of this RepTarget.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RepTarget.

        The update time of the policy.  # noqa: E501

        :param update_time: The update_time of this RepTarget.  # noqa: E501
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
        if issubclass(RepTarget, dict):
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
        if not isinstance(other, RepTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
