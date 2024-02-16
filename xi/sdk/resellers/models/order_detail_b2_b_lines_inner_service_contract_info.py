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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_contract_info import OrderDetailB2BLinesInnerServiceContractInfoContractInfo
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_license_info import OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_subscriptions import OrderDetailB2BLinesInnerServiceContractInfoSubscriptions
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BLinesInnerServiceContractInfo(BaseModel):
    """
    OrderDetailB2BLinesInnerServiceContractInfo
    """ # noqa: E501
    contract_info: Optional[OrderDetailB2BLinesInnerServiceContractInfoContractInfo] = Field(default=None, alias="contractInfo")
    subscriptions: Optional[OrderDetailB2BLinesInnerServiceContractInfoSubscriptions] = None
    license_info: Optional[OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo] = Field(default=None, alias="licenseInfo")
    __properties: ClassVar[List[str]] = ["contractInfo", "subscriptions", "licenseInfo"]

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
        """Create an instance of OrderDetailB2BLinesInnerServiceContractInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contract_info
        if self.contract_info:
            _dict['contractInfo'] = self.contract_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subscriptions
        if self.subscriptions:
            _dict['subscriptions'] = self.subscriptions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of license_info
        if self.license_info:
            _dict['licenseInfo'] = self.license_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailB2BLinesInnerServiceContractInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contractInfo": OrderDetailB2BLinesInnerServiceContractInfoContractInfo.from_dict(obj["contractInfo"]) if obj.get("contractInfo") is not None else None,
            "subscriptions": OrderDetailB2BLinesInnerServiceContractInfoSubscriptions.from_dict(obj["subscriptions"]) if obj.get("subscriptions") is not None else None,
            "licenseInfo": OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo.from_dict(obj["licenseInfo"]) if obj.get("licenseInfo") is not None else None
        })
        return _obj


