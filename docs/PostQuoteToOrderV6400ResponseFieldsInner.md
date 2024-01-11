# PostQuoteToOrderV6400ResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of the field. | [optional] 
**message** | **str** | A filed level error message. | [optional] 
**value** | **str** | Value of the message. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.post_quote_to_order_v6400_response_fields_inner import PostQuoteToOrderV6400ResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostQuoteToOrderV6400ResponseFieldsInner from a JSON string
post_quote_to_order_v6400_response_fields_inner_instance = PostQuoteToOrderV6400ResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print PostQuoteToOrderV6400ResponseFieldsInner.to_json()

# convert the object into a dict
post_quote_to_order_v6400_response_fields_inner_dict = post_quote_to_order_v6400_response_fields_inner_instance.to_dict()
# create an instance of PostQuoteToOrderV6400ResponseFieldsInner from a dict
post_quote_to_order_v6400_response_fields_inner_form_dict = post_quote_to_order_v6400_response_fields_inner.from_dict(post_quote_to_order_v6400_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


