# PostRenewalssearch400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traceid** | **str** | Unique Id to identify error. | [optional] 
**type** | **str** | Describes the type of the error. | [optional] 
**fields** | [**List[GetResellerV6ValidateQuote400ResponseFieldsInner]**](GetResellerV6ValidateQuote400ResponseFieldsInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.post_renewalssearch400_response import PostRenewalssearch400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostRenewalssearch400Response from a JSON string
post_renewalssearch400_response_instance = PostRenewalssearch400Response.from_json(json)
# print the JSON string representation of the object
print PostRenewalssearch400Response.to_json()

# convert the object into a dict
post_renewalssearch400_response_dict = post_renewalssearch400_response_instance.to_dict()
# create an instance of PostRenewalssearch400Response from a dict
post_renewalssearch400_response_form_dict = post_renewalssearch400_response.from_dict(post_renewalssearch400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


