# VendorRequiredInfoRequestProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_part_number** | **str** | Ingram Micro unique part number for the product. | [optional] 
**vendor_part_number** | **str** | Vendor’s part number for the product. It can be either TS Product or Cloud Product vendorpartnumber. | [optional] 
**plan_id** | **str** | The ID of the subscription plan. | [optional] 

## Example

```python
from xi.sdk.resellers.models.vendor_required_info_request_products_inner import VendorRequiredInfoRequestProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRequiredInfoRequestProductsInner from a JSON string
vendor_required_info_request_products_inner_instance = VendorRequiredInfoRequestProductsInner.from_json(json)
# print the JSON string representation of the object
print(VendorRequiredInfoRequestProductsInner.to_json())

# convert the object into a dict
vendor_required_info_request_products_inner_dict = vendor_required_info_request_products_inner_instance.to_dict()
# create an instance of VendorRequiredInfoRequestProductsInner from a dict
vendor_required_info_request_products_inner_from_dict = VendorRequiredInfoRequestProductsInner.from_dict(vendor_required_info_request_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


