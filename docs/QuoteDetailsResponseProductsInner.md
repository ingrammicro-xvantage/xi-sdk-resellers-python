# QuoteDetailsResponseProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_product_guid** | **str** | Quote Product GUID  is the primary quote key in Ingram Micro&#39;s CRM - needed to retrieve quote details. | [optional] 
**line_number** | **str** | Line number which the product will appear in the quote.  Line number is manditory when unique configurations are included in a quote and mainting the item line order is required. | [optional] 
**quantity** | **int** | Quantity of product line item quoted. | [optional] 
**notes** | **str** | Product line item comments. | [optional] 
**ean** | **str** | EANUPC | [optional] 
**coo** | **str** | Country of Origin. | [optional] 
**ingram_part_number** | **str** | Ingram Micro SKU (stock keeping unit). An identification, usually alphanumeric, of a particular product that allows it to be tracked for inventory purposes | [optional] 
**vendor_part_number** | **str** | Vendor Part Number | [optional] 
**description** | **str** | Product description.  Note - The quote view api returns only the product short description as maintained in Ingram Micro&#39;s crm system.  For long descriptions, please refer to alternative information sources. | [optional] 
**weight** | **int** | Weight is provided based on country standard.  For countries following Imperial standards - weight is presented as pounds with decimal.  In countries following metric standards, weight is provided as kilograms with decimal. | [optional] 
**weight_uom** | **str** | Unit of measure | [optional] 
**is_suggestion_product** | **bool** | Flag to indicate if a product line item is a suggested product.  The suggested product is provided in addition to the requested quoted products and a suggested option.  Suggested products are grouped together for subtotal and total calculations. | [optional] 
**vpn_category** | **str** | Vendor product category specific to Cisco. HWDW (hardware) or service. | [optional] 
**quote_products_supplier_part_auxiliary_id** | **str** | Vendor product configuration ID specific to Cisco. | [optional] 
**vendor_name** | **str** | Vendor name of the product | [optional] 
**terms** | **str** | Terms of the quote | [optional] 
**is_subscription** | **bool** |  | [optional] 
**reseller_margin** | **str** |  | [optional] 
**price** | [**QuoteDetailsResponseProductsInnerPrice**](QuoteDetailsResponseProductsInnerPrice.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_details_response_products_inner import QuoteDetailsResponseProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseProductsInner from a JSON string
quote_details_response_products_inner_instance = QuoteDetailsResponseProductsInner.from_json(json)
# print the JSON string representation of the object
print(QuoteDetailsResponseProductsInner.to_json())

# convert the object into a dict
quote_details_response_products_inner_dict = quote_details_response_products_inner_instance.to_dict()
# create an instance of QuoteDetailsResponseProductsInner from a dict
quote_details_response_products_inner_from_dict = QuoteDetailsResponseProductsInner.from_dict(quote_details_response_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


