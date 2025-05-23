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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.validate_quote_response_lines_inner_vmf_additional_attributes_lines_inner import ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner
from typing import Optional, Set
from typing_extensions import Self

class ValidateQuoteResponseLinesInner(BaseModel):
    """
    ValidateQuoteResponseLinesInner
    """ # noqa: E501
    customer_line_number: Optional[StrictStr] = Field(default=None, description="The reseller's line item number for reference in their system.", alias="customerLineNumber")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Unique Ingram Micro part number.", alias="ingramPartNumber")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity of the line item.")
    vmf_additional_attributes_lines: Optional[List[ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner]] = Field(default=None, description="The object containing the list of fields required at a line level by the vendor.", alias="vmfAdditionalAttributesLines")
    __properties: ClassVar[List[str]] = ["customerLineNumber", "ingramPartNumber", "quantity", "vmfAdditionalAttributesLines"]

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
        """Create an instance of ValidateQuoteResponseLinesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vmf_additional_attributes_lines (list)
        _items = []
        if self.vmf_additional_attributes_lines:
            for _item_vmf_additional_attributes_lines in self.vmf_additional_attributes_lines:
                if _item_vmf_additional_attributes_lines:
                    _items.append(_item_vmf_additional_attributes_lines.to_dict())
            _dict['vmfAdditionalAttributesLines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidateQuoteResponseLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerLineNumber": obj.get("customerLineNumber"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "quantity": obj.get("quantity"),
            "vmfAdditionalAttributesLines": [ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner.from_dict(_item) for _item in obj["vmfAdditionalAttributesLines"]] if obj.get("vmfAdditionalAttributesLines") is not None else None
        })
        return _obj


