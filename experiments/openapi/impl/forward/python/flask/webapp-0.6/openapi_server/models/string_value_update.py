from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.update_base import UpdateBase
from openapi_server import util

from openapi_server.models.update_base import UpdateBase  # noqa: E501

class StringValueUpdate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, path=None, value=None):  # noqa: E501
        """StringValueUpdate - a model defined in OpenAPI

        :param type: The type of this StringValueUpdate.  # noqa: E501
        :type type: str
        :param path: The path of this StringValueUpdate.  # noqa: E501
        :type path: str
        :param value: The value of this StringValueUpdate.  # noqa: E501
        :type value: str
        """
        self.openapi_types = {
            'type': str,
            'path': str,
            'value': str
        }

        self.attribute_map = {
            'type': 'type',
            'path': 'path',
            'value': 'value'
        }

        self._type = type
        self._path = path
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'StringValueUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StringValueUpdate of this StringValueUpdate.  # noqa: E501
        :rtype: StringValueUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this StringValueUpdate.


        :return: The type of this StringValueUpdate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this StringValueUpdate.


        :param type: The type of this StringValueUpdate.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def path(self) -> str:
        """Gets the path of this StringValueUpdate.

        The target path that the update applies to.   # noqa: E501

        :return: The path of this StringValueUpdate.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this StringValueUpdate.

        The target path that the update applies to.   # noqa: E501

        :param path: The path of this StringValueUpdate.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def value(self) -> str:
        """Gets the value of this StringValueUpdate.

        The string value to use.   # noqa: E501

        :return: The value of this StringValueUpdate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this StringValueUpdate.

        The string value to use.   # noqa: E501

        :param value: The value of this StringValueUpdate.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
