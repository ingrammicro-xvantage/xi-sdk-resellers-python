# OrderCreateRequestLinesInnerEndUserInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_user_type** | **str** | Specifies the type of endUser. It can be endUser or endUserContact for SAP flow. | [optional] 
**end_user_id** | **str** | ID for the end user/customer in Ingram Micro&#39;s system. | [optional] 
**contact** | **str** | The contact name for the end user/customer. | [optional] 
**company_name** | **str** | The company name for the end user/customer. | [optional] 
**name1** | **str** | name1 | [optional] 
**name2** | **str** | name2 | [optional] 
**address_line1** | **str** | The end user/customer&#39;s street address and building or house number. | [optional] 
**address_line2** | **str** | The end user/customer&#39;s apartment number. | [optional] 
**address_line3** | **str** | Line 3 of the address for the end user/customer. | [optional] 
**address_line4** | **str** | Street address4 | [optional] 
**city** | **str** | The end user/customer&#39;s city. | [optional] 
**state** | **str** | The end user/customer&#39;s state. | [optional] 
**postal_code** | **str** | The end user/customer&#39;s zip or postal code. | [optional] 
**country_code** | **str** | The end user/customer&#39;s two-character ISO country code. | [optional] 
**phone_number** | **float** | The end user/customer&#39;s phone number. | [optional] 
**email** | **str** | The end user/customer&#39;s email. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_create_request_lines_inner_end_user_info_inner import OrderCreateRequestLinesInnerEndUserInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestLinesInnerEndUserInfoInner from a JSON string
order_create_request_lines_inner_end_user_info_inner_instance = OrderCreateRequestLinesInnerEndUserInfoInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestLinesInnerEndUserInfoInner.to_json()

# convert the object into a dict
order_create_request_lines_inner_end_user_info_inner_dict = order_create_request_lines_inner_end_user_info_inner_instance.to_dict()
# create an instance of OrderCreateRequestLinesInnerEndUserInfoInner from a dict
order_create_request_lines_inner_end_user_info_inner_form_dict = order_create_request_lines_inner_end_user_info_inner.from_dict(order_create_request_lines_inner_end_user_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


