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
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BLinesInnerScheduleLinesInner(BaseModel):
    """
    OrderDetailB2BLinesInnerScheduleLinesInner
    """ # noqa: E501
    line_number: Optional[StrictStr] = Field(default=None, description="Line number.", alias="lineNumber")
    schedule_line_date: Optional[StrictStr] = Field(default=None, description="schedule Line Date.", alias="scheduleLineDate")
    requested_quantity: Optional[StrictStr] = Field(default=None, description="Requested quantity.", alias="requestedQuantity")
    confirmed_quantity: Optional[StrictStr] = Field(default=None, description="Confirmed quantity.", alias="confirmedQuantity")
    goods_issue_date: Optional[StrictStr] = Field(default=None, description="Date when good issued.", alias="goodsIssueDate")
    __properties: ClassVar[List[str]] = ["lineNumber", "scheduleLineDate", "requestedQuantity", "confirmedQuantity", "goodsIssueDate"]

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
        """Create an instance of OrderDetailB2BLinesInnerScheduleLinesInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailB2BLinesInnerScheduleLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lineNumber": obj.get("lineNumber"),
            "scheduleLineDate": obj.get("scheduleLineDate"),
            "requestedQuantity": obj.get("requestedQuantity"),
            "confirmedQuantity": obj.get("confirmedQuantity"),
            "goodsIssueDate": obj.get("goodsIssueDate")
        })
        return _obj


