# VendorRequiredInforesponseVmfAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_name** | **str** | The name of vendor. | [optional] 
**product_id** | **str** | The ID of product. | [optional] 
**additional_attributes** | [**List[VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner]**](VendorRequiredInforesponseVmfAdditionalAttributesInnerAdditionalAttributesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.vendor_required_inforesponse_vmf_additional_attributes_inner import VendorRequiredInforesponseVmfAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRequiredInforesponseVmfAdditionalAttributesInner from a JSON string
vendor_required_inforesponse_vmf_additional_attributes_inner_instance = VendorRequiredInforesponseVmfAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(VendorRequiredInforesponseVmfAdditionalAttributesInner.to_json())

# convert the object into a dict
vendor_required_inforesponse_vmf_additional_attributes_inner_dict = vendor_required_inforesponse_vmf_additional_attributes_inner_instance.to_dict()
# create an instance of VendorRequiredInforesponseVmfAdditionalAttributesInner from a dict
vendor_required_inforesponse_vmf_additional_attributes_inner_from_dict = VendorRequiredInforesponseVmfAdditionalAttributesInner.from_dict(vendor_required_inforesponse_vmf_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


