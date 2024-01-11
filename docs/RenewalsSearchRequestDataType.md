# RenewalsSearchRequestDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | [**RenewalsSearchRequestDataTypeStartDate**](RenewalsSearchRequestDataTypeStartDate.md) |  | [optional] 
**end_date** | [**RenewalsSearchRequestDataTypeEndDate**](RenewalsSearchRequestDataTypeEndDate.md) |  | [optional] 
**invoice_date** | [**RenewalsSearchRequestDataTypeInvoiceDate**](RenewalsSearchRequestDataTypeInvoiceDate.md) |  | [optional] 
**expiration_date** | [**RenewalsSearchRequestDataTypeExpirationDate**](RenewalsSearchRequestDataTypeExpirationDate.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.renewals_search_request_data_type import RenewalsSearchRequestDataType

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequestDataType from a JSON string
renewals_search_request_data_type_instance = RenewalsSearchRequestDataType.from_json(json)
# print the JSON string representation of the object
print RenewalsSearchRequestDataType.to_json()

# convert the object into a dict
renewals_search_request_data_type_dict = renewals_search_request_data_type_instance.to_dict()
# create an instance of RenewalsSearchRequestDataType from a dict
renewals_search_request_data_type_form_dict = renewals_search_request_data_type.from_dict(renewals_search_request_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


