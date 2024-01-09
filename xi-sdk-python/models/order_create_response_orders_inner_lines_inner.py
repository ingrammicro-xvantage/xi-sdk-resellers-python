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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from xi-sdk-python.models.order_create_response_orders_inner_lines_inner_additional_attributes_inner import OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner
from xi-sdk-python.models.order_create_response_orders_inner_lines_inner_shipment_details_inner import OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderCreateResponseOrdersInnerLinesInner(BaseModel):
    """
    OrderCreateResponseOrdersInnerLinesInner
    """ # noqa: E501
    sub_order_number: Optional[StrictStr] = Field(default=None, description="The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number.", alias="subOrderNumber")
    ingram_line_number: Optional[StrictStr] = Field(default=None, description="The Ingram Micro line number for the product.", alias="ingramLineNumber")
    customer_line_number: Optional[StrictStr] = Field(default=None, description="The reseller's line number for reference in their system.", alias="customerLineNumber")
    line_status: Optional[StrictStr] = Field(default=None, description="The status for the line item in the order. One of: Backordered, Open", alias="lineStatus")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="The Ingram Micro part number for the line item.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="The vendor part number for the line item.", alias="vendorPartNumber")
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unit price for the line item.", alias="unitPrice")
    extended_unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The extended list price (unit price X quantity) for the line item.", alias="extendedUnitPrice")
    quantity_ordered: Optional[StrictInt] = Field(default=None, description="The quantity of the line item ordered.", alias="quantityOrdered")
    quantity_confirmed: Optional[StrictInt] = Field(default=None, description="The quantity of the line item that has been confirmed.", alias="quantityConfirmed")
    quantity_back_ordered: Optional[StrictInt] = Field(default=None, description="The quantity of the line item that is backordered.", alias="quantityBackOrdered")
    special_bid_number: Optional[StrictStr] = Field(default=None, description="The bid number for the line item provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers.", alias="specialBidNumber")
    notes: Optional[StrictStr] = Field(default=None, description="Line-level notes.")
    shipment_details: Optional[List[OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner]] = Field(default=None, description="The shipment details for the line item.", alias="shipmentDetails")
    additional_attributes: Optional[List[OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner]] = Field(default=None, description="SAP requested and country-specific line level details.", alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["subOrderNumber", "ingramLineNumber", "customerLineNumber", "lineStatus", "ingramPartNumber", "vendorPartNumber", "unitPrice", "extendedUnitPrice", "quantityOrdered", "quantityConfirmed", "quantityBackOrdered", "specialBidNumber", "notes", "shipmentDetails", "additionalAttributes"]

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
        """Create an instance of OrderCreateResponseOrdersInnerLinesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in shipment_details (list)
        _items = []
        if self.shipment_details:
            for _item in self.shipment_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shipmentDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item in self.additional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderCreateResponseOrdersInnerLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subOrderNumber": obj.get("subOrderNumber"),
            "ingramLineNumber": obj.get("ingramLineNumber"),
            "customerLineNumber": obj.get("customerLineNumber"),
            "lineStatus": obj.get("lineStatus"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "unitPrice": obj.get("unitPrice"),
            "extendedUnitPrice": obj.get("extendedUnitPrice"),
            "quantityOrdered": obj.get("quantityOrdered"),
            "quantityConfirmed": obj.get("quantityConfirmed"),
            "quantityBackOrdered": obj.get("quantityBackOrdered"),
            "specialBidNumber": obj.get("specialBidNumber"),
            "notes": obj.get("notes"),
            "shipmentDetails": [OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner.from_dict(_item) for _item in obj.get("shipmentDetails")] if obj.get("shipmentDetails") is not None else None,
            "additionalAttributes": [OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner.from_dict(_item) for _item in obj.get("additionalAttributes")] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


