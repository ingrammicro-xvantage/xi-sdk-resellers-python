# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_delivery_date_range import OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery(BaseModel):
    """
    OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery
    """ # noqa: E501
    delivery_date_type: Optional[StrictStr] = Field(default=None, description="Date type. Example Single or multiple dates.", alias="deliveryDateType")
    delivery_date_range: Optional[OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange] = Field(default=None, alias="deliveryDateRange")
    delivery_source: Optional[StrictStr] = Field(default=None, description="Source of the delivery.", alias="deliverySource")
    delivery_description: Optional[StrictStr] = Field(default=None, description="Delivery description.", alias="deliveryDescription")
    delivered_date: Optional[StrictStr] = Field(default=None, description="Delivery date.", alias="deliveredDate")
    __properties: ClassVar[List[str]] = ["deliveryDateType", "deliveryDateRange", "deliverySource", "deliveryDescription", "deliveredDate"]

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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of delivery_date_range
        if self.delivery_date_range:
            _dict['deliveryDateRange'] = self.delivery_date_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deliveryDateType": obj.get("deliveryDateType"),
            "deliveryDateRange": OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange.from_dict(obj["deliveryDateRange"]) if obj.get("deliveryDateRange") is not None else None,
            "deliverySource": obj.get("deliverySource"),
            "deliveryDescription": obj.get("deliveryDescription"),
            "deliveredDate": obj.get("deliveredDate")
        })
        return _obj


