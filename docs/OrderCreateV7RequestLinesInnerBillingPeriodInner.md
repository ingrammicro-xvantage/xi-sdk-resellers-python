# OrderCreateV7RequestLinesInnerBillingPeriodInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Billing period of the subscription. Example, Years, Months | [optional] 
**duration** | **int** | Length of the billing period. Example 1, 3 | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_billing_period_inner import OrderCreateV7RequestLinesInnerBillingPeriodInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestLinesInnerBillingPeriodInner from a JSON string
order_create_v7_request_lines_inner_billing_period_inner_instance = OrderCreateV7RequestLinesInnerBillingPeriodInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestLinesInnerBillingPeriodInner.to_json())

# convert the object into a dict
order_create_v7_request_lines_inner_billing_period_inner_dict = order_create_v7_request_lines_inner_billing_period_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestLinesInnerBillingPeriodInner from a dict
order_create_v7_request_lines_inner_billing_period_inner_from_dict = OrderCreateV7RequestLinesInnerBillingPeriodInner.from_dict(order_create_v7_request_lines_inner_billing_period_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


