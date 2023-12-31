# coding: utf-8

"""
    Bacularis API

    This is the Bacularis API documentation.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: marcin.haba@bacula.pl
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Client(object):
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
        'clientid': 'int',
        'name': 'str',
        'uname': 'str',
        'autoprune': 'int',
        'fileretention': 'int',
        'jobretention': 'int'
    }

    attribute_map = {
        'clientid': 'clientid',
        'name': 'name',
        'uname': 'uname',
        'autoprune': 'autoprune',
        'fileretention': 'fileretention',
        'jobretention': 'jobretention'
    }

    def __init__(self, clientid=None, name=None, uname=None, autoprune=None, fileretention=None, jobretention=None):  # noqa: E501
        """Client - a model defined in Swagger"""  # noqa: E501
        self._clientid = None
        self._name = None
        self._uname = None
        self._autoprune = None
        self._fileretention = None
        self._jobretention = None
        self.discriminator = None
        if clientid is not None:
            self.clientid = clientid
        if name is not None:
            self.name = name
        if uname is not None:
            self.uname = uname
        if autoprune is not None:
            self.autoprune = autoprune
        if fileretention is not None:
            self.fileretention = fileretention
        if jobretention is not None:
            self.jobretention = jobretention

    @property
    def clientid(self):
        """Gets the clientid of this Client.  # noqa: E501

        Unique client identifier  # noqa: E501

        :return: The clientid of this Client.  # noqa: E501
        :rtype: int
        """
        return self._clientid

    @clientid.setter
    def clientid(self, clientid):
        """Sets the clientid of this Client.

        Unique client identifier  # noqa: E501

        :param clientid: The clientid of this Client.  # noqa: E501
        :type: int
        """

        self._clientid = clientid

    @property
    def name(self):
        """Gets the name of this Client.  # noqa: E501

        Client name  # noqa: E501

        :return: The name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Client.

        Client name  # noqa: E501

        :param name: The name of this Client.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uname(self):
        """Gets the uname of this Client.  # noqa: E501

        Uname for client  # noqa: E501

        :return: The uname of this Client.  # noqa: E501
        :rtype: str
        """
        return self._uname

    @uname.setter
    def uname(self, uname):
        """Sets the uname of this Client.

        Uname for client  # noqa: E501

        :param uname: The uname of this Client.  # noqa: E501
        :type: str
        """

        self._uname = uname

    @property
    def autoprune(self):
        """Gets the autoprune of this Client.  # noqa: E501

        Determines if automatic prunning is enabled/disabled  # noqa: E501

        :return: The autoprune of this Client.  # noqa: E501
        :rtype: int
        """
        return self._autoprune

    @autoprune.setter
    def autoprune(self, autoprune):
        """Sets the autoprune of this Client.

        Determines if automatic prunning is enabled/disabled  # noqa: E501

        :param autoprune: The autoprune of this Client.  # noqa: E501
        :type: int
        """

        self._autoprune = autoprune

    @property
    def fileretention(self):
        """Gets the fileretention of this Client.  # noqa: E501

        Retention time (in seconds) for files  # noqa: E501

        :return: The fileretention of this Client.  # noqa: E501
        :rtype: int
        """
        return self._fileretention

    @fileretention.setter
    def fileretention(self, fileretention):
        """Sets the fileretention of this Client.

        Retention time (in seconds) for files  # noqa: E501

        :param fileretention: The fileretention of this Client.  # noqa: E501
        :type: int
        """

        self._fileretention = fileretention

    @property
    def jobretention(self):
        """Gets the jobretention of this Client.  # noqa: E501

        Retention time (in seconds) for jobs  # noqa: E501

        :return: The jobretention of this Client.  # noqa: E501
        :rtype: int
        """
        return self._jobretention

    @jobretention.setter
    def jobretention(self, jobretention):
        """Sets the jobretention of this Client.

        Retention time (in seconds) for jobs  # noqa: E501

        :param jobretention: The jobretention of this Client.  # noqa: E501
        :type: int
        """

        self._jobretention = jobretention

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
        if issubclass(Client, dict):
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
        if not isinstance(other, Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
