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


class ChartMetadata(object):
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
        'name': 'str',
        'home': 'str',
        'sources': 'list[str]',
        'version': 'str',
        'description': 'str',
        'keywords': 'list[str]',
        'engine': 'str',
        'icon': 'str',
        'api_version': 'str',
        'app_version': 'str',
        'deprecated': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'home': 'home',
        'sources': 'sources',
        'version': 'version',
        'description': 'description',
        'keywords': 'keywords',
        'engine': 'engine',
        'icon': 'icon',
        'api_version': 'apiVersion',
        'app_version': 'appVersion',
        'deprecated': 'deprecated'
    }

    def __init__(self, name=None, home=None, sources=None, version=None, description=None, keywords=None, engine=None, icon=None, api_version=None, app_version=None, deprecated=None):  # noqa: E501
        """ChartMetadata - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._home = None
        self._sources = None
        self._version = None
        self._description = None
        self._keywords = None
        self._engine = None
        self._icon = None
        self._api_version = None
        self._app_version = None
        self._deprecated = None
        self.discriminator = None

        self.name = name
        if home is not None:
            self.home = home
        if sources is not None:
            self.sources = sources
        self.version = version
        if description is not None:
            self.description = description
        if keywords is not None:
            self.keywords = keywords
        self.engine = engine
        self.icon = icon
        self.api_version = api_version
        self.app_version = app_version
        if deprecated is not None:
            self.deprecated = deprecated

    @property
    def name(self):
        """Gets the name of this ChartMetadata.  # noqa: E501

        The name of the chart  # noqa: E501

        :return: The name of this ChartMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChartMetadata.

        The name of the chart  # noqa: E501

        :param name: The name of this ChartMetadata.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def home(self):
        """Gets the home of this ChartMetadata.  # noqa: E501

        The URL to the relevant project page  # noqa: E501

        :return: The home of this ChartMetadata.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this ChartMetadata.

        The URL to the relevant project page  # noqa: E501

        :param home: The home of this ChartMetadata.  # noqa: E501
        :type: str
        """

        self._home = home

    @property
    def sources(self):
        """Gets the sources of this ChartMetadata.  # noqa: E501

        The URL to the source code of chart  # noqa: E501

        :return: The sources of this ChartMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this ChartMetadata.

        The URL to the source code of chart  # noqa: E501

        :param sources: The sources of this ChartMetadata.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    @property
    def version(self):
        """Gets the version of this ChartMetadata.  # noqa: E501

        A SemVer 2 version of chart  # noqa: E501

        :return: The version of this ChartMetadata.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChartMetadata.

        A SemVer 2 version of chart  # noqa: E501

        :param version: The version of this ChartMetadata.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def description(self):
        """Gets the description of this ChartMetadata.  # noqa: E501

        A one-sentence description of chart  # noqa: E501

        :return: The description of this ChartMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChartMetadata.

        A one-sentence description of chart  # noqa: E501

        :param description: The description of this ChartMetadata.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def keywords(self):
        """Gets the keywords of this ChartMetadata.  # noqa: E501

        A list of string keywords  # noqa: E501

        :return: The keywords of this ChartMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this ChartMetadata.

        A list of string keywords  # noqa: E501

        :param keywords: The keywords of this ChartMetadata.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def engine(self):
        """Gets the engine of this ChartMetadata.  # noqa: E501

        The name of template engine  # noqa: E501

        :return: The engine of this ChartMetadata.  # noqa: E501
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ChartMetadata.

        The name of template engine  # noqa: E501

        :param engine: The engine of this ChartMetadata.  # noqa: E501
        :type: str
        """
        if engine is None:
            raise ValueError("Invalid value for `engine`, must not be `None`")  # noqa: E501

        self._engine = engine

    @property
    def icon(self):
        """Gets the icon of this ChartMetadata.  # noqa: E501

        The URL to an icon file  # noqa: E501

        :return: The icon of this ChartMetadata.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ChartMetadata.

        The URL to an icon file  # noqa: E501

        :param icon: The icon of this ChartMetadata.  # noqa: E501
        :type: str
        """
        if icon is None:
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

    @property
    def api_version(self):
        """Gets the api_version of this ChartMetadata.  # noqa: E501

        The API version of this chart  # noqa: E501

        :return: The api_version of this ChartMetadata.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ChartMetadata.

        The API version of this chart  # noqa: E501

        :param api_version: The api_version of this ChartMetadata.  # noqa: E501
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def app_version(self):
        """Gets the app_version of this ChartMetadata.  # noqa: E501

        The version of the application enclosed in the chart  # noqa: E501

        :return: The app_version of this ChartMetadata.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this ChartMetadata.

        The version of the application enclosed in the chart  # noqa: E501

        :param app_version: The app_version of this ChartMetadata.  # noqa: E501
        :type: str
        """
        if app_version is None:
            raise ValueError("Invalid value for `app_version`, must not be `None`")  # noqa: E501

        self._app_version = app_version

    @property
    def deprecated(self):
        """Gets the deprecated of this ChartMetadata.  # noqa: E501

        Whether or not this chart is deprecated  # noqa: E501

        :return: The deprecated of this ChartMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this ChartMetadata.

        Whether or not this chart is deprecated  # noqa: E501

        :param deprecated: The deprecated of this ChartMetadata.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

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
        if issubclass(ChartMetadata, dict):
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
        if not isinstance(other, ChartMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
