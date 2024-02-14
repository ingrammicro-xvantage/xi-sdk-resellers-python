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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RenewalsDetailsResponseEndUserInfoInner(BaseModel):
    """
    RenewalsDetailsResponseEndUserInfoInner
    """ # noqa: E501
    contact: Optional[StrictStr] = Field(default=None, description="The contact name for the end user/customer.")
    name1: Optional[StrictStr] = Field(default=None, description="The name1 for the end user/customer.")
    name2: Optional[StrictStr] = Field(default=None, description="The name2 for the end user/customer.")
    company_name: Optional[StrictStr] = Field(default=None, description="The company name for the end user/customer.", alias="companyName")
    address_line1: Optional[StrictStr] = Field(default=None, description="The address line 1 for the end user/customer.", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="The address line 2 for the end user/customer.", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="The address line 3 for the end user/customer.", alias="addressLine3")
    address_line4: Optional[StrictStr] = Field(default=None, description="The address line 4 for the end user/customer.", alias="addressLine4")
    city: Optional[StrictStr] = Field(default=None, description="The end user/customer's city.")
    state: Optional[StrictStr] = Field(default=None, description="The end user/customer's state.")
    postal_code: Optional[StrictStr] = Field(default=None, description="The end user/customer's zip or postal code.", alias="postalCode")
    country_code: Optional[StrictStr] = Field(default=None, description="The end user/customer's two character ISO country code.", alias="countryCode")
    phone_number: Optional[StrictStr] = Field(default=None, description="The end user/customer's phone number.", alias="phoneNumber")
    email: Optional[StrictStr] = Field(default=None, description="The end user/customer's email.")
    __properties: ClassVar[List[str]] = ["contact", "name1", "name2", "companyName", "addressLine1", "addressLine2", "addressLine3", "addressLine4", "city", "state", "postalCode", "countryCode", "phoneNumber", "email"]

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
        """Create an instance of RenewalsDetailsResponseEndUserInfoInner from a JSON string"""
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
        """Create an instance of RenewalsDetailsResponseEndUserInfoInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact": obj.get("contact"),
            "name1": obj.get("name1"),
            "name2": obj.get("name2"),
            "companyName": obj.get("companyName"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "addressLine4": obj.get("addressLine4"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode"),
            "phoneNumber": obj.get("phoneNumber"),
            "email": obj.get("email")
        })
        return _obj


