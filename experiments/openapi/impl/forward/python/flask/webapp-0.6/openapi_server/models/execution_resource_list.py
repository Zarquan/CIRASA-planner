from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_compute_resource import AbstractComputeResource
from openapi_server.models.abstract_data_resource import AbstractDataResource
from openapi_server.models.abstract_storage_resource import AbstractStorageResource
from openapi_server import util

from openapi_server.models.abstract_compute_resource import AbstractComputeResource  # noqa: E501
from openapi_server.models.abstract_data_resource import AbstractDataResource  # noqa: E501
from openapi_server.models.abstract_storage_resource import AbstractStorageResource  # noqa: E501

class ExecutionResourceList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, compute=None, storage=None, data=None):  # noqa: E501
        """ExecutionResourceList - a model defined in OpenAPI

        :param compute: The compute of this ExecutionResourceList.  # noqa: E501
        :type compute: List[AbstractComputeResource]
        :param storage: The storage of this ExecutionResourceList.  # noqa: E501
        :type storage: List[AbstractStorageResource]
        :param data: The data of this ExecutionResourceList.  # noqa: E501
        :type data: List[AbstractDataResource]
        """
        self.openapi_types = {
            'compute': List[AbstractComputeResource],
            'storage': List[AbstractStorageResource],
            'data': List[AbstractDataResource]
        }

        self.attribute_map = {
            'compute': 'compute',
            'storage': 'storage',
            'data': 'data'
        }

        self._compute = compute
        self._storage = storage
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ExecutionResourceList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExecutionResourceList of this ExecutionResourceList.  # noqa: E501
        :rtype: ExecutionResourceList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def compute(self) -> List[AbstractComputeResource]:
        """Gets the compute of this ExecutionResourceList.

        A list of compute resources.   # noqa: E501

        :return: The compute of this ExecutionResourceList.
        :rtype: List[AbstractComputeResource]
        """
        return self._compute

    @compute.setter
    def compute(self, compute: List[AbstractComputeResource]):
        """Sets the compute of this ExecutionResourceList.

        A list of compute resources.   # noqa: E501

        :param compute: The compute of this ExecutionResourceList.
        :type compute: List[AbstractComputeResource]
        """

        self._compute = compute

    @property
    def storage(self) -> List[AbstractStorageResource]:
        """Gets the storage of this ExecutionResourceList.

        A list of storage resources.   # noqa: E501

        :return: The storage of this ExecutionResourceList.
        :rtype: List[AbstractStorageResource]
        """
        return self._storage

    @storage.setter
    def storage(self, storage: List[AbstractStorageResource]):
        """Sets the storage of this ExecutionResourceList.

        A list of storage resources.   # noqa: E501

        :param storage: The storage of this ExecutionResourceList.
        :type storage: List[AbstractStorageResource]
        """

        self._storage = storage

    @property
    def data(self) -> List[AbstractDataResource]:
        """Gets the data of this ExecutionResourceList.

        A list of data resources.   # noqa: E501

        :return: The data of this ExecutionResourceList.
        :rtype: List[AbstractDataResource]
        """
        return self._data

    @data.setter
    def data(self, data: List[AbstractDataResource]):
        """Sets the data of this ExecutionResourceList.

        A list of data resources.   # noqa: E501

        :param data: The data of this ExecutionResourceList.
        :type data: List[AbstractDataResource]
        """

        self._data = data