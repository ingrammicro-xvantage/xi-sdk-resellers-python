# OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateof_purchase** | **date** | Date of purchase of the hardware. | [optional] 
**ship_date** | **date** | Vendor specific mandatory field, date of hardware/product shipment from vendor. | [optional] 
**primary_serial_number** | **str** | Serial number of the hardware/product. | [optional] 
**secondary_serial_number** | **str** | Serial number of accessory associated with the above hardware/product. | [optional] 

## Example

```python
from xi-sdk-python.models.order_create_request_lines_inner_warranty_info_inner_serial_info_inner import OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner from a JSON string
order_create_request_lines_inner_warranty_info_inner_serial_info_inner_instance = OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner.to_json()

# convert the object into a dict
order_create_request_lines_inner_warranty_info_inner_serial_info_inner_dict = order_create_request_lines_inner_warranty_info_inner_serial_info_inner_instance.to_dict()
# create an instance of OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner from a dict
order_create_request_lines_inner_warranty_info_inner_serial_info_inner_form_dict = order_create_request_lines_inner_warranty_info_inner_serial_info_inner.from_dict(order_create_request_lines_inner_warranty_info_inner_serial_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


