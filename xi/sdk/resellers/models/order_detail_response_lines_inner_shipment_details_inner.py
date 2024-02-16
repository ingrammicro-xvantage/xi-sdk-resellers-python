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

from datetime import date
from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details import OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailResponseLinesInnerShipmentDetailsInner(BaseModel):
    """
    Shipping details for the line item.
    """ # noqa: E501
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity shipped of the line item.")
    estimated_ship_date: Optional[date] = Field(default=None, description="The estimated ship date for the line item.", alias="estimatedShipDate")
    shipped_date: Optional[date] = Field(default=None, description="The date the line item was shipped.", alias="shippedDate")
    estimated_delivery_date: Optional[date] = Field(default=None, description="The date the line item is expected to be delivered.", alias="estimatedDeliveryDate")
    delivered_date: Optional[date] = Field(default=None, description="The actual date of delivery of the line item.", alias="deliveredDate")
    ship_from_warehouse_id: Optional[StrictStr] = Field(default=None, description="The ID of the warehouse the product will ship from.", alias="shipFromWarehouseId")
    ship_from_location: Optional[StrictStr] = Field(default=None, description="The city and state the line item ships from.", alias="shipFromLocation")
    invoice_number: Optional[StrictStr] = Field(default=None, description="The Ingram Micro invoice number for the line item.", alias="invoiceNumber")
    invoice_date: Optional[date] = Field(default=None, description="The date the IngramMicro invoice was created for the line item.", alias="invoiceDate")
    carrier_details: Optional[OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails] = Field(default=None, alias="carrierDetails")
    __properties: ClassVar[List[str]] = ["quantity", "estimatedShipDate", "shippedDate", "estimatedDeliveryDate", "deliveredDate", "shipFromWarehouseId", "shipFromLocation", "invoiceNumber", "invoiceDate", "carrierDetails"]

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
        """Create an instance of OrderDetailResponseLinesInnerShipmentDetailsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of carrier_details
        if self.carrier_details:
            _dict['carrierDetails'] = self.carrier_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailResponseLinesInnerShipmentDetailsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": obj.get("quantity"),
            "estimatedShipDate": obj.get("estimatedShipDate"),
            "shippedDate": obj.get("shippedDate"),
            "estimatedDeliveryDate": obj.get("estimatedDeliveryDate"),
            "deliveredDate": obj.get("deliveredDate"),
            "shipFromWarehouseId": obj.get("shipFromWarehouseId"),
            "shipFromLocation": obj.get("shipFromLocation"),
            "invoiceNumber": obj.get("invoiceNumber"),
            "invoiceDate": obj.get("invoiceDate"),
            "carrierDetails": OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails.from_dict(obj["carrierDetails"]) if obj.get("carrierDetails") is not None else None
        })
        return _obj


