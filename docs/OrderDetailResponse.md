# OrderDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_order_number** | **str** | The IngramMicro sales order number. | [optional] 
**ingram_order_date** | **str** | The date and time in UTC format that the order was created. | [optional] 
**order_type** | **str** | The order type. One of B &#x3D; Branch Transfer, C &#x3D; COD, D &#x3D; Direct Ship, F &#x3D; Future Order, P &#x3D; Special Order, M &#x3D; Memo, Q &#x3D; Quote, S &#x3D; Sales Order. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**end_customer_order_number** | **str** | The end user/customer&#39;s order number for reference in their system. | [optional] 
**vendor_sales_order_number** | **str** | The vendor&#39;s order number for reference in their system. | [optional] 
**order_status** | **str** | The header-level status of the order. One of- Shipped, Canceled, Backordered, Processing, On Hold, Delivered. | [optional] 
**order_total** | **float** | The total cost for the order, includes subtotal, freight charges, and tax. | [optional] 
**order_sub_total** | **float** | The sub total cost for the order, not including tax and freight. | [optional] 
**freight_charges** | **float** | The freight charges for the order. | [optional] 
**currency_code** | **str** | The country-specific three digit ISO 4217 currency code for the order. | [optional] 
**total_weight** | **float** | The total weight of the order. Pounds in North America, KG in all other countries. | [optional] 
**total_tax** | **float** | The total tax for the order. | [optional] 
**payment_terms** | **str** | The payment terms of the order. (Ex- Net 30 days). | [optional] 
**notes** | **str** | The header-level notes for the order. | [optional] 
**bill_to_info** | [**OrderDetailResponseBillToInfo**](OrderDetailResponseBillToInfo.md) |  | [optional] 
**ship_to_info** | [**OrderDetailResponseShipToInfo**](OrderDetailResponseShipToInfo.md) |  | [optional] 
**end_user_info** | [**OrderDetailResponseEndUserInfo**](OrderDetailResponseEndUserInfo.md) |  | [optional] 
**lines** | [**List[OrderDetailResponseLinesInner]**](OrderDetailResponseLinesInner.md) |  | [optional] 
**miscellaneous_charges** | [**List[OrderDetailResponseMiscellaneousChargesInner]**](OrderDetailResponseMiscellaneousChargesInner.md) |  | [optional] 
**additional_attributes** | [**List[OrderDetailResponseLinesInnerAdditionalAttributesInner]**](OrderDetailResponseLinesInnerAdditionalAttributesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_response import OrderDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponse from a JSON string
order_detail_response_instance = OrderDetailResponse.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponse.to_json()

# convert the object into a dict
order_detail_response_dict = order_detail_response_instance.to_dict()
# create an instance of OrderDetailResponse from a dict
order_detail_response_form_dict = order_detail_response.from_dict(order_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


