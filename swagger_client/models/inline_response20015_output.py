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

class InlineResponse20015Output(object):
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
        'jobid': 'int',
        'name': 'str',
        'file': 'str',
        'starttime': 'str',
        'endtime': 'str',
        'type': 'str',
        'level': 'str',
        'jobstatus': 'str',
        'jobfiles': 'int',
        'jobbytes': 'int'
    }

    attribute_map = {
        'jobid': 'jobid',
        'name': 'name',
        'file': 'file',
        'starttime': 'starttime',
        'endtime': 'endtime',
        'type': 'type',
        'level': 'level',
        'jobstatus': 'jobstatus',
        'jobfiles': 'jobfiles',
        'jobbytes': 'jobbytes'
    }

    def __init__(self, jobid=None, name=None, file=None, starttime=None, endtime=None, type=None, level=None, jobstatus=None, jobfiles=None, jobbytes=None):  # noqa: E501
        """InlineResponse20015Output - a model defined in Swagger"""  # noqa: E501
        self._jobid = None
        self._name = None
        self._file = None
        self._starttime = None
        self._endtime = None
        self._type = None
        self._level = None
        self._jobstatus = None
        self._jobfiles = None
        self._jobbytes = None
        self.discriminator = None
        if jobid is not None:
            self.jobid = jobid
        if name is not None:
            self.name = name
        if file is not None:
            self.file = file
        if starttime is not None:
            self.starttime = starttime
        if endtime is not None:
            self.endtime = endtime
        if type is not None:
            self.type = type
        if level is not None:
            self.level = level
        if jobstatus is not None:
            self.jobstatus = jobstatus
        if jobfiles is not None:
            self.jobfiles = jobfiles
        if jobbytes is not None:
            self.jobbytes = jobbytes

    @property
    def jobid(self):
        """Gets the jobid of this InlineResponse20015Output.  # noqa: E501

        Job identifier  # noqa: E501

        :return: The jobid of this InlineResponse20015Output.  # noqa: E501
        :rtype: int
        """
        return self._jobid

    @jobid.setter
    def jobid(self, jobid):
        """Sets the jobid of this InlineResponse20015Output.

        Job identifier  # noqa: E501

        :param jobid: The jobid of this InlineResponse20015Output.  # noqa: E501
        :type: int
        """

        self._jobid = jobid

    @property
    def name(self):
        """Gets the name of this InlineResponse20015Output.  # noqa: E501

        Job name  # noqa: E501

        :return: The name of this InlineResponse20015Output.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20015Output.

        Job name  # noqa: E501

        :param name: The name of this InlineResponse20015Output.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file(self):
        """Gets the file of this InlineResponse20015Output.  # noqa: E501

        Filename with full path  # noqa: E501

        :return: The file of this InlineResponse20015Output.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InlineResponse20015Output.

        Filename with full path  # noqa: E501

        :param file: The file of this InlineResponse20015Output.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def starttime(self):
        """Gets the starttime of this InlineResponse20015Output.  # noqa: E501

        Job start time  # noqa: E501

        :return: The starttime of this InlineResponse20015Output.  # noqa: E501
        :rtype: str
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this InlineResponse20015Output.

        Job start time  # noqa: E501

        :param starttime: The starttime of this InlineResponse20015Output.  # noqa: E501
        :type: str
        """

        self._starttime = starttime

    @property
    def endtime(self):
        """Gets the endtime of this InlineResponse20015Output.  # noqa: E501

        Job end time  # noqa: E501

        :return: The endtime of this InlineResponse20015Output.  # noqa: E501
        :rtype: str
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime):
        """Sets the endtime of this InlineResponse20015Output.

        Job end time  # noqa: E501

        :param endtime: The endtime of this InlineResponse20015Output.  # noqa: E501
        :type: str
        """

        self._endtime = endtime

    @property
    def type(self):
        """Gets the type of this InlineResponse20015Output.  # noqa: E501

        Job type  # noqa: E501

        :return: The type of this InlineResponse20015Output.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20015Output.

        Job type  # noqa: E501

        :param type: The type of this InlineResponse20015Output.  # noqa: E501
        :type: str
        """
        allowed_values = ["B", "M", "V", "R", "I", "D", "A", "C", "c", "g"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def level(self):
        """Gets the level of this InlineResponse20015Output.  # noqa: E501

        Job level  # noqa: E501

        :return: The level of this InlineResponse20015Output.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this InlineResponse20015Output.

        Job level  # noqa: E501

        :param level: The level of this InlineResponse20015Output.  # noqa: E501
        :type: str
        """
        allowed_values = ["F", "I", "D"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                .format(level, allowed_values)
            )

        self._level = level

    @property
    def jobstatus(self):
        """Gets the jobstatus of this InlineResponse20015Output.  # noqa: E501

        Job status. Note, some statuses can be not visible outside (used internally by Bacula)  # noqa: E501

        :return: The jobstatus of this InlineResponse20015Output.  # noqa: E501
        :rtype: str
        """
        return self._jobstatus

    @jobstatus.setter
    def jobstatus(self, jobstatus):
        """Sets the jobstatus of this InlineResponse20015Output.

        Job status. Note, some statuses can be not visible outside (used internally by Bacula)  # noqa: E501

        :param jobstatus: The jobstatus of this InlineResponse20015Output.  # noqa: E501
        :type: str
        """
        allowed_values = ["C", "R", "B", "T", "W", "E", "e", "f", "D", "A", "I", "F", "S", "m", "M", "s", "j", "c", "d", "t", "p", "i", "a", "l", "L"]  # noqa: E501
        if jobstatus not in allowed_values:
            raise ValueError(
                "Invalid value for `jobstatus` ({0}), must be one of {1}"  # noqa: E501
                .format(jobstatus, allowed_values)
            )

        self._jobstatus = jobstatus

    @property
    def jobfiles(self):
        """Gets the jobfiles of this InlineResponse20015Output.  # noqa: E501

        Job files  # noqa: E501

        :return: The jobfiles of this InlineResponse20015Output.  # noqa: E501
        :rtype: int
        """
        return self._jobfiles

    @jobfiles.setter
    def jobfiles(self, jobfiles):
        """Sets the jobfiles of this InlineResponse20015Output.

        Job files  # noqa: E501

        :param jobfiles: The jobfiles of this InlineResponse20015Output.  # noqa: E501
        :type: int
        """

        self._jobfiles = jobfiles

    @property
    def jobbytes(self):
        """Gets the jobbytes of this InlineResponse20015Output.  # noqa: E501

        Job bytes  # noqa: E501

        :return: The jobbytes of this InlineResponse20015Output.  # noqa: E501
        :rtype: int
        """
        return self._jobbytes

    @jobbytes.setter
    def jobbytes(self, jobbytes):
        """Sets the jobbytes of this InlineResponse20015Output.

        Job bytes  # noqa: E501

        :param jobbytes: The jobbytes of this InlineResponse20015Output.  # noqa: E501
        :type: int
        """

        self._jobbytes = jobbytes

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
        if issubclass(InlineResponse20015Output, dict):
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
        if not isinstance(other, InlineResponse20015Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
