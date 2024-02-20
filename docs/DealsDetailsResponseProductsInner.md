# DealsDetailsResponseProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_part_number** | **str** | Unique Ingram part number. | [optional] 
**vendor_part_number** | **str** | Vendor Part number for the product. | [optional] 
**upc** | **str** | The UPC code for the product. Consists of 12 numeric digits that are uniquely assigned to each trade item. | [optional] 
**product_description** | **str** | Description of the product. | [optional] 
**msrp** | **float** | Manufacturer Suggested Retail Price. | [optional] 
**extended_msrp** | **float** | Extended MSRP - Manufacturer Suggested Retail Price X Quantity. | [optional] 
**standard_price** | **float** | Standard price of the line item. | [optional] 
**approved_quantity** | **int** | Total quantity approved for the deal. | [optional] 
**remaining_quantity** | **int** | The quantity remaining as part of the deal for the customer to order. | [optional] 
**comments** | **str** | Comments of the deal. | [optional] 
**special_conditions** | **str** | Special conditions of the deal. | [optional] 
**start_date** | **str** | Start Date. | [optional] 
**expiration_date** | **str** | Expiration date. | [optional] 
**days_remaining** | **int** | Number of days remaining before the deal expires. | [optional] 

## Example

```python
from xi.sdk.resellers.models.deals_details_response_products_inner import DealsDetailsResponseProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DealsDetailsResponseProductsInner from a JSON string
deals_details_response_products_inner_instance = DealsDetailsResponseProductsInner.from_json(json)
# print the JSON string representation of the object
print DealsDetailsResponseProductsInner.to_json()

# convert the object into a dict
deals_details_response_products_inner_dict = deals_details_response_products_inner_instance.to_dict()
# create an instance of DealsDetailsResponseProductsInner from a dict
deals_details_response_products_inner_form_dict = deals_details_response_products_inner.from_dict(deals_details_response_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


