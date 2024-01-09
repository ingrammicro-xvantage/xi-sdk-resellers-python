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

class InvoiceDetailsv61ResponseSummaryMiscChargesInner(BaseModel):
    """
    InvoiceDetailsv61ResponseSummaryMiscChargesInner
    """ # noqa: E501
    charge_description: Optional[StrictStr] = Field(default=None, description="Description of the charge.", alias="chargeDescription")
    misc_charge_line_count: Optional[StrictInt] = Field(default=None, description="The number of lines for which miscellaneous charges are applicable.", alias="miscChargeLineCount")
    misc_charge_line_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Miscellaneous charge amount.", alias="miscChargeLineTotal")
    charge_line_reference: Optional[StrictStr] = Field(default=None, description="Reference of the chargeLine.", alias="chargeLineReference")
    is_non_misc: Optional[StrictStr] = Field(default=None, description="Is charge non miscellaneous.", alias="isNonMisc")
    __properties: ClassVar[List[str]] = ["chargeDescription", "miscChargeLineCount", "miscChargeLineTotal", "chargeLineReference", "isNonMisc"]

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
        """Create an instance of InvoiceDetailsv61ResponseSummaryMiscChargesInner from a JSON string"""
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
        """Create an instance of InvoiceDetailsv61ResponseSummaryMiscChargesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chargeDescription": obj.get("chargeDescription"),
            "miscChargeLineCount": obj.get("miscChargeLineCount"),
            "miscChargeLineTotal": obj.get("miscChargeLineTotal"),
            "chargeLineReference": obj.get("chargeLineReference"),
            "isNonMisc": obj.get("isNonMisc")
        })
        return _obj


