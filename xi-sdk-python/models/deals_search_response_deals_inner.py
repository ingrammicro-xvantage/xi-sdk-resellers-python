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

from datetime import date
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from xi-sdk-python.models.renewals_search_response_renewals_inner_links_inner import RenewalsSearchResponseRenewalsInnerLinksInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DealsSearchResponseDealsInner(BaseModel):
    """
    DealsSearchResponseDealsInner
    """ # noqa: E501
    deal_id: Optional[StrictStr] = Field(default=None, description="Deal/Special bid number.", alias="dealId")
    version: Optional[StrictStr] = Field(default=None, description="Most recent version number of the deal.")
    end_user: Optional[StrictStr] = Field(default=None, description="The end user/customer's name.", alias="endUser")
    vendor: Optional[StrictStr] = Field(default=None, description="The vendor's name.")
    deal_expiry_date: Optional[date] = Field(default=None, description="Expiration date of the deal/Special bid.", alias="dealExpiryDate")
    links: Optional[List[RenewalsSearchResponseRenewalsInnerLinksInner]] = None
    __properties: ClassVar[List[str]] = ["dealId", "version", "endUser", "vendor", "dealExpiryDate", "links"]

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
        """Create an instance of DealsSearchResponseDealsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DealsSearchResponseDealsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dealId": obj.get("dealId"),
            "version": obj.get("version"),
            "endUser": obj.get("endUser"),
            "vendor": obj.get("vendor"),
            "dealExpiryDate": obj.get("dealExpiryDate"),
            "links": [RenewalsSearchResponseRenewalsInnerLinksInner.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj


