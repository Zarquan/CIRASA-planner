from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.option_base import OptionBase
from openapi_server import util

from openapi_server.models.option_base import OptionBase  # noqa: E501

class IntegerValueOption(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, path=None, min=None, max=None, units=None):  # noqa: E501
        """IntegerValueOption - a model defined in OpenAPI

        :param type: The type of this IntegerValueOption.  # noqa: E501
        :type type: str
        :param path: The path of this IntegerValueOption.  # noqa: E501
        :type path: str
        :param min: The min of this IntegerValueOption.  # noqa: E501
        :type min: int
        :param max: The max of this IntegerValueOption.  # noqa: E501
        :type max: int
        :param units: The units of this IntegerValueOption.  # noqa: E501
        :type units: str
        """
        self.openapi_types = {
            'type': str,
            'path': str,
            'min': int,
            'max': int,
            'units': str
        }

        self.attribute_map = {
            'type': 'type',
            'path': 'path',
            'min': 'min',
            'max': 'max',
            'units': 'units'
        }

        self._type = type
        self._path = path
        self._min = min
        self._max = max
        self._units = units

    @classmethod
    def from_dict(cls, dikt) -> 'IntegerValueOption':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IntegerValueOption of this IntegerValueOption.  # noqa: E501
        :rtype: IntegerValueOption
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this IntegerValueOption.


        :return: The type of this IntegerValueOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this IntegerValueOption.


        :param type: The type of this IntegerValueOption.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def path(self) -> str:
        """Gets the path of this IntegerValueOption.

        The target path that the option applies to.   # noqa: E501

        :return: The path of this IntegerValueOption.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this IntegerValueOption.

        The target path that the option applies to.   # noqa: E501

        :param path: The path of this IntegerValueOption.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def min(self) -> int:
        """Gets the min of this IntegerValueOption.

        The minimum value that can be set.   # noqa: E501

        :return: The min of this IntegerValueOption.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min: int):
        """Sets the min of this IntegerValueOption.

        The minimum value that can be set.   # noqa: E501

        :param min: The min of this IntegerValueOption.
        :type min: int
        """

        self._min = min

    @property
    def max(self) -> int:
        """Gets the max of this IntegerValueOption.

        The maximum value that can be set.   # noqa: E501

        :return: The max of this IntegerValueOption.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max: int):
        """Sets the max of this IntegerValueOption.

        The maximum value that can be set.   # noqa: E501

        :param max: The max of this IntegerValueOption.
        :type max: int
        """

        self._max = max

    @property
    def units(self) -> str:
        """Gets the units of this IntegerValueOption.

        The units used for the maximum and minimum values and the default units used for the update. The client may specify different units in the update if they need to.   # noqa: E501

        :return: The units of this IntegerValueOption.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units: str):
        """Sets the units of this IntegerValueOption.

        The units used for the maximum and minimum values and the default units used for the update. The client may specify different units in the update if they need to.   # noqa: E501

        :param units: The units of this IntegerValueOption.
        :type units: str
        """

        self._units = units
