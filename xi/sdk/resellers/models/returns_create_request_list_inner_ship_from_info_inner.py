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

class ReturnsCreateRequestListInnerShipFromInfoInner(BaseModel):
    """
    ReturnsCreateRequestListInnerShipFromInfoInner
    """ # noqa: E501
    company_name: StrictStr = Field(description="Name of the company from where the product will be shipped.", alias="companyName")
    contact: StrictStr = Field(description="Contact name of the person from where the product will be shipped.")
    address_line1: StrictStr = Field(description="Ship from Address Line1.", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="Ship from Address Line2.", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="Ship from Address Line3.", alias="addressLine3")
    city: StrictStr = Field(description="Ship from City.")
    state: StrictStr = Field(description="Ship from state.")
    postal_code: StrictStr = Field(description="Ship from postal code.", alias="postalCode")
    country_code: StrictStr = Field(description="ship from country code.", alias="countryCode")
    email: StrictStr = Field(description="Ship from email.")
    phone_number: Optional[StrictStr] = Field(default=None, description="Ship from phone number.", alias="phoneNumber")
    __properties: ClassVar[List[str]] = ["companyName", "contact", "addressLine1", "addressLine2", "addressLine3", "city", "state", "postalCode", "countryCode", "email", "phoneNumber"]

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
        """Create an instance of ReturnsCreateRequestListInnerShipFromInfoInner from a JSON string"""
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
        """Create an instance of ReturnsCreateRequestListInnerShipFromInfoInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "companyName": obj.get("companyName"),
            "contact": obj.get("contact"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode"),
            "email": obj.get("email"),
            "phoneNumber": obj.get("phoneNumber")
        })
        return _obj

