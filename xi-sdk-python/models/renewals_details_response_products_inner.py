# coding: utf-8

"""
    Reseller API Documentation - United States

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RenewalsDetailsResponseProductsInner(BaseModel):
    """
    RenewalsDetailsResponseProductsInner
    """ # noqa: E501
    ingram_line_number: Optional[StrictStr] = Field(default=None, description="Unique Ingram Micro line number.", alias="ingramLineNumber")
    product_description: Optional[StrictStr] = Field(default=None, description="The description of the product.", alias="productDescription")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="The vendor's part number for the line item.", alias="vendorPartNumber")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Unique IngramMicro part number.", alias="ingramPartNumber")
    manufacturer_part_number: Optional[StrictStr] = Field(default=None, description="The manufacturer's part number for the line item.", alias="manufacturerPartNumber")
    quantity: Optional[StrictStr] = Field(default=None, description="The quantity of the line item.")
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unit price of the line item.", alias="unitPrice")
    is_consolidated: Optional[StrictStr] = Field(default=None, description="Is the line item consolidated? Yes or No.", alias="isConsolidated")
    __properties: ClassVar[List[str]] = ["ingramLineNumber", "productDescription", "vendorPartNumber", "ingramPartNumber", "manufacturerPartNumber", "quantity", "unitPrice", "isConsolidated"]

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
        """Create an instance of RenewalsDetailsResponseProductsInner from a JSON string"""
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
        """Create an instance of RenewalsDetailsResponseProductsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramLineNumber": obj.get("ingramLineNumber"),
            "productDescription": obj.get("productDescription"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "manufacturerPartNumber": obj.get("manufacturerPartNumber"),
            "quantity": obj.get("quantity"),
            "unitPrice": obj.get("unitPrice"),
            "isConsolidated": obj.get("isConsolidated")
        })
        return _obj


