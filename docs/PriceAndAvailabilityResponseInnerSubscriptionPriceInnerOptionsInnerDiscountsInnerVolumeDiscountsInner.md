# PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The 3-digit ISO currency code. | [optional] 
**quantity** | **int** | Quantity of the line item. | [optional] 
**msrp** | **float** | Manufacturer Suggested Retail Price. | [optional] 
**unit_price** | **float** | The unit price of the line item. | [optional] 
**margin** | **float** | Reseller’s margin percentage | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_volume_discounts_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner from a JSON string
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_volume_discounts_inner_instance = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner.to_json())

# convert the object into a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_volume_discounts_inner_dict = price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_volume_discounts_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner from a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_volume_discounts_inner_from_dict = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner.from_dict(price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_volume_discounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


