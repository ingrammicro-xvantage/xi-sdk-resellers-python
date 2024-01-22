# OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_number** | **List[str]** | License numbers. | [optional] 
**license_start_date** | **str** | Start Date of the license. | [optional] 
**license_end_date** | **str** | End Date of the license. | [optional] 
**description** | **str** | Description of the license. | [optional] 
**quantity** | **str** | Quantity of the license. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_license_info import OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo from a JSON string
order_detail_b2_b_lines_inner_service_contract_info_license_info_instance = OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_service_contract_info_license_info_dict = order_detail_b2_b_lines_inner_service_contract_info_license_info_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo from a dict
order_detail_b2_b_lines_inner_service_contract_info_license_info_form_dict = order_detail_b2_b_lines_inner_service_contract_info_license_info.from_dict(order_detail_b2_b_lines_inner_service_contract_info_license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


