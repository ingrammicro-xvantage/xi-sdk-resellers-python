# OrderModifyResponseServiceresponseOrdermodifyresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responseflag** | **str** |  | [optional] 
**errortype** | **str** |  | [optional] 
**acktriggered** | **str** |  | [optional] 
**warncode** | **str** |  | [optional] 
**headerresponse** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_modify_response_serviceresponse_ordermodifyresponse import OrderModifyResponseServiceresponseOrdermodifyresponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyResponseServiceresponseOrdermodifyresponse from a JSON string
order_modify_response_serviceresponse_ordermodifyresponse_instance = OrderModifyResponseServiceresponseOrdermodifyresponse.from_json(json)
# print the JSON string representation of the object
print OrderModifyResponseServiceresponseOrdermodifyresponse.to_json()

# convert the object into a dict
order_modify_response_serviceresponse_ordermodifyresponse_dict = order_modify_response_serviceresponse_ordermodifyresponse_instance.to_dict()
# create an instance of OrderModifyResponseServiceresponseOrdermodifyresponse from a dict
order_modify_response_serviceresponse_ordermodifyresponse_form_dict = order_modify_response_serviceresponse_ordermodifyresponse.from_dict(order_modify_response_serviceresponse_ordermodifyresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


