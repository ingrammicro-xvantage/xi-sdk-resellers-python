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
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner(BaseModel):
    """
    PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name of the type of pricing.")
    quantity: Optional[StrictStr] = Field(default=None, description="Quantity of the line item.")
    msrp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Manufacturer Suggested Retail Price.")
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unit price of the line item.", alias="unitPrice")
    margin: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Reseller’s margin percentage")
    currency_code: Optional[StrictStr] = Field(default=None, description="The 3-digit ISO currency code.", alias="currencyCode")
    subscription_period: Optional[StrictStr] = Field(default=None, description="The subscription period of the line item.", alias="subscriptionPeriod")
    __properties: ClassVar[List[str]] = ["name", "quantity", "msrp", "unitPrice", "margin", "currencyCode", "subscriptionPeriod"]

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
        """Create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if msrp (nullable) is None
        # and model_fields_set contains the field
        if self.msrp is None and "msrp" in self.model_fields_set:
            _dict['msrp'] = None

        # set to None if unit_price (nullable) is None
        # and model_fields_set contains the field
        if self.unit_price is None and "unit_price" in self.model_fields_set:
            _dict['unitPrice'] = None

        # set to None if margin (nullable) is None
        # and model_fields_set contains the field
        if self.margin is None and "margin" in self.model_fields_set:
            _dict['margin'] = None

        # set to None if currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.currency_code is None and "currency_code" in self.model_fields_set:
            _dict['currencyCode'] = None

        # set to None if subscription_period (nullable) is None
        # and model_fields_set contains the field
        if self.subscription_period is None and "subscription_period" in self.model_fields_set:
            _dict['subscriptionPeriod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "quantity": obj.get("quantity"),
            "msrp": obj.get("msrp"),
            "unitPrice": obj.get("unitPrice"),
            "margin": obj.get("margin"),
            "currencyCode": obj.get("currencyCode"),
            "subscriptionPeriod": obj.get("subscriptionPeriod")
        })
        return _obj


