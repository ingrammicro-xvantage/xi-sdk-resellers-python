# OrderDetailB2BLinesInnerServiceContractInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_info** | [**OrderDetailB2BLinesInnerServiceContractInfoContractInfo**](OrderDetailB2BLinesInnerServiceContractInfoContractInfo.md) |  | [optional] 
**subscriptions** | [**OrderDetailB2BLinesInnerServiceContractInfoSubscriptions**](OrderDetailB2BLinesInnerServiceContractInfoSubscriptions.md) |  | [optional] 
**license_info** | [**OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo**](OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_b2_b_lines_inner_service_contract_info import OrderDetailB2BLinesInnerServiceContractInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerServiceContractInfo from a JSON string
order_detail_b2_b_lines_inner_service_contract_info_instance = OrderDetailB2BLinesInnerServiceContractInfo.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerServiceContractInfo.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_service_contract_info_dict = order_detail_b2_b_lines_inner_service_contract_info_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerServiceContractInfo from a dict
order_detail_b2_b_lines_inner_service_contract_info_form_dict = order_detail_b2_b_lines_inner_service_contract_info.from_dict(order_detail_b2_b_lines_inner_service_contract_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


