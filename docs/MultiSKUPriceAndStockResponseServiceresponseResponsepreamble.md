# MultiSKUPriceAndStockResponseServiceresponseResponsepreamble


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsestatus** | **str** | SUCCESS or FAILED, sometimes PARTIAL SUCCESS if connection to 1 of the systems fails | [optional] 
**responsemessage** | **str** | Overall status message including error message | [optional] 
**statuscode** | **str** | Statuscode Message | [optional] 

## Example

```python
from xi.sdk.resellers.models.multi_sku_price_and_stock_response_serviceresponse_responsepreamble import MultiSKUPriceAndStockResponseServiceresponseResponsepreamble

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockResponseServiceresponseResponsepreamble from a JSON string
multi_sku_price_and_stock_response_serviceresponse_responsepreamble_instance = MultiSKUPriceAndStockResponseServiceresponseResponsepreamble.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockResponseServiceresponseResponsepreamble.to_json()

# convert the object into a dict
multi_sku_price_and_stock_response_serviceresponse_responsepreamble_dict = multi_sku_price_and_stock_response_serviceresponse_responsepreamble_instance.to_dict()
# create an instance of MultiSKUPriceAndStockResponseServiceresponseResponsepreamble from a dict
multi_sku_price_and_stock_response_serviceresponse_responsepreamble_form_dict = multi_sku_price_and_stock_response_serviceresponse_responsepreamble.from_dict(multi_sku_price_and_stock_response_serviceresponse_responsepreamble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


