# OrderCreateV7RequestVmfVendorAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_name** | **str** | The name of the vendor | [optional] 
**product_id** | **str** | The Product ID from the vendor | [optional] 
**additional_attributes** | [**List[OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner]**](OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_vmf_vendor_additional_attributes_inner import OrderCreateV7RequestVmfVendorAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestVmfVendorAdditionalAttributesInner from a JSON string
order_create_v7_request_vmf_vendor_additional_attributes_inner_instance = OrderCreateV7RequestVmfVendorAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestVmfVendorAdditionalAttributesInner.to_json())

# convert the object into a dict
order_create_v7_request_vmf_vendor_additional_attributes_inner_dict = order_create_v7_request_vmf_vendor_additional_attributes_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestVmfVendorAdditionalAttributesInner from a dict
order_create_v7_request_vmf_vendor_additional_attributes_inner_from_dict = OrderCreateV7RequestVmfVendorAdditionalAttributesInner.from_dict(order_create_v7_request_vmf_vendor_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


