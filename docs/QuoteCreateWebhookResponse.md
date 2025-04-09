# QuoteCreateWebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Field for identifying whether it is a reseller or vendor event. For eg, resellers/orders | [optional] 
**event** | **str** | The event sent in the request. For eg, im::create. | [optional] 
**event_time_stamp** | **str** | The timestamp at which the event was sent. | [optional] 
**event_id** | **str** | A unique id used as identifier for the sepcific event and used for generating the x-hub signature. | [optional] 
**resource** | [**QuoteCreateWebhookResponseResource**](QuoteCreateWebhookResponseResource.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_create_webhook_response import QuoteCreateWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteCreateWebhookResponse from a JSON string
quote_create_webhook_response_instance = QuoteCreateWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteCreateWebhookResponse.to_json())

# convert the object into a dict
quote_create_webhook_response_dict = quote_create_webhook_response_instance.to_dict()
# create an instance of QuoteCreateWebhookResponse from a dict
quote_create_webhook_response_from_dict = QuoteCreateWebhookResponse.from_dict(quote_create_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


