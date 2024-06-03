# QuoteDetailsResponseProductsInnerPriceDiscountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**avaliable_qunatity** | **int** |  | [optional] 
**minimum_quantity** | **int** |  | [optional] 
**bid_number** | **str** |  | [optional] 
**bid_version** | **str** |  | [optional] 
**valid_from** | **str** |  | [optional] 
**valid_to** | **str** |  | [optional] 
**discount_off_list** | **float** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_details_response_products_inner_price_discounts_inner import QuoteDetailsResponseProductsInnerPriceDiscountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseProductsInnerPriceDiscountsInner from a JSON string
quote_details_response_products_inner_price_discounts_inner_instance = QuoteDetailsResponseProductsInnerPriceDiscountsInner.from_json(json)
# print the JSON string representation of the object
print(QuoteDetailsResponseProductsInnerPriceDiscountsInner.to_json())

# convert the object into a dict
quote_details_response_products_inner_price_discounts_inner_dict = quote_details_response_products_inner_price_discounts_inner_instance.to_dict()
# create an instance of QuoteDetailsResponseProductsInnerPriceDiscountsInner from a dict
quote_details_response_products_inner_price_discounts_inner_from_dict = QuoteDetailsResponseProductsInnerPriceDiscountsInner.from_dict(quote_details_response_products_inner_price_discounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


