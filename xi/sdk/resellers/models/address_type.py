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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AddressType(BaseModel):
    """
    Address type object
    """ # noqa: E501
    attention: Optional[StrictStr] = None
    name1: Optional[StrictStr] = None
    name2: Optional[StrictStr] = None
    addressline1: Optional[StrictStr] = None
    addressline2: Optional[StrictStr] = None
    addressline3: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    postalcode: Optional[StrictStr] = None
    countrycode: Optional[StrictStr] = None
    fax: Optional[StrictStr] = None
    phonenumber: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["attention", "name1", "name2", "addressline1", "addressline2", "addressline3", "city", "state", "postalcode", "countrycode", "fax", "phonenumber", "email"]

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
        """Create an instance of AddressType from a JSON string"""
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
        """Create an instance of AddressType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attention": obj.get("attention"),
            "name1": obj.get("name1"),
            "name2": obj.get("name2"),
            "addressline1": obj.get("addressline1"),
            "addressline2": obj.get("addressline2"),
            "addressline3": obj.get("addressline3"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalcode": obj.get("postalcode"),
            "countrycode": obj.get("countrycode"),
            "fax": obj.get("fax"),
            "phonenumber": obj.get("phonenumber"),
            "email": obj.get("email")
        })
        return _obj


