# OrderCreateV7RequestLinesInnerEndUserInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_user_id** | **str** | ID for the end user/customer in Ingram Micro&#39;s system. | [optional] 
**end_user_type** | **str** | Specifies the type of endUser. It can be endUser or endUserContact for SAP flow. | [optional] 
**company_name** | **str** | The company name for the end user/customer. | [optional] 
**address_line1** | **str** | The end user/customer&#39;s street address and building or house number. | [optional] 
**address_line2** | **str** | The end user/customer&#39;s apartment number. | [optional] 
**contact** | **str** | The contact name for the end user/customer. | [optional] 
**city** | **str** | The end user/customer&#39;s city. | [optional] 
**state** | **str** | The end user/customer&#39;s state. | [optional] 
**postal_code** | **str** | The end user/customer&#39;s zip or postal code. | [optional] 
**country_code** | **str** | The end user/customer&#39;s two-character ISO country code. | [optional] 
**phone_number** | **str** | End User Name | [optional] 
**email** | **str** | The end user/customer&#39;s email. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_end_user_info_inner import OrderCreateV7RequestLinesInnerEndUserInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestLinesInnerEndUserInfoInner from a JSON string
order_create_v7_request_lines_inner_end_user_info_inner_instance = OrderCreateV7RequestLinesInnerEndUserInfoInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestLinesInnerEndUserInfoInner.to_json())

# convert the object into a dict
order_create_v7_request_lines_inner_end_user_info_inner_dict = order_create_v7_request_lines_inner_end_user_info_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestLinesInnerEndUserInfoInner from a dict
order_create_v7_request_lines_inner_end_user_info_inner_from_dict = OrderCreateV7RequestLinesInnerEndUserInfoInner.from_dict(order_create_v7_request_lines_inner_end_user_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


