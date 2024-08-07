from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class AbstractComponent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ident=None, name=None, properties=None):  # noqa: E501
        """AbstractComponent - a model defined in OpenAPI

        :param ident: The ident of this AbstractComponent.  # noqa: E501
        :type ident: str
        :param name: The name of this AbstractComponent.  # noqa: E501
        :type name: str
        :param properties: The properties of this AbstractComponent.  # noqa: E501
        :type properties: Dict[str, str]
        """
        self.openapi_types = {
            'ident': str,
            'name': str,
            'properties': Dict[str, str]
        }

        self.attribute_map = {
            'ident': 'ident',
            'name': 'name',
            'properties': 'properties'
        }

        self._ident = ident
        self._name = name
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt) -> 'AbstractComponent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AbstractComponent of this AbstractComponent.  # noqa: E501
        :rtype: AbstractComponent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ident(self) -> str:
        """Gets the ident of this AbstractComponent.


        :return: The ident of this AbstractComponent.
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident: str):
        """Sets the ident of this AbstractComponent.


        :param ident: The ident of this AbstractComponent.
        :type ident: str
        """

        self._ident = ident

    @property
    def name(self) -> str:
        """Gets the name of this AbstractComponent.


        :return: The name of this AbstractComponent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AbstractComponent.


        :param name: The name of this AbstractComponent.
        :type name: str
        """

        self._name = name

    @property
    def properties(self) -> Dict[str, str]:
        """Gets the properties of this AbstractComponent.

        A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/   # noqa: E501

        :return: The properties of this AbstractComponent.
        :rtype: Dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties: Dict[str, str]):
        """Sets the properties of this AbstractComponent.

        A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/   # noqa: E501

        :param properties: The properties of this AbstractComponent.
        :type properties: Dict[str, str]
        """

        self._properties = properties
