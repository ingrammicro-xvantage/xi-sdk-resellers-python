# AddressType

Address type object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** |  | [optional] 
**name1** | **str** |  | [optional] 
**name2** | **str** |  | [optional] 
**addressline1** | **str** |  | [optional] 
**addressline2** | **str** |  | [optional] 
**addressline3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**postalcode** | **str** |  | [optional] 
**countrycode** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**phonenumber** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from xi-sdk-python.models.address_type import AddressType

# TODO update the JSON string below
json = "{}"
# create an instance of AddressType from a JSON string
address_type_instance = AddressType.from_json(json)
# print the JSON string representation of the object
print AddressType.to_json()

# convert the object into a dict
address_type_dict = address_type_instance.to_dict()
# create an instance of AddressType from a dict
address_type_form_dict = address_type.from_dict(address_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


