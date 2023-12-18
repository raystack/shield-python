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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from frontier_api.models.v1beta1_checkout_feature_body import V1beta1CheckoutFeatureBody
from frontier_api.models.v1beta1_checkout_subscription_body import V1beta1CheckoutSubscriptionBody

class FrontierServiceCreateCheckoutRequest(BaseModel):
    """
    FrontierServiceCreateCheckoutRequest
    """
    success_url: Optional[StrictStr] = Field(None, alias="successUrl")
    cancel_url: Optional[StrictStr] = Field(None, alias="cancelUrl")
    subscription_body: Optional[V1beta1CheckoutSubscriptionBody] = Field(None, alias="subscriptionBody")
    feature_body: Optional[V1beta1CheckoutFeatureBody] = Field(None, alias="featureBody")
    __properties = ["successUrl", "cancelUrl", "subscriptionBody", "featureBody"]

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
    def from_json(cls, json_str: str) -> FrontierServiceCreateCheckoutRequest:
        """Create an instance of FrontierServiceCreateCheckoutRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of subscription_body
        if self.subscription_body:
            _dict['subscriptionBody'] = self.subscription_body.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feature_body
        if self.feature_body:
            _dict['featureBody'] = self.feature_body.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FrontierServiceCreateCheckoutRequest:
        """Create an instance of FrontierServiceCreateCheckoutRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FrontierServiceCreateCheckoutRequest.parse_obj(obj)

        _obj = FrontierServiceCreateCheckoutRequest.parse_obj({
            "success_url": obj.get("successUrl"),
            "cancel_url": obj.get("cancelUrl"),
            "subscription_body": V1beta1CheckoutSubscriptionBody.from_dict(obj.get("subscriptionBody")) if obj.get("subscriptionBody") is not None else None,
            "feature_body": V1beta1CheckoutFeatureBody.from_dict(obj.get("featureBody")) if obj.get("featureBody") is not None else None
        })
        return _obj


