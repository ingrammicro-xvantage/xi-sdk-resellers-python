# OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** | Customer contact name | [optional] 
**addressline1** | **str** | Company Name or person to deliver. *If there isn’t an attention line please add the company name on address line 1.   UPS and FedEx will create surcharges if address line 1 contains a physical address. | 
**addressline2** | **str** | Street address for delivery | 
**addressline3** | **str** | Continuation of address line 2 | [optional] 
**city** | **str** | Ship to city | 
**state** | **str** | Ship to State or Region | 
**postalcode** | **str** | Ship to Zip code or Postal code | 
**countrycode** | **str** | Ship to country | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_request_ordercreaterequest_ordercreatedetails_shiptoaddress import OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress from a JSON string
order_create_request_ordercreaterequest_ordercreatedetails_shiptoaddress_instance = OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress.to_json()

# convert the object into a dict
order_create_request_ordercreaterequest_ordercreatedetails_shiptoaddress_dict = order_create_request_ordercreaterequest_ordercreatedetails_shiptoaddress_instance.to_dict()
# create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress from a dict
order_create_request_ordercreaterequest_ordercreatedetails_shiptoaddress_form_dict = order_create_request_ordercreaterequest_ordercreatedetails_shiptoaddress.from_dict(order_create_request_ordercreaterequest_ordercreatedetails_shiptoaddress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


