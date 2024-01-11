# MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itemstatus** | **str** |  | [optional] 
**statusmessage** | **str** |  | [optional] 
**ingrampartnumber** | **str** | SKU number for the product for which order needs to be created with Ingram Micro | [optional] 
**vendorpartnumber** | **str** | Vendor Part number for the product | [optional] 
**globalskuid** | **str** |  | [optional] 
**customerprice** | **str** | Customer specific price for the product, excluding taxes | [optional] 
**partdescription1** | **str** | Description on the part number that is being requested | [optional] 
**partdescription2** | **str** | Contuiation of description on the part number that is being requested | [optional] 
**vendornumber** | **str** | Internal four digit code assigned by Ingram | [optional] 
**vendorname** | **str** | Name of the vendor | [optional] 
**cpucode** | **str** | Ingram internal code for a product | [optional] 
**var_class** | **str** | Ingram Micro assigned product classification. | [optional] 
**skustatus** | **str** | Identifies if the SKU has been discontinued. Rules must be defined on the values to be sent out to partner. | [optional] 
**mediacpu** | **str** |  | [optional] 
**categorysubcategory** | **str** | Ingram&#39;s internal categorization of the product | [optional] 
**retailprice** | **float** | MSRP Price 0.00 | 
**newmedia** | **str** | Internal four-digit code assigned by Ingram to represent the item group | [optional] 
**enduserrequired** | **str** | Y - End user required N - Not required End user | [optional] 
**backorderflag** | **str** | Y- Allow Backorder Flag N- Not allowed | [optional] 
**skuauthorized** | **str** |  | [optional] 
**extendedvendorpartnumber** | **str** |  | [optional] 
**warehousedetails** | [**List[MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner]**](MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner import MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInner from a JSON string
multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_instance = MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInner.from_json(json)
# print the JSON string representation of the object
print MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInner.to_json()

# convert the object into a dict
multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_dict = multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_instance.to_dict()
# create an instance of MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInner from a dict
multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_form_dict = multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner.from_dict(multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


