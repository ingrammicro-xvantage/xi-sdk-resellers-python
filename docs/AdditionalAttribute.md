# AdditionalAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the vendor mandatory field. | [optional] 
**attribute_value** | **str** | The value of the vendor mandatory field. | [optional] 
**attribute_description** | **str** | The description of the vendor mandatory field. | [optional] 
**attribute_hint** | **str** | The hint of the vendor mandatory field. | [optional] 
**attribute_required** | **str** | Indicates if the attribute is mandatory (Added to align with C#). | [optional] 
**choices** | [**List[AdditionalAttribute]**](AdditionalAttribute.md) | A list of possible choices for the attribute. | [optional] 

## Example

```python
from xi.sdk.resellers.models.additional_attribute import AdditionalAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAttribute from a JSON string
additional_attribute_instance = AdditionalAttribute.from_json(json)
# print the JSON string representation of the object
print(AdditionalAttribute.to_json())

# convert the object into a dict
additional_attribute_dict = additional_attribute_instance.to_dict()
# create an instance of AdditionalAttribute from a dict
additional_attribute_from_dict = AdditionalAttribute.from_dict(additional_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


