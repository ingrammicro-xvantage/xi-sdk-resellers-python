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
from pydantic import BaseModel, StrictBool, StrictInt
from pydantic import Field
from xi-sdk-resellers-python.models.price_and_availability_response_inner_availability_availability_by_warehouse_inner import PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PriceAndAvailabilityResponseInnerAvailability(BaseModel):
    """
    PriceAndAvailabilityResponseInnerAvailability
    """ # noqa: E501
    available: Optional[StrictBool] = Field(default=None, description="Boolean that indicates if the product ordered is available")
    total_availability: Optional[StrictInt] = Field(default=None, description="The total amount of available products", alias="totalAvailability")
    availability_by_warehouse: Optional[List[PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner]] = Field(default=None, alias="availabilityByWarehouse")
    __properties: ClassVar[List[str]] = ["available", "totalAvailability", "availabilityByWarehouse"]

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
        """Create an instance of PriceAndAvailabilityResponseInnerAvailability from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in availability_by_warehouse (list)
        _items = []
        if self.availability_by_warehouse:
            for _item in self.availability_by_warehouse:
                if _item:
                    _items.append(_item.to_dict())
            _dict['availabilityByWarehouse'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PriceAndAvailabilityResponseInnerAvailability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available": obj.get("available"),
            "totalAvailability": obj.get("totalAvailability"),
            "availabilityByWarehouse": [PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner.from_dict(_item) for _item in obj.get("availabilityByWarehouse")] if obj.get("availabilityByWarehouse") is not None else None
        })
        return _obj

