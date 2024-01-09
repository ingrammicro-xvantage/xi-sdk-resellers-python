# OrderDetailB2BLinesInnerServiceContractInfoContractInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_description** | **str** | The description of the contract. | [optional] 
**contract_number** | **str** | Contract number. | [optional] 
**contract_status** | **str** | The status of the contract. | [optional] 
**contract_start_date** | **str** | Start date of the contract. | [optional] 
**contract_end_date** | **str** | End date of the contract. | [optional] 
**contract_duration** | **str** | The duration of the contract. | [optional] 

## Example

```python
from xi-sdk-python.models.order_detail_b2_b_lines_inner_service_contract_info_contract_info import OrderDetailB2BLinesInnerServiceContractInfoContractInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerServiceContractInfoContractInfo from a JSON string
order_detail_b2_b_lines_inner_service_contract_info_contract_info_instance = OrderDetailB2BLinesInnerServiceContractInfoContractInfo.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerServiceContractInfoContractInfo.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_service_contract_info_contract_info_dict = order_detail_b2_b_lines_inner_service_contract_info_contract_info_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerServiceContractInfoContractInfo from a dict
order_detail_b2_b_lines_inner_service_contract_info_contract_info_form_dict = order_detail_b2_b_lines_inner_service_contract_info_contract_info.from_dict(order_detail_b2_b_lines_inner_service_contract_info_contract_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


