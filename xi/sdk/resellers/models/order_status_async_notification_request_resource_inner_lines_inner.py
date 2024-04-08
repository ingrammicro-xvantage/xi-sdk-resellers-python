# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_lines_inner_serial_number_details_inner import OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner
from xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner import OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner
from typing import Optional, Set
from typing_extensions import Self

class OrderStatusAsyncNotificationRequestResourceInnerLinesInner(BaseModel):
    """
    OrderStatusAsyncNotificationRequestResourceInnerLinesInner
    """ # noqa: E501
    line_number: Optional[StrictStr] = Field(default=None, description="The Ingram Micro line number for the product", alias="LineNumber")
    sub_order_number: Optional[StrictStr] = Field(default=None, description="The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number.", alias="subOrderNumber")
    line_status: Optional[StrictStr] = Field(default=None, description="The status for the line item in the order. One of: Backordered, Open, Shipped", alias="lineStatus")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="The Ingram Micro part number for the line item.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="The vendor part number for the line item.", alias="vendorPartNumber")
    requested_quantity: Optional[StrictStr] = Field(default=None, description="The quantity of the line item requested.", alias="requestedQuantity")
    shipped_quantity: Optional[StrictStr] = Field(default=None, description="The quantity of the line item that has been shipped.", alias="shippedQuantity")
    backordered_quantity: Optional[StrictStr] = Field(default=None, description="The quantity of the line item that is backordered.", alias="backorderedQuantity")
    shipment_details: Optional[List[OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner]] = Field(default=None, alias="shipmentDetails")
    serial_number_details: Optional[List[OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner]] = Field(default=None, alias="serialNumberDetails")
    __properties: ClassVar[List[str]] = ["LineNumber", "subOrderNumber", "lineStatus", "ingramPartNumber", "vendorPartNumber", "requestedQuantity", "shippedQuantity", "backorderedQuantity", "shipmentDetails", "serialNumberDetails"]

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
        """Create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in shipment_details (list)
        _items = []
        if self.shipment_details:
            for _item in self.shipment_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shipmentDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in serial_number_details (list)
        _items = []
        if self.serial_number_details:
            for _item in self.serial_number_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serialNumberDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LineNumber": obj.get("LineNumber"),
            "subOrderNumber": obj.get("subOrderNumber"),
            "lineStatus": obj.get("lineStatus"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "requestedQuantity": obj.get("requestedQuantity"),
            "shippedQuantity": obj.get("shippedQuantity"),
            "backorderedQuantity": obj.get("backorderedQuantity"),
            "shipmentDetails": [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner.from_dict(_item) for _item in obj["shipmentDetails"]] if obj.get("shipmentDetails") is not None else None,
            "serialNumberDetails": [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner.from_dict(_item) for _item in obj["serialNumberDetails"]] if obj.get("serialNumberDetails") is not None else None
        })
        return _obj


