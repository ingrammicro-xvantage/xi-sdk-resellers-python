# OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subordernumber** | **str** | A sub order number | [optional] 
**statuscode** | **str** | Order status code | [optional] 
**status** | **str** | Details of the order statuscode - i.e. statuscode &#x3D; 4 then status &#x3D; SHIPPED | [optional] 
**holdreasoncode** | **str** | Will be returned in case of order on hold | [optional] 
**holdreason** | **str** | Reason for order hold - will be returned if the order is on hold | [optional] 
**links** | [**List[OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInnerLinksInner]**](OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInnerLinksInner.md) | HATEOAS links for the details and invoices of the sub-orders if available | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner import OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner from a JSON string
order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_instance = OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner.to_json()

# convert the object into a dict
order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_dict = order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_instance.to_dict()
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInner from a dict
order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_form_dict = order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner.from_dict(order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


