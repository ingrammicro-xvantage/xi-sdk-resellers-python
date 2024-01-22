# OrderSearchResponseServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**OrderSearchResponseServiceResponseResponsepreamble**](OrderSearchResponseServiceResponseResponsepreamble.md) |  | [optional] 
**ordersearchresponse** | [**OrderSearchResponseServiceResponseOrdersearchresponse**](OrderSearchResponseServiceResponseOrdersearchresponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_search_response_service_response import OrderSearchResponseServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseServiceResponse from a JSON string
order_search_response_service_response_instance = OrderSearchResponseServiceResponse.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponseServiceResponse.to_json()

# convert the object into a dict
order_search_response_service_response_dict = order_search_response_service_response_instance.to_dict()
# create an instance of OrderSearchResponseServiceResponse from a dict
order_search_response_service_response_form_dict = order_search_response_service_response.from_dict(order_search_response_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


