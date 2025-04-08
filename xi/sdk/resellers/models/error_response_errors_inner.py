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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.error_response_errors_inner_fields_inner import ErrorResponseErrorsInnerFieldsInner
from typing import Optional, Set
from typing_extensions import Self

class ErrorResponseErrorsInner(BaseModel):
    """
    ErrorResponseErrorsInner
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique Id to identify error.")
    type: Optional[StrictStr] = Field(default=None, description="Describes the type of the error.")
    message: Optional[StrictStr] = Field(default=None, description="Describes the error message.")
    fields: Optional[List[ErrorResponseErrorsInnerFieldsInner]] = None
    __properties: ClassVar[List[str]] = ["id", "type", "message", "fields"]

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
        """Create an instance of ErrorResponseErrorsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ErrorResponseErrorsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "message": obj.get("message"),
            "fields": [ErrorResponseErrorsInnerFieldsInner.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None
        })
        return _obj


