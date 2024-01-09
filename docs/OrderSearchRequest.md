# OrderSearchRequest

Request schema for order search endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicerequest** | [**OrderSearchRequestServicerequest**](OrderSearchRequestServicerequest.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_search_request import OrderSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchRequest from a JSON string
order_search_request_instance = OrderSearchRequest.from_json(json)
# print the JSON string representation of the object
print OrderSearchRequest.to_json()

# convert the object into a dict
order_search_request_dict = order_search_request_instance.to_dict()
# create an instance of OrderSearchRequest from a dict
order_search_request_form_dict = order_search_request.from_dict(order_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


