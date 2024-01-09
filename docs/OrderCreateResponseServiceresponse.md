# OrderCreateResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**InvoiceDetailResponseServiceresponseResponsepreamble**](InvoiceDetailResponseServiceresponseResponsepreamble.md) |  | [optional] 
**ordersummary** | [**OrderCreateResponseServiceresponseOrdersummary**](OrderCreateResponseServiceresponseOrdersummary.md) |  | [optional] 
**ordercreateresponse** | [**List[OrderCreateResponseServiceresponseOrdercreateresponseInner]**](OrderCreateResponseServiceresponseOrdercreateresponseInner.md) | Collection of orders | [optional] 

## Example

```python
from xi-sdk-python.models.order_create_response_serviceresponse import OrderCreateResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseServiceresponse from a JSON string
order_create_response_serviceresponse_instance = OrderCreateResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseServiceresponse.to_json()

# convert the object into a dict
order_create_response_serviceresponse_dict = order_create_response_serviceresponse_instance.to_dict()
# create an instance of OrderCreateResponseServiceresponse from a dict
order_create_response_serviceresponse_form_dict = order_create_response_serviceresponse.from_dict(order_create_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


