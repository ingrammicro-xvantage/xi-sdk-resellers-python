# coding: utf-8

"""
    Reseller API Documentation

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner(BaseModel):
    """
    Attribute Name and Value: This field identifies if your order is a DIRECT SHIP order (license / warranty) or how you want your Backorders managed as well as other process options like placing your order on hold or adding a comment. 
    """ # noqa: E501
    attributename: Optional[StrictStr] = None
    attributevalue: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["attributename", "attributevalue"]

    @field_validator('attributename')
    def attributename_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Isdirectshiporder', 'emailaddress', 'Isbackorderflagallowed', 'placeoncustomerhold', 'signaturerequired', 'commenttext', 'resellerctacemail', 'duplicatecustomerordernumbervalidate', 'quotenumber', 'shipctacphone', 'vendauthnumber', 'continueonerror'):
            raise ValueError("must be one of enum values ('Isdirectshiporder', 'emailaddress', 'Isbackorderflagallowed', 'placeoncustomerhold', 'signaturerequired', 'commenttext', 'resellerctacemail', 'duplicatecustomerordernumbervalidate', 'quotenumber', 'shipctacphone', 'vendauthnumber', 'continueonerror')")
        return value

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
        """Create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attributename": obj.get("attributename"),
            "attributevalue": obj.get("attributevalue")
        })
        return _obj

