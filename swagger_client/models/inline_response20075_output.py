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

class InlineResponse20075Output(object):
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
        'drives': 'list[AutochangerDriveVolume]',
        'slots': 'list[AutochangerSlotVolume]',
        'ie_slots': 'list[AutochangerSlotVolume]'
    }

    attribute_map = {
        'drives': 'drives',
        'slots': 'slots',
        'ie_slots': 'ie_slots'
    }

    def __init__(self, drives=None, slots=None, ie_slots=None):  # noqa: E501
        """InlineResponse20075Output - a model defined in Swagger"""  # noqa: E501
        self._drives = None
        self._slots = None
        self._ie_slots = None
        self.discriminator = None
        if drives is not None:
            self.drives = drives
        if slots is not None:
            self.slots = slots
        if ie_slots is not None:
            self.ie_slots = ie_slots

    @property
    def drives(self):
        """Gets the drives of this InlineResponse20075Output.  # noqa: E501

        Tape drive list  # noqa: E501

        :return: The drives of this InlineResponse20075Output.  # noqa: E501
        :rtype: list[AutochangerDriveVolume]
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """Sets the drives of this InlineResponse20075Output.

        Tape drive list  # noqa: E501

        :param drives: The drives of this InlineResponse20075Output.  # noqa: E501
        :type: list[AutochangerDriveVolume]
        """

        self._drives = drives

    @property
    def slots(self):
        """Gets the slots of this InlineResponse20075Output.  # noqa: E501

        Regular slot list  # noqa: E501

        :return: The slots of this InlineResponse20075Output.  # noqa: E501
        :rtype: list[AutochangerSlotVolume]
        """
        return self._slots

    @slots.setter
    def slots(self, slots):
        """Sets the slots of this InlineResponse20075Output.

        Regular slot list  # noqa: E501

        :param slots: The slots of this InlineResponse20075Output.  # noqa: E501
        :type: list[AutochangerSlotVolume]
        """

        self._slots = slots

    @property
    def ie_slots(self):
        """Gets the ie_slots of this InlineResponse20075Output.  # noqa: E501

        Import/export slot list  # noqa: E501

        :return: The ie_slots of this InlineResponse20075Output.  # noqa: E501
        :rtype: list[AutochangerSlotVolume]
        """
        return self._ie_slots

    @ie_slots.setter
    def ie_slots(self, ie_slots):
        """Sets the ie_slots of this InlineResponse20075Output.

        Import/export slot list  # noqa: E501

        :param ie_slots: The ie_slots of this InlineResponse20075Output.  # noqa: E501
        :type: list[AutochangerSlotVolume]
        """

        self._ie_slots = ie_slots

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
        if issubclass(InlineResponse20075Output, dict):
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
        if not isinstance(other, InlineResponse20075Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
