# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateV7RequestShipmentDetails(BaseModel):
    """
    Shipping details for the order provided by the customer.
    """ # noqa: E501
    carrier_code: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="The code for the shipping carrier for the line item.", alias="carrierCode")
    requested_delivery_date: Optional[Annotated[str, Field(strict=True, max_length=8)]] = Field(default=None, description="The reseller-requested delivery date in UTC format. Delivery date is not guaranteed. Must be a future date.", alias="requestedDeliveryDate")
    ship_complete: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="Specifies whether the shipment will be shipped only when all products are fulfilled. The value of this field along with acceptBackOrder field decides the value of backorderflag. If this field is set, acceptBackOrder field is ignored. Possible values for this field are true, C, P, E.With value as true or C, backorderflag will be set as C.With value as P, or E, backorderflag will be set as P or E respectively.C = Ship complete at distribution level.P = ship complete at line level.E = ship complete across all distributions.", alias="shipComplete")
    shipping_instructions: Optional[Annotated[str, Field(strict=True, max_length=132)]] = Field(default=None, description="Any special shipping instructions for the order.", alias="shippingInstructions")
    freight_account_number: Optional[StrictStr] = Field(default=None, description="The reseller 's shipping account number with carrier. Used to bill the shipping carrier directly from the reseller's account with the carrier.", alias="freightAccountNumber")
    signature_required: Optional[StrictBool] = Field(default=None, description="Specifies whether a signature is required for delivery. Default is False.", alias="signatureRequired")
    __properties: ClassVar[List[str]] = ["carrierCode", "requestedDeliveryDate", "shipComplete", "shippingInstructions", "freightAccountNumber", "signatureRequired"]

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
        """Create an instance of OrderCreateV7RequestShipmentDetails from a JSON string"""
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
        # set to None if carrier_code (nullable) is None
        # and model_fields_set contains the field
        if self.carrier_code is None and "carrier_code" in self.model_fields_set:
            _dict['carrierCode'] = None

        # set to None if requested_delivery_date (nullable) is None
        # and model_fields_set contains the field
        if self.requested_delivery_date is None and "requested_delivery_date" in self.model_fields_set:
            _dict['requestedDeliveryDate'] = None

        # set to None if ship_complete (nullable) is None
        # and model_fields_set contains the field
        if self.ship_complete is None and "ship_complete" in self.model_fields_set:
            _dict['shipComplete'] = None

        # set to None if shipping_instructions (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_instructions is None and "shipping_instructions" in self.model_fields_set:
            _dict['shippingInstructions'] = None

        # set to None if freight_account_number (nullable) is None
        # and model_fields_set contains the field
        if self.freight_account_number is None and "freight_account_number" in self.model_fields_set:
            _dict['freightAccountNumber'] = None

        # set to None if signature_required (nullable) is None
        # and model_fields_set contains the field
        if self.signature_required is None and "signature_required" in self.model_fields_set:
            _dict['signatureRequired'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCreateV7RequestShipmentDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrierCode": obj.get("carrierCode"),
            "requestedDeliveryDate": obj.get("requestedDeliveryDate"),
            "shipComplete": obj.get("shipComplete"),
            "shippingInstructions": obj.get("shippingInstructions"),
            "freightAccountNumber": obj.get("freightAccountNumber"),
            "signatureRequired": obj.get("signatureRequired")
        })
        return _obj


