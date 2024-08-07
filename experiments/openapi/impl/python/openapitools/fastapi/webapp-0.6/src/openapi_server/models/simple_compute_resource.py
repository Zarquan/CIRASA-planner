# coding: utf-8

"""
    IVOA ExecutionBroker

    Prototype implementation of the IVOA ExecutionBroker interface 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.abstract_compute_resource import AbstractComputeResource
from openapi_server.models.compute_resource_volume import ComputeResourceVolume
from openapi_server.models.min_max_integer import MinMaxInteger
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SimpleComputeResource(AbstractComputeResource):
    """
    A simple compute resource. 
    """ # noqa: E501
    ident: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    properties: Optional[Dict[str, StrictStr]] = Field(default=None, description="A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/ ")
    type: StrictStr
    cores: Optional[MinMaxInteger] = None
    memory: Optional[MinMaxInteger] = None
    volumes: Optional[List[ComputeResourceVolume]] = Field(default=None, description="A list of resources that need to be mounted as volumes. ")
    __properties: ClassVar[List[str]] = ["ident", "name", "properties", "type", "cores", "memory", "volumes"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SimpleComputeResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cores
        if self.cores:
            _dict['cores'] = self.cores.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory
        if self.memory:
            _dict['memory'] = self.memory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SimpleComputeResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ident": obj.get("ident"),
            "name": obj.get("name"),
            "properties": obj.get("properties"),
            "type": obj.get("type"),
            "cores": MinMaxInteger.from_dict(obj.get("cores")) if obj.get("cores") is not None else None,
            "memory": MinMaxInteger.from_dict(obj.get("memory")) if obj.get("memory") is not None else None,
            "volumes": [ComputeResourceVolume.from_dict(_item) for _item in obj.get("volumes")] if obj.get("volumes") is not None else None
        })
        return _obj


