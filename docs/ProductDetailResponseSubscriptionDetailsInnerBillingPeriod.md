# ProductDetailResponseSubscriptionDetailsInnerBillingPeriod

Details of the subscription billing period. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_period_unit** | **str** | Billing unit period of the subscription. Example, Years, Months | [optional] 
**billing_period** | **str** | Billing period of the subscription. Example 1, 3 | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_detail_response_subscription_details_inner_billing_period import ProductDetailResponseSubscriptionDetailsInnerBillingPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseSubscriptionDetailsInnerBillingPeriod from a JSON string
product_detail_response_subscription_details_inner_billing_period_instance = ProductDetailResponseSubscriptionDetailsInnerBillingPeriod.from_json(json)
# print the JSON string representation of the object
print(ProductDetailResponseSubscriptionDetailsInnerBillingPeriod.to_json())

# convert the object into a dict
product_detail_response_subscription_details_inner_billing_period_dict = product_detail_response_subscription_details_inner_billing_period_instance.to_dict()
# create an instance of ProductDetailResponseSubscriptionDetailsInnerBillingPeriod from a dict
product_detail_response_subscription_details_inner_billing_period_from_dict = ProductDetailResponseSubscriptionDetailsInnerBillingPeriod.from_dict(product_detail_response_subscription_details_inner_billing_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


