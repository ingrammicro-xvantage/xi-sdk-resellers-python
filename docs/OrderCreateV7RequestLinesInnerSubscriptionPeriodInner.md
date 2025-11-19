# OrderCreateV7RequestLinesInnerSubscriptionPeriodInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Unit period of the subscription. Example, Years, Months | [optional] 
**duration** | **int** | Length of the subscription. Example 1, 3 | [optional] 
**start_date** | **str** | The date on which subscription will start. | [optional] 
**end_date_alignment_type** | **str** | Subscription period end date alignment. ENUM -- &#39;MATCH_END_OF_CALENDAR_MONTH&#39;, &#39;CO_TERM_ON_SUBSCRIPTION&#39; | [optional] 
**subscription_id** | **str** | The ID of an existing active subscription. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_subscription_period_inner import OrderCreateV7RequestLinesInnerSubscriptionPeriodInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestLinesInnerSubscriptionPeriodInner from a JSON string
order_create_v7_request_lines_inner_subscription_period_inner_instance = OrderCreateV7RequestLinesInnerSubscriptionPeriodInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestLinesInnerSubscriptionPeriodInner.to_json())

# convert the object into a dict
order_create_v7_request_lines_inner_subscription_period_inner_dict = order_create_v7_request_lines_inner_subscription_period_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestLinesInnerSubscriptionPeriodInner from a dict
order_create_v7_request_lines_inner_subscription_period_inner_from_dict = OrderCreateV7RequestLinesInnerSubscriptionPeriodInner.from_dict(order_create_v7_request_lines_inner_subscription_period_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


