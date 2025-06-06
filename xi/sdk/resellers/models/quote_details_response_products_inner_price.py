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
from xi.sdk.resellers.models.quote_details_response_products_inner_price_discounts_inner import QuoteDetailsResponseProductsInnerPriceDiscountsInner
from xi.sdk.resellers.models.quote_details_response_products_inner_price_extra_fees_details_inner import QuoteDetailsResponseProductsInnerPriceExtraFeesDetailsInner
from typing import Optional, Set
from typing_extensions import Self

class QuoteDetailsResponseProductsInnerPrice(BaseModel):
    """
    QuoteDetailsResponseProductsInnerPrice
    """ # noqa: E501
    quote_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Ingram Micro quoted price specific to the reseller and quote.", alias="quotePrice")
    msrp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Manufacturer Suggested Retail Price")
    extended_msrp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Extended MSRP - Manufacturer Suggested Retail Price X Quantity", alias="extendedMsrp")
    extended_quote_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Extended reseller quoted price (cost to reseller) X Quantity", alias="extendedQuotePrice")
    remaining_quantity_extended_msrp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="remainingQuantityExtendedMsrp")
    remaining_quantity_extended_quote_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="remainingQuantityExtendedQuotePrice")
    discount_off_list: Optional[StrictStr] = Field(default=None, description="Discount off list percentage extended", alias="discountOffList")
    type: Optional[StrictStr] = None
    recurring_price_model: Optional[StrictStr] = Field(default=None, alias="recurringPriceModel")
    unit_of_measure: Optional[StrictStr] = Field(default=None, alias="unitOfMeasure")
    tax: Optional[Union[StrictFloat, StrictInt]] = None
    extrafees: Optional[Union[StrictFloat, StrictInt]] = None
    extra_fees_details: Optional[List[QuoteDetailsResponseProductsInnerPriceExtraFeesDetailsInner]] = Field(default=None, alias="extraFeesDetails")
    discounts: Optional[List[QuoteDetailsResponseProductsInnerPriceDiscountsInner]] = None
    __properties: ClassVar[List[str]] = ["quotePrice", "msrp", "extendedMsrp", "extendedQuotePrice", "remainingQuantityExtendedMsrp", "remainingQuantityExtendedQuotePrice", "discountOffList", "type", "recurringPriceModel", "unitOfMeasure", "tax", "extrafees", "extraFeesDetails", "discounts"]

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
        """Create an instance of QuoteDetailsResponseProductsInnerPrice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in extra_fees_details (list)
        _items = []
        if self.extra_fees_details:
            for _item_extra_fees_details in self.extra_fees_details:
                if _item_extra_fees_details:
                    _items.append(_item_extra_fees_details.to_dict())
            _dict['extraFeesDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in discounts (list)
        _items = []
        if self.discounts:
            for _item_discounts in self.discounts:
                if _item_discounts:
                    _items.append(_item_discounts.to_dict())
            _dict['discounts'] = _items
        # set to None if quote_price (nullable) is None
        # and model_fields_set contains the field
        if self.quote_price is None and "quote_price" in self.model_fields_set:
            _dict['quotePrice'] = None

        # set to None if msrp (nullable) is None
        # and model_fields_set contains the field
        if self.msrp is None and "msrp" in self.model_fields_set:
            _dict['msrp'] = None

        # set to None if extended_msrp (nullable) is None
        # and model_fields_set contains the field
        if self.extended_msrp is None and "extended_msrp" in self.model_fields_set:
            _dict['extendedMsrp'] = None

        # set to None if extended_quote_price (nullable) is None
        # and model_fields_set contains the field
        if self.extended_quote_price is None and "extended_quote_price" in self.model_fields_set:
            _dict['extendedQuotePrice'] = None

        # set to None if remaining_quantity_extended_msrp (nullable) is None
        # and model_fields_set contains the field
        if self.remaining_quantity_extended_msrp is None and "remaining_quantity_extended_msrp" in self.model_fields_set:
            _dict['remainingQuantityExtendedMsrp'] = None

        # set to None if remaining_quantity_extended_quote_price (nullable) is None
        # and model_fields_set contains the field
        if self.remaining_quantity_extended_quote_price is None and "remaining_quantity_extended_quote_price" in self.model_fields_set:
            _dict['remainingQuantityExtendedQuotePrice'] = None

        # set to None if discount_off_list (nullable) is None
        # and model_fields_set contains the field
        if self.discount_off_list is None and "discount_off_list" in self.model_fields_set:
            _dict['discountOffList'] = None

        # set to None if tax (nullable) is None
        # and model_fields_set contains the field
        if self.tax is None and "tax" in self.model_fields_set:
            _dict['tax'] = None

        # set to None if extrafees (nullable) is None
        # and model_fields_set contains the field
        if self.extrafees is None and "extrafees" in self.model_fields_set:
            _dict['extrafees'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuoteDetailsResponseProductsInnerPrice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quotePrice": obj.get("quotePrice"),
            "msrp": obj.get("msrp"),
            "extendedMsrp": obj.get("extendedMsrp"),
            "extendedQuotePrice": obj.get("extendedQuotePrice"),
            "remainingQuantityExtendedMsrp": obj.get("remainingQuantityExtendedMsrp"),
            "remainingQuantityExtendedQuotePrice": obj.get("remainingQuantityExtendedQuotePrice"),
            "discountOffList": obj.get("discountOffList"),
            "type": obj.get("type"),
            "recurringPriceModel": obj.get("recurringPriceModel"),
            "unitOfMeasure": obj.get("unitOfMeasure"),
            "tax": obj.get("tax"),
            "extrafees": obj.get("extrafees"),
            "extraFeesDetails": [QuoteDetailsResponseProductsInnerPriceExtraFeesDetailsInner.from_dict(_item) for _item in obj["extraFeesDetails"]] if obj.get("extraFeesDetails") is not None else None,
            "discounts": [QuoteDetailsResponseProductsInnerPriceDiscountsInner.from_dict(_item) for _item in obj["discounts"]] if obj.get("discounts") is not None else None
        })
        return _obj


