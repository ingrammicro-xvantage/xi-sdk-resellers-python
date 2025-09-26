# VendorRequiredInforesponseResponseMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID to identify the error. | [optional] 
**trace_id** | **str** | A unique trace id to identify the issue. | [optional] 
**type** | **str** | Type of the error message. | [optional] 
**message** | **str** | A detailed error message. | [optional] 

## Example

```python
from xi.sdk.resellers.models.vendor_required_inforesponse_response_messages_inner import VendorRequiredInforesponseResponseMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRequiredInforesponseResponseMessagesInner from a JSON string
vendor_required_inforesponse_response_messages_inner_instance = VendorRequiredInforesponseResponseMessagesInner.from_json(json)
# print the JSON string representation of the object
print(VendorRequiredInforesponseResponseMessagesInner.to_json())

# convert the object into a dict
vendor_required_inforesponse_response_messages_inner_dict = vendor_required_inforesponse_response_messages_inner_instance.to_dict()
# create an instance of VendorRequiredInforesponseResponseMessagesInner from a dict
vendor_required_inforesponse_response_messages_inner_from_dict = VendorRequiredInforesponseResponseMessagesInner.from_dict(vendor_required_inforesponse_response_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


