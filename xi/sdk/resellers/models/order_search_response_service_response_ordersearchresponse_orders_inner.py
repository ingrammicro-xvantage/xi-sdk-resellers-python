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
from xi.sdk.resellers.models.order_search_response_service_response_ordersearchresponse_orders_inner_links import OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks
from xi.sdk.resellers.models.order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner import OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner(BaseModel):
    """
    OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner
    """ # noqa: E501
    ordernumber: StrictStr = Field(description="Ingram micro sales order number")
    entrytimestamp: StrictStr = Field(description="The order creation date-time in UTC format")
    customerordernumber: Optional[StrictStr] = Field(default=None, description="PO/Order number submitted while creating the order")
    suborders: Optional[List[OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner]] = Field(default=None, description="An order MAY get divided into various sub orders, for example if the SKUs are being shipped from different warehouse.")
    links: Optional[OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks] = None
    __properties: ClassVar[List[str]] = ["ordernumber", "entrytimestamp", "customerordernumber", "suborders", "links"]

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
        """Create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in suborders (list)
        _items = []
        if self.suborders:
            for _item in self.suborders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['suborders'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ordernumber": obj.get("ordernumber"),
            "entrytimestamp": obj.get("entrytimestamp"),
            "customerordernumber": obj.get("customerordernumber"),
            "suborders": [OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner.from_dict(_item) for _item in obj.get("suborders")] if obj.get("suborders") is not None else None,
            "links": OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None
        })
        return _obj


