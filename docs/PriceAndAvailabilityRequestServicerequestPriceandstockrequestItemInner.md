# PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**ingrampartnumber** | **str** | Ingram Micro SKU number | [optional] 
**vendorpartnumber** | **str** | Vendor/Manufacture Part Number | [optional] 
**upc** | **str** | Universal Product code | [optional] 
**customerpartnumber** | **str** | Unique identoifier for the customer, needs custom setup. | [optional] 
**warehouseidlist** | **List[str]** | Unique identity for Ingram Micro warehouses against which stock details are returned. | [optional] 
**extendedvendorpartnumber** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**enduserid** | **str** |  | [optional] 
**govtprogramtype** | **str** |  | [optional] 
**govtendusertype** | **str** |  | [optional] 
**specialbidnumber** | **str** |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.price_and_availability_request_servicerequest_priceandstockrequest_item_inner import PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner from a JSON string
price_and_availability_request_servicerequest_priceandstockrequest_item_inner_instance = PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner.to_json()

# convert the object into a dict
price_and_availability_request_servicerequest_priceandstockrequest_item_inner_dict = price_and_availability_request_servicerequest_priceandstockrequest_item_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner from a dict
price_and_availability_request_servicerequest_priceandstockrequest_item_inner_form_dict = price_and_availability_request_servicerequest_priceandstockrequest_item_inner.from_dict(price_and_availability_request_servicerequest_priceandstockrequest_item_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


