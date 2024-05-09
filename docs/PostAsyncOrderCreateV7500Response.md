# PostAsyncOrderCreateV7500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traceid** | **str** | Unique Id to identify error. | [optional] 
**type** | **str** | Describes the type of the error. | [optional] 
**message** | **str** | Describes the error message. | [optional] 
**fields** | **List[object]** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.post_async_order_create_v7500_response import PostAsyncOrderCreateV7500Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAsyncOrderCreateV7500Response from a JSON string
post_async_order_create_v7500_response_instance = PostAsyncOrderCreateV7500Response.from_json(json)
# print the JSON string representation of the object
print(PostAsyncOrderCreateV7500Response.to_json())

# convert the object into a dict
post_async_order_create_v7500_response_dict = post_async_order_create_v7500_response_instance.to_dict()
# create an instance of PostAsyncOrderCreateV7500Response from a dict
post_async_order_create_v7500_response_from_dict = PostAsyncOrderCreateV7500Response.from_dict(post_async_order_create_v7500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


