# PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | [optional] 
**resource_uid** | **str** | The resource id of the subscription product. | [optional] 
**resource_name** | **str** | The name of the resource of the subscription product. | [optional] 
**vendor_part_number** | **str** | Vendor’s part number for the subscription product. | [optional] 
**min_units** | **float** | Minimum unit needs to purchased. | [optional] 
**max_units** | **float** | Maximum unit available for a purchase. | [optional] 
**recurringpricemodel** | **str** | Recurring price model | [optional] 
**unit_of_measure** | **str** | Unit of mesaure for a subscription product. | [optional] 
**resource_pricing** | [**List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner]**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner.md) |  | [optional] 
**discounts** | [**List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner]**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner.md) |  | [optional] 
**fees** | [**List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerFeesInner]**](PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerFeesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner from a JSON string
price_and_availability_response_inner_subscription_price_inner_options_inner_instance = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner.to_json())

# convert the object into a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_dict = price_and_availability_response_inner_subscription_price_inner_options_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner from a dict
price_and_availability_response_inner_subscription_price_inner_options_inner_from_dict = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner.from_dict(price_and_availability_response_inner_subscription_price_inner_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


