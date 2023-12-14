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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from frontier_api.models.v1beta1_group import V1beta1Group
from frontier_api.models.v1beta1_list_current_user_groups_response_access_pair import V1beta1ListCurrentUserGroupsResponseAccessPair
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1beta1ListCurrentUserGroupsResponse(BaseModel):
    """
    V1beta1ListCurrentUserGroupsResponse
    """ # noqa: E501
    groups: Optional[List[V1beta1Group]] = None
    access_pairs: Optional[List[V1beta1ListCurrentUserGroupsResponseAccessPair]] = Field(default=None, alias="accessPairs")
    __properties: ClassVar[List[str]] = ["groups", "accessPairs"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
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
        """Create an instance of V1beta1ListCurrentUserGroupsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item in self.groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in access_pairs (list)
        _items = []
        if self.access_pairs:
            for _item in self.access_pairs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accessPairs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1beta1ListCurrentUserGroupsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "groups": [V1beta1Group.from_dict(_item) for _item in obj.get("groups")] if obj.get("groups") is not None else None,
            "accessPairs": [V1beta1ListCurrentUserGroupsResponseAccessPair.from_dict(_item) for _item in obj.get("accessPairs")] if obj.get("accessPairs") is not None else None
        })
        return _obj


