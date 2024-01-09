# MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**showwarehouseavailability** | **str** | True/false to show the availability of individual warehouses | [optional] 
**extravailabilityflag** | **str** | Y/N to show extra availability flag | [optional] 
**includeallsystems** | **bool** | Flag to indicate if the price and stock information is required for all Ingram Micro systems. If it is set to true, the price and stock details will be returned from all Ingram Micro systems and if false, the price and stock will have returned from the system where the reseller number is set up in. | [optional] 
**item** | [**MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem**](MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.multi_sku_price_and_stock_request_servicerequest_priceandstockrequest import MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest from a JSON string
multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_instance = MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest.to_json()

# convert the object into a dict
multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_dict = multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_instance.to_dict()
# create an instance of MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest from a dict
multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_form_dict = multi_sku_price_and_stock_request_servicerequest_priceandstockrequest.from_dict(multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


