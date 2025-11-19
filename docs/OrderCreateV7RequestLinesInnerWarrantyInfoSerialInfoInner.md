# OrderCreateV7RequestLinesInnerWarrantyInfoSerialInfoInner

Serial information of the hardware to be associated with the warranty, applicable on post sale orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_purchase** | **str** | Date of purchase of the hardware. | [optional] 
**ship_date** | **str** | Vendor specific mandatory field, date of hardware/product shipment from vendor. | [optional] 
**primary_serial_number** | **str** | Serial number of the hardware/product. | [optional] 
**secondary_serial_number** | **str** | Serial number of accessory associated with the above hardware/product. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_warranty_info_serial_info_inner import OrderCreateV7RequestLinesInnerWarrantyInfoSerialInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestLinesInnerWarrantyInfoSerialInfoInner from a JSON string
order_create_v7_request_lines_inner_warranty_info_serial_info_inner_instance = OrderCreateV7RequestLinesInnerWarrantyInfoSerialInfoInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestLinesInnerWarrantyInfoSerialInfoInner.to_json())

# convert the object into a dict
order_create_v7_request_lines_inner_warranty_info_serial_info_inner_dict = order_create_v7_request_lines_inner_warranty_info_serial_info_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestLinesInnerWarrantyInfoSerialInfoInner from a dict
order_create_v7_request_lines_inner_warranty_info_serial_info_inner_from_dict = OrderCreateV7RequestLinesInnerWarrantyInfoSerialInfoInner.from_dict(order_create_v7_request_lines_inner_warranty_info_serial_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


