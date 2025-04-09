# QuoteCreateRequestProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_line_number** | **str** | The reseller&#39;s line item number for reference in their system. | [optional] 
**ingram_part_number** | **str** | Ingram Micro SKU (stock keeping unit). An identification, usually alphanumeric, of a particular product that allows it to be tracked for inventory purposes | [optional] 
**vendor_part_number** | **str** | Vendor Part Number | [optional] 
**quantity** | **str** | Quantity of product line item quoted. | [optional] 
**special_bid** | **str** | Special bid associated with product line item | [optional] 
**line_level_notes** | **str** | Product line-item comments. | [optional] 
**pricing_type** | **str** | Pricing type of the quote | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_create_request_products_inner import QuoteCreateRequestProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteCreateRequestProductsInner from a JSON string
quote_create_request_products_inner_instance = QuoteCreateRequestProductsInner.from_json(json)
# print the JSON string representation of the object
print(QuoteCreateRequestProductsInner.to_json())

# convert the object into a dict
quote_create_request_products_inner_dict = quote_create_request_products_inner_instance.to_dict()
# create an instance of QuoteCreateRequestProductsInner from a dict
quote_create_request_products_inner_from_dict = QuoteCreateRequestProductsInner.from_dict(quote_create_request_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


