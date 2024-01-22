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
from xi.sdk.resellers.models.order_modify_request_servicerequest_ordermodifyrequest_headerdata import OrderModifyRequestServicerequestOrdermodifyrequestHeaderdata
from xi.sdk.resellers.models.order_modify_request_servicerequest_ordermodifyrequest_linedata_inner import OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner
from xi.sdk.resellers.models.order_modify_request_servicerequest_ordermodifyrequest_shipto import OrderModifyRequestServicerequestOrdermodifyrequestShipto
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderModifyRequestServicerequestOrdermodifyrequest(BaseModel):
    """
    OrderModifyRequestServicerequestOrdermodifyrequest
    """ # noqa: E501
    ingramorderbranch: Optional[StrictStr] = None
    ingramordernumber: Optional[StrictStr] = None
    ingramorderdist: Optional[StrictStr] = None
    ingramordership: Optional[StrictStr] = None
    customerponumber: Optional[StrictStr] = None
    shipto: Optional[OrderModifyRequestServicerequestOrdermodifyrequestShipto] = None
    headerdata: Optional[OrderModifyRequestServicerequestOrdermodifyrequestHeaderdata] = None
    linedata: Optional[List[OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner]] = None
    __properties: ClassVar[List[str]] = ["ingramorderbranch", "ingramordernumber", "ingramorderdist", "ingramordership", "customerponumber", "shipto", "headerdata", "linedata"]

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
        """Create an instance of OrderModifyRequestServicerequestOrdermodifyrequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shipto
        if self.shipto:
            _dict['shipto'] = self.shipto.to_dict()
        # override the default output from pydantic by calling `to_dict()` of headerdata
        if self.headerdata:
            _dict['headerdata'] = self.headerdata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in linedata (list)
        _items = []
        if self.linedata:
            for _item in self.linedata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['linedata'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderModifyRequestServicerequestOrdermodifyrequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramorderbranch": obj.get("ingramorderbranch"),
            "ingramordernumber": obj.get("ingramordernumber"),
            "ingramorderdist": obj.get("ingramorderdist"),
            "ingramordership": obj.get("ingramordership"),
            "customerponumber": obj.get("customerponumber"),
            "shipto": OrderModifyRequestServicerequestOrdermodifyrequestShipto.from_dict(obj.get("shipto")) if obj.get("shipto") is not None else None,
            "headerdata": OrderModifyRequestServicerequestOrdermodifyrequestHeaderdata.from_dict(obj.get("headerdata")) if obj.get("headerdata") is not None else None,
            "linedata": [OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner.from_dict(_item) for _item in obj.get("linedata")] if obj.get("linedata") is not None else None
        })
        return _obj

