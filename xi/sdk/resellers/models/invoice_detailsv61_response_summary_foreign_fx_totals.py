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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InvoiceDetailsv61ResponseSummaryForeignFxTotals(BaseModel):
    """
    InvoiceDetailsv61ResponseSummaryForeignFxTotals
    """ # noqa: E501
    foreign_currency_code: Optional[StrictStr] = Field(default=None, description="Foreign Currency Code.", alias="foreignCurrencyCode")
    foreign_currency_fx_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Foreign rate.", alias="foreignCurrencyFxRate")
    foreign_total_taxable_amount: Optional[StrictStr] = Field(default=None, description="Foreign amount.", alias="foreignTotalTaxableAmount")
    foreign_total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Foreign amount.", alias="foreignTotalTaxAmount")
    foreign_invoice_amount_due: Optional[StrictStr] = Field(default=None, description="Foreign due.", alias="foreignInvoiceAmountDue")
    __properties: ClassVar[List[str]] = ["foreignCurrencyCode", "foreignCurrencyFxRate", "foreignTotalTaxableAmount", "foreignTotalTaxAmount", "foreignInvoiceAmountDue"]

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
        """Create an instance of InvoiceDetailsv61ResponseSummaryForeignFxTotals from a JSON string"""
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
        """Create an instance of InvoiceDetailsv61ResponseSummaryForeignFxTotals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "foreignCurrencyCode": obj.get("foreignCurrencyCode"),
            "foreignCurrencyFxRate": obj.get("foreignCurrencyFxRate"),
            "foreignTotalTaxableAmount": obj.get("foreignTotalTaxableAmount"),
            "foreignTotalTaxAmount": obj.get("foreignTotalTaxAmount"),
            "foreignInvoiceAmountDue": obj.get("foreignInvoiceAmountDue")
        })
        return _obj


