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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from xi-sdk-resellers-python.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner import OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner(BaseModel):
    """
    OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner
    """ # noqa: E501
    carrier_code: Optional[StrictStr] = Field(default=None, description="The carrier code for the shipment containing the line item.", alias="carrierCode")
    carrier_name: Optional[StrictStr] = Field(default=None, description="The name of the carrier of the shipment containing the line item.", alias="carrierName")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity shipped of the line item.")
    shipped_date: Optional[StrictStr] = Field(default=None, description="The actual date when line item shipped.", alias="shippedDate")
    estimated_delivery_date: Optional[StrictStr] = Field(default=None, description="The date the line item is expected to be delivered.", alias="estimatedDeliveryDate")
    delivered_date: Optional[StrictStr] = Field(default=None, description="The actual date of delivery of the line item.", alias="deliveredDate")
    carrier_pickup_date: Optional[StrictStr] = Field(default=None, description="The actual date when carrier picked up line item.", alias="carrierPickupDate")
    tracking_details: Optional[List[OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner]] = Field(default=None, description="The tracking details for the shipment containing the line item.", alias="trackingDetails")
    __properties: ClassVar[List[str]] = ["carrierCode", "carrierName", "quantity", "shippedDate", "estimatedDeliveryDate", "deliveredDate", "carrierPickupDate", "trackingDetails"]

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
        """Create an instance of OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tracking_details (list)
        _items = []
        if self.tracking_details:
            for _item in self.tracking_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['trackingDetails'] = _items
        # set to None if tracking_details (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_details is None and "tracking_details" in self.model_fields_set:
            _dict['trackingDetails'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrierCode": obj.get("carrierCode"),
            "carrierName": obj.get("carrierName"),
            "quantity": obj.get("quantity"),
            "shippedDate": obj.get("shippedDate"),
            "estimatedDeliveryDate": obj.get("estimatedDeliveryDate"),
            "deliveredDate": obj.get("deliveredDate"),
            "carrierPickupDate": obj.get("carrierPickupDate"),
            "trackingDetails": [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner.from_dict(_item) for _item in obj.get("trackingDetails")] if obj.get("trackingDetails") is not None else None
        })
        return _obj

