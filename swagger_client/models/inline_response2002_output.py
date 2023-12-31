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

class InlineResponse2002Output(object):
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
        'enabled': 'str',
        'address': 'str',
        'fdport': 'str',
        'maxjobs': 'str',
        'numjobs': 'str',
        'jobretention': 'str',
        'fileretention': 'str',
        'autoprune': 'str',
        'dbport': 'str',
        'db_name': 'str',
        'db_driver': 'str',
        'db_user': 'str',
        'multidbconn': 'str'
    }

    attribute_map = {
        'name': 'name',
        'enabled': 'enabled',
        'address': 'address',
        'fdport': 'fdport',
        'maxjobs': 'maxjobs',
        'numjobs': 'numjobs',
        'jobretention': 'jobretention',
        'fileretention': 'fileretention',
        'autoprune': 'autoprune',
        'dbport': 'dbport',
        'db_name': 'db_name',
        'db_driver': 'db_driver',
        'db_user': 'db_user',
        'multidbconn': 'multidbconn'
    }

    def __init__(self, name=None, enabled=None, address=None, fdport=None, maxjobs=None, numjobs=None, jobretention=None, fileretention=None, autoprune=None, dbport=None, db_name=None, db_driver=None, db_user=None, multidbconn=None):  # noqa: E501
        """InlineResponse2002Output - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._enabled = None
        self._address = None
        self._fdport = None
        self._maxjobs = None
        self._numjobs = None
        self._jobretention = None
        self._fileretention = None
        self._autoprune = None
        self._dbport = None
        self._db_name = None
        self._db_driver = None
        self._db_user = None
        self._multidbconn = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if address is not None:
            self.address = address
        if fdport is not None:
            self.fdport = fdport
        if maxjobs is not None:
            self.maxjobs = maxjobs
        if numjobs is not None:
            self.numjobs = numjobs
        if jobretention is not None:
            self.jobretention = jobretention
        if fileretention is not None:
            self.fileretention = fileretention
        if autoprune is not None:
            self.autoprune = autoprune
        if dbport is not None:
            self.dbport = dbport
        if db_name is not None:
            self.db_name = db_name
        if db_driver is not None:
            self.db_driver = db_driver
        if db_user is not None:
            self.db_user = db_user
        if multidbconn is not None:
            self.multidbconn = multidbconn

    @property
    def name(self):
        """Gets the name of this InlineResponse2002Output.  # noqa: E501

        Client name  # noqa: E501

        :return: The name of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2002Output.

        Client name  # noqa: E501

        :param name: The name of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this InlineResponse2002Output.  # noqa: E501

        Enabled state  # noqa: E501

        :return: The enabled of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InlineResponse2002Output.

        Enabled state  # noqa: E501

        :param enabled: The enabled of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def address(self):
        """Gets the address of this InlineResponse2002Output.  # noqa: E501

        File Daemon address  # noqa: E501

        :return: The address of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InlineResponse2002Output.

        File Daemon address  # noqa: E501

        :param address: The address of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def fdport(self):
        """Gets the fdport of this InlineResponse2002Output.  # noqa: E501

        File Daemon port  # noqa: E501

        :return: The fdport of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._fdport

    @fdport.setter
    def fdport(self, fdport):
        """Sets the fdport of this InlineResponse2002Output.

        File Daemon port  # noqa: E501

        :param fdport: The fdport of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._fdport = fdport

    @property
    def maxjobs(self):
        """Gets the maxjobs of this InlineResponse2002Output.  # noqa: E501

        Maximum Concurrent Jobs value for client  # noqa: E501

        :return: The maxjobs of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._maxjobs

    @maxjobs.setter
    def maxjobs(self, maxjobs):
        """Sets the maxjobs of this InlineResponse2002Output.

        Maximum Concurrent Jobs value for client  # noqa: E501

        :param maxjobs: The maxjobs of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._maxjobs = maxjobs

    @property
    def numjobs(self):
        """Gets the numjobs of this InlineResponse2002Output.  # noqa: E501

        Number jobs run on client  # noqa: E501

        :return: The numjobs of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._numjobs

    @numjobs.setter
    def numjobs(self, numjobs):
        """Sets the numjobs of this InlineResponse2002Output.

        Number jobs run on client  # noqa: E501

        :param numjobs: The numjobs of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._numjobs = numjobs

    @property
    def jobretention(self):
        """Gets the jobretention of this InlineResponse2002Output.  # noqa: E501

        Job retention time  # noqa: E501

        :return: The jobretention of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._jobretention

    @jobretention.setter
    def jobretention(self, jobretention):
        """Sets the jobretention of this InlineResponse2002Output.

        Job retention time  # noqa: E501

        :param jobretention: The jobretention of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._jobretention = jobretention

    @property
    def fileretention(self):
        """Gets the fileretention of this InlineResponse2002Output.  # noqa: E501

        File retention time  # noqa: E501

        :return: The fileretention of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._fileretention

    @fileretention.setter
    def fileretention(self, fileretention):
        """Sets the fileretention of this InlineResponse2002Output.

        File retention time  # noqa: E501

        :param fileretention: The fileretention of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._fileretention = fileretention

    @property
    def autoprune(self):
        """Gets the autoprune of this InlineResponse2002Output.  # noqa: E501

        AutoPrune state  # noqa: E501

        :return: The autoprune of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._autoprune

    @autoprune.setter
    def autoprune(self, autoprune):
        """Sets the autoprune of this InlineResponse2002Output.

        AutoPrune state  # noqa: E501

        :param autoprune: The autoprune of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._autoprune = autoprune

    @property
    def dbport(self):
        """Gets the dbport of this InlineResponse2002Output.  # noqa: E501

        Database port  # noqa: E501

        :return: The dbport of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._dbport

    @dbport.setter
    def dbport(self, dbport):
        """Sets the dbport of this InlineResponse2002Output.

        Database port  # noqa: E501

        :param dbport: The dbport of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._dbport = dbport

    @property
    def db_name(self):
        """Gets the db_name of this InlineResponse2002Output.  # noqa: E501

        Database name  # noqa: E501

        :return: The db_name of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this InlineResponse2002Output.

        Database name  # noqa: E501

        :param db_name: The db_name of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def db_driver(self):
        """Gets the db_driver of this InlineResponse2002Output.  # noqa: E501

        Database driver  # noqa: E501

        :return: The db_driver of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._db_driver

    @db_driver.setter
    def db_driver(self, db_driver):
        """Sets the db_driver of this InlineResponse2002Output.

        Database driver  # noqa: E501

        :param db_driver: The db_driver of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._db_driver = db_driver

    @property
    def db_user(self):
        """Gets the db_user of this InlineResponse2002Output.  # noqa: E501

        Database user  # noqa: E501

        :return: The db_user of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this InlineResponse2002Output.

        Database user  # noqa: E501

        :param db_user: The db_user of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._db_user = db_user

    @property
    def multidbconn(self):
        """Gets the multidbconn of this InlineResponse2002Output.  # noqa: E501

        Multiple database connection  # noqa: E501

        :return: The multidbconn of this InlineResponse2002Output.  # noqa: E501
        :rtype: str
        """
        return self._multidbconn

    @multidbconn.setter
    def multidbconn(self, multidbconn):
        """Sets the multidbconn of this InlineResponse2002Output.

        Multiple database connection  # noqa: E501

        :param multidbconn: The multidbconn of this InlineResponse2002Output.  # noqa: E501
        :type: str
        """

        self._multidbconn = multidbconn

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
        if issubclass(InlineResponse2002Output, dict):
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
        if not isinstance(other, InlineResponse2002Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
