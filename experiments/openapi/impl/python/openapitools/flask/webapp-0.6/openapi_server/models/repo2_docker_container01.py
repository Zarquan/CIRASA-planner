from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_executable import AbstractExecutable
from openapi_server import util

from openapi_server.models.abstract_executable import AbstractExecutable  # noqa: E501

class Repo2DockerContainer01(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ident=None, name=None, properties=None, type=None, source=None):  # noqa: E501
        """Repo2DockerContainer01 - a model defined in OpenAPI

        :param ident: The ident of this Repo2DockerContainer01.  # noqa: E501
        :type ident: str
        :param name: The name of this Repo2DockerContainer01.  # noqa: E501
        :type name: str
        :param properties: The properties of this Repo2DockerContainer01.  # noqa: E501
        :type properties: Dict[str, str]
        :param type: The type of this Repo2DockerContainer01.  # noqa: E501
        :type type: str
        :param source: The source of this Repo2DockerContainer01.  # noqa: E501
        :type source: str
        """
        self.openapi_types = {
            'ident': str,
            'name': str,
            'properties': Dict[str, str],
            'type': str,
            'source': str
        }

        self.attribute_map = {
            'ident': 'ident',
            'name': 'name',
            'properties': 'properties',
            'type': 'type',
            'source': 'source'
        }

        self._ident = ident
        self._name = name
        self._properties = properties
        self._type = type
        self._source = source

    @classmethod
    def from_dict(cls, dikt) -> 'Repo2DockerContainer01':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Repo2DockerContainer01 of this Repo2DockerContainer01.  # noqa: E501
        :rtype: Repo2DockerContainer01
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ident(self) -> str:
        """Gets the ident of this Repo2DockerContainer01.


        :return: The ident of this Repo2DockerContainer01.
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident: str):
        """Sets the ident of this Repo2DockerContainer01.


        :param ident: The ident of this Repo2DockerContainer01.
        :type ident: str
        """

        self._ident = ident

    @property
    def name(self) -> str:
        """Gets the name of this Repo2DockerContainer01.


        :return: The name of this Repo2DockerContainer01.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Repo2DockerContainer01.


        :param name: The name of this Repo2DockerContainer01.
        :type name: str
        """

        self._name = name

    @property
    def properties(self) -> Dict[str, str]:
        """Gets the properties of this Repo2DockerContainer01.

        A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/   # noqa: E501

        :return: The properties of this Repo2DockerContainer01.
        :rtype: Dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties: Dict[str, str]):
        """Sets the properties of this Repo2DockerContainer01.

        A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/   # noqa: E501

        :param properties: The properties of this Repo2DockerContainer01.
        :type properties: Dict[str, str]
        """

        self._properties = properties

    @property
    def type(self) -> str:
        """Gets the type of this Repo2DockerContainer01.


        :return: The type of this Repo2DockerContainer01.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Repo2DockerContainer01.


        :param type: The type of this Repo2DockerContainer01.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def source(self) -> str:
        """Gets the source of this Repo2DockerContainer01.

        The URL of the repository to package.   # noqa: E501

        :return: The source of this Repo2DockerContainer01.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this Repo2DockerContainer01.

        The URL of the repository to package.   # noqa: E501

        :param source: The source of this Repo2DockerContainer01.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source
