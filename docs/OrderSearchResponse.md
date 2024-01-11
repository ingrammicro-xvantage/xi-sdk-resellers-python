# OrderSearchResponse

Response schema for order search endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_response** | [**OrderSearchResponseServiceResponse**](OrderSearchResponseServiceResponse.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_search_response import OrderSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponse from a JSON string
order_search_response_instance = OrderSearchResponse.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponse.to_json()

# convert the object into a dict
order_search_response_dict = order_search_response_instance.to_dict()
# create an instance of OrderSearchResponse from a dict
order_search_response_form_dict = order_search_response.from_dict(order_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


