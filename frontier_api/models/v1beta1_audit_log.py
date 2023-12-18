# coding: utf-8

"""
    Frontier Administration API

    The Frontier APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Frontier APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Frontier APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Frontier into your existing applications and workflows.

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from frontier_api.models.v1beta1_audit_log_actor import V1beta1AuditLogActor
from frontier_api.models.v1beta1_audit_log_target import V1beta1AuditLogTarget

class V1beta1AuditLog(BaseModel):
    """
    V1beta1AuditLog
    """
    id: Optional[StrictStr] = None
    source: StrictStr = Field(..., description="The source service generating the event.")
    action: StrictStr = Field(...)
    actor: Optional[V1beta1AuditLogActor] = None
    target: Optional[V1beta1AuditLogTarget] = None
    context: Optional[Dict[str, StrictStr]] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="The time the log was created.")
    __properties = ["id", "source", "action", "actor", "target", "context", "createdAt"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> V1beta1AuditLog:
        """Create an instance of V1beta1AuditLog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1beta1AuditLog:
        """Create an instance of V1beta1AuditLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1beta1AuditLog.parse_obj(obj)

        _obj = V1beta1AuditLog.parse_obj({
            "id": obj.get("id"),
            "source": obj.get("source"),
            "action": obj.get("action"),
            "actor": V1beta1AuditLogActor.from_dict(obj.get("actor")) if obj.get("actor") is not None else None,
            "target": V1beta1AuditLogTarget.from_dict(obj.get("target")) if obj.get("target") is not None else None,
            "context": obj.get("context"),
            "created_at": obj.get("createdAt")
        })
        return _obj


