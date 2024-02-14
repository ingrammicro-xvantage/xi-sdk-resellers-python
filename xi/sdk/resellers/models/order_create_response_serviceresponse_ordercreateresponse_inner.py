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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner import OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateResponseServiceresponseOrdercreateresponseInner(BaseModel):
    """
    OrderCreateResponseServiceresponseOrdercreateresponseInner
    """ # noqa: E501
    numberoflineswithsuccess: Optional[StrictStr] = Field(default=None, description="Number of line items that were successful")
    numberoflineswitherror: Optional[StrictStr] = Field(default=None, description="Number of line items with error")
    numberoflineswithwarning: Optional[StrictStr] = Field(default=None, description="Number of line items with warnings")
    globalorderid: Optional[StrictStr] = Field(default=None, description="Ingram sales order number")
    ordertype: Optional[StrictStr] = Field(default=None, description="S=Stocked PO D=Direct Ship PO")
    ordertimestamp: Optional[StrictStr] = Field(default=None, description="Time order received")
    invoicingsystemorderid: Optional[StrictStr] = Field(default=None, description="Ingram Micro generated order number")
    taxamount: Optional[Union[StrictFloat, StrictInt]] = None
    freightamount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Freight amount customer pays for freight")
    orderamount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total amount of order with freight and taxes")
    lines: Optional[List[OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner]] = Field(default=None, description="Collection of lines", alias="Lines")
    __properties: ClassVar[List[str]] = ["numberoflineswithsuccess", "numberoflineswitherror", "numberoflineswithwarning", "globalorderid", "ordertype", "ordertimestamp", "invoicingsystemorderid", "taxamount", "freightamount", "orderamount", "Lines"]

    @field_validator('ordertype')
    def ordertype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['S', 'D']):
            raise ValueError("must be one of enum values ('S', 'D')")
        return value

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
        """Create an instance of OrderCreateResponseServiceresponseOrdercreateresponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Lines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCreateResponseServiceresponseOrdercreateresponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numberoflineswithsuccess": obj.get("numberoflineswithsuccess"),
            "numberoflineswitherror": obj.get("numberoflineswitherror"),
            "numberoflineswithwarning": obj.get("numberoflineswithwarning"),
            "globalorderid": obj.get("globalorderid"),
            "ordertype": obj.get("ordertype"),
            "ordertimestamp": obj.get("ordertimestamp"),
            "invoicingsystemorderid": obj.get("invoicingsystemorderid"),
            "taxamount": obj.get("taxamount"),
            "freightamount": obj.get("freightamount"),
            "orderamount": obj.get("orderamount"),
            "Lines": [OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner.from_dict(_item) for _item in obj["Lines"]] if obj.get("Lines") is not None else None
        })
        return _obj


