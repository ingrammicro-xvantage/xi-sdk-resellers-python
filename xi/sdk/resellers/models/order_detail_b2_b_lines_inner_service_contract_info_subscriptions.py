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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BLinesInnerServiceContractInfoSubscriptions(BaseModel):
    """
    OrderDetailB2BLinesInnerServiceContractInfoSubscriptions
    """ # noqa: E501
    subscription_id: Optional[StrictStr] = Field(default=None, description="The ID of the subscription.", alias="subscriptionId")
    subscription_term: Optional[StrictStr] = Field(default=None, description="The term of the subscription.", alias="subscriptionTerm")
    renewal_term: Optional[StrictStr] = Field(default=None, description="The renewal term of the subscription.", alias="renewalTerm")
    billing_model: Optional[StrictStr] = Field(default=None, description="The billing model of the billing.", alias="billingModel")
    subcription_start_date: Optional[StrictStr] = Field(default=None, description="Start date of the subcription.", alias="subcriptionStartDate")
    subcription_end_date: Optional[StrictStr] = Field(default=None, description="End date of the subcription.", alias="subcriptionEndDate")
    __properties: ClassVar[List[str]] = ["subscriptionId", "subscriptionTerm", "renewalTerm", "billingModel", "subcriptionStartDate", "subcriptionEndDate"]

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
        """Create an instance of OrderDetailB2BLinesInnerServiceContractInfoSubscriptions from a JSON string"""
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
        """Create an instance of OrderDetailB2BLinesInnerServiceContractInfoSubscriptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subscriptionId": obj.get("subscriptionId"),
            "subscriptionTerm": obj.get("subscriptionTerm"),
            "renewalTerm": obj.get("renewalTerm"),
            "billingModel": obj.get("billingModel"),
            "subcriptionStartDate": obj.get("subcriptionStartDate"),
            "subcriptionEndDate": obj.get("subcriptionEndDate")
        })
        return _obj


