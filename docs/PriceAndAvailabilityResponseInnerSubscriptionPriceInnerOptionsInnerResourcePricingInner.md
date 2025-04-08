# PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the type of pricing. | [optional] 
**quantity** | **str** | Quantity of the line item. | [optional] 
**msrp** | **float** | Manufacturer Suggested Retail Price. | [optional] 
**unit_price** | **float** | The unit price of the line item. | [optional] 
**margin** | **float** | Reseller’s margin percentage | [optional] 
**currency_code** | **str** | The 3-digit ISO currency code. | [optional] 
**subscription_period** | **str** | The subscription period of the line item. | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_resource_pricing_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner from a JSON string
price_and_availability_response_inner_subscription_price_inner_options_inner_resource_pricing_inner_instance = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner.to_json())

# convert the object into a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_resource_pricing_inner_dict = price_and_availability_response_inner_subscription_price_inner_options_inner_resource_pricing_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner from a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_resource_pricing_inner_from_dict = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner.from_dict(price_and_availability_response_inner_subscription_price_inner_options_inner_resource_pricing_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


