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
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BLinesInnerServiceContractInfoContractInfo(BaseModel):
    """
    OrderDetailB2BLinesInnerServiceContractInfoContractInfo
    """ # noqa: E501
    contract_description: Optional[StrictStr] = Field(default=None, description="The description of the contract.", alias="contractDescription")
    contract_number: Optional[StrictStr] = Field(default=None, description="Contract number.", alias="contractNumber")
    contract_status: Optional[StrictStr] = Field(default=None, description="The status of the contract.", alias="contractStatus")
    contract_start_date: Optional[StrictStr] = Field(default=None, description="Start date of the contract.", alias="contractStartDate")
    contract_end_date: Optional[StrictStr] = Field(default=None, description="End date of the contract.", alias="contractEndDate")
    contract_duration: Optional[StrictStr] = Field(default=None, description="The duration of the contract.", alias="contractDuration")
    __properties: ClassVar[List[str]] = ["contractDescription", "contractNumber", "contractStatus", "contractStartDate", "contractEndDate", "contractDuration"]

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
        """Create an instance of OrderDetailB2BLinesInnerServiceContractInfoContractInfo from a JSON string"""
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
        """Create an instance of OrderDetailB2BLinesInnerServiceContractInfoContractInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contractDescription": obj.get("contractDescription"),
            "contractNumber": obj.get("contractNumber"),
            "contractStatus": obj.get("contractStatus"),
            "contractStartDate": obj.get("contractStartDate"),
            "contractEndDate": obj.get("contractEndDate"),
            "contractDuration": obj.get("contractDuration")
        })
        return _obj


