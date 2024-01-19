# QuoteProductListPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_price** | **float** |  | [optional] 
**msrp** | **float** |  | [optional] 
**extended_msrp** | **float** |  | [optional] 
**extended_quote_price** | **float** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_product_list_price import QuoteProductListPrice

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteProductListPrice from a JSON string
quote_product_list_price_instance = QuoteProductListPrice.from_json(json)
# print the JSON string representation of the object
print QuoteProductListPrice.to_json()

# convert the object into a dict
quote_product_list_price_dict = quote_product_list_price_instance.to_dict()
# create an instance of QuoteProductListPrice from a dict
quote_product_list_price_form_dict = quote_product_list_price.from_dict(quote_product_list_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


