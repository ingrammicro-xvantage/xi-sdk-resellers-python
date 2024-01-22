# coding: utf-8

"""
    Reseller API

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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner import OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner(BaseModel):
    """
    OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner
    """ # noqa: E501
    shipment_date: Optional[StrictStr] = Field(default=None, description="The date the line item was shipped.", alias="shipmentDate")
    ship_from_warehouse_id: Optional[StrictStr] = Field(default=None, description="The ID of the warehouse the product will ship from.", alias="shipFromWarehouseId")
    warehouse_name: Optional[StrictStr] = Field(default=None, description="\"\"", alias="warehouseName")
    carrier_code: Optional[StrictStr] = Field(default=None, description="The carrier code for the shipment containing the  line item.", alias="carrierCode")
    carrier_name: Optional[StrictStr] = Field(default=None, description="The name of the carrier of the shipment containing   the line item.", alias="carrierName")
    package_details: Optional[List[OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner]] = Field(default=None, alias="packageDetails")
    __properties: ClassVar[List[str]] = ["shipmentDate", "shipFromWarehouseId", "warehouseName", "carrierCode", "carrierName", "packageDetails"]

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
        """Create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in package_details (list)
        _items = []
        if self.package_details:
            for _item in self.package_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['packageDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipmentDate": obj.get("shipmentDate"),
            "shipFromWarehouseId": obj.get("shipFromWarehouseId"),
            "warehouseName": obj.get("warehouseName"),
            "carrierCode": obj.get("carrierCode"),
            "carrierName": obj.get("carrierName"),
            "packageDetails": [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner.from_dict(_item) for _item in obj.get("packageDetails")] if obj.get("packageDetails") is not None else None
        })
        return _obj

