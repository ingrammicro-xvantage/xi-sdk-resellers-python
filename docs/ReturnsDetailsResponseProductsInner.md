# ReturnsDetailsResponseProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_line_number** | **int** | Unique Ingram Micro line number. | [optional] 
**description** | **str** | The description of the line item product. | [optional] 
**ingram_part_number** | **str** | Unique IngramMicro part number. | [optional] 
**vendor_part_number** | **str** | The vendor&#39;s part number for the line item. | [optional] 
**upc** | **str** | The UPC code of a product. | [optional] 
**invoice_date** | **str** | The date of the invoice. | [optional] 
**invoice_number** | **str** | Ingram micro Invoice number. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**quantity** | **float** | The quantity of the line item. | [optional] 
**unit_price** | **float** | The unit price of the line item. | [optional] 
**extended_price** | **float** | Unit price X quantity for the line item. | [optional] 
**status** | **str** | The status of the line item. | [optional] 
**return_branch** | **str** | The code of the return branch. | [optional] 
**ship_from_branch** | **str** | The code of the ship from branch. | [optional] 
**request_details** | **str** | Request details. | [optional] 
**additional_details** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.returns_details_response_products_inner import ReturnsDetailsResponseProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsDetailsResponseProductsInner from a JSON string
returns_details_response_products_inner_instance = ReturnsDetailsResponseProductsInner.from_json(json)
# print the JSON string representation of the object
print ReturnsDetailsResponseProductsInner.to_json()

# convert the object into a dict
returns_details_response_products_inner_dict = returns_details_response_products_inner_instance.to_dict()
# create an instance of ReturnsDetailsResponseProductsInner from a dict
returns_details_response_products_inner_form_dict = returns_details_response_products_inner.from_dict(returns_details_response_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


