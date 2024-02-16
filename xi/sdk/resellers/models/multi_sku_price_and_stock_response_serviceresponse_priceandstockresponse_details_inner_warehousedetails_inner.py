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

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner(BaseModel):
    """
    MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner
    """ # noqa: E501
    warehouseid: Optional[StrictStr] = Field(default=None, description="Unique 2-digit code of the Ingram Micro warehouse")
    warehousedescription: Optional[StrictStr] = Field(default=None, description="City of the Ingram Micro warehouse location")
    availablequantity: Optional[StrictInt] = Field(default=None, description="On hand available quantity")
    onorderquantity: Optional[StrictInt] = Field(default=None, description="On Order quantity")
    onholdquantity: Optional[StrictStr] = None
    etadate: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["warehouseid", "warehousedescription", "availablequantity", "onorderquantity", "onholdquantity", "etadate"]

    @field_validator('warehouseid')
    def warehouseid_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['10-Mira Loma CA', '20-Carrollton TX', '30-Millington TN', '40-Carol Stream IL', '80-Jonestown PA']):
            raise ValueError("must be one of enum values ('10-Mira Loma CA', '20-Carrollton TX', '30-Millington TN', '40-Carol Stream IL', '80-Jonestown PA')")
        return value

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
        """Create an instance of MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "warehouseid": obj.get("warehouseid"),
            "warehousedescription": obj.get("warehousedescription"),
            "availablequantity": obj.get("availablequantity"),
            "onorderquantity": obj.get("onorderquantity"),
            "onholdquantity": obj.get("onholdquantity"),
            "etadate": obj.get("etadate")
        })
        return _obj


