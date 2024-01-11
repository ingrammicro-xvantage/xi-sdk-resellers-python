# QuoteProductList



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_product_guid** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**bid_start_date** | **str** |  | [optional] 
**bid_expiry_date** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**line_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**vendor_part_number** | **str** |  | [optional] 
**weight** | **str** |  | [optional] 
**is_suggestion_product** | **str** |  | [optional] 
**vpn_category** | **str** |  | [optional] 
**quote_products_supplier_part_auxiliary_id** | **str** |  | [optional] 
**quote_products_vendor** | **str** |  | [optional] 
**price** | [**QuoteProductListPrice**](QuoteProductListPrice.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.quote_product_list import QuoteProductList

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteProductList from a JSON string
quote_product_list_instance = QuoteProductList.from_json(json)
# print the JSON string representation of the object
print QuoteProductList.to_json()

# convert the object into a dict
quote_product_list_dict = quote_product_list_instance.to_dict()
# create an instance of QuoteProductList from a dict
quote_product_list_form_dict = quote_product_list.from_dict(quote_product_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


