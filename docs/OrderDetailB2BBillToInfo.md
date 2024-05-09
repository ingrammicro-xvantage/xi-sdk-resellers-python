# OrderDetailB2BBillToInfo

The billing information provided by the reseller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | The company contact provided by the reseller. | [optional] 
**company_name** | **str** | The name of the company the order will be billed to. | [optional] 
**address_line1** | **str** | The address line 1 the order will be billed to. | [optional] 
**address_line2** | **str** | The address line 2 the order will be billed to. | [optional] 
**address_line3** | **str** | The address line 3 the order will be billed to. | [optional] 
**city** | **str** | The city the order will be billed to. | [optional] 
**state** | **str** | The state the order will be billed to. | [optional] 
**postal_code** | **str** | The zip or postal code the order will be billed to. | [optional] 
**country_code** | **str** | The two-character ISO country code the order will be billed to. | [optional] 
**phone_number** | **str** | The company contact phone number. | [optional] 
**email** | **str** | The company contact email address. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_b2_b_bill_to_info import OrderDetailB2BBillToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BBillToInfo from a JSON string
order_detail_b2_b_bill_to_info_instance = OrderDetailB2BBillToInfo.from_json(json)
# print the JSON string representation of the object
print(OrderDetailB2BBillToInfo.to_json())

# convert the object into a dict
order_detail_b2_b_bill_to_info_dict = order_detail_b2_b_bill_to_info_instance.to_dict()
# create an instance of OrderDetailB2BBillToInfo from a dict
order_detail_b2_b_bill_to_info_from_dict = OrderDetailB2BBillToInfo.from_dict(order_detail_b2_b_bill_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


