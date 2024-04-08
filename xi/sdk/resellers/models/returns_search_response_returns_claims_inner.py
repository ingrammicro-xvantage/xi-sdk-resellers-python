# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.returns_search_response_returns_claims_inner_links_inner import ReturnsSearchResponseReturnsClaimsInnerLinksInner
from typing import Optional, Set
from typing_extensions import Self

class ReturnsSearchResponseReturnsClaimsInner(BaseModel):
    """
    ReturnsSearchResponseReturnsClaimsInner
    """ # noqa: E501
    return_claim_id: Optional[StrictStr] = Field(default=None, description="A unique return claim Id.", alias="returnClaimId")
    case_request_number: Optional[StrictStr] = Field(default=None, description="A unique return request number.", alias="caseRequestNumber")
    created_on: Optional[StrictStr] = Field(default=None, description="The date on which the return request was created. ", alias="createdOn")
    type: Optional[StrictStr] = Field(default=None, description="Type of request.")
    return_reason: Optional[StrictStr] = Field(default=None, description="The reason for the return.", alias="returnReason")
    reference_number: Optional[StrictStr] = Field(default=None, description="The reference number for the return.", alias="referenceNumber")
    estimated_total_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The estimated total value of the return.", alias="estimatedTotalValue")
    credit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of credit.")
    modified_on: Optional[StrictStr] = Field(default=None, description="The date on which the return request was last updated.", alias="modifiedOn")
    status: Optional[StrictStr] = Field(default=None, description="The status of the request.")
    links: Optional[List[ReturnsSearchResponseReturnsClaimsInnerLinksInner]] = None
    __properties: ClassVar[List[str]] = ["returnClaimId", "caseRequestNumber", "createdOn", "type", "returnReason", "referenceNumber", "estimatedTotalValue", "credit", "modifiedOn", "status", "links"]

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
        """Create an instance of ReturnsSearchResponseReturnsClaimsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReturnsSearchResponseReturnsClaimsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "returnClaimId": obj.get("returnClaimId"),
            "caseRequestNumber": obj.get("caseRequestNumber"),
            "createdOn": obj.get("createdOn"),
            "type": obj.get("type"),
            "returnReason": obj.get("returnReason"),
            "referenceNumber": obj.get("referenceNumber"),
            "estimatedTotalValue": obj.get("estimatedTotalValue"),
            "credit": obj.get("credit"),
            "modifiedOn": obj.get("modifiedOn"),
            "status": obj.get("status"),
            "links": [ReturnsSearchResponseReturnsClaimsInnerLinksInner.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
        })
        return _obj


