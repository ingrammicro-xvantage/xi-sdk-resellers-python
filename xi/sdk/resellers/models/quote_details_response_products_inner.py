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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.quote_details_response_products_inner_bill_details_inner import QuoteDetailsResponseProductsInnerBillDetailsInner
from xi.sdk.resellers.models.quote_details_response_products_inner_price import QuoteDetailsResponseProductsInnerPrice
from typing import Optional, Set
from typing_extensions import Self

class QuoteDetailsResponseProductsInner(BaseModel):
    """
    QuoteDetailsResponseProductsInner
    """ # noqa: E501
    quote_product_guid: Optional[StrictStr] = Field(default=None, description="Quote Product GUID  is the primary quote key in Ingram Micro's CRM - needed to retrieve quote details.", alias="quoteProductGuid")
    line_number: Optional[StrictStr] = Field(default=None, description="Line number which the product will appear in the quote.  Line number is manditory when unique configurations are included in a quote and mainting the item line order is required.", alias="lineNumber")
    quantity: Optional[StrictInt] = Field(default=None, description="Quantity of product line item quoted.")
    notes: Optional[StrictStr] = Field(default=None, description="Product line item comments.")
    ean: Optional[StrictStr] = Field(default=None, description="EANUPC")
    coo: Optional[StrictStr] = Field(default=None, description="Country of Origin.")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Ingram Micro SKU (stock keeping unit). An identification, usually alphanumeric, of a particular product that allows it to be tracked for inventory purposes", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="Vendor Part Number", alias="vendorPartNumber")
    description: Optional[StrictStr] = Field(default=None, description="Product description.  Note - The quote view api returns only the product short description as maintained in Ingram Micro's crm system.  For long descriptions, please refer to alternative information sources.")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Weight is provided based on country standard.  For countries following Imperial standards - weight is presented as pounds with decimal.  In countries following metric standards, weight is provided as kilograms with decimal.")
    weight_uom: Optional[StrictStr] = Field(default=None, description="Unit of measure", alias="weightUom")
    is_suggestion_product: Optional[StrictBool] = Field(default=None, description="Flag to indicate if a product line item is a suggested product.  The suggested product is provided in addition to the requested quoted products and a suggested option.  Suggested products are grouped together for subtotal and total calculations.", alias="isSuggestionProduct")
    vpn_category: Optional[StrictStr] = Field(default=None, description="Vendor product category specific to Cisco. HWDW (hardware) or service.", alias="vpnCategory")
    quote_products_supplier_part_auxiliary_id: Optional[StrictStr] = Field(default=None, description="Vendor product configuration ID specific to Cisco.", alias="quoteProductsSupplierPartAuxiliaryId")
    vendor_name: Optional[StrictStr] = Field(default=None, description="Vendor name of the product", alias="vendorName")
    terms: Optional[StrictStr] = Field(default=None, description="Terms of the quote")
    plan_description: Optional[StrictStr] = Field(default=None, alias="planDescription")
    is_subscription: Optional[StrictBool] = Field(default=None, alias="isSubscription")
    reseller_margin: Optional[StrictStr] = Field(default=None, alias="resellerMargin")
    requested_start_date: Optional[StrictStr] = Field(default=None, alias="requestedStartDate")
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    serial_number: Optional[StrictStr] = Field(default=None, alias="serialNumber")
    price: Optional[QuoteDetailsResponseProductsInnerPrice] = None
    bill_details: Optional[List[QuoteDetailsResponseProductsInnerBillDetailsInner]] = Field(default=None, alias="billDetails")
    __properties: ClassVar[List[str]] = ["quoteProductGuid", "lineNumber", "quantity", "notes", "ean", "coo", "ingramPartNumber", "vendorPartNumber", "description", "weight", "weightUom", "isSuggestionProduct", "vpnCategory", "quoteProductsSupplierPartAuxiliaryId", "vendorName", "terms", "planDescription", "isSubscription", "resellerMargin", "requestedStartDate", "startDate", "endDate", "serialNumber", "price", "billDetails"]

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
        """Create an instance of QuoteDetailsResponseProductsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in bill_details (list)
        _items = []
        if self.bill_details:
            for _item in self.bill_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['billDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuoteDetailsResponseProductsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quoteProductGuid": obj.get("quoteProductGuid"),
            "lineNumber": obj.get("lineNumber"),
            "quantity": obj.get("quantity"),
            "notes": obj.get("notes"),
            "ean": obj.get("ean"),
            "coo": obj.get("coo"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "description": obj.get("description"),
            "weight": obj.get("weight"),
            "weightUom": obj.get("weightUom"),
            "isSuggestionProduct": obj.get("isSuggestionProduct"),
            "vpnCategory": obj.get("vpnCategory"),
            "quoteProductsSupplierPartAuxiliaryId": obj.get("quoteProductsSupplierPartAuxiliaryId"),
            "vendorName": obj.get("vendorName"),
            "terms": obj.get("terms"),
            "planDescription": obj.get("planDescription"),
            "isSubscription": obj.get("isSubscription"),
            "resellerMargin": obj.get("resellerMargin"),
            "requestedStartDate": obj.get("requestedStartDate"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "serialNumber": obj.get("serialNumber"),
            "price": QuoteDetailsResponseProductsInnerPrice.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "billDetails": [QuoteDetailsResponseProductsInnerBillDetailsInner.from_dict(_item) for _item in obj["billDetails"]] if obj.get("billDetails") is not None else None
        })
        return _obj


