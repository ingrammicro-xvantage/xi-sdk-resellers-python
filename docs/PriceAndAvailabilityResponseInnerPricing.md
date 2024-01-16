# PriceAndAvailabilityResponseInnerPricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The 3-digit ISO currency code. | [optional] 
**retail_price** | **float** | The retail price of the product. | [optional] 
**map_price** | **float** | Minimum Advertised Price (MAP). If required by the vendor, resellers can not sell below MAP price. | [optional] 
**customer_price** | **float** | The price customer pays after all special pricing and discounts have been applied. | [optional] 
**special_bid_pricing_available** | **bool** | Boolean values specifies whether special Bid discounts are available for the product. | [optional] 
**web_discounts_available** | **bool** | Boolean values specifies whether web Discounts are available for the product. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.price_and_availability_response_inner_pricing import PriceAndAvailabilityResponseInnerPricing

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerPricing from a JSON string
price_and_availability_response_inner_pricing_instance = PriceAndAvailabilityResponseInnerPricing.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseInnerPricing.to_json()

# convert the object into a dict
price_and_availability_response_inner_pricing_dict = price_and_availability_response_inner_pricing_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerPricing from a dict
price_and_availability_response_inner_pricing_form_dict = price_and_availability_response_inner_pricing.from_dict(price_and_availability_response_inner_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


