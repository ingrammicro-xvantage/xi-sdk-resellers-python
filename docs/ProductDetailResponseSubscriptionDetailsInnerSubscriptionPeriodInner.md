# ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_period_unit** | **str** | Unit period of the subscription. Example, Years, Months | [optional] 
**subscription_period** | **int** | Length of the subscription. Example 1, 3 | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_detail_response_subscription_details_inner_subscription_period_inner import ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner from a JSON string
product_detail_response_subscription_details_inner_subscription_period_inner_instance = ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner.from_json(json)
# print the JSON string representation of the object
print(ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner.to_json())

# convert the object into a dict
product_detail_response_subscription_details_inner_subscription_period_inner_dict = product_detail_response_subscription_details_inner_subscription_period_inner_instance.to_dict()
# create an instance of ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner from a dict
product_detail_response_subscription_details_inner_subscription_period_inner_from_dict = ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner.from_dict(product_detail_response_subscription_details_inner_subscription_period_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


