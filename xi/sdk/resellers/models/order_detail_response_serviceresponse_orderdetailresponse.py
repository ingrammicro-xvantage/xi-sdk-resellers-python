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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_billtoaddress import OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_commentlines_inner import OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_enduserinfo import OrderDetailResponseServiceresponseOrderdetailresponseEnduserinfo
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_extendedspecs_inner import OrderDetailResponseServiceresponseOrderdetailresponseExtendedspecsInner
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_lines_inner import OrderDetailResponseServiceresponseOrderdetailresponseLinesInner
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_miscfeeline_inner import OrderDetailResponseServiceresponseOrderdetailresponseMiscfeelineInner
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_shiptoaddress import OrderDetailResponseServiceresponseOrderdetailresponseShiptoaddress
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderDetailResponseServiceresponseOrderdetailresponse(BaseModel):
    """
    OrderDetailResponseServiceresponseOrderdetailresponse
    """ # noqa: E501
    ordernumber: Optional[StrictStr] = None
    ordertype: Optional[StrictStr] = Field(default=None, description="Order Type   B - BRANCH TRANSFER C - CASH ORDER D - DIRECT ORDER F - FUTURE ORDER P - SPECIAL ORDER Q - QUOTE ORDER S - STOCK ORDER M - MEMO ORDER")
    customerordernumber: Optional[StrictStr] = Field(default=None, description="Customer PO number")
    enduserponumber: Optional[StrictStr] = Field(default=None, description="End User PO number")
    orderstatus: Optional[StrictStr] = Field(default=None, description="Status of order within Ingram system S - SALES HOLD H - TAG HOLD I - INVOICED P - PENDING E - BILLING ERROR F - FORCE BILLING V - VOIDED T - TRANSFERRED D - HOLD SHIPMENT R - RELEASED O - IM ONLINE HOLD U - BILL FOR HISTORY ONLY W - ORDER NOT PRINTED A - DROP SHIP HOLD B - INTERNET CUST ORIG HOLD 1 - PICKED 2 - INSPECTED 3 - PACKED 4 - SHIPPED C - CREDIT HOLD 9 - CISCO 3A6 Q - RMA HOLD G - CREDIT HOLD N - CREDIT HOLD")
    entrytimestamp: Optional[StrictStr] = Field(default=None, description="Time stamp of the order placed")
    entrymethoddescription: Optional[StrictStr] = Field(default=None, description="Description of the entry method ")
    ordertotalvalue: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total order value")
    ordersubtotal: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Subtotal order value")
    freightamount: Optional[StrictStr] = Field(default=None, description="Freight charges")
    currencycode: Optional[StrictStr] = Field(default=None, description="Country specific currency code")
    totalweight: Optional[StrictStr] = Field(default=None, description="Total order weight. unit -- North america - Pounds , other countries will be KG")
    totaltax: Optional[StrictStr] = Field(default=None, description="total tax on the orders placed")
    billtoaddress: Optional[OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress] = None
    shiptoaddress: Optional[OrderDetailResponseServiceresponseOrderdetailresponseShiptoaddress] = None
    enduserinfo: Optional[OrderDetailResponseServiceresponseOrderdetailresponseEnduserinfo] = None
    lines: Optional[List[OrderDetailResponseServiceresponseOrderdetailresponseLinesInner]] = None
    commentlines: Optional[List[OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner]] = None
    miscfeeline: Optional[List[OrderDetailResponseServiceresponseOrderdetailresponseMiscfeelineInner]] = None
    extendedspecs: Optional[List[OrderDetailResponseServiceresponseOrderdetailresponseExtendedspecsInner]] = None
    __properties: ClassVar[List[str]] = ["ordernumber", "ordertype", "customerordernumber", "enduserponumber", "orderstatus", "entrytimestamp", "entrymethoddescription", "ordertotalvalue", "ordersubtotal", "freightamount", "currencycode", "totalweight", "totaltax", "billtoaddress", "shiptoaddress", "enduserinfo", "lines", "commentlines", "miscfeeline", "extendedspecs"]

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
        """Create an instance of OrderDetailResponseServiceresponseOrderdetailresponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billtoaddress
        if self.billtoaddress:
            _dict['billtoaddress'] = self.billtoaddress.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shiptoaddress
        if self.shiptoaddress:
            _dict['shiptoaddress'] = self.shiptoaddress.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enduserinfo
        if self.enduserinfo:
            _dict['enduserinfo'] = self.enduserinfo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in commentlines (list)
        _items = []
        if self.commentlines:
            for _item in self.commentlines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['commentlines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in miscfeeline (list)
        _items = []
        if self.miscfeeline:
            for _item in self.miscfeeline:
                if _item:
                    _items.append(_item.to_dict())
            _dict['miscfeeline'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in extendedspecs (list)
        _items = []
        if self.extendedspecs:
            for _item in self.extendedspecs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['extendedspecs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderDetailResponseServiceresponseOrderdetailresponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ordernumber": obj.get("ordernumber"),
            "ordertype": obj.get("ordertype"),
            "customerordernumber": obj.get("customerordernumber"),
            "enduserponumber": obj.get("enduserponumber"),
            "orderstatus": obj.get("orderstatus"),
            "entrytimestamp": obj.get("entrytimestamp"),
            "entrymethoddescription": obj.get("entrymethoddescription"),
            "ordertotalvalue": obj.get("ordertotalvalue"),
            "ordersubtotal": obj.get("ordersubtotal"),
            "freightamount": obj.get("freightamount"),
            "currencycode": obj.get("currencycode"),
            "totalweight": obj.get("totalweight"),
            "totaltax": obj.get("totaltax"),
            "billtoaddress": OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress.from_dict(obj.get("billtoaddress")) if obj.get("billtoaddress") is not None else None,
            "shiptoaddress": OrderDetailResponseServiceresponseOrderdetailresponseShiptoaddress.from_dict(obj.get("shiptoaddress")) if obj.get("shiptoaddress") is not None else None,
            "enduserinfo": OrderDetailResponseServiceresponseOrderdetailresponseEnduserinfo.from_dict(obj.get("enduserinfo")) if obj.get("enduserinfo") is not None else None,
            "lines": [OrderDetailResponseServiceresponseOrderdetailresponseLinesInner.from_dict(_item) for _item in obj.get("lines")] if obj.get("lines") is not None else None,
            "commentlines": [OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner.from_dict(_item) for _item in obj.get("commentlines")] if obj.get("commentlines") is not None else None,
            "miscfeeline": [OrderDetailResponseServiceresponseOrderdetailresponseMiscfeelineInner.from_dict(_item) for _item in obj.get("miscfeeline")] if obj.get("miscfeeline") is not None else None,
            "extendedspecs": [OrderDetailResponseServiceresponseOrderdetailresponseExtendedspecsInner.from_dict(_item) for _item in obj.get("extendedspecs")] if obj.get("extendedspecs") is not None else None
        })
        return _obj


