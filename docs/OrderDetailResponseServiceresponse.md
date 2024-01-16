# OrderDetailResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**InvoiceDetailResponseServiceresponseResponsepreamble**](InvoiceDetailResponseServiceresponseResponsepreamble.md) |  | [optional] 
**orderdetailresponse** | [**OrderDetailResponseServiceresponseOrderdetailresponse**](OrderDetailResponseServiceresponseOrderdetailresponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_detail_response_serviceresponse import OrderDetailResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseServiceresponse from a JSON string
order_detail_response_serviceresponse_instance = OrderDetailResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseServiceresponse.to_json()

# convert the object into a dict
order_detail_response_serviceresponse_dict = order_detail_response_serviceresponse_instance.to_dict()
# create an instance of OrderDetailResponseServiceresponse from a dict
order_detail_response_serviceresponse_form_dict = order_detail_response_serviceresponse.from_dict(order_detail_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


