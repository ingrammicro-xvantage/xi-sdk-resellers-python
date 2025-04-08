# QuoteDetailsResponseProductsInnerPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_price** | **float** | Ingram Micro quoted price specific to the reseller and quote. | [optional] 
**msrp** | **float** | Manufacturer Suggested Retail Price | [optional] 
**extended_msrp** | **float** | Extended MSRP - Manufacturer Suggested Retail Price X Quantity | [optional] 
**extended_quote_price** | **float** | Extended reseller quoted price (cost to reseller) X Quantity | [optional] 
**remaining_quantity_extended_msrp** | **float** |  | [optional] 
**remaining_quantity_extended_quote_price** | **float** |  | [optional] 
**discount_off_list** | **str** | Discount off list percentage extended | [optional] 
**type** | **str** |  | [optional] 
**recurring_price_model** | **str** |  | [optional] 
**unit_of_measure** | **str** |  | [optional] 
**tax** | **float** |  | [optional] 
**extrafees** | **float** |  | [optional] 
**extra_fees_details** | [**List[QuoteDetailsResponseProductsInnerPriceExtraFeesDetailsInner]**](QuoteDetailsResponseProductsInnerPriceExtraFeesDetailsInner.md) |  | [optional] 
**discounts** | [**List[QuoteDetailsResponseProductsInnerPriceDiscountsInner]**](QuoteDetailsResponseProductsInnerPriceDiscountsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_details_response_products_inner_price import QuoteDetailsResponseProductsInnerPrice

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseProductsInnerPrice from a JSON string
quote_details_response_products_inner_price_instance = QuoteDetailsResponseProductsInnerPrice.from_json(json)
# print the JSON string representation of the object
print(QuoteDetailsResponseProductsInnerPrice.to_json())

# convert the object into a dict
quote_details_response_products_inner_price_dict = quote_details_response_products_inner_price_instance.to_dict()
# create an instance of QuoteDetailsResponseProductsInnerPrice from a dict
quote_details_response_products_inner_price_from_dict = QuoteDetailsResponseProductsInnerPrice.from_dict(quote_details_response_products_inner_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


