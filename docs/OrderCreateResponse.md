# OrderCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_order_number** | **str** | The reseller&#39;s unique PO/Order number. | [optional] 
**end_customer_order_number** | **str** | The end user/customer&#39;s Purchase Order number. | [optional] 
**bill_to_address_id** | **str** | Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit | [optional] 
**special_bid_number** | **str** | The bid number provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers. | [optional] 
**order_split** | **bool** | true for multiple orders | [optional] 
**processed_partially** | **bool** | true for partial order succesfully placed | [optional] 
**purchase_order_total** | **float** | Total of all the orders including taxes and fees. | [optional] 
**ship_to_info** | [**OrderCreateResponseShipToInfo**](OrderCreateResponseShipToInfo.md) |  | [optional] 
**end_user_info** | [**OrderCreateResponseEndUserInfo**](OrderCreateResponseEndUserInfo.md) |  | [optional] 
**orders** | [**List[OrderCreateResponseOrdersInner]**](OrderCreateResponseOrdersInner.md) | Order-level details. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_response import OrderCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponse from a JSON string
order_create_response_instance = OrderCreateResponse.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponse.to_json()

# convert the object into a dict
order_create_response_dict = order_create_response_instance.to_dict()
# create an instance of OrderCreateResponse from a dict
order_create_response_form_dict = order_create_response.from_dict(order_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


