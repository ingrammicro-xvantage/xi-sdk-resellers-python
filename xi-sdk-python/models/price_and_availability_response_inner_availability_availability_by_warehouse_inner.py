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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from xi-sdk-python.models.price_and_availability_response_inner_availability_availability_by_warehouse_inner_back_order_info_inner import PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner(BaseModel):
    """
    PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner
    """ # noqa: E501
    location: Optional[StrictStr] = Field(default=None, description="Indicates where (location) the product is available.")
    warehouse_id: Optional[StrictStr] = Field(default=None, description="Indicates where (Ingram Warehouse Id) the product is available.", alias="warehouseId")
    quantity_available: Optional[StrictInt] = Field(default=None, description="The quantity of the product available in a given warehouse.", alias="quantityAvailable")
    quantity_backordered: Optional[StrictInt] = Field(default=None, description="The quantity of a product backordered in a given warehouse.", alias="quantityBackordered")
    quantity_backordered_eta: Optional[StrictStr] = Field(default=None, description="The estimated time of arrival of a product that has been backordered in a given warehouse.", alias="quantityBackorderedEta")
    back_order_info: Optional[List[PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner]] = Field(default=None, description="*Currently, this feature is not available in these countries (Mexico, Turkey, New Zealand, Colombia, Chile, Brazil, Peru, Western Sahara).", alias="backOrderInfo")
    __properties: ClassVar[List[str]] = ["location", "warehouseId", "quantityAvailable", "quantityBackordered", "quantityBackorderedEta", "backOrderInfo"]

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
        """Create an instance of PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in back_order_info (list)
        _items = []
        if self.back_order_info:
            for _item in self.back_order_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['backOrderInfo'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location": obj.get("location"),
            "warehouseId": obj.get("warehouseId"),
            "quantityAvailable": obj.get("quantityAvailable"),
            "quantityBackordered": obj.get("quantityBackordered"),
            "quantityBackorderedEta": obj.get("quantityBackorderedEta"),
            "backOrderInfo": [PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner.from_dict(_item) for _item in obj.get("backOrderInfo")] if obj.get("backOrderInfo") is not None else None
        })
        return _obj


