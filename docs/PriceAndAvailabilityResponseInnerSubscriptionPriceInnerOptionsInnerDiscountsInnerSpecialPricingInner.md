# PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The 3-digit ISO currency code. | [optional] 
**discount** | **float** | The discount for the line item. | [optional] 
**discount_type** | **str** | The type of the discount | [optional] 
**discount_qty_limit** | **int** | The quantity available at the discounted price | [optional] 
**discount_expiry_date** | **str** | The date when discount expires. | [optional] 
**vendor_program_name** | **str** | The vendors discount program name. | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_special_pricing_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner from a JSON string
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_special_pricing_inner_instance = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner.to_json())

# convert the object into a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_special_pricing_inner_dict = price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_special_pricing_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner from a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_special_pricing_inner_from_dict = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner.from_dict(price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_special_pricing_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


