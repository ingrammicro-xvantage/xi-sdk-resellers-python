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
from typing_extensions import Annotated
from xi.sdk.resellers.models.order_create_request_lines_inner_warranty_info_inner_serial_info_inner import OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderCreateRequestLinesInnerWarrantyInfoInner(BaseModel):
    """
    OrderCreateRequestLinesInnerWarrantyInfoInner
    """ # noqa: E501
    direct_line_link: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Unique value to link hardware and warranty lines. Should be used only when products are purchased from both Ingram and/or vendor but the warranty is purchased through Ingram for them.", alias="directLineLink")
    warranty_line_link: Optional[StrictStr] = Field(default=None, description="Customer line number of the hardware product in this request for linkage, either hardwareLineLink or warrantyLineLink can be used in a line.", alias="warrantyLineLink")
    hardware_line_link: Optional[StrictStr] = Field(default=None, description="Customer line number of the warranty product in this request for linkage, either hardwareLineLink or warrantyLineLink can be used in a line ", alias="hardwareLineLink")
    serial_info: Optional[List[OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner]] = Field(default=None, description="Serial information of the hardware to be associated with the warranty, applicable on post sale orders.", alias="serialInfo")
    __properties: ClassVar[List[str]] = ["directLineLink", "warrantyLineLink", "hardwareLineLink", "serialInfo"]

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
        """Create an instance of OrderCreateRequestLinesInnerWarrantyInfoInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in serial_info (list)
        _items = []
        if self.serial_info:
            for _item in self.serial_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serialInfo'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderCreateRequestLinesInnerWarrantyInfoInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "directLineLink": obj.get("directLineLink"),
            "warrantyLineLink": obj.get("warrantyLineLink"),
            "hardwareLineLink": obj.get("hardwareLineLink"),
            "serialInfo": [OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner.from_dict(_item) for _item in obj.get("serialInfo")] if obj.get("serialInfo") is not None else None
        })
        return _obj


