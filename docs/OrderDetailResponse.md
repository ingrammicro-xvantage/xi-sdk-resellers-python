# OrderDetailResponse

Response schema for order details endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceresponse** | [**OrderDetailResponseServiceresponse**](OrderDetailResponseServiceresponse.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_response import OrderDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponse from a JSON string
order_detail_response_instance = OrderDetailResponse.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponse.to_json()

# convert the object into a dict
order_detail_response_dict = order_detail_response_instance.to_dict()
# create an instance of OrderDetailResponse from a dict
order_detail_response_form_dict = order_detail_response.from_dict(order_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


