# PostCreateorderV7400ResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of the field. | [optional] 
**message** | **str** | A filed level error message. | [optional] 
**value** | **str** | Value of the message. | [optional] 

## Example

```python
from xi.sdk.resellers.models.post_createorder_v7400_response_fields_inner import PostCreateorderV7400ResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateorderV7400ResponseFieldsInner from a JSON string
post_createorder_v7400_response_fields_inner_instance = PostCreateorderV7400ResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(PostCreateorderV7400ResponseFieldsInner.to_json())

# convert the object into a dict
post_createorder_v7400_response_fields_inner_dict = post_createorder_v7400_response_fields_inner_instance.to_dict()
# create an instance of PostCreateorderV7400ResponseFieldsInner from a dict
post_createorder_v7400_response_fields_inner_from_dict = PostCreateorderV7400ResponseFieldsInner.from_dict(post_createorder_v7400_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


