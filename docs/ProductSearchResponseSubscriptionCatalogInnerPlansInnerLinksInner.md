# ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Provides the details of the product. | [optional] 
**href** | **str** | The URL endpoint for accessing the relevant data.. | [optional] 
**type** | **str** | The type of call that can be made to the href link(GET) | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_search_response_subscription_catalog_inner_plans_inner_links_inner import ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner from a JSON string
product_search_response_subscription_catalog_inner_plans_inner_links_inner_instance = ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print(ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner.to_json())

# convert the object into a dict
product_search_response_subscription_catalog_inner_plans_inner_links_inner_dict = product_search_response_subscription_catalog_inner_plans_inner_links_inner_instance.to_dict()
# create an instance of ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner from a dict
product_search_response_subscription_catalog_inner_plans_inner_links_inner_from_dict = ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner.from_dict(product_search_response_subscription_catalog_inner_plans_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


