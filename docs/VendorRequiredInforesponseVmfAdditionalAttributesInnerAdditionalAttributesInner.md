# VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the vendor mandatory field. | [optional] 
**attribute_value** | **str** | The value of the vendor mandatory field. | [optional] 
**attribute_description** | **str** | The description of the vendor mandatory field. | [optional] 
**attribute_hint** | **str** | The hint of the vendor mandatory field. | [optional] 
**choices** | [**List[VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInnerChoicesInner]**](VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInnerChoicesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.vendor_required_inforesponse_vmf_additional_attributes_inner_additional_attributes_inner import VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner from a JSON string
vendor_required_inforesponse_vmf_additional_attributes_inner_additional_attributes_inner_instance = VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner.to_json())

# convert the object into a dict
vendor_required_inforesponse_vmf_additional_attributes_inner_additional_attributes_inner_dict = vendor_required_inforesponse_vmf_additional_attributes_inner_additional_attributes_inner_instance.to_dict()
# create an instance of VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner from a dict
vendor_required_inforesponse_vmf_additional_attributes_inner_additional_attributes_inner_from_dict = VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner.from_dict(vendor_required_inforesponse_vmf_additional_attributes_inner_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


