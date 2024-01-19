# PriceAndAvailabilityResponseInnerDiscountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_pricing** | [**List[PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner]**](PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner.md) |  | [optional] 
**quantity_discounts** | [**List[PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner]**](PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_discounts_inner import PriceAndAvailabilityResponseInnerDiscountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerDiscountsInner from a JSON string
price_and_availability_response_inner_discounts_inner_instance = PriceAndAvailabilityResponseInnerDiscountsInner.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseInnerDiscountsInner.to_json()

# convert the object into a dict
price_and_availability_response_inner_discounts_inner_dict = price_and_availability_response_inner_discounts_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerDiscountsInner from a dict
price_and_availability_response_inner_discounts_inner_form_dict = price_and_availability_response_inner_discounts_inner.from_dict(price_and_availability_response_inner_discounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


