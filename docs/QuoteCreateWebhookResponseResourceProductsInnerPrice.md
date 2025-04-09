# QuoteCreateWebhookResponseResourceProductsInnerPrice



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_price** | **int** | Ingram Micro quoted price specific to the reseller and quote. | [optional] 
**msrp** | **int** | Manufacturer Suggested Retail Price | [optional] 
**extended_msrp** | **int** | Extended MSRP - Manufacturer Suggested Retail Price X Quantity | [optional] 
**extended_quote_price** | **int** | Extended reseller quoted price (cost to reseller) X Quantity | [optional] 
**discount_off_list** | **float** | Discount off list percentage | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_create_webhook_response_resource_products_inner_price import QuoteCreateWebhookResponseResourceProductsInnerPrice

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteCreateWebhookResponseResourceProductsInnerPrice from a JSON string
quote_create_webhook_response_resource_products_inner_price_instance = QuoteCreateWebhookResponseResourceProductsInnerPrice.from_json(json)
# print the JSON string representation of the object
print(QuoteCreateWebhookResponseResourceProductsInnerPrice.to_json())

# convert the object into a dict
quote_create_webhook_response_resource_products_inner_price_dict = quote_create_webhook_response_resource_products_inner_price_instance.to_dict()
# create an instance of QuoteCreateWebhookResponseResourceProductsInnerPrice from a dict
quote_create_webhook_response_resource_products_inner_price_from_dict = QuoteCreateWebhookResponseResourceProductsInnerPrice.from_dict(quote_create_webhook_response_resource_products_inner_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


