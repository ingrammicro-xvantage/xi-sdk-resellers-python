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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner(BaseModel):
    """
    OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner
    """ # noqa: E501
    dateof_purchase: Optional[date] = Field(default=None, description="Date of purchase of the hardware.", alias="dateofPurchase")
    ship_date: Optional[date] = Field(default=None, description="Vendor specific mandatory field, date of hardware/product shipment from vendor.", alias="shipDate")
    primary_serial_number: Optional[StrictStr] = Field(default=None, description="Serial number of the hardware/product.", alias="primarySerialNumber")
    secondary_serial_number: Optional[StrictStr] = Field(default=None, description="Serial number of accessory associated with the above hardware/product.", alias="secondarySerialNumber")
    __properties: ClassVar[List[str]] = ["dateofPurchase", "shipDate", "primarySerialNumber", "secondarySerialNumber"]

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
        """Create an instance of OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner from a JSON string"""
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
        """Create an instance of OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dateofPurchase": obj.get("dateofPurchase"),
            "shipDate": obj.get("shipDate"),
            "primarySerialNumber": obj.get("primarySerialNumber"),
            "secondarySerialNumber": obj.get("secondarySerialNumber")
        })
        return _obj


