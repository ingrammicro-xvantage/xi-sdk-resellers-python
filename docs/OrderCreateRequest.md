# OrderCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_order_number** | **str** | The reseller&#39;s unique PO/Order number. | 
**end_customer_order_number** | **str** | The end user/customer&#39;s Purchase Order number. | [optional] 
**bill_to_address_id** | **str** | Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit. | [optional] 
**special_bid_number** | **str** | The bid number provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers. | [optional] 
**notes** | **str** | Order level notes. | [optional] 
**accept_back_order** | **bool** | ENUM [\&quot;true\&quot;,\&quot;false\&quot;] - accept order if this item is backordered. This field along with shipComplete field decides the value of backorderflag. The value of this field is ignored when shipComplete field is present. | [optional] 
**reseller_info** | [**OrderCreateRequestResellerInfo**](OrderCreateRequestResellerInfo.md) |  | [optional] 
**vmf** | [**OrderCreateRequestVmf**](OrderCreateRequestVmf.md) |  | [optional] 
**ship_to_info** | [**OrderCreateRequestShipToInfo**](OrderCreateRequestShipToInfo.md) |  | [optional] 
**end_user_info** | [**OrderCreateRequestEndUserInfo**](OrderCreateRequestEndUserInfo.md) |  | [optional] 
**lines** | [**List[OrderCreateRequestLinesInner]**](OrderCreateRequestLinesInner.md) | The line-level details of the order. | [optional] 
**shipment_details** | [**OrderCreateRequestShipmentDetails**](OrderCreateRequestShipmentDetails.md) |  | [optional] 
**additional_attributes** | [**List[OrderCreateRequestAdditionalAttributesInner]**](OrderCreateRequestAdditionalAttributesInner.md) | Shipment-level additional attributes. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_request import OrderCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequest from a JSON string
order_create_request_instance = OrderCreateRequest.from_json(json)
# print the JSON string representation of the object
print(OrderCreateRequest.to_json())

# convert the object into a dict
order_create_request_dict = order_create_request_instance.to_dict()
# create an instance of OrderCreateRequest from a dict
order_create_request_form_dict = order_create_request.from_dict(order_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


