# MultiSKUPriceAndStockRequestServicerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**MultiSKUPriceAndStockRequestServicerequestRequestpreamble**](MultiSKUPriceAndStockRequestServicerequestRequestpreamble.md) |  | [optional] 
**priceandstockrequest** | [**MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest**](MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.multi_sku_price_and_stock_request_servicerequest import MultiSKUPriceAndStockRequestServicerequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockRequestServicerequest from a JSON string
multi_sku_price_and_stock_request_servicerequest_instance = MultiSKUPriceAndStockRequestServicerequest.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockRequestServicerequest.to_json()

# convert the object into a dict
multi_sku_price_and_stock_request_servicerequest_dict = multi_sku_price_and_stock_request_servicerequest_instance.to_dict()
# create an instance of MultiSKUPriceAndStockRequestServicerequest from a dict
multi_sku_price_and_stock_request_servicerequest_form_dict = multi_sku_price_and_stock_request_servicerequest.from_dict(multi_sku_price_and_stock_request_servicerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


