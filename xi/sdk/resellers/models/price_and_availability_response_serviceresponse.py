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
from pydantic import BaseModel
from xi.sdk.resellers.models.price_and_availability_response_serviceresponse_priceandstockresponse import PriceAndAvailabilityResponseServiceresponsePriceandstockresponse
from xi.sdk.resellers.models.price_and_availability_response_serviceresponse_responsepreamble import PriceAndAvailabilityResponseServiceresponseResponsepreamble
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PriceAndAvailabilityResponseServiceresponse(BaseModel):
    """
    PriceAndAvailabilityResponseServiceresponse
    """ # noqa: E501
    responsepreamble: Optional[PriceAndAvailabilityResponseServiceresponseResponsepreamble] = None
    priceandstockresponse: Optional[PriceAndAvailabilityResponseServiceresponsePriceandstockresponse] = None
    __properties: ClassVar[List[str]] = ["responsepreamble", "priceandstockresponse"]

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
        """Create an instance of PriceAndAvailabilityResponseServiceresponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of responsepreamble
        if self.responsepreamble:
            _dict['responsepreamble'] = self.responsepreamble.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priceandstockresponse
        if self.priceandstockresponse:
            _dict['priceandstockresponse'] = self.priceandstockresponse.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PriceAndAvailabilityResponseServiceresponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "responsepreamble": PriceAndAvailabilityResponseServiceresponseResponsepreamble.from_dict(obj.get("responsepreamble")) if obj.get("responsepreamble") is not None else None,
            "priceandstockresponse": PriceAndAvailabilityResponseServiceresponsePriceandstockresponse.from_dict(obj.get("priceandstockresponse")) if obj.get("priceandstockresponse") is not None else None
        })
        return _obj


