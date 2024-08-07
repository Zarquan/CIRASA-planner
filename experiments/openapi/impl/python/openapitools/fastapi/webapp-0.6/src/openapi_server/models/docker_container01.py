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




from pydantic import ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.abstract_executable import AbstractExecutable
from openapi_server.models.docker_network_spec import DockerNetworkSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DockerContainer01(AbstractExecutable):
    """
    A Docker or OCI container executable. See https://opencontainers.org/ 
    """ # noqa: E501
    ident: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    properties: Optional[Dict[str, StrictStr]] = Field(default=None, description="A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/ ")
    type: StrictStr
    image: StrictStr = Field(description="The image name, with or without the repository, namespace or tag. ")
    namespace: Optional[StrictStr] = Field(default=None, description="The namespace within the repository, if not already specified in the image name. ")
    tag: Optional[StrictStr] = Field(default=None, description="The image tag, if not already specified in the image name.")
    repository: Optional[StrictStr] = Field(default=None, description="The respository tag, if not already specified in the image name.")
    platform: Optional[StrictStr] = Field(default=None, description="The target CPU architecture the container is built for. The default is `linux/amd64`. ")
    privileged: Optional[StrictBool] = Field(default=False, description="Set the privileged flag on execution. The default is `false`. See https://docs.docker.com/reference/cli/docker/container/run/#privileged. ")
    entrypoint: Optional[StrictStr] = None
    environment: Optional[Dict[str, StrictStr]] = Field(default=None, description="A map of name->value properties. See https://swagger.io/docs/specification/data-models/dictionaries/ ")
    network: Optional[DockerNetworkSpec] = None
    __properties: ClassVar[List[str]] = ["ident", "name", "properties", "type", "image", "namespace", "tag", "repository", "platform", "privileged", "entrypoint", "environment", "network"]

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
        """Create an instance of DockerContainer01 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DockerContainer01 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ident": obj.get("ident"),
            "name": obj.get("name"),
            "properties": obj.get("properties"),
            "type": obj.get("type"),
            "image": obj.get("image"),
            "namespace": obj.get("namespace"),
            "tag": obj.get("tag"),
            "repository": obj.get("repository"),
            "platform": obj.get("platform"),
            "privileged": obj.get("privileged") if obj.get("privileged") is not None else False,
            "entrypoint": obj.get("entrypoint"),
            "environment": obj.get("environment"),
            "network": DockerNetworkSpec.from_dict(obj.get("network")) if obj.get("network") is not None else None
        })
        return _obj


