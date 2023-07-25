# coding: utf-8

"""
    Shield Administration API

    The Shield APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Shield APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Shield APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Shield into your existing applications and workflows.  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from shield_api import schemas  # noqa: F401


class V1beta1AuthTokenResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            accessToken = schemas.StrSchema
            tokenType = schemas.StrSchema
            __annotations__ = {
                "accessToken": accessToken,
                "tokenType": tokenType,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessToken"]) -> MetaOapg.properties.accessToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenType"]) -> MetaOapg.properties.tokenType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accessToken", "tokenType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessToken"]) -> typing.Union[MetaOapg.properties.accessToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenType"]) -> typing.Union[MetaOapg.properties.tokenType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accessToken", "tokenType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accessToken: typing.Union[MetaOapg.properties.accessToken, str, schemas.Unset] = schemas.unset,
        tokenType: typing.Union[MetaOapg.properties.tokenType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1beta1AuthTokenResponse':
        return super().__new__(
            cls,
            *_args,
            accessToken=accessToken,
            tokenType=tokenType,
            _configuration=_configuration,
            **kwargs,
        )
