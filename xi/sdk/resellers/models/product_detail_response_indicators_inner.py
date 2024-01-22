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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProductDetailResponseIndicatorsInner(BaseModel):
    """
    ProductDetailResponseIndicatorsInner
    """ # noqa: E501
    has_warranty: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product has a warranty.", alias="hasWarranty")
    is_new_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s a new product. ", alias="isNewProduct")
    has_return_limits: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether there is any limit to return the product.", alias="HasReturnLimits")
    is_back_order_allowed: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether back order is allowed for the product.", alias="IsBackOrderAllowed")
    is_shipped_from_partner: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product is shipped from the partner.", alias="isShippedFromPartner")
    is_replacement_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product is a replacement product.", alias="isReplacementProduct")
    is_directship: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s a direct ship product.", alias="isDirectship")
    is_downloadable: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product is downloadable.", alias="isDownloadable")
    is_digital_type: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s a digital product. ", alias="isDigitalType")
    sku_type: Optional[StrictStr] = Field(default=None, description="skutype", alias="skuType")
    has_std_special_price: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product has any standard special price.", alias="hasStdSpecialPrice")
    has_acop_special_price: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product has any ACOP special price.", alias="hasAcopSpecialPrice")
    has_acop_quantity_break: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product has any ACOP quantity break.", alias="hasAcopQuantityBreak")
    has_std_web_discount: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product has any standard web discount.", alias="hasStdWebDiscount")
    has_special_bid: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product has any special bid.", alias="hasSpecialBid")
    is_exportable_to_country: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product is exportable.", alias="isExportableToCountry")
    is_discontinued_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s a discontinued product.", alias="isDiscontinuedProduct")
    is_refurbished_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product is refurbished.", alias="isRefurbishedProduct")
    is_returnable_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates if the product can be returned.", alias="isReturnableProduct")
    is_ingram_ship: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s a Ingram shipped product.", alias="isIngramShip")
    is_enduser_required: Optional[StrictBool] = Field(default=None, description="Do vendor requires Enduser name required to create an order.", alias="isEnduserRequired")
    is_heavy_weight: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s  heavy weight product.", alias="isHeavyWeight")
    has_ltl: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it hasLtl or not.", alias="hasLtl")
    is_clearance_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s clearnce product.", alias="isClearanceProduct")
    has_bundle: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s a bundled product.", alias="hasBundle")
    is_oversize_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s oversized product.", alias="isOversizeProduct")
    is_preorder_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s a preorder product.", alias="isPreorderProduct")
    is_license_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether it’s a licened product.", alias="isLicenseProduct")
    is_directship_orderable: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product is directship orderable.", alias="isDirectshipOrderable")
    is_service_sku: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product is service SKU.", alias="isServiceSku")
    is_configurable: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether product is configurable.", alias="isConfigurable")
    __properties: ClassVar[List[str]] = ["hasWarranty", "isNewProduct", "HasReturnLimits", "IsBackOrderAllowed", "isShippedFromPartner", "isReplacementProduct", "isDirectship", "isDownloadable", "isDigitalType", "skuType", "hasStdSpecialPrice", "hasAcopSpecialPrice", "hasAcopQuantityBreak", "hasStdWebDiscount", "hasSpecialBid", "isExportableToCountry", "isDiscontinuedProduct", "isRefurbishedProduct", "isReturnableProduct", "isIngramShip", "isEnduserRequired", "isHeavyWeight", "hasLtl", "isClearanceProduct", "hasBundle", "isOversizeProduct", "isPreorderProduct", "isLicenseProduct", "isDirectshipOrderable", "isServiceSku", "isConfigurable"]

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
        """Create an instance of ProductDetailResponseIndicatorsInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProductDetailResponseIndicatorsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hasWarranty": obj.get("hasWarranty"),
            "isNewProduct": obj.get("isNewProduct"),
            "HasReturnLimits": obj.get("HasReturnLimits"),
            "IsBackOrderAllowed": obj.get("IsBackOrderAllowed"),
            "isShippedFromPartner": obj.get("isShippedFromPartner"),
            "isReplacementProduct": obj.get("isReplacementProduct"),
            "isDirectship": obj.get("isDirectship"),
            "isDownloadable": obj.get("isDownloadable"),
            "isDigitalType": obj.get("isDigitalType"),
            "skuType": obj.get("skuType"),
            "hasStdSpecialPrice": obj.get("hasStdSpecialPrice"),
            "hasAcopSpecialPrice": obj.get("hasAcopSpecialPrice"),
            "hasAcopQuantityBreak": obj.get("hasAcopQuantityBreak"),
            "hasStdWebDiscount": obj.get("hasStdWebDiscount"),
            "hasSpecialBid": obj.get("hasSpecialBid"),
            "isExportableToCountry": obj.get("isExportableToCountry"),
            "isDiscontinuedProduct": obj.get("isDiscontinuedProduct"),
            "isRefurbishedProduct": obj.get("isRefurbishedProduct"),
            "isReturnableProduct": obj.get("isReturnableProduct"),
            "isIngramShip": obj.get("isIngramShip"),
            "isEnduserRequired": obj.get("isEnduserRequired"),
            "isHeavyWeight": obj.get("isHeavyWeight"),
            "hasLtl": obj.get("hasLtl"),
            "isClearanceProduct": obj.get("isClearanceProduct"),
            "hasBundle": obj.get("hasBundle"),
            "isOversizeProduct": obj.get("isOversizeProduct"),
            "isPreorderProduct": obj.get("isPreorderProduct"),
            "isLicenseProduct": obj.get("isLicenseProduct"),
            "isDirectshipOrderable": obj.get("isDirectshipOrderable"),
            "isServiceSku": obj.get("isServiceSku"),
            "isConfigurable": obj.get("isConfigurable")
        })
        return _obj


