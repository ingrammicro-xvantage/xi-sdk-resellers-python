# OrderDetailB2BLinesInnerServiceContractInfoSubscriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | The ID of the subscription. | [optional] 
**subscription_term** | **str** | The term of the subscription. | [optional] 
**renewal_term** | **str** | The renewal term of the subscription. | [optional] 
**billing_model** | **str** | The billing model of the billing. | [optional] 
**subcription_start_date** | **str** | Start date of the subcription. | [optional] 
**subcription_end_date** | **str** | End date of the subcription. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_subscriptions import OrderDetailB2BLinesInnerServiceContractInfoSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerServiceContractInfoSubscriptions from a JSON string
order_detail_b2_b_lines_inner_service_contract_info_subscriptions_instance = OrderDetailB2BLinesInnerServiceContractInfoSubscriptions.from_json(json)
# print the JSON string representation of the object
print(OrderDetailB2BLinesInnerServiceContractInfoSubscriptions.to_json())

# convert the object into a dict
order_detail_b2_b_lines_inner_service_contract_info_subscriptions_dict = order_detail_b2_b_lines_inner_service_contract_info_subscriptions_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerServiceContractInfoSubscriptions from a dict
order_detail_b2_b_lines_inner_service_contract_info_subscriptions_form_dict = order_detail_b2_b_lines_inner_service_contract_info_subscriptions.from_dict(order_detail_b2_b_lines_inner_service_contract_info_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


