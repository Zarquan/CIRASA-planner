from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class ComputeResourceVolume(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ident=None, name=None, properties=None, path=None, mode=None, resource=None):  # noqa: E501
        """ComputeResourceVolume - a model defined in OpenAPI

        :param ident: The ident of this ComputeResourceVolume.  # noqa: E501
        :type ident: str
        :param name: The name of this ComputeResourceVolume.  # noqa: E501
        :type name: str
        :param properties: The properties of this ComputeResourceVolume.  # noqa: E501
        :type properties: Dict[str, str]
        :param path: The path of this ComputeResourceVolume.  # noqa: E501
        :type path: str
        :param mode: The mode of this ComputeResourceVolume.  # noqa: E501
        :type mode: str
        :param resource: The resource of this ComputeResourceVolume.  # noqa: E501
        :type resource: str
        """
        self.openapi_types = {
            'ident': str,
            'name': str,
            'properties': Dict[str, str],
            'path': str,
            'mode': str,
            'resource': str
        }

        self.attribute_map = {
            'ident': 'ident',
            'name': 'name',
            'properties': 'properties',
            'path': 'path',
            'mode': 'mode',
            'resource': 'resource'
        }

        self._ident = ident
        self._name = name
        self._properties = properties
        self._path = path
        self._mode = mode
        self._resource = resource

    @classmethod
    def from_dict(cls, dikt) -> 'ComputeResourceVolume':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ComputeResourceVolume of this ComputeResourceVolume.  # noqa: E501
        :rtype: ComputeResourceVolume
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ident(self) -> str:
        """Gets the ident of this ComputeResourceVolume.


        :return: The ident of this ComputeResourceVolume.
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident: str):
        """Sets the ident of this ComputeResourceVolume.


        :param ident: The ident of this ComputeResourceVolume.
        :type ident: str
        """

        self._ident = ident

    @property
    def name(self) -> str:
        """Gets the name of this ComputeResourceVolume.


        :return: The name of this ComputeResourceVolume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ComputeResourceVolume.


        :param name: The name of this ComputeResourceVolume.
        :type name: str
        """

        self._name = name

    @property
    def properties(self) -> Dict[str, str]:
        """Gets the properties of this ComputeResourceVolume.

        A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/   # noqa: E501

        :return: The properties of this ComputeResourceVolume.
        :rtype: Dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties: Dict[str, str]):
        """Sets the properties of this ComputeResourceVolume.

        A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/   # noqa: E501

        :param properties: The properties of this ComputeResourceVolume.
        :type properties: Dict[str, str]
        """

        self._properties = properties

    @property
    def path(self) -> str:
        """Gets the path of this ComputeResourceVolume.

        The mount point in the target filesystem.   # noqa: E501

        :return: The path of this ComputeResourceVolume.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this ComputeResourceVolume.

        The mount point in the target filesystem.   # noqa: E501

        :param path: The path of this ComputeResourceVolume.
        :type path: str
        """

        self._path = path

    @property
    def mode(self) -> str:
        """Gets the mode of this ComputeResourceVolume.

        The read-write mode.   # noqa: E501

        :return: The mode of this ComputeResourceVolume.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        """Sets the mode of this ComputeResourceVolume.

        The read-write mode.   # noqa: E501

        :param mode: The mode of this ComputeResourceVolume.
        :type mode: str
        """
        allowed_values = ["READONLY", "READWRITE"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def resource(self) -> str:
        """Gets the resource of this ComputeResourceVolume.

        The name or ident of the resource to mount.   # noqa: E501

        :return: The resource of this ComputeResourceVolume.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource: str):
        """Sets the resource of this ComputeResourceVolume.

        The name or ident of the resource to mount.   # noqa: E501

        :param resource: The resource of this ComputeResourceVolume.
        :type resource: str
        """

        self._resource = resource
