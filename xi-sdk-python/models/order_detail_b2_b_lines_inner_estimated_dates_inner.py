# coding: utf-8

"""
    Reseller API Documentation - United States

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
from pydantic import BaseModel
from xi-sdk-python.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery import OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery
from xi-sdk-python.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship import OrderDetailB2BLinesInnerEstimatedDatesInnerShip
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderDetailB2BLinesInnerEstimatedDatesInner(BaseModel):
    """
    OrderDetailB2BLinesInnerEstimatedDatesInner
    """ # noqa: E501
    ship: Optional[OrderDetailB2BLinesInnerEstimatedDatesInnerShip] = None
    delivery: Optional[OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery] = None
    __properties: ClassVar[List[str]] = ["ship", "delivery"]

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
        """Create an instance of OrderDetailB2BLinesInnerEstimatedDatesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ship
        if self.ship:
            _dict['ship'] = self.ship.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivery
        if self.delivery:
            _dict['delivery'] = self.delivery.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderDetailB2BLinesInnerEstimatedDatesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ship": OrderDetailB2BLinesInnerEstimatedDatesInnerShip.from_dict(obj.get("ship")) if obj.get("ship") is not None else None,
            "delivery": OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery.from_dict(obj.get("delivery")) if obj.get("delivery") is not None else None
        })
        return _obj


