# VmfVriAdditionalAttributeContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_name** | **str** | The name of vendor. | [optional] 
**product_id** | **str** | The ID of product. | [optional] 
**additional_attributes** | [**List[AdditionalAttribute]**](AdditionalAttribute.md) | List of required attributes for the specific product. | [optional] 

## Example

```python
from xi.sdk.resellers.models.vmf_vri_additional_attribute_container import VmfVriAdditionalAttributeContainer

# TODO update the JSON string below
json = "{}"
# create an instance of VmfVriAdditionalAttributeContainer from a JSON string
vmf_vri_additional_attribute_container_instance = VmfVriAdditionalAttributeContainer.from_json(json)
# print the JSON string representation of the object
print(VmfVriAdditionalAttributeContainer.to_json())

# convert the object into a dict
vmf_vri_additional_attribute_container_dict = vmf_vri_additional_attribute_container_instance.to_dict()
# create an instance of VmfVriAdditionalAttributeContainer from a dict
vmf_vri_additional_attribute_container_from_dict = VmfVriAdditionalAttributeContainer.from_dict(vmf_vri_additional_attribute_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


