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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner import OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BLinesInnerShipmentDetailsInner(BaseModel):
    """
    OrderDetailB2BLinesInnerShipmentDetailsInner
    """ # noqa: E501
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity shipped of the line item.")
    delivery_number: Optional[StrictStr] = Field(default=None, description="The actual date of delivery of the line item.", alias="deliveryNumber")
    estimated_ship_date: Optional[StrictStr] = Field(default=None, description="The date the line item is expected to be shipped.", alias="estimatedShipDate")
    ship_from_warehouse_id: Optional[StrictStr] = Field(default=None, description="The ID of the warehouse the product will ship from.", alias="shipFromWarehouseId")
    ship_from_location: Optional[StrictStr] = Field(default=None, description="The city and state the line item ships from.", alias="shipFromLocation")
    invoice_number: Optional[StrictStr] = Field(default=None, description="The Ingram Micro invoice number for the line item.", alias="invoiceNumber")
    invoice_date: Optional[StrictStr] = Field(default=None, description="The date the IngramMicro invoice was created for the line item.", alias="invoiceDate")
    carrier_details: Optional[List[OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner]] = Field(default=None, description="The shipment carrier details for the line item.", alias="carrierDetails")
    __properties: ClassVar[List[str]] = ["quantity", "deliveryNumber", "estimatedShipDate", "shipFromWarehouseId", "shipFromLocation", "invoiceNumber", "invoiceDate", "carrierDetails"]

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
        """Create an instance of OrderDetailB2BLinesInnerShipmentDetailsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in carrier_details (list)
        _items = []
        if self.carrier_details:
            for _item in self.carrier_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['carrierDetails'] = _items
        # set to None if carrier_details (nullable) is None
        # and model_fields_set contains the field
        if self.carrier_details is None and "carrier_details" in self.model_fields_set:
            _dict['carrierDetails'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailB2BLinesInnerShipmentDetailsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": obj.get("quantity"),
            "deliveryNumber": obj.get("deliveryNumber"),
            "estimatedShipDate": obj.get("estimatedShipDate"),
            "shipFromWarehouseId": obj.get("shipFromWarehouseId"),
            "shipFromLocation": obj.get("shipFromLocation"),
            "invoiceNumber": obj.get("invoiceNumber"),
            "invoiceDate": obj.get("invoiceDate"),
            "carrierDetails": [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner.from_dict(_item) for _item in obj["carrierDetails"]] if obj.get("carrierDetails") is not None else None
        })
        return _obj


