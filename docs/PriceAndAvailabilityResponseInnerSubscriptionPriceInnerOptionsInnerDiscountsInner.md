# PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_discounts** | [**List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner]**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner.md) |  | [optional] 
**special_pricing** | [**List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner]**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner from a JSON string
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_instance = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner.to_json())

# convert the object into a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_dict = price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner from a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_from_dict = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner.from_dict(price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


