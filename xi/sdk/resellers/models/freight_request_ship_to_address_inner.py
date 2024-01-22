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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FreightRequestShipToAddressInner(BaseModel):
    """
    FreightRequestShipToAddressInner
    """ # noqa: E501
    company_name: Optional[StrictStr] = Field(default=None, description="The name of the company the order will be shipped to.", alias="companyName")
    address_line1: Optional[StrictStr] = Field(default=None, description="Line 1 of the address the order will be shipped to.", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="Line 2 of the address the order will be shipped to.", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="Line 3 of the address the order will be shipped to.", alias="addressLine3")
    city: Optional[StrictStr] = Field(default=None, description="The city the order will be shipped to.")
    state: Optional[StrictStr] = Field(default=None, description="The state the order will be shipped to.")
    postal_code: Optional[StrictStr] = Field(default=None, description="The zip or postal code the order will be shipped to.", alias="postalCode")
    country_code: Optional[StrictStr] = Field(default=None, description="The two-character ISO country code the order will be shipped to.", alias="countryCode")
    __properties: ClassVar[List[str]] = ["companyName", "addressLine1", "addressLine2", "addressLine3", "city", "state", "postalCode", "countryCode"]

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
        """Create an instance of FreightRequestShipToAddressInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FreightRequestShipToAddressInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "companyName": obj.get("companyName"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode")
        })
        return _obj

