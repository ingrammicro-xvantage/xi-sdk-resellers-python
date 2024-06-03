# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.freight_request_lines_inner import FreightRequestLinesInner
from xi.sdk.resellers.models.freight_request_ship_to_address_inner import FreightRequestShipToAddressInner
from typing import Optional, Set
from typing_extensions import Self

class FreightRequest(BaseModel):
    """
    FreightRequest
    """ # noqa: E501
    bill_to_address_id: Optional[StrictStr] = Field(default=None, description="Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit.", alias="billToAddressId")
    ship_to_address_id: Optional[StrictStr] = Field(default=None, description="The ID references the reseller's address in Ingram Micro's system for shipping. Provided to resellers during the onboarding process.", alias="shipToAddressId")
    ship_to_address: Optional[List[FreightRequestShipToAddressInner]] = Field(default=None, description="The shipping information.", alias="shipToAddress")
    lines: Optional[List[FreightRequestLinesInner]] = None
    __properties: ClassVar[List[str]] = ["billToAddressId", "shipToAddressId", "shipToAddress", "lines"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FreightRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in ship_to_address (list)
        _items = []
        if self.ship_to_address:
            for _item in self.ship_to_address:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shipToAddress'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FreightRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billToAddressId": obj.get("billToAddressId"),
            "shipToAddressId": obj.get("shipToAddressId"),
            "shipToAddress": [FreightRequestShipToAddressInner.from_dict(_item) for _item in obj["shipToAddress"]] if obj.get("shipToAddress") is not None else None,
            "lines": [FreightRequestLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None
        })
        return _obj


