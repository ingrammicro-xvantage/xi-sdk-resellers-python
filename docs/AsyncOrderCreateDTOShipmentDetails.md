# AsyncOrderCreateDTOShipmentDetails

Shipping details for the order provided by the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | The code for the shipping carrier for the line item. | [optional] 
**requested_delivery_date** | **str** | The reseller-requested delivery date in UTC format. Delivery date is not guaranteed. | [optional] 
**ship_complete** | **str** | Specifies whether the shipment will be shipped only when all products are fulfilled. The value of this field along with acceptBackOrder field decides the value of backorderflag. If this field is set, acceptBackOrder field is ignored. Possible values for this field are true, C, P, E. | [optional] 
**shipping_instructions** | **str** | Any special shipping instructions for the order. | [optional] 
**freight_account_number** | **str** | The reseller &#39;s shipping account number with carrier. Used to bill the shipping carrier directly from the reseller&#39;s account with the carrier. | [optional] 
**signature_required** | **bool** | Specifies whether a signature is required for delivery. Default is False. | [optional] 

## Example

```python
from xi.sdk.resellers.models.async_order_create_dto_shipment_details import AsyncOrderCreateDTOShipmentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOrderCreateDTOShipmentDetails from a JSON string
async_order_create_dto_shipment_details_instance = AsyncOrderCreateDTOShipmentDetails.from_json(json)
# print the JSON string representation of the object
print(AsyncOrderCreateDTOShipmentDetails.to_json())

# convert the object into a dict
async_order_create_dto_shipment_details_dict = async_order_create_dto_shipment_details_instance.to_dict()
# create an instance of AsyncOrderCreateDTOShipmentDetails from a dict
async_order_create_dto_shipment_details_from_dict = AsyncOrderCreateDTOShipmentDetails.from_dict(async_order_create_dto_shipment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


