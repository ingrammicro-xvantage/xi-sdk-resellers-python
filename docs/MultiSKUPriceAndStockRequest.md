# MultiSKUPriceAndStockRequest

Request object model for the multi sku price and stock API endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicerequest** | [**MultiSKUPriceAndStockRequestServicerequest**](MultiSKUPriceAndStockRequestServicerequest.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.multi_sku_price_and_stock_request import MultiSKUPriceAndStockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockRequest from a JSON string
multi_sku_price_and_stock_request_instance = MultiSKUPriceAndStockRequest.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockRequest.to_json()

# convert the object into a dict
multi_sku_price_and_stock_request_dict = multi_sku_price_and_stock_request_instance.to_dict()
# create an instance of MultiSKUPriceAndStockRequest from a dict
multi_sku_price_and_stock_request_form_dict = multi_sku_price_and_stock_request.from_dict(multi_sku_price_and_stock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


