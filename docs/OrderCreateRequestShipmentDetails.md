# OrderCreateRequestShipmentDetails

Shipping details for the order provided by the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | The code for the shipping carrier for the line item. | [optional] 
**freight_account_number** | **str** | The reseller &#39;s shipping account number with carrier. Used to bill the shipping carrier directly from the reseller&#39;s account with the carrier. | [optional] 
**ship_complete** | **str** | Specifies whether the shipment will be shipped only when all products are fulfilled. The value of this field along with acceptBackOrder field decides the value of backorderflag. If this field is set, acceptBackOrder field is ignored. Possible values for this field are true, C, P, E.    With value as true or C, backorderflag will be set as C.    With value as P, or E, backorderflag will be set as P or E respectively.    C &#x3D; Ship complete at distribution level.    P &#x3D; ship complete at line level.    E &#x3D; ship complete across all distributions.  | [optional] 
**requested_delivery_date** | **date** | The reseller-requested delivery date in UTC format. Delivery date is not guaranteed. | [optional] 
**signature_required** | **bool** | Specifies whether a signature is required for delivery. Default is False. | [optional] 
**shipping_instructions** | **str** |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_create_request_shipment_details import OrderCreateRequestShipmentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestShipmentDetails from a JSON string
order_create_request_shipment_details_instance = OrderCreateRequestShipmentDetails.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestShipmentDetails.to_json()

# convert the object into a dict
order_create_request_shipment_details_dict = order_create_request_shipment_details_instance.to_dict()
# create an instance of OrderCreateRequestShipmentDetails from a dict
order_create_request_shipment_details_form_dict = order_create_request_shipment_details.from_dict(order_create_request_shipment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


