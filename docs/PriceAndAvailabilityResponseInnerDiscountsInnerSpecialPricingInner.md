# PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type** | **str** | The type of discount being given to the customer. | [optional] 
**special_bid_numer** | **str** | Pre-approved special pricing/bid number provided to the reseller by the vendor for special pricing and discounts. Used to track the bid number where different line items have different bid numbers. Line-level bid numbers take precedence over header-level bid numbers. | [optional] 
**special_pricing_discount** | **float** | Special pricing discount amount given to the customer. | [optional] 
**special_pricing_effective_date** | **date** | The effective date of the special pricing available to the customer. | [optional] 
**special_pricing_expiration_date** | **date** | The expiration date of the special pricing available to the customer. | [optional] 
**special_pricing_available_quantity** | **int** | The available quantity of products with discounts. | [optional] 
**special_pricing_min_quantity** | **int** | The minimum quantity of products that have to be purchased to ensure the discount is applied. | [optional] 
**government_discount_type** | **str** | Type of Government Discount. *Currently, this discount is only available in the USA. | [optional] 
**government_discounted_customer_price** | **float** | Government Discounted Customer Price. *Currently, this discount is only available in the USA. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.price_and_availability_response_inner_discounts_inner_special_pricing_inner import PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner from a JSON string
price_and_availability_response_inner_discounts_inner_special_pricing_inner_instance = PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner.to_json()

# convert the object into a dict
price_and_availability_response_inner_discounts_inner_special_pricing_inner_dict = price_and_availability_response_inner_discounts_inner_special_pricing_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner from a dict
price_and_availability_response_inner_discounts_inner_special_pricing_inner_form_dict = price_and_availability_response_inner_discounts_inner_special_pricing_inner.from_dict(price_and_availability_response_inner_discounts_inner_special_pricing_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


