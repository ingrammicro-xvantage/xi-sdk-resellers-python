# OrderModifyResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**OrderModifyResponseServiceresponseResponsepreamble**](OrderModifyResponseServiceresponseResponsepreamble.md) |  | [optional] 
**ordermodifyresponse** | [**OrderModifyResponseServiceresponseOrdermodifyresponse**](OrderModifyResponseServiceresponseOrdermodifyresponse.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_modify_response_serviceresponse import OrderModifyResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyResponseServiceresponse from a JSON string
order_modify_response_serviceresponse_instance = OrderModifyResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print OrderModifyResponseServiceresponse.to_json()

# convert the object into a dict
order_modify_response_serviceresponse_dict = order_modify_response_serviceresponse_instance.to_dict()
# create an instance of OrderModifyResponseServiceresponse from a dict
order_modify_response_serviceresponse_form_dict = order_modify_response_serviceresponse.from_dict(order_modify_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


