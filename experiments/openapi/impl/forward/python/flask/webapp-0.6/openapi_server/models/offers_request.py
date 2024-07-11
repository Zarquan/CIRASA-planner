from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_executable import AbstractExecutable
from openapi_server.models.execution_resource_list import ExecutionResourceList
from openapi_server.models.execution_schedule_item import ExecutionScheduleItem
from openapi_server import util

from openapi_server.models.abstract_executable import AbstractExecutable  # noqa: E501
from openapi_server.models.execution_resource_list import ExecutionResourceList  # noqa: E501
from openapi_server.models.execution_schedule_item import ExecutionScheduleItem  # noqa: E501

class OffersRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, executable=None, resources=None, schedule=None):  # noqa: E501
        """OffersRequest - a model defined in OpenAPI

        :param executable: The executable of this OffersRequest.  # noqa: E501
        :type executable: AbstractExecutable
        :param resources: The resources of this OffersRequest.  # noqa: E501
        :type resources: ExecutionResourceList
        :param schedule: The schedule of this OffersRequest.  # noqa: E501
        :type schedule: List[ExecutionScheduleItem]
        """
        self.openapi_types = {
            'executable': AbstractExecutable,
            'resources': ExecutionResourceList,
            'schedule': List[ExecutionScheduleItem]
        }

        self.attribute_map = {
            'executable': 'executable',
            'resources': 'resources',
            'schedule': 'schedule'
        }

        self._executable = executable
        self._resources = resources
        self._schedule = schedule

    @classmethod
    def from_dict(cls, dikt) -> 'OffersRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OffersRequest of this OffersRequest.  # noqa: E501
        :rtype: OffersRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def executable(self) -> AbstractExecutable:
        """Gets the executable of this OffersRequest.


        :return: The executable of this OffersRequest.
        :rtype: AbstractExecutable
        """
        return self._executable

    @executable.setter
    def executable(self, executable: AbstractExecutable):
        """Sets the executable of this OffersRequest.


        :param executable: The executable of this OffersRequest.
        :type executable: AbstractExecutable
        """

        self._executable = executable

    @property
    def resources(self) -> ExecutionResourceList:
        """Gets the resources of this OffersRequest.


        :return: The resources of this OffersRequest.
        :rtype: ExecutionResourceList
        """
        return self._resources

    @resources.setter
    def resources(self, resources: ExecutionResourceList):
        """Sets the resources of this OffersRequest.


        :param resources: The resources of this OffersRequest.
        :type resources: ExecutionResourceList
        """

        self._resources = resources

    @property
    def schedule(self) -> List[ExecutionScheduleItem]:
        """Gets the schedule of this OffersRequest.


        :return: The schedule of this OffersRequest.
        :rtype: List[ExecutionScheduleItem]
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule: List[ExecutionScheduleItem]):
        """Sets the schedule of this OffersRequest.


        :param schedule: The schedule of this OffersRequest.
        :type schedule: List[ExecutionScheduleItem]
        """

        self._schedule = schedule
