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
from typing_extensions import Annotated
from xi.sdk.resellers.models.order_create_request_additional_attributes_inner import OrderCreateRequestAdditionalAttributesInner
from xi.sdk.resellers.models.order_create_request_end_user_info import OrderCreateRequestEndUserInfo
from xi.sdk.resellers.models.order_create_request_lines_inner import OrderCreateRequestLinesInner
from xi.sdk.resellers.models.order_create_request_reseller_info import OrderCreateRequestResellerInfo
from xi.sdk.resellers.models.order_create_request_ship_to_info import OrderCreateRequestShipToInfo
from xi.sdk.resellers.models.order_create_request_shipment_details import OrderCreateRequestShipmentDetails
from xi.sdk.resellers.models.order_create_request_vmf import OrderCreateRequestVmf
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateRequest(BaseModel):
    """
    OrderCreateRequest
    """ # noqa: E501
    customer_order_number: Annotated[str, Field(strict=True, max_length=35)] = Field(description="The reseller's unique PO/Order number.", alias="customerOrderNumber")
    end_customer_order_number: Optional[StrictStr] = Field(default=None, description="The end user/customer's Purchase Order number.", alias="endCustomerOrderNumber")
    bill_to_address_id: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit.", alias="billToAddressId")
    special_bid_number: Optional[StrictStr] = Field(default=None, description="The bid number provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers.", alias="specialBidNumber")
    notes: Optional[StrictStr] = Field(default=None, description="Order level notes.")
    accept_back_order: Optional[StrictBool] = Field(default=None, description="ENUM [\"true\",\"false\"] - accept order if this item is backordered. This field along with shipComplete field decides the value of backorderflag. The value of this field is ignored when shipComplete field is present.", alias="acceptBackOrder")
    reseller_info: Optional[OrderCreateRequestResellerInfo] = Field(default=None, alias="resellerInfo")
    vmf: Optional[OrderCreateRequestVmf] = None
    ship_to_info: Optional[OrderCreateRequestShipToInfo] = Field(default=None, alias="shipToInfo")
    end_user_info: Optional[OrderCreateRequestEndUserInfo] = Field(default=None, alias="endUserInfo")
    lines: Optional[List[OrderCreateRequestLinesInner]] = Field(default=None, description="The line-level details of the order.")
    shipment_details: Optional[OrderCreateRequestShipmentDetails] = Field(default=None, alias="shipmentDetails")
    additional_attributes: Optional[List[OrderCreateRequestAdditionalAttributesInner]] = Field(default=None, description="Shipment-level additional attributes.", alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["customerOrderNumber", "endCustomerOrderNumber", "billToAddressId", "specialBidNumber", "notes", "acceptBackOrder", "resellerInfo", "vmf", "shipToInfo", "endUserInfo", "lines", "shipmentDetails", "additionalAttributes"]

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
        """Create an instance of OrderCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reseller_info
        if self.reseller_info:
            _dict['resellerInfo'] = self.reseller_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vmf
        if self.vmf:
            _dict['vmf'] = self.vmf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_info
        if self.ship_to_info:
            _dict['shipToInfo'] = self.ship_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_user_info
        if self.end_user_info:
            _dict['endUserInfo'] = self.end_user_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of shipment_details
        if self.shipment_details:
            _dict['shipmentDetails'] = self.shipment_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item in self.additional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "endCustomerOrderNumber": obj.get("endCustomerOrderNumber"),
            "billToAddressId": obj.get("billToAddressId"),
            "specialBidNumber": obj.get("specialBidNumber"),
            "notes": obj.get("notes"),
            "acceptBackOrder": obj.get("acceptBackOrder"),
            "resellerInfo": OrderCreateRequestResellerInfo.from_dict(obj["resellerInfo"]) if obj.get("resellerInfo") is not None else None,
            "vmf": OrderCreateRequestVmf.from_dict(obj["vmf"]) if obj.get("vmf") is not None else None,
            "shipToInfo": OrderCreateRequestShipToInfo.from_dict(obj["shipToInfo"]) if obj.get("shipToInfo") is not None else None,
            "endUserInfo": OrderCreateRequestEndUserInfo.from_dict(obj["endUserInfo"]) if obj.get("endUserInfo") is not None else None,
            "lines": [OrderCreateRequestLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "shipmentDetails": OrderCreateRequestShipmentDetails.from_dict(obj["shipmentDetails"]) if obj.get("shipmentDetails") is not None else None,
            "additionalAttributes": [OrderCreateRequestAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


