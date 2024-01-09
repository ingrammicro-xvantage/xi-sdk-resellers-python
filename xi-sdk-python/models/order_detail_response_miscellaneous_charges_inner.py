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

class OrderDetailResponseMiscellaneousChargesInner(BaseModel):
    """
    OrderDetailResponseMiscellaneousChargesInner
    """ # noqa: E501
    sub_order_number: Optional[StrictStr] = Field(default=None, description="The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number.", alias="subOrderNumber")
    charge_line_reference: Optional[StrictStr] = Field(default=None, description="Impulse line number for the miscellaneous charge.", alias="chargeLineReference")
    charge_description: Optional[StrictStr] = Field(default=None, description="Description of the miscellaneous charges.", alias="chargeDescription")
    charge_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of miscellaneous charges.", alias="chargeAmount")
    __properties: ClassVar[List[str]] = ["subOrderNumber", "chargeLineReference", "chargeDescription", "chargeAmount"]

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
        """Create an instance of OrderDetailResponseMiscellaneousChargesInner from a JSON string"""
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
        """Create an instance of OrderDetailResponseMiscellaneousChargesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subOrderNumber": obj.get("subOrderNumber"),
            "chargeLineReference": obj.get("chargeLineReference"),
            "chargeDescription": obj.get("chargeDescription"),
            "chargeAmount": obj.get("chargeAmount")
        })
        return _obj


