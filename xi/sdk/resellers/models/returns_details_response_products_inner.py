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

from datetime import date
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ReturnsDetailsResponseProductsInner(BaseModel):
    """
    ReturnsDetailsResponseProductsInner
    """ # noqa: E501
    ingram_line_number: Optional[StrictStr] = Field(default=None, description="Unique Ingram Micro line number.", alias="ingramLineNumber")
    description: Optional[StrictStr] = Field(default=None, description="The description of the line item product.")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Unique IngramMicro part number.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="The vendor's part number for the line item.", alias="vendorPartNumber")
    upc: Optional[StrictStr] = Field(default=None, description="The UPC code of a product.")
    invoice_date: Optional[date] = Field(default=None, description="The date of the invoice.", alias="invoiceDate")
    invoice_number: Optional[StrictStr] = Field(default=None, description="Ingram micro Invoice number.", alias="invoiceNumber")
    customer_order_number: Optional[StrictInt] = Field(default=None, description="The reseller's order number for reference in their system.", alias="customerOrderNumber")
    request_details: Optional[StrictInt] = Field(default=None, description="Request details.", alias="requestDetails")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity of the line item.")
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unit price of the line item.", alias="unitPrice")
    extended_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Unit price X quantity for the line item.", alias="extendedPrice")
    status: Optional[StrictStr] = Field(default=None, description="The status of the line item.")
    return_branch: Optional[StrictInt] = Field(default=None, description="The code of the return branch.", alias="returnBranch")
    ship_from_branch: Optional[StrictInt] = Field(default=None, description="The code of the ship from branch.", alias="shipFromBranch")
    __properties: ClassVar[List[str]] = ["ingramLineNumber", "description", "ingramPartNumber", "vendorPartNumber", "upc", "invoiceDate", "invoiceNumber", "customerOrderNumber", "requestDetails", "quantity", "unitPrice", "extendedPrice", "status", "returnBranch", "shipFromBranch"]

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
        """Create an instance of ReturnsDetailsResponseProductsInner from a JSON string"""
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
        """Create an instance of ReturnsDetailsResponseProductsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramLineNumber": obj.get("ingramLineNumber"),
            "description": obj.get("description"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "upc": obj.get("upc"),
            "invoiceDate": obj.get("invoiceDate"),
            "invoiceNumber": obj.get("invoiceNumber"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "requestDetails": obj.get("requestDetails"),
            "quantity": obj.get("quantity"),
            "unitPrice": obj.get("unitPrice"),
            "extendedPrice": obj.get("extendedPrice"),
            "status": obj.get("status"),
            "returnBranch": obj.get("returnBranch"),
            "shipFromBranch": obj.get("shipFromBranch")
        })
        return _obj


