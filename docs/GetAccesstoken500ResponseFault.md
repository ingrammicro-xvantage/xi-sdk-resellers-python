# GetAccesstoken500ResponseFault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faultstring** | **str** |  | [optional] 
**detail** | [**GetAccesstoken500ResponseFaultDetail**](GetAccesstoken500ResponseFaultDetail.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.get_accesstoken500_response_fault import GetAccesstoken500ResponseFault

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccesstoken500ResponseFault from a JSON string
get_accesstoken500_response_fault_instance = GetAccesstoken500ResponseFault.from_json(json)
# print the JSON string representation of the object
print(GetAccesstoken500ResponseFault.to_json())

# convert the object into a dict
get_accesstoken500_response_fault_dict = get_accesstoken500_response_fault_instance.to_dict()
# create an instance of GetAccesstoken500ResponseFault from a dict
get_accesstoken500_response_fault_from_dict = GetAccesstoken500ResponseFault.from_dict(get_accesstoken500_response_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


