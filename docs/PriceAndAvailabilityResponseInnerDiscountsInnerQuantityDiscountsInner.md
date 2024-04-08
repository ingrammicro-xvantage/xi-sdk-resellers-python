# PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_type** | **str** | Indicates when the discount is applied after ordering the product. | [optional] 
**currency_code** | **str** | The country-specific three digit ISO 4217 currency code for the order. | [optional] 
**currency_type** | **str** | Type of currency. | [optional] 
**quantity** | **int** | The total discounted quantity of the product. | [optional] 
**amount** | **float** | The total price of all the discounts applied. | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_discounts_inner_quantity_discounts_inner import PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner from a JSON string
price_and_availability_response_inner_discounts_inner_quantity_discounts_inner_instance = PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner.to_json())

# convert the object into a dict
price_and_availability_response_inner_discounts_inner_quantity_discounts_inner_dict = price_and_availability_response_inner_discounts_inner_quantity_discounts_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner from a dict
price_and_availability_response_inner_discounts_inner_quantity_discounts_inner_form_dict = price_and_availability_response_inner_discounts_inner_quantity_discounts_inner.from_dict(price_and_availability_response_inner_discounts_inner_quantity_discounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


