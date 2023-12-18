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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from frontier_api.models.v1beta1_organization import V1beta1Organization

class V1beta1ListOrganizationsByUserResponse(BaseModel):
    """
    V1beta1ListOrganizationsByUserResponse
    """
    organizations: Optional[conlist(V1beta1Organization)] = None
    joinable_via_domain: Optional[conlist(V1beta1Organization)] = Field(None, alias="joinableViaDomain")
    __properties = ["organizations", "joinableViaDomain"]

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
    def from_json(cls, json_str: str) -> V1beta1ListOrganizationsByUserResponse:
        """Create an instance of V1beta1ListOrganizationsByUserResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in organizations (list)
        _items = []
        if self.organizations:
            for _item in self.organizations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['organizations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in joinable_via_domain (list)
        _items = []
        if self.joinable_via_domain:
            for _item in self.joinable_via_domain:
                if _item:
                    _items.append(_item.to_dict())
            _dict['joinableViaDomain'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1beta1ListOrganizationsByUserResponse:
        """Create an instance of V1beta1ListOrganizationsByUserResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1beta1ListOrganizationsByUserResponse.parse_obj(obj)

        _obj = V1beta1ListOrganizationsByUserResponse.parse_obj({
            "organizations": [V1beta1Organization.from_dict(_item) for _item in obj.get("organizations")] if obj.get("organizations") is not None else None,
            "joinable_via_domain": [V1beta1Organization.from_dict(_item) for _item in obj.get("joinableViaDomain")] if obj.get("joinableViaDomain") is not None else None
        })
        return _obj


