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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.returns_details_response_products_inner import ReturnsDetailsResponseProductsInner
from typing import Optional, Set
from typing_extensions import Self

class ReturnsDetailsResponse(BaseModel):
    """
    ReturnsDetailsResponse
    """ # noqa: E501
    type_of_details: Optional[StrictStr] = Field(default=None, description="The type of the details. Return or Claim.", alias="typeOfDetails")
    rma_claim_id: Optional[StrictStr] = Field(default=None, description="The rmaClaimId claim id.", alias="rmaClaimId")
    case_request_number: Optional[StrictStr] = Field(default=None, description="A unique return request number.", alias="caseRequestNumber")
    created_on: Optional[StrictStr] = Field(default=None, description="The date on which the return request was created.", alias="createdOn")
    return_reason: Optional[StrictStr] = Field(default=None, description="The reason for the return.", alias="returnReason")
    reference_number: Optional[StrictStr] = Field(default=None, description="The reference number for the return.", alias="referenceNumber")
    status: Optional[StrictStr] = Field(default=None, description="The status of the request.")
    return_warehouse_address: Optional[StrictStr] = Field(default=None, description="The address of the return warehouse.", alias="returnWarehouseAddress")
    products: Optional[List[ReturnsDetailsResponseProductsInner]] = None
    sub_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sub total amount of the return request.", alias="subTotal")
    tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The tax amount of the return request.")
    additional_fees: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The additional fees for the return request.", alias="additionalFees")
    estimated_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total estimated amount for the return request.", alias="estimatedTotal")
    __properties: ClassVar[List[str]] = ["typeOfDetails", "rmaClaimId", "caseRequestNumber", "createdOn", "returnReason", "referenceNumber", "status", "returnWarehouseAddress", "products", "subTotal", "tax", "additionalFees", "estimatedTotal"]

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
        """Create an instance of ReturnsDetailsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item in self.products:
                if _item:
                    _items.append(_item.to_dict())
            _dict['products'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReturnsDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "typeOfDetails": obj.get("typeOfDetails"),
            "rmaClaimId": obj.get("rmaClaimId"),
            "caseRequestNumber": obj.get("caseRequestNumber"),
            "createdOn": obj.get("createdOn"),
            "returnReason": obj.get("returnReason"),
            "referenceNumber": obj.get("referenceNumber"),
            "status": obj.get("status"),
            "returnWarehouseAddress": obj.get("returnWarehouseAddress"),
            "products": [ReturnsDetailsResponseProductsInner.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None,
            "subTotal": obj.get("subTotal"),
            "tax": obj.get("tax"),
            "additionalFees": obj.get("additionalFees"),
            "estimatedTotal": obj.get("estimatedTotal")
        })
        return _obj


