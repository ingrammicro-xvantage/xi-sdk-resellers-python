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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner_serial_info_inner import AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner
from xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner_vmf_additional_attributes_lines_inner import AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner
from typing import Optional, Set
from typing_extensions import Self

class AsyncOrderCreateDTOWarrantyInfoInner(BaseModel):
    """
    AsyncOrderCreateDTOWarrantyInfoInner
    """ # noqa: E501
    hardware_line_link: Optional[StrictStr] = Field(default=None, alias="hardwareLineLink")
    warranty_line_link: Optional[StrictStr] = Field(default=None, alias="warrantyLineLink")
    direct_line_link: Optional[StrictStr] = Field(default=None, alias="directLineLink")
    serial_info: Optional[List[AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner]] = Field(default=None, alias="serialInfo")
    vmf_additional_attributes_lines: Optional[List[AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner]] = Field(default=None, description="The object containing the list of fields required at a line level by the vendor.", alias="vmfAdditionalAttributesLines")
    __properties: ClassVar[List[str]] = ["hardwareLineLink", "warrantyLineLink", "directLineLink", "serialInfo", "vmfAdditionalAttributesLines"]

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
        """Create an instance of AsyncOrderCreateDTOWarrantyInfoInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in serial_info (list)
        _items = []
        if self.serial_info:
            for _item in self.serial_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serialInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vmf_additional_attributes_lines (list)
        _items = []
        if self.vmf_additional_attributes_lines:
            for _item in self.vmf_additional_attributes_lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vmfAdditionalAttributesLines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AsyncOrderCreateDTOWarrantyInfoInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hardwareLineLink": obj.get("hardwareLineLink"),
            "warrantyLineLink": obj.get("warrantyLineLink"),
            "directLineLink": obj.get("directLineLink"),
            "serialInfo": [AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner.from_dict(_item) for _item in obj["serialInfo"]] if obj.get("serialInfo") is not None else None,
            "vmfAdditionalAttributesLines": [AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner.from_dict(_item) for _item in obj["vmfAdditionalAttributesLines"]] if obj.get("vmfAdditionalAttributesLines") is not None else None
        })
        return _obj


