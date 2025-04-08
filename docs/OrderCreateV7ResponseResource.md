# OrderCreateV7ResponseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_order_number** | **str** | The reseller&#39;s unique PO/Order number. | [optional] 
**bill_to_address_id** | **str** | Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit | [optional] 
**order_split** | **bool** | true for multiple orders | [optional] 
**processed_partially** | **bool** | true for partial order succesfully placed | [optional] 
**purchase_order_total** | **float** | Total of all the orders including taxes and fees. | [optional] 
**ship_to_info** | [**OrderCreateV7ResponseResourceShipToInfo**](OrderCreateV7ResponseResourceShipToInfo.md) |  | [optional] 
**orders** | [**List[OrderCreateV7ResponseResourceOrdersInner]**](OrderCreateV7ResponseResourceOrdersInner.md) | Order-level details. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_response_resource import OrderCreateV7ResponseResource

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7ResponseResource from a JSON string
order_create_v7_response_resource_instance = OrderCreateV7ResponseResource.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7ResponseResource.to_json())

# convert the object into a dict
order_create_v7_response_resource_dict = order_create_v7_response_resource_instance.to_dict()
# create an instance of OrderCreateV7ResponseResource from a dict
order_create_v7_response_resource_from_dict = OrderCreateV7ResponseResource.from_dict(order_create_v7_response_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


