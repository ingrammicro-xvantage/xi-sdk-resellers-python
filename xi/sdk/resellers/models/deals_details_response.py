# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.deals_details_response_products_inner import DealsDetailsResponseProductsInner
from xi.sdk.resellers.models.renewals_details_response_end_user_info import RenewalsDetailsResponseEndUserInfo
from typing import Optional, Set
from typing_extensions import Self

class DealsDetailsResponse(BaseModel):
    """
    DealsDetailsResponse
    """ # noqa: E501
    deal_id: Optional[StrictStr] = Field(default=None, description="Deal/Special bid number.", alias="dealId")
    version: Optional[StrictStr] = Field(default=None, description="Most recent version number of the deal.")
    end_user: Optional[StrictStr] = Field(default=None, description="The end user/customer's name.", alias="endUser")
    extended_msrp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Extended MSRP - Manufacturer Suggested Retail Price X Quantity.", alias="extendedMsrp")
    vendor: Optional[StrictStr] = Field(default=None, description="The vendor's name.")
    deal_received_on: Optional[StrictStr] = Field(default=None, description="The date on which the deal starts.", alias="dealReceivedOn")
    deal_expiry_date: Optional[StrictStr] = Field(default=None, description="Expiration date of the deal/Special bid.", alias="dealExpiryDate")
    price_protection_end_date: Optional[StrictStr] = Field(default=None, description="The date on which the price protection will end.", alias="priceProtectionEndDate")
    currency_code: Optional[StrictStr] = Field(default=None, description="Country specific currency code.", alias="currencyCode")
    end_user_info: Optional[RenewalsDetailsResponseEndUserInfo] = Field(default=None, alias="endUserInfo")
    products: Optional[List[DealsDetailsResponseProductsInner]] = None
    __properties: ClassVar[List[str]] = ["dealId", "version", "endUser", "extendedMsrp", "vendor", "dealReceivedOn", "dealExpiryDate", "priceProtectionEndDate", "currencyCode", "endUserInfo", "products"]

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
        """Create an instance of DealsDetailsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of end_user_info
        if self.end_user_info:
            _dict['endUserInfo'] = self.end_user_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item_products in self.products:
                if _item_products:
                    _items.append(_item_products.to_dict())
            _dict['products'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DealsDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dealId": obj.get("dealId"),
            "version": obj.get("version"),
            "endUser": obj.get("endUser"),
            "extendedMsrp": obj.get("extendedMsrp"),
            "vendor": obj.get("vendor"),
            "dealReceivedOn": obj.get("dealReceivedOn"),
            "dealExpiryDate": obj.get("dealExpiryDate"),
            "priceProtectionEndDate": obj.get("priceProtectionEndDate"),
            "currencyCode": obj.get("currencyCode"),
            "endUserInfo": RenewalsDetailsResponseEndUserInfo.from_dict(obj["endUserInfo"]) if obj.get("endUserInfo") is not None else None,
            "products": [DealsDetailsResponseProductsInner.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None
        })
        return _obj


