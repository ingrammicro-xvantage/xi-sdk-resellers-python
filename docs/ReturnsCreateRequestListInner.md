# ReturnsCreateRequestListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** | The Invoice number of the order. | 
**invoice_date** | **date** | Date of an Invoice. | 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**ingram_part_number** | **str** | Unique line number from Ingram. | [optional] 
**vendor_part_number** | **str** | Vendor Part Number. | [optional] 
**serial_number** | **str** | Serial number of the product. | [optional] 
**quantity** | **int** | Return quantity of the product. | 
**primary_reason** | **str** | Primary reason to return the product. | 
**secondary_reason** | **str** | Secondary reason to return the product. | 
**notes** | **str** | Return notes. | [optional] 
**reference_number** | **str** | Reference number to return the product. | [optional] 
**bill_to_address_id** | **str** | Suffix used to identify billing address. | [optional] 
**ship_from_info** | [**List[ReturnsCreateRequestListInnerShipFromInfoInner]**](ReturnsCreateRequestListInnerShipFromInfoInner.md) |  | 
**number_of_boxes** | **int** | Number of boxes to return. | 

## Example

```python
from xi-sdk-python.models.returns_create_request_list_inner import ReturnsCreateRequestListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsCreateRequestListInner from a JSON string
returns_create_request_list_inner_instance = ReturnsCreateRequestListInner.from_json(json)
# print the JSON string representation of the object
print ReturnsCreateRequestListInner.to_json()

# convert the object into a dict
returns_create_request_list_inner_dict = returns_create_request_list_inner_instance.to_dict()
# create an instance of ReturnsCreateRequestListInner from a dict
returns_create_request_list_inner_form_dict = returns_create_request_list_inner.from_dict(returns_create_request_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


