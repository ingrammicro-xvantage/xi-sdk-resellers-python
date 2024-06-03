# OrderSearchResponseOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_order_number** | **str** | The Ingram Micro order number. | [optional] 
**ingram_order_date** | **str** | The date the order was created(UTC). | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**vendor_sales_order_number** | **str** | The vendor&#39;s order number.(only for D-Type Orders) | [optional] 
**vendor_name** | **str** | The name of the vendor. | [optional] 
**end_user_company_name** | **str** | The company name of the end user/customer. | [optional] 
**order_total** | **float** | The total of the order. | [optional] 
**order_status** | **str** | The header-level status of the order.(OPEN/CLOSED/CANCELLED) | [optional] 
**sub_orders** | [**List[OrderSearchResponseOrdersInnerSubOrdersInner]**](OrderSearchResponseOrdersInnerSubOrdersInner.md) | Individual Ingram Micro order numbers associated with a single reseller PO. | [optional] 
**links** | [**OrderSearchResponseOrdersInnerLinks**](OrderSearchResponseOrdersInnerLinks.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_search_response_orders_inner import OrderSearchResponseOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseOrdersInner from a JSON string
order_search_response_orders_inner_instance = OrderSearchResponseOrdersInner.from_json(json)
# print the JSON string representation of the object
print(OrderSearchResponseOrdersInner.to_json())

# convert the object into a dict
order_search_response_orders_inner_dict = order_search_response_orders_inner_instance.to_dict()
# create an instance of OrderSearchResponseOrdersInner from a dict
order_search_response_orders_inner_from_dict = OrderSearchResponseOrdersInner.from_dict(order_search_response_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


