# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.quote_details_response_additional_attributes_inner import QuoteDetailsResponseAdditionalAttributesInner
from xi.sdk.resellers.models.quote_details_response_end_user_info import QuoteDetailsResponseEndUserInfo
from xi.sdk.resellers.models.quote_details_response_products_inner import QuoteDetailsResponseProductsInner
from xi.sdk.resellers.models.quote_details_response_reseller_info import QuoteDetailsResponseResellerInfo
from typing import Optional, Set
from typing_extensions import Self

class QuoteDetailsResponse(BaseModel):
    """
    QuoteDetailsResponse
    """ # noqa: E501
    quote_name: Optional[StrictStr] = Field(default=None, description="Quote Name given to quote by sales team or system generated.  Generally used as a reference to identify the quote.", alias="quoteName")
    quote_number: Optional[StrictStr] = Field(default=None, description="Unique identifier generated by Ingram Micro's CRM specific to each quote.  When applying a filter to the quoteNumber and including a partial quote number in the filter, all quotes containing any information included in the filter can be retrieved as a subset of all available customer quotes.", alias="quoteNumber")
    revision: Optional[StrictStr] = Field(default=None, description="When a quote has been revised and updated, the quote number remains the same throughout the lifecycle of the quote, however, a Revision number is updated for each revision of the quote.  The revision numbers is associated with the Unique Quote Number.")
    ingram_quote_date: Optional[StrictStr] = Field(default=None, description="Date the Quote was initially Created.", alias="ingramQuoteDate")
    last_modified_date: Optional[StrictStr] = Field(default=None, description="Date the Quote was last updated or modified.", alias="lastModifiedDate")
    ingram_quote_expiry_date: Optional[StrictStr] = Field(default=None, description="Quote expiration date.", alias="ingramQuoteExpiryDate")
    currency_code: Optional[StrictStr] = Field(default=None, description="Three letter currency code.", alias="currencyCode")
    special_bid_id: Optional[StrictStr] = Field(default=None, description="Price discount identifyer to specify  a pricing discount that has been applied to the quote. If present - the priceDeviationStartDate and priceDeviationExpiryDate must be presented. Cisco refers to this as a Dart", alias="specialBidId")
    special_bid_effective_date: Optional[StrictStr] = Field(default=None, description="If price discount has been applied to the quote - the starting date the discount begins.", alias="specialBidEffectiveDate")
    special_bid_expiration_date: Optional[StrictStr] = Field(default=None, description="If a price discount has been applied to the quote - The date the discount expires and will no longer be applicable.", alias="specialBidExpirationDate")
    status: Optional[StrictStr] = Field(default=None, description="This refers to the primary status of the quote.  API responses will return")
    closing_reason: Optional[StrictStr] = Field(default=None, description="Closing Reason for quote.", alias="closingReason")
    date_closed: Optional[StrictStr] = Field(default=None, alias="dateClosed")
    customer_need: Optional[StrictStr] = Field(default=None, description="Details related to the customer's request for the quote entered by the sales representative or system generated.", alias="customerNeed")
    proposed_solution: Optional[StrictStr] = Field(default=None, description="Ingram Micro proposed solution and summary of quote.", alias="proposedSolution")
    intro_preamble: Optional[StrictStr] = Field(default=None, description="Introductory paragraph included in each quote.  Legally required - must be included when presenting the quote details.", alias="introPreamble")
    purchase_instructions: Optional[StrictStr] = Field(default=None, description="Purchase instructions.  Legally required - must be included when presenting the quote details.", alias="purchaseInstructions")
    legal_terms: Optional[StrictStr] = Field(default=None, description="Legal terms -  Legally required - must be included when presenting the quote details.", alias="legalTerms")
    quote_type: Optional[StrictStr] = Field(default=None, alias="quoteType")
    lease_info: Optional[StrictStr] = Field(default=None, description="Lease information.", alias="leaseInfo")
    leasing_instructions: Optional[StrictStr] = Field(default=None, description="Leasing information", alias="leasingInstructions")
    quote_sub_type: Optional[StrictStr] = Field(default=None, alias="quoteSubType")
    reseller_info: Optional[QuoteDetailsResponseResellerInfo] = Field(default=None, alias="resellerInfo")
    end_user_info: Optional[QuoteDetailsResponseEndUserInfo] = Field(default=None, alias="endUserInfo")
    products: Optional[List[QuoteDetailsResponseProductsInner]] = None
    products_count: Optional[StrictInt] = Field(default=None, description="Total number of products included in the quote", alias="productsCount")
    extended_msrp_total: Optional[StrictInt] = Field(default=None, description="Total extended MSRP for all products included in the quote", alias="extendedMsrpTotal")
    quantity_total: Optional[StrictInt] = Field(default=None, description="Total quantity of all items in the quote.", alias="quantityTotal")
    extended_quote_price_total: Optional[StrictInt] = Field(default=None, description="Total amount of quoted price for all products in the quote including both solution products and suggested products.", alias="extendedQuotePriceTotal")
    additional_attributes: Optional[List[QuoteDetailsResponseAdditionalAttributesInner]] = Field(default=None, alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["quoteName", "quoteNumber", "revision", "ingramQuoteDate", "lastModifiedDate", "ingramQuoteExpiryDate", "currencyCode", "specialBidId", "specialBidEffectiveDate", "specialBidExpirationDate", "status", "closingReason", "dateClosed", "customerNeed", "proposedSolution", "introPreamble", "purchaseInstructions", "legalTerms", "quoteType", "leaseInfo", "leasingInstructions", "quoteSubType", "resellerInfo", "endUserInfo", "products", "productsCount", "extendedMsrpTotal", "quantityTotal", "extendedQuotePriceTotal", "additionalAttributes"]

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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of QuoteDetailsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reseller_info
        if self.reseller_info:
            _dict['resellerInfo'] = self.reseller_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_user_info
        if self.end_user_info:
            _dict['endUserInfo'] = self.end_user_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item in self.products:
                if _item:
                    _items.append(_item.to_dict())
            _dict['products'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item in self.additional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuoteDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quoteName": obj.get("quoteName"),
            "quoteNumber": obj.get("quoteNumber"),
            "revision": obj.get("revision"),
            "ingramQuoteDate": obj.get("ingramQuoteDate"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "ingramQuoteExpiryDate": obj.get("ingramQuoteExpiryDate"),
            "currencyCode": obj.get("currencyCode"),
            "specialBidId": obj.get("specialBidId"),
            "specialBidEffectiveDate": obj.get("specialBidEffectiveDate"),
            "specialBidExpirationDate": obj.get("specialBidExpirationDate"),
            "status": obj.get("status"),
            "closingReason": obj.get("closingReason"),
            "dateClosed": obj.get("dateClosed"),
            "customerNeed": obj.get("customerNeed"),
            "proposedSolution": obj.get("proposedSolution"),
            "introPreamble": obj.get("introPreamble"),
            "purchaseInstructions": obj.get("purchaseInstructions"),
            "legalTerms": obj.get("legalTerms"),
            "quoteType": obj.get("quoteType"),
            "leaseInfo": obj.get("leaseInfo"),
            "leasingInstructions": obj.get("leasingInstructions"),
            "quoteSubType": obj.get("quoteSubType"),
            "resellerInfo": QuoteDetailsResponseResellerInfo.from_dict(obj["resellerInfo"]) if obj.get("resellerInfo") is not None else None,
            "endUserInfo": QuoteDetailsResponseEndUserInfo.from_dict(obj["endUserInfo"]) if obj.get("endUserInfo") is not None else None,
            "products": [QuoteDetailsResponseProductsInner.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None,
            "productsCount": obj.get("productsCount"),
            "extendedMsrpTotal": obj.get("extendedMsrpTotal"),
            "quantityTotal": obj.get("quantityTotal"),
            "extendedQuotePriceTotal": obj.get("extendedQuotePriceTotal"),
            "additionalAttributes": [QuoteDetailsResponseAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


