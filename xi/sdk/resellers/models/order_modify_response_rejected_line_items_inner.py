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
from typing import Optional, Set
from typing_extensions import Self

class OrderModifyResponseRejectedLineItemsInner(BaseModel):
    """
    OrderModifyResponseRejectedLineItemsInner
    """ # noqa: E501
    ingram_line_number: Optional[StrictStr] = Field(default=None, description="The IngramMicro line number for the failed line item.", alias="ingramLineNumber")
    customer_line_number: Optional[StrictStr] = Field(default=None, description="The reseller's line number of the failed line item for reference in their system.", alias="customerLineNumber")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="The IngramMicro part number for the failed line item.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="The vendor's part number for the failed line item.", alias="vendorPartNumber")
    quantity_ordered: Optional[StrictInt] = Field(default=None, description="The quantity ordered of the failed line item.", alias="quantityOrdered")
    reject_code: Optional[StrictStr] = Field(default=None, description="The rejection code for the failed line item.", alias="rejectCode")
    reject_reason: Optional[StrictStr] = Field(default=None, description="The rejection reason for the failed line item.", alias="rejectReason")
    __properties: ClassVar[List[str]] = ["ingramLineNumber", "customerLineNumber", "ingramPartNumber", "vendorPartNumber", "quantityOrdered", "rejectCode", "rejectReason"]

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
        """Create an instance of OrderModifyResponseRejectedLineItemsInner from a JSON string"""
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
        """Create an instance of OrderModifyResponseRejectedLineItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramLineNumber": obj.get("ingramLineNumber"),
            "customerLineNumber": obj.get("customerLineNumber"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "quantityOrdered": obj.get("quantityOrdered"),
            "rejectCode": obj.get("rejectCode"),
            "rejectReason": obj.get("rejectReason")
        })
        return _obj


