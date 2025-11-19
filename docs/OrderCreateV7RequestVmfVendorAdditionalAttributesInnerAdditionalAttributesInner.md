# OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the vendor mandatory field | [optional] 
**attribute_value** | **str** | The value of the vendor mandatory field | [optional] 
**attribute_description** | **str** | The description of the vendor mandatory field | [optional] 
**attribute_hint** | **str** | The hint of the vendor mandatory field. | [optional] 
**choices** | [**List[OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInnerChoicesInner]**](OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInnerChoicesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_vmf_vendor_additional_attributes_inner_additional_attributes_inner import OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner from a JSON string
order_create_v7_request_vmf_vendor_additional_attributes_inner_additional_attributes_inner_instance = OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner.to_json())

# convert the object into a dict
order_create_v7_request_vmf_vendor_additional_attributes_inner_additional_attributes_inner_dict = order_create_v7_request_vmf_vendor_additional_attributes_inner_additional_attributes_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner from a dict
order_create_v7_request_vmf_vendor_additional_attributes_inner_additional_attributes_inner_from_dict = OrderCreateV7RequestVmfVendorAdditionalAttributesInnerAdditionalAttributesInner.from_dict(order_create_v7_request_vmf_vendor_additional_attributes_inner_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


