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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.price_and_availability_request_additional_attributes_inner import PriceAndAvailabilityRequestAdditionalAttributesInner
from xi.sdk.resellers.models.price_and_availability_request_availability_by_warehouse_inner import PriceAndAvailabilityRequestAvailabilityByWarehouseInner
from xi.sdk.resellers.models.price_and_availability_request_products_inner import PriceAndAvailabilityRequestProductsInner
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityRequest(BaseModel):
    """
    PriceAndAvailabilityRequest
    """ # noqa: E501
    show_available_discounts: Optional[StrictBool] = Field(default=None, description="Boolean value that will display Discount details in the response when true.", alias="showAvailableDiscounts")
    show_reserve_inventory_details: Optional[StrictBool] = Field(default=None, description="Boolean value that will display reserve inventory details in the response when true.", alias="showReserveInventoryDetails")
    special_bid_number: Optional[StrictStr] = Field(default=None, description="Pre-approved special pricing/bid number provided to the reseller by the vendor for special pricing and discounts. Used to track the bid number where different line items have different bid numbers.", alias="specialBidNumber")
    availability_by_warehouse: Optional[List[PriceAndAvailabilityRequestAvailabilityByWarehouseInner]] = Field(default=None, alias="availabilityByWarehouse")
    products: Optional[List[PriceAndAvailabilityRequestProductsInner]] = None
    additional_attributes: Optional[List[Optional[PriceAndAvailabilityRequestAdditionalAttributesInner]]] = Field(default=None, alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["showAvailableDiscounts", "showReserveInventoryDetails", "specialBidNumber", "availabilityByWarehouse", "products", "additionalAttributes"]

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
        """Create an instance of PriceAndAvailabilityRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in availability_by_warehouse (list)
        _items = []
        if self.availability_by_warehouse:
            for _item_availability_by_warehouse in self.availability_by_warehouse:
                if _item_availability_by_warehouse:
                    _items.append(_item_availability_by_warehouse.to_dict())
            _dict['availabilityByWarehouse'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item_products in self.products:
                if _item_products:
                    _items.append(_item_products.to_dict())
            _dict['products'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item_additional_attributes in self.additional_attributes:
                if _item_additional_attributes:
                    _items.append(_item_additional_attributes.to_dict())
            _dict['additionalAttributes'] = _items
        # set to None if show_available_discounts (nullable) is None
        # and model_fields_set contains the field
        if self.show_available_discounts is None and "show_available_discounts" in self.model_fields_set:
            _dict['showAvailableDiscounts'] = None

        # set to None if show_reserve_inventory_details (nullable) is None
        # and model_fields_set contains the field
        if self.show_reserve_inventory_details is None and "show_reserve_inventory_details" in self.model_fields_set:
            _dict['showReserveInventoryDetails'] = None

        # set to None if special_bid_number (nullable) is None
        # and model_fields_set contains the field
        if self.special_bid_number is None and "special_bid_number" in self.model_fields_set:
            _dict['specialBidNumber'] = None

        # set to None if availability_by_warehouse (nullable) is None
        # and model_fields_set contains the field
        if self.availability_by_warehouse is None and "availability_by_warehouse" in self.model_fields_set:
            _dict['availabilityByWarehouse'] = None

        # set to None if additional_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.additional_attributes is None and "additional_attributes" in self.model_fields_set:
            _dict['additionalAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "showAvailableDiscounts": obj.get("showAvailableDiscounts"),
            "showReserveInventoryDetails": obj.get("showReserveInventoryDetails"),
            "specialBidNumber": obj.get("specialBidNumber"),
            "availabilityByWarehouse": [PriceAndAvailabilityRequestAvailabilityByWarehouseInner.from_dict(_item) for _item in obj["availabilityByWarehouse"]] if obj.get("availabilityByWarehouse") is not None else None,
            "products": [PriceAndAvailabilityRequestProductsInner.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None,
            "additionalAttributes": [PriceAndAvailabilityRequestAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


