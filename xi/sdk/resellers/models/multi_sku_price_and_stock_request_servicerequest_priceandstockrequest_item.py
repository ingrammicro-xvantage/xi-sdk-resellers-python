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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem(BaseModel):
    """
    MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem
    """ # noqa: E501
    index: Optional[StrictInt] = None
    ingrampartnumber: Optional[StrictStr] = Field(default=None, description="Ingram Micro system specific SKU number for the product for which the price is requested at Ingram Micro")
    vendorpartnumber: Optional[StrictStr] = Field(default=None, description="Vendor Part Number for the product for which the price is requested at Ingram Micro")
    upc: Optional[StrictStr] = Field(default=None, description="Universal Product code for the product for which the price is requested at Ingram Micro", alias="UPC")
    customerpartnumber: Optional[StrictStr] = Field(default=None, description="Unique identification number of customer. For this option the Ingram Micro Sales rep must set up a cross reference table. ")
    warehouseidlist: Optional[StrictStr] = Field(default=None, description="Unique identity for Ingram Micro warehouses against which stock details are returned.")
    __properties: ClassVar[List[str]] = ["index", "ingrampartnumber", "vendorpartnumber", "UPC", "customerpartnumber", "warehouseidlist"]

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
        """Create an instance of MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem from a JSON string"""
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
        """Create an instance of MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "index": obj.get("index"),
            "ingrampartnumber": obj.get("ingrampartnumber"),
            "vendorpartnumber": obj.get("vendorpartnumber"),
            "UPC": obj.get("UPC"),
            "customerpartnumber": obj.get("customerpartnumber"),
            "warehouseidlist": obj.get("warehouseidlist")
        })
        return _obj


