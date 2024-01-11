# OrderCreateRequestOrdercreaterequestOrdercreatedetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerponumber** | **str** | The customers unique Purchase Order number. Keep it unique to retrieve order information | 
**ordertype** | **str** | Order Type - Standard orders, Direct ship orders | 
**enduserordernumber** | **str** | Customers End-user PO number | [optional] 
**billtosuffix** | **str** | Designates flooring acct to be used | [optional] 
**shiptosuffix** | **str** | Applies to customers with multiple ship to locations (store locations) | [optional] 
**shiptoaddress** | [**OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress**](OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress.md) |  | 
**carriercode** | **str** | A customer can dictate what carrier to use for their shipment (Ingram 2-digit carrier code is required). Our recommendation is leave this field blank which will allow Ingram Micro to choose the best carrier to gain the best freight rates. | [optional] 
**thirdpartyfreightaccountnumber** | **str** | Refers to a third-party freight account number for charging freight against. The account number should be passed within this field and the appropriate carrier code should be supplied within the carrier code tags. Prior to sending your request containing the third-party account number, it must be first entered into our system. Your Ingram Micro Sales Representative can action this for you. If submitted within an order without this preapproval the third-party account number will be ignored.  Note: USA partners- For FedEx Air only (carrier codes F1, FO, F2, FG.), please send three leading zeros before your third-party freight account number (i.e.: 000999999999.)  | [optional] 
**specialbidnumber** | **str** | This is the special quote number given to a customer either by a vendor for special pricing or by Ingram Micro. To receive the special pricing assigned to this number it must be included on the order. | [optional] 
**lines** | [**List[OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner]**](OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner.md) |  | 
**extendedspecs** | [**List[OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner]**](OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_create_request_ordercreaterequest_ordercreatedetails import OrderCreateRequestOrdercreaterequestOrdercreatedetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetails from a JSON string
order_create_request_ordercreaterequest_ordercreatedetails_instance = OrderCreateRequestOrdercreaterequestOrdercreatedetails.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestOrdercreaterequestOrdercreatedetails.to_json()

# convert the object into a dict
order_create_request_ordercreaterequest_ordercreatedetails_dict = order_create_request_ordercreaterequest_ordercreatedetails_instance.to_dict()
# create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetails from a dict
order_create_request_ordercreaterequest_ordercreatedetails_form_dict = order_create_request_ordercreaterequest_ordercreatedetails.from_dict(order_create_request_ordercreaterequest_ordercreatedetails_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


