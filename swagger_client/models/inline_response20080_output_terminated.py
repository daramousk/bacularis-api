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

class InlineResponse20080OutputTerminated(object):
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
        'level': 'str',
        'type': 'str',
        'status': 'str',
        'status_desc': 'str',
        'jobbytes': 'str',
        'jobfiles': 'str',
        'job': 'str',
        'starttime_epoch': 'str',
        'starttime': 'str',
        'endtime_epoch': 'str',
        'endtime': 'str',
        'errors': 'str'
    }

    attribute_map = {
        'level': 'level',
        'type': 'type',
        'status': 'status',
        'status_desc': 'status_desc',
        'jobbytes': 'jobbytes',
        'jobfiles': 'jobfiles',
        'job': 'job',
        'starttime_epoch': 'starttime_epoch',
        'starttime': 'starttime',
        'endtime_epoch': 'endtime_epoch',
        'endtime': 'endtime',
        'errors': 'errors'
    }

    def __init__(self, level=None, type=None, status=None, status_desc=None, jobbytes=None, jobfiles=None, job=None, starttime_epoch=None, starttime=None, endtime_epoch=None, endtime=None, errors=None):  # noqa: E501
        """InlineResponse20080OutputTerminated - a model defined in Swagger"""  # noqa: E501
        self._level = None
        self._type = None
        self._status = None
        self._status_desc = None
        self._jobbytes = None
        self._jobfiles = None
        self._job = None
        self._starttime_epoch = None
        self._starttime = None
        self._endtime_epoch = None
        self._endtime = None
        self._errors = None
        self.discriminator = None
        if level is not None:
            self.level = level
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if status_desc is not None:
            self.status_desc = status_desc
        if jobbytes is not None:
            self.jobbytes = jobbytes
        if jobfiles is not None:
            self.jobfiles = jobfiles
        if job is not None:
            self.job = job
        if starttime_epoch is not None:
            self.starttime_epoch = starttime_epoch
        if starttime is not None:
            self.starttime = starttime
        if endtime_epoch is not None:
            self.endtime_epoch = endtime_epoch
        if endtime is not None:
            self.endtime = endtime
        if errors is not None:
            self.errors = errors

    @property
    def level(self):
        """Gets the level of this InlineResponse20080OutputTerminated.  # noqa: E501

        Job level  # noqa: E501

        :return: The level of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this InlineResponse20080OutputTerminated.

        Job level  # noqa: E501

        :param level: The level of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def type(self):
        """Gets the type of this InlineResponse20080OutputTerminated.  # noqa: E501

        Job type  # noqa: E501

        :return: The type of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20080OutputTerminated.

        Job type  # noqa: E501

        :param type: The type of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this InlineResponse20080OutputTerminated.  # noqa: E501

        Job status letter  # noqa: E501

        :return: The status of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20080OutputTerminated.

        Job status letter  # noqa: E501

        :param status: The status of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_desc(self):
        """Gets the status_desc of this InlineResponse20080OutputTerminated.  # noqa: E501

        Status description  # noqa: E501

        :return: The status_desc of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this InlineResponse20080OutputTerminated.

        Status description  # noqa: E501

        :param status_desc: The status_desc of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._status_desc = status_desc

    @property
    def jobbytes(self):
        """Gets the jobbytes of this InlineResponse20080OutputTerminated.  # noqa: E501

        jobbytes  # noqa: E501

        :return: The jobbytes of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._jobbytes

    @jobbytes.setter
    def jobbytes(self, jobbytes):
        """Sets the jobbytes of this InlineResponse20080OutputTerminated.

        jobbytes  # noqa: E501

        :param jobbytes: The jobbytes of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._jobbytes = jobbytes

    @property
    def jobfiles(self):
        """Gets the jobfiles of this InlineResponse20080OutputTerminated.  # noqa: E501

        Job files  # noqa: E501

        :return: The jobfiles of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._jobfiles

    @jobfiles.setter
    def jobfiles(self, jobfiles):
        """Sets the jobfiles of this InlineResponse20080OutputTerminated.

        Job files  # noqa: E501

        :param jobfiles: The jobfiles of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._jobfiles = jobfiles

    @property
    def job(self):
        """Gets the job of this InlineResponse20080OutputTerminated.  # noqa: E501

        Job uname  # noqa: E501

        :return: The job of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this InlineResponse20080OutputTerminated.

        Job uname  # noqa: E501

        :param job: The job of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._job = job

    @property
    def starttime_epoch(self):
        """Gets the starttime_epoch of this InlineResponse20080OutputTerminated.  # noqa: E501

        Start time epoch  # noqa: E501

        :return: The starttime_epoch of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._starttime_epoch

    @starttime_epoch.setter
    def starttime_epoch(self, starttime_epoch):
        """Sets the starttime_epoch of this InlineResponse20080OutputTerminated.

        Start time epoch  # noqa: E501

        :param starttime_epoch: The starttime_epoch of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._starttime_epoch = starttime_epoch

    @property
    def starttime(self):
        """Gets the starttime of this InlineResponse20080OutputTerminated.  # noqa: E501

        Start time  # noqa: E501

        :return: The starttime of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this InlineResponse20080OutputTerminated.

        Start time  # noqa: E501

        :param starttime: The starttime of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._starttime = starttime

    @property
    def endtime_epoch(self):
        """Gets the endtime_epoch of this InlineResponse20080OutputTerminated.  # noqa: E501

        End time epoch  # noqa: E501

        :return: The endtime_epoch of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._endtime_epoch

    @endtime_epoch.setter
    def endtime_epoch(self, endtime_epoch):
        """Sets the endtime_epoch of this InlineResponse20080OutputTerminated.

        End time epoch  # noqa: E501

        :param endtime_epoch: The endtime_epoch of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._endtime_epoch = endtime_epoch

    @property
    def endtime(self):
        """Gets the endtime of this InlineResponse20080OutputTerminated.  # noqa: E501

        End time  # noqa: E501

        :return: The endtime of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime):
        """Sets the endtime of this InlineResponse20080OutputTerminated.

        End time  # noqa: E501

        :param endtime: The endtime of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._endtime = endtime

    @property
    def errors(self):
        """Gets the errors of this InlineResponse20080OutputTerminated.  # noqa: E501

        Errors  # noqa: E501

        :return: The errors of this InlineResponse20080OutputTerminated.  # noqa: E501
        :rtype: str
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponse20080OutputTerminated.

        Errors  # noqa: E501

        :param errors: The errors of this InlineResponse20080OutputTerminated.  # noqa: E501
        :type: str
        """

        self._errors = errors

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
        if issubclass(InlineResponse20080OutputTerminated, dict):
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
        if not isinstance(other, InlineResponse20080OutputTerminated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
