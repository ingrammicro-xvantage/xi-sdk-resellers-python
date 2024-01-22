# OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordernumber** | **str** | Ingram micro sales order number | 
**entrytimestamp** | **str** | The order creation date-time in UTC format | 
**customerordernumber** | **str** | PO/Order number submitted while creating the order | [optional] 
**suborders** | [**List[OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner]**](OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner.md) | An order MAY get divided into various sub orders, for example if the SKUs are being shipped from different warehouse. | [optional] 
**links** | [**OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks**](OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_search_response_service_response_ordersearchresponse_orders_inner import OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner from a JSON string
order_search_response_service_response_ordersearchresponse_orders_inner_instance = OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner.to_json()

# convert the object into a dict
order_search_response_service_response_ordersearchresponse_orders_inner_dict = order_search_response_service_response_ordersearchresponse_orders_inner_instance.to_dict()
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner from a dict
order_search_response_service_response_ordersearchresponse_orders_inner_form_dict = order_search_response_service_response_ordersearchresponse_orders_inner.from_dict(order_search_response_service_response_ordersearchresponse_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


