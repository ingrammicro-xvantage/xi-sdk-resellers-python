# InvoiceDetailsv61ResponseLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_line_number** | **str** | Unique line number from Ingram. | [optional] 
**customer_line_number** | **str** | Line number passes by customer while creating an order. | [optional] [default to '0']
**ingram_part_number** | **str** | Ingram Micro SKU (stock keeping unit). An identification, usually alphanumeric, of a particular product that allows it to be tracked for inventory purposes. | [optional] 
**vendor_part_number** | **str** | Vendor Part Number. | [optional] 
**customer_part_number** | **str** | Part number from customer&#39;s system. | [optional] 
**vendor_name** | **str** | Name of the vendor. | [optional] 
**product_description** | **str** | Description of the product. | [optional] 
**unit_weight** | **str** | Weight of the product. | [optional] 
**quantity** | **int** | Quantity of the product. | [optional] 
**unit_price** | **float** | Unit price of the product. | [optional] 
**unit_of_measure** | **str** | Unit of measure of the product. | [optional] 
**currency_code** | **str** | Currency code. | [optional] 
**extended_price** | **float** | Extended price of the product. | [optional] 
**tax_percentage** | **float** | Tax percentage | [optional] 
**tax_rate** | **float** | Tax rate | [optional] 
**tax_amount** | **float** | Line level tax amount. | [optional] 
**serial_numbers** | [**List[InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner]**](InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner.md) |  | [optional] 
**quantity_ordered** | **int** | Quantity ordered by the customer. | [optional] 
**quantity_shipped** | **int** | Quantity shipped to the customer. | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detailsv61_response_lines_inner import InvoiceDetailsv61ResponseLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseLinesInner from a JSON string
invoice_detailsv61_response_lines_inner_instance = InvoiceDetailsv61ResponseLinesInner.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailsv61ResponseLinesInner.to_json()

# convert the object into a dict
invoice_detailsv61_response_lines_inner_dict = invoice_detailsv61_response_lines_inner_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseLinesInner from a dict
invoice_detailsv61_response_lines_inner_form_dict = invoice_detailsv61_response_lines_inner.from_dict(invoice_detailsv61_response_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


