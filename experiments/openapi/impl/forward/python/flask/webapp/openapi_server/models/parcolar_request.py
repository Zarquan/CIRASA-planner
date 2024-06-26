from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.parcolar_request_executable import ParcolarRequestExecutable
from openapi_server.models.resources import Resources
from openapi_server import util

from openapi_server.models.parcolar_request_executable import ParcolarRequestExecutable  # noqa: E501
from openapi_server.models.resources import Resources  # noqa: E501

class ParcolarRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, executable=None, resources=None):  # noqa: E501
        """ParcolarRequest - a model defined in OpenAPI

        :param executable: The executable of this ParcolarRequest.  # noqa: E501
        :type executable: ParcolarRequestExecutable
        :param resources: The resources of this ParcolarRequest.  # noqa: E501
        :type resources: Resources
        """
        self.openapi_types = {
            'executable': ParcolarRequestExecutable,
            'resources': Resources
        }

        self.attribute_map = {
            'executable': 'executable',
            'resources': 'resources'
        }

        self._executable = executable
        self._resources = resources

    @classmethod
    def from_dict(cls, dikt) -> 'ParcolarRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ParcolarRequest of this ParcolarRequest.  # noqa: E501
        :rtype: ParcolarRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def executable(self) -> ParcolarRequestExecutable:
        """Gets the executable of this ParcolarRequest.


        :return: The executable of this ParcolarRequest.
        :rtype: ParcolarRequestExecutable
        """
        return self._executable

    @executable.setter
    def executable(self, executable: ParcolarRequestExecutable):
        """Sets the executable of this ParcolarRequest.


        :param executable: The executable of this ParcolarRequest.
        :type executable: ParcolarRequestExecutable
        """

        self._executable = executable

    @property
    def resources(self) -> Resources:
        """Gets the resources of this ParcolarRequest.


        :return: The resources of this ParcolarRequest.
        :rtype: Resources
        """
        return self._resources

    @resources.setter
    def resources(self, resources: Resources):
        """Sets the resources of this ParcolarRequest.


        :param resources: The resources of this ParcolarRequest.
        :type resources: Resources
        """

        self._resources = resources
