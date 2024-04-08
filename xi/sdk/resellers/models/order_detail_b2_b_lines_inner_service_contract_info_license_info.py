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

class OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo(BaseModel):
    """
    OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo
    """ # noqa: E501
    license_number: Optional[List[StrictStr]] = Field(default=None, description="License numbers.", alias="licenseNumber")
    license_start_date: Optional[StrictStr] = Field(default=None, description="Start Date of the license.", alias="licenseStartDate")
    license_end_date: Optional[StrictStr] = Field(default=None, description="End Date of the license.", alias="licenseEndDate")
    description: Optional[StrictStr] = Field(default=None, description="Description of the license.")
    quantity: Optional[StrictStr] = Field(default=None, description="Quantity of the license.")
    __properties: ClassVar[List[str]] = ["licenseNumber", "licenseStartDate", "licenseEndDate", "description", "quantity"]

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
        """Create an instance of OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo from a JSON string"""
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
        # set to None if license_number (nullable) is None
        # and model_fields_set contains the field
        if self.license_number is None and "license_number" in self.model_fields_set:
            _dict['licenseNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "licenseNumber": obj.get("licenseNumber"),
            "licenseStartDate": obj.get("licenseStartDate"),
            "licenseEndDate": obj.get("licenseEndDate"),
            "description": obj.get("description"),
            "quantity": obj.get("quantity")
        })
        return _obj


