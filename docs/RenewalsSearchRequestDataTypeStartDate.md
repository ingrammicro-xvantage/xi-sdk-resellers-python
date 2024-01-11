# RenewalsSearchRequestDataTypeStartDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_start_date** | **str** | Custom from date for Renewal Start date. | [optional] 
**custom_end_date** | **str** | Custom to date for Renewal Start date. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.renewals_search_request_data_type_start_date import RenewalsSearchRequestDataTypeStartDate

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequestDataTypeStartDate from a JSON string
renewals_search_request_data_type_start_date_instance = RenewalsSearchRequestDataTypeStartDate.from_json(json)
# print the JSON string representation of the object
print RenewalsSearchRequestDataTypeStartDate.to_json()

# convert the object into a dict
renewals_search_request_data_type_start_date_dict = renewals_search_request_data_type_start_date_instance.to_dict()
# create an instance of RenewalsSearchRequestDataTypeStartDate from a dict
renewals_search_request_data_type_start_date_form_dict = renewals_search_request_data_type_start_date.from_dict(renewals_search_request_data_type_start_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


