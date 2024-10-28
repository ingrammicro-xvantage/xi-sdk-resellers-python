# OrderCreateV7RequestVmfAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the header level field. | [optional] 
**attribute_value** | **str** | The value of the header level field. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_vmf_additional_attributes_inner import OrderCreateV7RequestVmfAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestVmfAdditionalAttributesInner from a JSON string
order_create_v7_request_vmf_additional_attributes_inner_instance = OrderCreateV7RequestVmfAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestVmfAdditionalAttributesInner.to_json())

# convert the object into a dict
order_create_v7_request_vmf_additional_attributes_inner_dict = order_create_v7_request_vmf_additional_attributes_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestVmfAdditionalAttributesInner from a dict
order_create_v7_request_vmf_additional_attributes_inner_from_dict = OrderCreateV7RequestVmfAdditionalAttributesInner.from_dict(order_create_v7_request_vmf_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


