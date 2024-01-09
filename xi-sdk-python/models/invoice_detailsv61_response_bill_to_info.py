# coding: utf-8

"""
    Reseller API Documentation - United States

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

class InvoiceDetailsv61ResponseBillToInfo(BaseModel):
    """
    InvoiceDetailsv61ResponseBillToInfo
    """ # noqa: E501
    contact: Optional[StrictStr] = Field(default=None, description="Bill to Name.")
    company_name: Optional[StrictStr] = Field(default=None, description="Bill to company.", alias="companyName")
    address_line1: Optional[StrictStr] = Field(default=None, description="Bill to Address Line1.", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="Bill to Address Line2.", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="Bill to Address Line3.", alias="addressLine3")
    city: Optional[StrictStr] = Field(default=None, description="Bill to City.")
    state: Optional[StrictStr] = Field(default=None, description="Bill to State code")
    postal_code: Optional[StrictStr] = Field(default=None, description="Bill to Postalcode code.", alias="postalCode")
    country_code: Optional[StrictStr] = Field(default=None, description="Bill to Country code.", alias="countryCode")
    phone_number: Optional[StrictStr] = Field(default=None, description="Phone number of the bill to company.", alias="phoneNumber")
    email: Optional[StrictStr] = Field(default=None, description="Email address of the bill to company.")
    __properties: ClassVar[List[str]] = ["contact", "companyName", "addressLine1", "addressLine2", "addressLine3", "city", "state", "postalCode", "countryCode", "phoneNumber", "email"]

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
        """Create an instance of InvoiceDetailsv61ResponseBillToInfo from a JSON string"""
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
        """Create an instance of InvoiceDetailsv61ResponseBillToInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact": obj.get("contact"),
            "companyName": obj.get("companyName"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode"),
            "phoneNumber": obj.get("phoneNumber"),
            "email": obj.get("email")
        })
        return _obj


