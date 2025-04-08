# ProductDetailResponseSubscriptionDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | ID of the subscription plan. | [optional] 
**plan_name** | **str** | Name of the subscription plan. | [optional] 
**plan_description** | **str** | Description of the subscription plan. | [optional] 
**groups** | [**List[ProductDetailResponseSubscriptionDetailsInnerGroupsInner]**](ProductDetailResponseSubscriptionDetailsInnerGroupsInner.md) | Details of the groups subscription product part of. | [optional] 
**subscription_period** | [**List[ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner]**](ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner.md) | Details of the subscription period. | [optional] 
**billing_period** | [**ProductDetailResponseSubscriptionDetailsInnerBillingPeriod**](ProductDetailResponseSubscriptionDetailsInnerBillingPeriod.md) |  | [optional] 
**options** | [**List[ProductDetailResponseSubscriptionDetailsInnerOptionsInner]**](ProductDetailResponseSubscriptionDetailsInnerOptionsInner.md) | Details of the resources available. | [optional] 
**links** | [**List[ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner]**](ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner.md) |  | [optional] 
**next_page** | **str** | link/URL for accessing next page. | [optional] 
**previous_page** | **str** | link/URL for accessing previous page. | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_detail_response_subscription_details_inner import ProductDetailResponseSubscriptionDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseSubscriptionDetailsInner from a JSON string
product_detail_response_subscription_details_inner_instance = ProductDetailResponseSubscriptionDetailsInner.from_json(json)
# print the JSON string representation of the object
print(ProductDetailResponseSubscriptionDetailsInner.to_json())

# convert the object into a dict
product_detail_response_subscription_details_inner_dict = product_detail_response_subscription_details_inner_instance.to_dict()
# create an instance of ProductDetailResponseSubscriptionDetailsInner from a dict
product_detail_response_subscription_details_inner_from_dict = ProductDetailResponseSubscriptionDetailsInner.from_dict(product_detail_response_subscription_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


