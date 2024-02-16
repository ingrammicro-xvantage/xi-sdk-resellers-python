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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.invoice_detailsv61_response_lines_inner_serial_numbers_inner import InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner
from typing import Optional, Set
from typing_extensions import Self

class InvoiceDetailsv61ResponseLinesInner(BaseModel):
    """
    InvoiceDetailsv61ResponseLinesInner
    """ # noqa: E501
    ingram_line_number: Optional[StrictStr] = Field(default=None, description="Unique line number from Ingram.", alias="ingramLineNumber")
    customer_line_number: Optional[StrictStr] = Field(default='0', description="Line number passes by customer while creating an order.", alias="customerLineNumber")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Ingram Micro SKU (stock keeping unit). An identification, usually alphanumeric, of a particular product that allows it to be tracked for inventory purposes.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="Vendor Part Number.", alias="vendorPartNumber")
    customer_part_number: Optional[StrictStr] = Field(default=None, description="Part number from customer's system.", alias="customerPartNumber")
    vendor_name: Optional[StrictStr] = Field(default=None, description="Name of the vendor.", alias="vendorName")
    product_description: Optional[StrictStr] = Field(default=None, description="Description of the product.", alias="productDescription")
    unit_weight: Optional[StrictStr] = Field(default=None, description="Weight of the product.", alias="unitWeight")
    quantity: Optional[StrictInt] = Field(default=None, description="Quantity of the product.")
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Unit price of the product.", alias="unitPrice")
    unit_of_measure: Optional[StrictStr] = Field(default=None, description="Unit of measure of the product.", alias="unitOfMeasure")
    currency_code: Optional[StrictStr] = Field(default=None, description="Currency code.", alias="currencyCode")
    extended_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Extended price of the product.", alias="extendedPrice")
    tax_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Tax percentage", alias="taxPercentage")
    tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Tax rate", alias="taxRate")
    tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Line level tax amount.", alias="taxAmount")
    serial_numbers: Optional[List[InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner]] = Field(default=None, alias="serialNumbers")
    quantity_ordered: Optional[StrictInt] = Field(default=None, description="Quantity ordered by the customer.", alias="quantityOrdered")
    quantity_shipped: Optional[StrictInt] = Field(default=None, description="Quantity shipped to the customer.", alias="quantityShipped")
    __properties: ClassVar[List[str]] = ["ingramLineNumber", "customerLineNumber", "ingramPartNumber", "vendorPartNumber", "customerPartNumber", "vendorName", "productDescription", "unitWeight", "quantity", "unitPrice", "unitOfMeasure", "currencyCode", "extendedPrice", "taxPercentage", "taxRate", "taxAmount", "serialNumbers", "quantityOrdered", "quantityShipped"]

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
        """Create an instance of InvoiceDetailsv61ResponseLinesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in serial_numbers (list)
        _items = []
        if self.serial_numbers:
            for _item in self.serial_numbers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serialNumbers'] = _items
        # set to None if serial_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.serial_numbers is None and "serial_numbers" in self.model_fields_set:
            _dict['serialNumbers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceDetailsv61ResponseLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramLineNumber": obj.get("ingramLineNumber"),
            "customerLineNumber": obj.get("customerLineNumber") if obj.get("customerLineNumber") is not None else '0',
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "customerPartNumber": obj.get("customerPartNumber"),
            "vendorName": obj.get("vendorName"),
            "productDescription": obj.get("productDescription"),
            "unitWeight": obj.get("unitWeight"),
            "quantity": obj.get("quantity"),
            "unitPrice": obj.get("unitPrice"),
            "unitOfMeasure": obj.get("unitOfMeasure"),
            "currencyCode": obj.get("currencyCode"),
            "extendedPrice": obj.get("extendedPrice"),
            "taxPercentage": obj.get("taxPercentage"),
            "taxRate": obj.get("taxRate"),
            "taxAmount": obj.get("taxAmount"),
            "serialNumbers": [InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner.from_dict(_item) for _item in obj["serialNumbers"]] if obj.get("serialNumbers") is not None else None,
            "quantityOrdered": obj.get("quantityOrdered"),
            "quantityShipped": obj.get("quantityShipped")
        })
        return _obj


