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

from swagger_client.models.project_metadata import ProjectMetadata  # noqa: F401,E501


class ProjectReq(object):
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
        'project_name': 'str',
        'metadata': 'ProjectMetadata'
    }

    attribute_map = {
        'project_name': 'project_name',
        'metadata': 'metadata'
    }

    def __init__(self, project_name=None, metadata=None):  # noqa: E501
        """ProjectReq - a model defined in Swagger"""  # noqa: E501

        self._project_name = None
        self._metadata = None
        self.discriminator = None

        if project_name is not None:
            self.project_name = project_name
        if metadata is not None:
            self.metadata = metadata

    @property
    def project_name(self):
        """Gets the project_name of this ProjectReq.  # noqa: E501

        The name of the project.  # noqa: E501

        :return: The project_name of this ProjectReq.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ProjectReq.

        The name of the project.  # noqa: E501

        :param project_name: The project_name of this ProjectReq.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def metadata(self):
        """Gets the metadata of this ProjectReq.  # noqa: E501

        The metadata of the project.  # noqa: E501

        :return: The metadata of this ProjectReq.  # noqa: E501
        :rtype: ProjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ProjectReq.

        The metadata of the project.  # noqa: E501

        :param metadata: The metadata of this ProjectReq.  # noqa: E501
        :type: ProjectMetadata
        """

        self._metadata = metadata

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
        if issubclass(ProjectReq, dict):
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
        if not isinstance(other, ProjectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
