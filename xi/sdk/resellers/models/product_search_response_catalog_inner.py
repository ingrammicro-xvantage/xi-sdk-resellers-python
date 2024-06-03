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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.product_search_response_catalog_inner_links_inner import ProductSearchResponseCatalogInnerLinksInner
from typing import Optional, Set
from typing_extensions import Self

class ProductSearchResponseCatalogInner(BaseModel):
    """
    ProductSearchResponseCatalogInner
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="The description of the product.")
    category: Optional[StrictStr] = Field(default=None, description="The category of the product. Example: Displays.")
    sub_category: Optional[StrictStr] = Field(default=None, description="The sub category for the product. Example: ComputernMonitors.", alias="subCategory")
    product_type: Optional[StrictStr] = Field(default=None, description="The product type of the product. Example: LCD Monitors.", alias="productType")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="The Unique IngramMicro part number for the product.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="The vendor part number for the product.", alias="vendorPartNumber")
    upc_code: Optional[StrictStr] = Field(default=None, description="The UPC code for the product. Consists of 12 numeric digits that are uniquly assigned to each trade item.", alias="upcCode")
    vendor_name: Optional[StrictStr] = Field(default=None, description="The name of the vendor/manufacturer of the product.", alias="vendorName")
    end_user_required: Optional[StrictStr] = Field(default=None, description="Indicates whether the contact information for the end user/customer is required, which determines pricing and discounts.", alias="endUserRequired")
    has_discounts: Optional[StrictStr] = Field(default=None, description="Specifies if there are discounts available for the product.", alias="hasDiscounts")
    type: Optional[StrictStr] = Field(default=None, description="The SKU type of product. One of Physical, Digital, or Any.")
    discontinued: Optional[StrictStr] = Field(default=None, description="Indicates if the product has been discontinued.")
    new_product: Optional[StrictStr] = Field(default=None, description="Indicates if the product is new. For digital products, newer than 10 days. For physical products, newer than 150 days.", alias="newProduct")
    direct_ship: Optional[StrictStr] = Field(default=None, description="Indicates if the product will be shipped directly to the reseller or end user from the vendor/manufacturer.", alias="directShip")
    has_warranty: Optional[StrictStr] = Field(default=None, description="Indicates if the product has a warranty.", alias="hasWarranty")
    links: Optional[List[ProductSearchResponseCatalogInnerLinksInner]] = None
    extra_description: Optional[StrictStr] = Field(default=None, description="The extended description of the product.", alias="extraDescription")
    replacement_sku: Optional[StrictStr] = Field(default=None, description="Identifies a SKU that is a comparable subsititution of the current SKU if available.", alias="replacementSku")
    authorized_to_purchase: Optional[StrictStr] = Field(default=None, description="It is true when it exists in matched queries field of ealstic search API.", alias="authorizedToPurchase")
    __properties: ClassVar[List[str]] = ["description", "category", "subCategory", "productType", "ingramPartNumber", "vendorPartNumber", "upcCode", "vendorName", "endUserRequired", "hasDiscounts", "type", "discontinued", "newProduct", "directShip", "hasWarranty", "links", "extraDescription", "replacementSku", "authorizedToPurchase"]

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
        """Create an instance of ProductSearchResponseCatalogInner from a JSON string"""
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
        """Create an instance of ProductSearchResponseCatalogInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "category": obj.get("category"),
            "subCategory": obj.get("subCategory"),
            "productType": obj.get("productType"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "upcCode": obj.get("upcCode"),
            "vendorName": obj.get("vendorName"),
            "endUserRequired": obj.get("endUserRequired"),
            "hasDiscounts": obj.get("hasDiscounts"),
            "type": obj.get("type"),
            "discontinued": obj.get("discontinued"),
            "newProduct": obj.get("newProduct"),
            "directShip": obj.get("directShip"),
            "hasWarranty": obj.get("hasWarranty"),
            "links": [ProductSearchResponseCatalogInnerLinksInner.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "extraDescription": obj.get("extraDescription"),
            "replacementSku": obj.get("replacementSku"),
            "authorizedToPurchase": obj.get("authorizedToPurchase")
        })
        return _obj


