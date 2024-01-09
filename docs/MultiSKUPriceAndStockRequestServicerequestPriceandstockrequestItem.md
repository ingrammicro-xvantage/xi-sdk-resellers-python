# MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**ingrampartnumber** | **str** | Ingram Micro system specific SKU number for the product for which the price is requested at Ingram Micro | [optional] 
**vendorpartnumber** | **str** | Vendor Part Number for the product for which the price is requested at Ingram Micro | [optional] 
**upc** | **str** | Universal Product code for the product for which the price is requested at Ingram Micro | [optional] 
**customerpartnumber** | **str** | Unique identification number of customer. For this option the Ingram Micro Sales rep must set up a cross reference table.  | [optional] 
**warehouseidlist** | **str** | Unique identity for Ingram Micro warehouses against which stock details are returned. | [optional] 

## Example

```python
from xi-sdk-python.models.multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item import MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem from a JSON string
multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item_instance = MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem.to_json()

# convert the object into a dict
multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item_dict = multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item_instance.to_dict()
# create an instance of MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem from a dict
multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item_form_dict = multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item.from_dict(multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


