# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.returns_search_response_returns_claims_inner_links_inner import ReturnsSearchResponseReturnsClaimsInnerLinksInner
from typing import Optional, Set
from typing_extensions import Self

class ReturnsCreateResponseReturnsClaimsInner(BaseModel):
    """
    ReturnsCreateResponseReturnsClaimsInner
    """ # noqa: E501
    rma_claim_id: Optional[StrictStr] = Field(default=None, description="The rmaClaimId claim id.", alias="rmaClaimId")
    case_request_number: Optional[StrictStr] = Field(default=None, description="A unique return request number.", alias="caseRequestNumber")
    reference_number: Optional[StrictStr] = Field(default=None, description="The reference number for the return.", alias="referenceNumber")
    created_on: Optional[date] = Field(default=None, description="The date on which the return request was created. ", alias="createdOn")
    type: Optional[StrictStr] = Field(default=None, description="Type of request.")
    return_reason: Optional[StrictStr] = Field(default=None, description="The reason for the return.", alias="returnReason")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Unique line number from Ingram.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="Vendor Part Number.", alias="vendorPartNumber")
    quantity: Optional[StrictInt] = Field(default=None, description="Return quantity of the product.")
    notes: Optional[StrictStr] = Field(default=None, description="Return notes.")
    estimated_total_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The estimated total value of the return.", alias="estimatedTotalValue")
    credit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of credit.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the request.")
    links: Optional[List[ReturnsSearchResponseReturnsClaimsInnerLinksInner]] = None
    __properties: ClassVar[List[str]] = ["rmaClaimId", "caseRequestNumber", "referenceNumber", "createdOn", "type", "returnReason", "ingramPartNumber", "vendorPartNumber", "quantity", "notes", "estimatedTotalValue", "credit", "status", "links"]

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
        """Create an instance of ReturnsCreateResponseReturnsClaimsInner from a JSON string"""
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
        """Create an instance of ReturnsCreateResponseReturnsClaimsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rmaClaimId": obj.get("rmaClaimId"),
            "caseRequestNumber": obj.get("caseRequestNumber"),
            "referenceNumber": obj.get("referenceNumber"),
            "createdOn": obj.get("createdOn"),
            "type": obj.get("type"),
            "returnReason": obj.get("returnReason"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "quantity": obj.get("quantity"),
            "notes": obj.get("notes"),
            "estimatedTotalValue": obj.get("estimatedTotalValue"),
            "credit": obj.get("credit"),
            "status": obj.get("status"),
            "links": [ReturnsSearchResponseReturnsClaimsInnerLinksInner.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
        })
        return _obj


