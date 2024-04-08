# PostAsyncOrderCreateV7400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traceid** | **str** | A unique trace id to identify the issue. | [optional] 
**type** | **str** | Type of the error message. | [optional] 
**message** | **str** | A detailed error message. | [optional] 
**fields** | [**List[PostAsyncOrderCreateV7400ResponseFieldsInner]**](PostAsyncOrderCreateV7400ResponseFieldsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.post_async_order_create_v7400_response import PostAsyncOrderCreateV7400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAsyncOrderCreateV7400Response from a JSON string
post_async_order_create_v7400_response_instance = PostAsyncOrderCreateV7400Response.from_json(json)
# print the JSON string representation of the object
print(PostAsyncOrderCreateV7400Response.to_json())

# convert the object into a dict
post_async_order_create_v7400_response_dict = post_async_order_create_v7400_response_instance.to_dict()
# create an instance of PostAsyncOrderCreateV7400Response from a dict
post_async_order_create_v7400_response_form_dict = post_async_order_create_v7400_response.from_dict(post_async_order_create_v7400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


