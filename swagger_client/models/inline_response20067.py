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

class InlineResponse20067(object):
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
        'output': 'object',
        'error': 'int'
    }

    attribute_map = {
        'output': 'output',
        'error': 'error'
    }

    def __init__(self, output=None, error=None):  # noqa: E501
        """InlineResponse20067 - a model defined in Swagger"""  # noqa: E501
        self._output = None
        self._error = None
        self.discriminator = None
        if output is not None:
            self.output = output
        if error is not None:
            self.error = error

    @property
    def output(self):
        """Gets the output of this InlineResponse20067.  # noqa: E501

        Set resources config error message  # noqa: E501

        :return: The output of this InlineResponse20067.  # noqa: E501
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this InlineResponse20067.

        Set resources config error message  # noqa: E501

        :param output: The output of this InlineResponse20067.  # noqa: E501
        :type: object
        """

        self._output = output

    @property
    def error(self):
        """Gets the error of this InlineResponse20067.  # noqa: E501

        Error code  # noqa: E501

        :return: The error of this InlineResponse20067.  # noqa: E501
        :rtype: int
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse20067.

        Error code  # noqa: E501

        :param error: The error of this InlineResponse20067.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 11, 80, 81, 82, 83, 84, 90, 91, 92, 93, 94, 1000]  # noqa: E501
        if error not in allowed_values:
            raise ValueError(
                "Invalid value for `error` ({0}), must be one of {1}"  # noqa: E501
                .format(error, allowed_values)
            )

        self._error = error

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
        if issubclass(InlineResponse20067, dict):
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
        if not isinstance(other, InlineResponse20067):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
