# OrderCreateResponseServiceresponseOrdersummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerponumber** | **str** |  | [optional] 
**totalorderamount** | **str** | Total of all the orders including taxes and fees | [optional] 
**totalordercreated** | **str** | Number of orders created, in some cases we may create more than one order. | [optional] 
**shiptoaddress** | [**OrderCreateResponseServiceresponseOrdersummaryShiptoaddress**](OrderCreateResponseServiceresponseOrdersummaryShiptoaddress.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_create_response_serviceresponse_ordersummary import OrderCreateResponseServiceresponseOrdersummary

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseServiceresponseOrdersummary from a JSON string
order_create_response_serviceresponse_ordersummary_instance = OrderCreateResponseServiceresponseOrdersummary.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseServiceresponseOrdersummary.to_json()

# convert the object into a dict
order_create_response_serviceresponse_ordersummary_dict = order_create_response_serviceresponse_ordersummary_instance.to_dict()
# create an instance of OrderCreateResponseServiceresponseOrdersummary from a dict
order_create_response_serviceresponse_ordersummary_form_dict = order_create_response_serviceresponse_ordersummary.from_dict(order_create_response_serviceresponse_ordersummary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


