# MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warehouseid** | **str** | Unique 2-digit code of the Ingram Micro warehouse | [optional] 
**warehousedescription** | **str** | City of the Ingram Micro warehouse location | [optional] 
**availablequantity** | **int** | On hand available quantity | [optional] 
**onorderquantity** | **int** | On Order quantity | [optional] 
**onholdquantity** | **str** |  | [optional] 
**etadate** | **str** |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner import MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner from a JSON string
multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner_instance = MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner.to_json()

# convert the object into a dict
multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner_dict = multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner_instance.to_dict()
# create an instance of MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner from a dict
multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner_form_dict = multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner.from_dict(multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


