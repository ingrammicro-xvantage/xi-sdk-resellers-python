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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.renewals_search_request_date_type_end_date import RenewalsSearchRequestDateTypeEndDate
from xi.sdk.resellers.models.renewals_search_request_date_type_expiration_date import RenewalsSearchRequestDateTypeExpirationDate
from xi.sdk.resellers.models.renewals_search_request_date_type_invoice_date import RenewalsSearchRequestDateTypeInvoiceDate
from xi.sdk.resellers.models.renewals_search_request_date_type_start_date import RenewalsSearchRequestDateTypeStartDate
from typing import Optional, Set
from typing_extensions import Self

class RenewalsSearchRequestDateType(BaseModel):
    """
    RenewalsSearchRequestDateType
    """ # noqa: E501
    start_date: Optional[RenewalsSearchRequestDateTypeStartDate] = Field(default=None, alias="startDate")
    end_date: Optional[RenewalsSearchRequestDateTypeEndDate] = Field(default=None, alias="endDate")
    invoice_date: Optional[RenewalsSearchRequestDateTypeInvoiceDate] = Field(default=None, alias="invoiceDate")
    expiration_date: Optional[RenewalsSearchRequestDateTypeExpirationDate] = Field(default=None, alias="expirationDate")
    __properties: ClassVar[List[str]] = ["startDate", "endDate", "invoiceDate", "expirationDate"]

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
        """Create an instance of RenewalsSearchRequestDateType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of start_date
        if self.start_date:
            _dict['startDate'] = self.start_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_date
        if self.end_date:
            _dict['endDate'] = self.end_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invoice_date
        if self.invoice_date:
            _dict['invoiceDate'] = self.invoice_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration_date
        if self.expiration_date:
            _dict['expirationDate'] = self.expiration_date.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RenewalsSearchRequestDateType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startDate": RenewalsSearchRequestDateTypeStartDate.from_dict(obj["startDate"]) if obj.get("startDate") is not None else None,
            "endDate": RenewalsSearchRequestDateTypeEndDate.from_dict(obj["endDate"]) if obj.get("endDate") is not None else None,
            "invoiceDate": RenewalsSearchRequestDateTypeInvoiceDate.from_dict(obj["invoiceDate"]) if obj.get("invoiceDate") is not None else None,
            "expirationDate": RenewalsSearchRequestDateTypeExpirationDate.from_dict(obj["expirationDate"]) if obj.get("expirationDate") is not None else None
        })
        return _obj


