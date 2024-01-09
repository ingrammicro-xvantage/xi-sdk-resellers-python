# OrderModifyResponse

Response schema for order modify endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceresponse** | [**OrderModifyResponseServiceresponse**](OrderModifyResponseServiceresponse.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_modify_response import OrderModifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyResponse from a JSON string
order_modify_response_instance = OrderModifyResponse.from_json(json)
# print the JSON string representation of the object
print OrderModifyResponse.to_json()

# convert the object into a dict
order_modify_response_dict = order_modify_response_instance.to_dict()
# create an instance of OrderModifyResponse from a dict
order_modify_response_form_dict = order_modify_response.from_dict(order_modify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


