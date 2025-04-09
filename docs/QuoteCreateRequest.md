# QuoteCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_name** | **str** | Quote Name given to quote by sales team or system generated. Generally used as a reference to identify the quote. | [optional] 
**firstname** | **str** | Logged in Users firstname | [optional] 
**lastname** | **str** | Logged in Users Lastname | [optional] 
**customer_contact** | **str** | Logged in Users email address contact. | [optional] 
**quote_expiry_date** | **str** | The date on which a quote will expire. | [optional] 
**customer_need** | **str** | Any special need from the customer. | [optional] 
**end_user_info** | [**QuoteCreateRequestEndUserInfo**](QuoteCreateRequestEndUserInfo.md) |  | [optional] 
**deal_id** | **str** | Price discount identifyer to specify a pricing discount that has been applied to the quote. | [optional] 
**pricing_type** | **str** | Pricing type of the quote. | [optional] 
**send_quote_copy** | **str** | List of email addressed to whom the quote will be emailed after it&#39;s created. (Max 10 email ids) | [optional] 
**products** | [**List[QuoteCreateRequestProductsInner]**](QuoteCreateRequestProductsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_create_request import QuoteCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteCreateRequest from a JSON string
quote_create_request_instance = QuoteCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuoteCreateRequest.to_json())

# convert the object into a dict
quote_create_request_dict = quote_create_request_instance.to_dict()
# create an instance of QuoteCreateRequest from a dict
quote_create_request_from_dict = QuoteCreateRequest.from_dict(quote_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


