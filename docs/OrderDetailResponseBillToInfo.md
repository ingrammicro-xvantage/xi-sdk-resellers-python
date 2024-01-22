# OrderDetailResponseBillToInfo

The billing information provided by the reseller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | The company contact provided by the reseller. | [optional] 
**company_name** | **str** | The name of the company the order will be billed to. | [optional] 
**name1** | **str** | First name. | [optional] 
**name2** | **str** | Last name. | [optional] 
**address_line1** | **str** | The street address and building or house number the order will be billed to. | [optional] 
**address_line2** | **str** | The apartment number the order will be billed to. | [optional] 
**address_line3** | **str** | Address line 3. | [optional] 
**city** | **str** | The city the order will be billed to. | [optional] 
**state** | **str** | The state the order will be billed to. | [optional] 
**postal_code** | **str** | The zip or postal code the order will be billed to. | [optional] 
**country_code** | **str** | The two-character ISO country code the order will be billed to. | [optional] 
**phone_number** | **str** | The company contact phone number. | [optional] 
**email** | **str** | The company contact email address. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_response_bill_to_info import OrderDetailResponseBillToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseBillToInfo from a JSON string
order_detail_response_bill_to_info_instance = OrderDetailResponseBillToInfo.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseBillToInfo.to_json()

# convert the object into a dict
order_detail_response_bill_to_info_dict = order_detail_response_bill_to_info_instance.to_dict()
# create an instance of OrderDetailResponseBillToInfo from a dict
order_detail_response_bill_to_info_form_dict = order_detail_response_bill_to_info.from_dict(order_detail_response_bill_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


