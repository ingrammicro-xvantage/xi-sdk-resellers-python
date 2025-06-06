# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

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
from xi.sdk.resellers.models.quote_search_response_quotes_inner_links import QuoteSearchResponseQuotesInnerLinks
from typing import Optional, Set
from typing_extensions import Self

class QuoteSearchResponseQuotesInner(BaseModel):
    """
    QuoteSearchResponseQuotesInner
    """ # noqa: E501
    quote_guid: Optional[StrictStr] = Field(default=None, alias="quoteGuid")
    quote_name: Optional[StrictStr] = Field(default=None, description="Quote Name given to quote by sales team or system generated.  Generally used as a reference to identify the quote.", alias="quoteName")
    quote_number: Optional[StrictStr] = Field(default=None, description="Unique identifier generated by Ingram Micros CRM specific to each quote.  When applying a filter to the quoteNumber and including a partial quote number in the filter, all quotes containing any information included in the filter can be retrieved as a subset of all available customer quotes.", alias="quoteNumber")
    revision: Optional[StrictStr] = Field(default=None, description="When a quote has been revised and updated, the quote number remains the same throughout the lifecycle of the quote, however, a Revision number is updated for each revision of the quote.  The revision numbers is associated with the Unique Quote Number.")
    currency_code: Optional[StrictStr] = Field(default=None, description="The country-specific three digit ISO 4217 currency code for the order.", alias="currencyCode")
    end_user_contact: Optional[StrictStr] = Field(default=None, description="End User Name is the end customer name that is associated with a quote in Ingram Micros CRM.", alias="endUserContact")
    special_bid_number: Optional[StrictStr] = Field(default=None, description="Special Pricing Bid Number, also refers to as Dart Number relates to a unique pricing deal associated with a vendor for the quote.", alias="specialBidNumber")
    quote_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total amount of quoted price for all products in the quote.", alias="quoteTotal")
    quote_status: Optional[StrictStr] = Field(default=None, description="This refers to the primary status of the quote.", alias="quoteStatus")
    ingram_quote_date: Optional[StrictStr] = Field(default=None, description="Date the Quote was initially Created.", alias="ingramQuoteDate")
    last_modified_date: Optional[StrictStr] = Field(default=None, description="Date the Quote was last updated or modified.", alias="lastModifiedDate")
    ingram_quote_expiry_date: Optional[StrictStr] = Field(default=None, description="Date when the Quote Expires.", alias="ingramQuoteExpiryDate")
    end_user_name: Optional[StrictStr] = Field(default=None, description="End User Name", alias="endUserName")
    vendor: Optional[StrictStr] = Field(default=None, description="Name of the vendor.")
    created_by: Optional[StrictStr] = Field(default=None, description="Name of the end user/customer who created a quote.", alias="createdBy")
    quote_type: Optional[StrictStr] = Field(default=None, description="Type of quote", alias="quoteType")
    links: Optional[QuoteSearchResponseQuotesInnerLinks] = None
    __properties: ClassVar[List[str]] = ["quoteGuid", "quoteName", "quoteNumber", "revision", "currencyCode", "endUserContact", "specialBidNumber", "quoteTotal", "quoteStatus", "ingramQuoteDate", "lastModifiedDate", "ingramQuoteExpiryDate", "endUserName", "vendor", "createdBy", "quoteType", "links"]

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
        """Create an instance of QuoteSearchResponseQuotesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuoteSearchResponseQuotesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quoteGuid": obj.get("quoteGuid"),
            "quoteName": obj.get("quoteName"),
            "quoteNumber": obj.get("quoteNumber"),
            "revision": obj.get("revision"),
            "currencyCode": obj.get("currencyCode"),
            "endUserContact": obj.get("endUserContact"),
            "specialBidNumber": obj.get("specialBidNumber"),
            "quoteTotal": obj.get("quoteTotal"),
            "quoteStatus": obj.get("quoteStatus"),
            "ingramQuoteDate": obj.get("ingramQuoteDate"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "ingramQuoteExpiryDate": obj.get("ingramQuoteExpiryDate"),
            "endUserName": obj.get("endUserName"),
            "vendor": obj.get("vendor"),
            "createdBy": obj.get("createdBy"),
            "quoteType": obj.get("quoteType"),
            "links": QuoteSearchResponseQuotesInnerLinks.from_dict(obj["links"]) if obj.get("links") is not None else None
        })
        return _obj


