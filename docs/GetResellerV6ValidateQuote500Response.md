# GetResellerV6ValidateQuote500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traceid** | **str** | Unique Id to identify error. | [optional] 
**type** | **str** | Describes the type of the error. | [optional] 
**message** | **str** | Describes the error message. | [optional] 
**fields** | **List[object]** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.get_reseller_v6_validate_quote500_response import GetResellerV6ValidateQuote500Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetResellerV6ValidateQuote500Response from a JSON string
get_reseller_v6_validate_quote500_response_instance = GetResellerV6ValidateQuote500Response.from_json(json)
# print the JSON string representation of the object
print(GetResellerV6ValidateQuote500Response.to_json())

# convert the object into a dict
get_reseller_v6_validate_quote500_response_dict = get_reseller_v6_validate_quote500_response_instance.to_dict()
# create an instance of GetResellerV6ValidateQuote500Response from a dict
get_reseller_v6_validate_quote500_response_form_dict = get_reseller_v6_validate_quote500_response.from_dict(get_reseller_v6_validate_quote500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


