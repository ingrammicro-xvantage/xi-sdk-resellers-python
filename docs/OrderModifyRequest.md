# OrderModifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** | Shipment-level notes. | [optional] 
**ship_to_info** | [**OrderModifyRequestShipToInfo**](OrderModifyRequestShipToInfo.md) |  | [optional] 
**lines** | [**List[OrderModifyRequestLinesInner]**](OrderModifyRequestLinesInner.md) | The order line items. | [optional] 
**additional_attributes** | [**List[OrderModifyRequestAdditionalAttributesInner]**](OrderModifyRequestAdditionalAttributesInner.md) | Header-level additional attributes. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_modify_request import OrderModifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyRequest from a JSON string
order_modify_request_instance = OrderModifyRequest.from_json(json)
# print the JSON string representation of the object
print(OrderModifyRequest.to_json())

# convert the object into a dict
order_modify_request_dict = order_modify_request_instance.to_dict()
# create an instance of OrderModifyRequest from a dict
order_modify_request_from_dict = OrderModifyRequest.from_dict(order_modify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


