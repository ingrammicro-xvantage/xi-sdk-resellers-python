# MultiSKUPriceAndStockResponse

Response object model for the multi sku price and stock API endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceresponse** | [**MultiSKUPriceAndStockResponseServiceresponse**](MultiSKUPriceAndStockResponseServiceresponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.multi_sku_price_and_stock_response import MultiSKUPriceAndStockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockResponse from a JSON string
multi_sku_price_and_stock_response_instance = MultiSKUPriceAndStockResponse.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockResponse.to_json()

# convert the object into a dict
multi_sku_price_and_stock_response_dict = multi_sku_price_and_stock_response_instance.to_dict()
# create an instance of MultiSKUPriceAndStockResponse from a dict
multi_sku_price_and_stock_response_form_dict = multi_sku_price_and_stock_response.from_dict(multi_sku_price_and_stock_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


