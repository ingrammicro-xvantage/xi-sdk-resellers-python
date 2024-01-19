# RenewalsSearchRequestDataTypeEndDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_start_date** | **str** | Custom from date for Renewal end date. | [optional] 
**custom_end_date** | **str** | Custom to date for Renewal end date. | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_search_request_data_type_end_date import RenewalsSearchRequestDataTypeEndDate

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequestDataTypeEndDate from a JSON string
renewals_search_request_data_type_end_date_instance = RenewalsSearchRequestDataTypeEndDate.from_json(json)
# print the JSON string representation of the object
print RenewalsSearchRequestDataTypeEndDate.to_json()

# convert the object into a dict
renewals_search_request_data_type_end_date_dict = renewals_search_request_data_type_end_date_instance.to_dict()
# create an instance of RenewalsSearchRequestDataTypeEndDate from a dict
renewals_search_request_data_type_end_date_form_dict = renewals_search_request_data_type_end_date.from_dict(renewals_search_request_data_type_end_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


