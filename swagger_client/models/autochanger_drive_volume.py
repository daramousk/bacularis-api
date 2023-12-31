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

class AutochangerDriveVolume(object):
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
        'type': 'str',
        'index': 'int',
        'drive': 'str',
        'device': 'str',
        'slot_ach': 'int',
        'state': 'str',
        'mediaid': 'int',
        'volume': 'str',
        'mediatype': 'str',
        'pool': 'str',
        'lastwritten': 'str',
        'whenexpire': 'str',
        'volbytes': 'int',
        'volstatus': 'int',
        'slot_cat': 'int'
    }

    attribute_map = {
        'type': 'type',
        'index': 'index',
        'drive': 'drive',
        'device': 'device',
        'slot_ach': 'slot_ach',
        'state': 'state',
        'mediaid': 'mediaid',
        'volume': 'volume',
        'mediatype': 'mediatype',
        'pool': 'pool',
        'lastwritten': 'lastwritten',
        'whenexpire': 'whenexpire',
        'volbytes': 'volbytes',
        'volstatus': 'volstatus',
        'slot_cat': 'slot_cat'
    }

    def __init__(self, type=None, index=None, drive=None, device=None, slot_ach=None, state=None, mediaid=None, volume=None, mediatype=None, pool=None, lastwritten=None, whenexpire=None, volbytes=None, volstatus=None, slot_cat=None):  # noqa: E501
        """AutochangerDriveVolume - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._index = None
        self._drive = None
        self._device = None
        self._slot_ach = None
        self._state = None
        self._mediaid = None
        self._volume = None
        self._mediatype = None
        self._pool = None
        self._lastwritten = None
        self._whenexpire = None
        self._volbytes = None
        self._volstatus = None
        self._slot_cat = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if index is not None:
            self.index = index
        if drive is not None:
            self.drive = drive
        if device is not None:
            self.device = device
        if slot_ach is not None:
            self.slot_ach = slot_ach
        if state is not None:
            self.state = state
        if mediaid is not None:
            self.mediaid = mediaid
        if volume is not None:
            self.volume = volume
        if mediatype is not None:
            self.mediatype = mediatype
        if pool is not None:
            self.pool = pool
        if lastwritten is not None:
            self.lastwritten = lastwritten
        if whenexpire is not None:
            self.whenexpire = whenexpire
        if volbytes is not None:
            self.volbytes = volbytes
        if volstatus is not None:
            self.volstatus = volstatus
        if slot_cat is not None:
            self.slot_cat = slot_cat

    @property
    def type(self):
        """Gets the type of this AutochangerDriveVolume.  # noqa: E501

        Element type (slot, ie_slot or drive)  # noqa: E501

        :return: The type of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutochangerDriveVolume.

        Element type (slot, ie_slot or drive)  # noqa: E501

        :param type: The type of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def index(self):
        """Gets the index of this AutochangerDriveVolume.  # noqa: E501

        Drive index  # noqa: E501

        :return: The index of this AutochangerDriveVolume.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this AutochangerDriveVolume.

        Drive index  # noqa: E501

        :param index: The index of this AutochangerDriveVolume.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def drive(self):
        """Gets the drive of this AutochangerDriveVolume.  # noqa: E501

        Drive name  # noqa: E501

        :return: The drive of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._drive

    @drive.setter
    def drive(self, drive):
        """Sets the drive of this AutochangerDriveVolume.

        Drive name  # noqa: E501

        :param drive: The drive of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """

        self._drive = drive

    @property
    def device(self):
        """Gets the device of this AutochangerDriveVolume.  # noqa: E501

        Device path (ex. /dev/tape/by-id/scsi-XYZZY_48-nst)  # noqa: E501

        :return: The device of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this AutochangerDriveVolume.

        Device path (ex. /dev/tape/by-id/scsi-XYZZY_48-nst)  # noqa: E501

        :param device: The device of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def slot_ach(self):
        """Gets the slot_ach of this AutochangerDriveVolume.  # noqa: E501

        Slot in autochanger  # noqa: E501

        :return: The slot_ach of this AutochangerDriveVolume.  # noqa: E501
        :rtype: int
        """
        return self._slot_ach

    @slot_ach.setter
    def slot_ach(self, slot_ach):
        """Sets the slot_ach of this AutochangerDriveVolume.

        Slot in autochanger  # noqa: E501

        :param slot_ach: The slot_ach of this AutochangerDriveVolume.  # noqa: E501
        :type: int
        """

        self._slot_ach = slot_ach

    @property
    def state(self):
        """Gets the state of this AutochangerDriveVolume.  # noqa: E501

        Element state: E - empty, F - full  # noqa: E501

        :return: The state of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AutochangerDriveVolume.

        Element state: E - empty, F - full  # noqa: E501

        :param state: The state of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """
        allowed_values = ["E", "F"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def mediaid(self):
        """Gets the mediaid of this AutochangerDriveVolume.  # noqa: E501

        Media identifier  # noqa: E501

        :return: The mediaid of this AutochangerDriveVolume.  # noqa: E501
        :rtype: int
        """
        return self._mediaid

    @mediaid.setter
    def mediaid(self, mediaid):
        """Sets the mediaid of this AutochangerDriveVolume.

        Media identifier  # noqa: E501

        :param mediaid: The mediaid of this AutochangerDriveVolume.  # noqa: E501
        :type: int
        """

        self._mediaid = mediaid

    @property
    def volume(self):
        """Gets the volume of this AutochangerDriveVolume.  # noqa: E501

        Volume name  # noqa: E501

        :return: The volume of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this AutochangerDriveVolume.

        Volume name  # noqa: E501

        :param volume: The volume of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def mediatype(self):
        """Gets the mediatype of this AutochangerDriveVolume.  # noqa: E501

        Media type  # noqa: E501

        :return: The mediatype of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._mediatype

    @mediatype.setter
    def mediatype(self, mediatype):
        """Sets the mediatype of this AutochangerDriveVolume.

        Media type  # noqa: E501

        :param mediatype: The mediatype of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """

        self._mediatype = mediatype

    @property
    def pool(self):
        """Gets the pool of this AutochangerDriveVolume.  # noqa: E501

        Pool name  # noqa: E501

        :return: The pool of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this AutochangerDriveVolume.

        Pool name  # noqa: E501

        :param pool: The pool of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """

        self._pool = pool

    @property
    def lastwritten(self):
        """Gets the lastwritten of this AutochangerDriveVolume.  # noqa: E501

        Date and time last write to volume  # noqa: E501

        :return: The lastwritten of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._lastwritten

    @lastwritten.setter
    def lastwritten(self, lastwritten):
        """Sets the lastwritten of this AutochangerDriveVolume.

        Date and time last write to volume  # noqa: E501

        :param lastwritten: The lastwritten of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """

        self._lastwritten = lastwritten

    @property
    def whenexpire(self):
        """Gets the whenexpire of this AutochangerDriveVolume.  # noqa: E501

        Expiration date and time  # noqa: E501

        :return: The whenexpire of this AutochangerDriveVolume.  # noqa: E501
        :rtype: str
        """
        return self._whenexpire

    @whenexpire.setter
    def whenexpire(self, whenexpire):
        """Sets the whenexpire of this AutochangerDriveVolume.

        Expiration date and time  # noqa: E501

        :param whenexpire: The whenexpire of this AutochangerDriveVolume.  # noqa: E501
        :type: str
        """

        self._whenexpire = whenexpire

    @property
    def volbytes(self):
        """Gets the volbytes of this AutochangerDriveVolume.  # noqa: E501

        Number of bytes written on volume  # noqa: E501

        :return: The volbytes of this AutochangerDriveVolume.  # noqa: E501
        :rtype: int
        """
        return self._volbytes

    @volbytes.setter
    def volbytes(self, volbytes):
        """Sets the volbytes of this AutochangerDriveVolume.

        Number of bytes written on volume  # noqa: E501

        :param volbytes: The volbytes of this AutochangerDriveVolume.  # noqa: E501
        :type: int
        """

        self._volbytes = volbytes

    @property
    def volstatus(self):
        """Gets the volstatus of this AutochangerDriveVolume.  # noqa: E501

        Volume status  # noqa: E501

        :return: The volstatus of this AutochangerDriveVolume.  # noqa: E501
        :rtype: int
        """
        return self._volstatus

    @volstatus.setter
    def volstatus(self, volstatus):
        """Sets the volstatus of this AutochangerDriveVolume.

        Volume status  # noqa: E501

        :param volstatus: The volstatus of this AutochangerDriveVolume.  # noqa: E501
        :type: int
        """

        self._volstatus = volstatus

    @property
    def slot_cat(self):
        """Gets the slot_cat of this AutochangerDriveVolume.  # noqa: E501

        Slot in the Catalog database  # noqa: E501

        :return: The slot_cat of this AutochangerDriveVolume.  # noqa: E501
        :rtype: int
        """
        return self._slot_cat

    @slot_cat.setter
    def slot_cat(self, slot_cat):
        """Sets the slot_cat of this AutochangerDriveVolume.

        Slot in the Catalog database  # noqa: E501

        :param slot_cat: The slot_cat of this AutochangerDriveVolume.  # noqa: E501
        :type: int
        """

        self._slot_cat = slot_cat

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
        if issubclass(AutochangerDriveVolume, dict):
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
        if not isinstance(other, AutochangerDriveVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
