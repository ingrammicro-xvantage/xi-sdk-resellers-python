# Fields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.fields import Fields

# TODO update the JSON string below
json = "{}"
# create an instance of Fields from a JSON string
fields_instance = Fields.from_json(json)
# print the JSON string representation of the object
print(Fields.to_json())

# convert the object into a dict
fields_dict = fields_instance.to_dict()
# create an instance of Fields from a dict
fields_from_dict = Fields.from_dict(fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


