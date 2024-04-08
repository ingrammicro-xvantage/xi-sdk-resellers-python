# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.product_search_response_catalog_inner import ProductSearchResponseCatalogInner
from typing import Optional, Set
from typing_extensions import Self

class ProductSearchResponse(BaseModel):
    """
    ProductSearchResponse
    """ # noqa: E501
    records_found: Optional[StrictInt] = Field(default=None, description="The number of recourds found for the search.", alias="recordsFound")
    page_size: Optional[StrictInt] = Field(default=None, description="The number of results per page. Default is 25.", alias="pageSize")
    page_number: Optional[StrictInt] = Field(default=None, description="current page number default is 1", alias="pageNumber")
    catalog: Optional[List[ProductSearchResponseCatalogInner]] = None
    next_page: Optional[StrictStr] = Field(default=None, description="link/URL for accessing next page.", alias="nextPage")
    previous_page: Optional[StrictStr] = Field(default=None, description="link/URL for accessing previous page.", alias="previousPage")
    __properties: ClassVar[List[str]] = ["recordsFound", "pageSize", "pageNumber", "catalog", "nextPage", "previousPage"]

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
        """Create an instance of ProductSearchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in catalog (list)
        _items = []
        if self.catalog:
            for _item in self.catalog:
                if _item:
                    _items.append(_item.to_dict())
            _dict['catalog'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductSearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recordsFound": obj.get("recordsFound"),
            "pageSize": obj.get("pageSize"),
            "pageNumber": obj.get("pageNumber"),
            "catalog": [ProductSearchResponseCatalogInner.from_dict(_item) for _item in obj["catalog"]] if obj.get("catalog") is not None else None,
            "nextPage": obj.get("nextPage"),
            "previousPage": obj.get("previousPage")
        })
        return _obj


