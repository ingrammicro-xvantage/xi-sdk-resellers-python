# ProductSearchResponseCatalogInnerLinksInner

HATEOAS links for the price and availability of the sku.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Provides the details of the product. | [optional] 
**href** | **str** | The URL endpoint for accessing the relevant data.. | [optional] 
**type** | **str** | The type of call that can be made to the href link(GET) | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_search_response_catalog_inner_links_inner import ProductSearchResponseCatalogInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchResponseCatalogInnerLinksInner from a JSON string
product_search_response_catalog_inner_links_inner_instance = ProductSearchResponseCatalogInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print(ProductSearchResponseCatalogInnerLinksInner.to_json())

# convert the object into a dict
product_search_response_catalog_inner_links_inner_dict = product_search_response_catalog_inner_links_inner_instance.to_dict()
# create an instance of ProductSearchResponseCatalogInnerLinksInner from a dict
product_search_response_catalog_inner_links_inner_form_dict = product_search_response_catalog_inner_links_inner.from_dict(product_search_response_catalog_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


