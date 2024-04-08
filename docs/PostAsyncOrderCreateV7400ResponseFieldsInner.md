# PostAsyncOrderCreateV7400ResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of the field. | [optional] 
**message** | **str** | A filed level error message. | [optional] 
**value** | **str** | Value of the message. | [optional] 

## Example

```python
from xi.sdk.resellers.models.post_async_order_create_v7400_response_fields_inner import PostAsyncOrderCreateV7400ResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostAsyncOrderCreateV7400ResponseFieldsInner from a JSON string
post_async_order_create_v7400_response_fields_inner_instance = PostAsyncOrderCreateV7400ResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(PostAsyncOrderCreateV7400ResponseFieldsInner.to_json())

# convert the object into a dict
post_async_order_create_v7400_response_fields_inner_dict = post_async_order_create_v7400_response_fields_inner_instance.to_dict()
# create an instance of PostAsyncOrderCreateV7400ResponseFieldsInner from a dict
post_async_order_create_v7400_response_fields_inner_form_dict = post_async_order_create_v7400_response_fields_inner.from_dict(post_async_order_create_v7400_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


