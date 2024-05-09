# OrderSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records_found** | **int** | No of recourds found for the search. | [optional] 
**page_size** | **int** | No of results per page.(default is 25) | [optional] 
**page_number** | **int** | Current page number.(default is 1) | [optional] 
**orders** | [**List[OrderSearchResponseOrdersInner]**](OrderSearchResponseOrdersInner.md) | The details for the order. | [optional] 
**next_page** | **str** | link/URL for accessing next page. | [optional] 
**previous_page** | **str** | link/URL for accessing previous page. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_search_response import OrderSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponse from a JSON string
order_search_response_instance = OrderSearchResponse.from_json(json)
# print the JSON string representation of the object
print(OrderSearchResponse.to_json())

# convert the object into a dict
order_search_response_dict = order_search_response_instance.to_dict()
# create an instance of OrderSearchResponse from a dict
order_search_response_from_dict = OrderSearchResponse.from_dict(order_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


