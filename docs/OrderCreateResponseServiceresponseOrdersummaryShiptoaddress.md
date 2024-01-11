# OrderCreateResponseServiceresponseOrdersummaryShiptoaddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**addressline1** | **str** |  | [optional] 
**addressline2** | **str** |  | [optional] 
**addressline3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**postalcode** | **str** |  | [optional] 
**countrycode** | **str** |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_create_response_serviceresponse_ordersummary_shiptoaddress import OrderCreateResponseServiceresponseOrdersummaryShiptoaddress

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseServiceresponseOrdersummaryShiptoaddress from a JSON string
order_create_response_serviceresponse_ordersummary_shiptoaddress_instance = OrderCreateResponseServiceresponseOrdersummaryShiptoaddress.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseServiceresponseOrdersummaryShiptoaddress.to_json()

# convert the object into a dict
order_create_response_serviceresponse_ordersummary_shiptoaddress_dict = order_create_response_serviceresponse_ordersummary_shiptoaddress_instance.to_dict()
# create an instance of OrderCreateResponseServiceresponseOrdersummaryShiptoaddress from a dict
order_create_response_serviceresponse_ordersummary_shiptoaddress_form_dict = order_create_response_serviceresponse_ordersummary_shiptoaddress.from_dict(order_create_response_serviceresponse_ordersummary_shiptoaddress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


