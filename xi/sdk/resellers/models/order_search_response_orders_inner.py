# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.order_search_response_orders_inner_links import OrderSearchResponseOrdersInnerLinks
from xi.sdk.resellers.models.order_search_response_orders_inner_sub_orders_inner import OrderSearchResponseOrdersInnerSubOrdersInner
from typing import Optional, Set
from typing_extensions import Self

class OrderSearchResponseOrdersInner(BaseModel):
    """
    OrderSearchResponseOrdersInner
    """ # noqa: E501
    ingram_order_number: Optional[StrictStr] = Field(default=None, description="The Ingram Micro order number.", alias="ingramOrderNumber")
    ingram_order_date: Optional[StrictStr] = Field(default=None, description="The date the order was created(UTC).", alias="ingramOrderDate")
    customer_order_number: Optional[StrictStr] = Field(default=None, description="The reseller's order number for reference in their system.", alias="customerOrderNumber")
    vendor_sales_order_number: Optional[StrictStr] = Field(default=None, description="The vendor's order number.(only for D-Type Orders)", alias="vendorSalesOrderNumber")
    vendor_name: Optional[StrictStr] = Field(default=None, description="The name of the vendor.", alias="vendorName")
    end_user_company_name: Optional[StrictStr] = Field(default=None, description="The company name of the end user/customer.", alias="endUserCompanyName")
    order_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total of the order.", alias="orderTotal")
    order_status: Optional[StrictStr] = Field(default=None, description="The header-level status of the order.(OPEN/CLOSED/CANCELLED)", alias="orderStatus")
    sub_orders: Optional[List[OrderSearchResponseOrdersInnerSubOrdersInner]] = Field(default=None, description="Individual Ingram Micro order numbers associated with a single reseller PO.", alias="subOrders")
    links: Optional[OrderSearchResponseOrdersInnerLinks] = None
    __properties: ClassVar[List[str]] = ["ingramOrderNumber", "ingramOrderDate", "customerOrderNumber", "vendorSalesOrderNumber", "vendorName", "endUserCompanyName", "orderTotal", "orderStatus", "subOrders", "links"]

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
        """Create an instance of OrderSearchResponseOrdersInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sub_orders (list)
        _items = []
        if self.sub_orders:
            for _item_sub_orders in self.sub_orders:
                if _item_sub_orders:
                    _items.append(_item_sub_orders.to_dict())
            _dict['subOrders'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderSearchResponseOrdersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramOrderNumber": obj.get("ingramOrderNumber"),
            "ingramOrderDate": obj.get("ingramOrderDate"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "vendorSalesOrderNumber": obj.get("vendorSalesOrderNumber"),
            "vendorName": obj.get("vendorName"),
            "endUserCompanyName": obj.get("endUserCompanyName"),
            "orderTotal": obj.get("orderTotal"),
            "orderStatus": obj.get("orderStatus"),
            "subOrders": [OrderSearchResponseOrdersInnerSubOrdersInner.from_dict(_item) for _item in obj["subOrders"]] if obj.get("subOrders") is not None else None,
            "links": OrderSearchResponseOrdersInnerLinks.from_dict(obj["links"]) if obj.get("links") is not None else None
        })
        return _obj


