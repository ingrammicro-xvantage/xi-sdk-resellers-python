# OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInnerLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | topic being orders or invoices, if it is orders then the link will provide details of the order. If its invoices then the link provides details of the invoice | [optional] 
**href** | **str** | The API endpoint for accessing the relevant data | [optional] 
**type** | **str** | The type of call that can be made to the href link | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_links_inner import OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInnerLinksInner from a JSON string
order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_links_inner_instance = OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInnerLinksInner.to_json()

# convert the object into a dict
order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_links_inner_dict = order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_links_inner_instance.to_dict()
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerSubordersInnerLinksInner from a dict
order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_links_inner_form_dict = order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_links_inner.from_dict(order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


