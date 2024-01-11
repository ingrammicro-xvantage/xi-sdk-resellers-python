# coding: utf-8

"""
    Reseller API Documentation

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
from xi-sdk-resellers-python.models.price_and_availability_request_servicerequest_priceandstockrequest import PriceAndAvailabilityRequestServicerequestPriceandstockrequest
from xi-sdk-resellers-python.models.price_and_availability_request_servicerequest_requestpreamble import PriceAndAvailabilityRequestServicerequestRequestpreamble
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PriceAndAvailabilityRequestServicerequest(BaseModel):
    """
    PriceAndAvailabilityRequestServicerequest
    """ # noqa: E501
    requestpreamble: Optional[PriceAndAvailabilityRequestServicerequestRequestpreamble] = None
    priceandstockrequest: Optional[PriceAndAvailabilityRequestServicerequestPriceandstockrequest] = None
    __properties: ClassVar[List[str]] = ["requestpreamble", "priceandstockrequest"]

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
        """Create an instance of PriceAndAvailabilityRequestServicerequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requestpreamble
        if self.requestpreamble:
            _dict['requestpreamble'] = self.requestpreamble.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priceandstockrequest
        if self.priceandstockrequest:
            _dict['priceandstockrequest'] = self.priceandstockrequest.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PriceAndAvailabilityRequestServicerequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "requestpreamble": PriceAndAvailabilityRequestServicerequestRequestpreamble.from_dict(obj.get("requestpreamble")) if obj.get("requestpreamble") is not None else None,
            "priceandstockrequest": PriceAndAvailabilityRequestServicerequestPriceandstockrequest.from_dict(obj.get("priceandstockrequest")) if obj.get("priceandstockrequest") is not None else None
        })
        return _obj

