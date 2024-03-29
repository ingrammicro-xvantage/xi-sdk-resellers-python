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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from xi.sdk.resellers.models.quote_to_order_details_dto_additional_attributes_inner import QuoteToOrderDetailsDTOAdditionalAttributesInner
from xi.sdk.resellers.models.quote_to_order_details_dto_end_user_info import QuoteToOrderDetailsDTOEndUserInfo
from xi.sdk.resellers.models.quote_to_order_details_dto_lines_inner import QuoteToOrderDetailsDTOLinesInner
from xi.sdk.resellers.models.quote_to_order_details_dto_ship_to_info import QuoteToOrderDetailsDTOShipToInfo
from xi.sdk.resellers.models.quote_to_order_details_dto_vmfadditional_attributes_inner import QuoteToOrderDetailsDTOVmfadditionalAttributesInner
from typing import Optional, Set
from typing_extensions import Self

class QuoteToOrderDetailsDTO(BaseModel):
    """
    QuoteToOrderDetailsDTO
    """ # noqa: E501
    quote_number: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="A unique identifier generated by Ingram Micro's CRM specific to each quote.", alias="quoteNumber")
    customer_order_number: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="The reseller's order number for reference in their system.", alias="customerOrderNumber")
    enduser_order_number: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="The end customer's order number for reference in their system.", alias="enduserOrderNumber")
    bill_to_address_id: Optional[StrictStr] = Field(default=None, description="Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit.", alias="billToAddressId")
    end_user_info: Optional[QuoteToOrderDetailsDTOEndUserInfo] = Field(default=None, alias="endUserInfo")
    ship_to_info: Optional[QuoteToOrderDetailsDTOShipToInfo] = Field(default=None, alias="shipToInfo")
    additional_attributes: Optional[List[QuoteToOrderDetailsDTOAdditionalAttributesInner]] = Field(default=None, description="Additional order create attributes.", alias="additionalAttributes")
    vmfadditional_attributes: Optional[List[QuoteToOrderDetailsDTOVmfadditionalAttributesInner]] = Field(default=None, description="The object containing the list of fields required at a header level by the vendor.", alias="vmfadditionalAttributes")
    lines: Optional[List[QuoteToOrderDetailsDTOLinesInner]] = Field(default=None, description="The object containing the lines that require vendor mandatory fields.")
    __properties: ClassVar[List[str]] = ["quoteNumber", "customerOrderNumber", "enduserOrderNumber", "billToAddressId", "endUserInfo", "shipToInfo", "additionalAttributes", "vmfadditionalAttributes", "lines"]

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
        """Create an instance of QuoteToOrderDetailsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of end_user_info
        if self.end_user_info:
            _dict['endUserInfo'] = self.end_user_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_info
        if self.ship_to_info:
            _dict['shipToInfo'] = self.ship_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item in self.additional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vmfadditional_attributes (list)
        _items = []
        if self.vmfadditional_attributes:
            for _item in self.vmfadditional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vmfadditionalAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        # set to None if quote_number (nullable) is None
        # and model_fields_set contains the field
        if self.quote_number is None and "quote_number" in self.model_fields_set:
            _dict['quoteNumber'] = None

        # set to None if customer_order_number (nullable) is None
        # and model_fields_set contains the field
        if self.customer_order_number is None and "customer_order_number" in self.model_fields_set:
            _dict['customerOrderNumber'] = None

        # set to None if enduser_order_number (nullable) is None
        # and model_fields_set contains the field
        if self.enduser_order_number is None and "enduser_order_number" in self.model_fields_set:
            _dict['enduserOrderNumber'] = None

        # set to None if bill_to_address_id (nullable) is None
        # and model_fields_set contains the field
        if self.bill_to_address_id is None and "bill_to_address_id" in self.model_fields_set:
            _dict['billToAddressId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuoteToOrderDetailsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quoteNumber": obj.get("quoteNumber"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "enduserOrderNumber": obj.get("enduserOrderNumber"),
            "billToAddressId": obj.get("billToAddressId"),
            "endUserInfo": QuoteToOrderDetailsDTOEndUserInfo.from_dict(obj["endUserInfo"]) if obj.get("endUserInfo") is not None else None,
            "shipToInfo": QuoteToOrderDetailsDTOShipToInfo.from_dict(obj["shipToInfo"]) if obj.get("shipToInfo") is not None else None,
            "additionalAttributes": [QuoteToOrderDetailsDTOAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None,
            "vmfadditionalAttributes": [QuoteToOrderDetailsDTOVmfadditionalAttributesInner.from_dict(_item) for _item in obj["vmfadditionalAttributes"]] if obj.get("vmfadditionalAttributes") is not None else None,
            "lines": [QuoteToOrderDetailsDTOLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None
        })
        return _obj


