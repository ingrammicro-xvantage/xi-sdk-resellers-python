# MultiSKUPriceAndStockResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**PriceAndAvailabilityResponseServiceresponseResponsepreamble**](PriceAndAvailabilityResponseServiceresponseResponsepreamble.md) |  | [optional] 
**priceandstockresponse** | [**MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse**](MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.multi_sku_price_and_stock_response_serviceresponse import MultiSKUPriceAndStockResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockResponseServiceresponse from a JSON string
multi_sku_price_and_stock_response_serviceresponse_instance = MultiSKUPriceAndStockResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockResponseServiceresponse.to_json()

# convert the object into a dict
multi_sku_price_and_stock_response_serviceresponse_dict = multi_sku_price_and_stock_response_serviceresponse_instance.to_dict()
# create an instance of MultiSKUPriceAndStockResponseServiceresponse from a dict
multi_sku_price_and_stock_response_serviceresponse_form_dict = multi_sku_price_and_stock_response_serviceresponse.from_dict(multi_sku_price_and_stock_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


