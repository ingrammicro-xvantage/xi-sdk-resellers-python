# PriceAndAvailabilityResponseInnerSubscriptionPriceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** |  | [optional] 
**plan_id** | **str** | Id of the plan. | [optional] 
**plan_uid** | **str** |  | [optional] 
**plan_name** | **str** | Name of the plan. | [optional] 
**plan_description** | **str** | The description of the plan. | [optional] 
**groups** | [**List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerGroupsInner]**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerGroupsInner.md) |  | [optional] 
**billing_period** | [**PriceAndAvailabilityResponseInnerSubscriptionPriceInnerBillingPeriod**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerBillingPeriod.md) |  | [optional] 
**subscription_period** | [**List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerSubscriptionPeriodInner]**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerSubscriptionPeriodInner.md) |  | [optional] 
**options** | [**List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner]**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInner from a JSON string
price_and_availability_response_inner_subscription_price_inner_instance = PriceAndAvailabilityResponseInnerSubscriptionPriceInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityResponseInnerSubscriptionPriceInner.to_json())

# convert the object into a dict
price_and_availability_response_inner_subscription_price_inner_dict = price_and_availability_response_inner_subscription_price_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInner from a dict
price_and_availability_response_inner_subscription_price_inner_from_dict = PriceAndAvailabilityResponseInnerSubscriptionPriceInner.from_dict(price_and_availability_response_inner_subscription_price_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


