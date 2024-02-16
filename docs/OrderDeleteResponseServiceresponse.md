# OrderDeleteResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**OrderDeleteResponseServiceresponseResponsepreamble**](OrderDeleteResponseServiceresponseResponsepreamble.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_delete_response_serviceresponse import OrderDeleteResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDeleteResponseServiceresponse from a JSON string
order_delete_response_serviceresponse_instance = OrderDeleteResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print OrderDeleteResponseServiceresponse.to_json()

# convert the object into a dict
order_delete_response_serviceresponse_dict = order_delete_response_serviceresponse_instance.to_dict()
# create an instance of OrderDeleteResponseServiceresponse from a dict
order_delete_response_serviceresponse_form_dict = order_delete_response_serviceresponse.from_dict(order_delete_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


