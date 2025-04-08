# ProductSearchResponseSubscriptionCatalogInnerPlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | ID of the Plan. | [optional] 
**plan_name** | **str** | Name of the Plan. | [optional] 
**plan_description** | **str** | The description of the Plan | [optional] 
**subscription_period_summary** | [**List[ProductSearchResponseSubscriptionCatalogInnerPlansInnerSubscriptionPeriodSummaryInner]**](ProductSearchResponseSubscriptionCatalogInnerPlansInnerSubscriptionPeriodSummaryInner.md) |  | [optional] 
**links** | [**List[ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner]**](ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_search_response_subscription_catalog_inner_plans_inner import ProductSearchResponseSubscriptionCatalogInnerPlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchResponseSubscriptionCatalogInnerPlansInner from a JSON string
product_search_response_subscription_catalog_inner_plans_inner_instance = ProductSearchResponseSubscriptionCatalogInnerPlansInner.from_json(json)
# print the JSON string representation of the object
print(ProductSearchResponseSubscriptionCatalogInnerPlansInner.to_json())

# convert the object into a dict
product_search_response_subscription_catalog_inner_plans_inner_dict = product_search_response_subscription_catalog_inner_plans_inner_instance.to_dict()
# create an instance of ProductSearchResponseSubscriptionCatalogInnerPlansInner from a dict
product_search_response_subscription_catalog_inner_plans_inner_from_dict = ProductSearchResponseSubscriptionCatalogInnerPlansInner.from_dict(product_search_response_subscription_catalog_inner_plans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


