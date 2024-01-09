# xi-sdk-python.StockUpdateApi

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resellers_v1_webhooks_availabilityupdate_post**](StockUpdateApi.md#resellers_v1_webhooks_availabilityupdate_post) | **POST** /resellers/v1/webhooks/availabilityupdate | Stock Update


# **resellers_v1_webhooks_availabilityupdate_post**
> resellers_v1_webhooks_availabilityupdate_post(targeturl, x_hub_signature, availability_async_notification_request)

Stock Update

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi-sdk-python
from xi-sdk-python.models.availability_async_notification_request import AvailabilityAsyncNotificationRequest
from xi-sdk-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = xi-sdk-python.Configuration(
    host = "https://api.ingrammicro.com:443/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi-sdk-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi-sdk-python.StockUpdateApi(api_client)
    targeturl = 'https://59a2dc5368073ab42fd9a92e210a9fdb.m.pipedream.net/' # str | The webhook url where the request needs to sent.
    x_hub_signature = '3LeaTfLE5FLj1FcYflwdwFosH4ADHmMbds6thtirGC3e9lEkF9/1pt4T2fQQGlxf40EznDBER0b60M75K6ZW0A==' # str | Ingram Micro creates a signature token by use of a secret key + Event ID. The algorithm to generate the secret ley is given at link https://developer.ingrammicro.com/reseller/article/how-use-webhook-secret-key. Use the event Id in the below sample along with your secret key to generate the key. Alternatively, to send try this out, use a random text to see how it works.
    availability_async_notification_request = {"topic":"resellers/catalog","event":"im::updated","eventTimeStamp":"2021-11-01T13:02:06.369Z","eventId":"AH7ESSIWSIO22Y77DD","resource":[{"eventType":"IM::STOCK_UPDATE","ingramPartNumber":"5CX579","vendorPartNumber":"710412-001-BTI","vendorName":"BATTERY TECHNOLOGY INC.","upcCode":"0886734869201","skuStatus":null,"backOrderFlag":"Y","totalAvailability":"120","links":[{"topic":"orders","href":"/resellers/v5/catalog/5CX579","type":"GET"}]},{"eventType":"IM::STOCK_UPDATE","ingramPartNumber":"5CT275","vendorPartNumber":"AC-U90W-HP","vendorName":"BATTERY TECHNOLOGY INC.","upcCode":"0745473120182","skuStatus":null,"backOrderFlag":"Y","totalAvailability":"120","links":[{"topic":"orders","href":"/resellers/v5/catalog/5CT275","type":"GET"}]}]} # AvailabilityAsyncNotificationRequest | 

    try:
        # Stock Update
        api_instance.resellers_v1_webhooks_availabilityupdate_post(targeturl, x_hub_signature, availability_async_notification_request)
    except Exception as e:
        print("Exception when calling StockUpdateApi->resellers_v1_webhooks_availabilityupdate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targeturl** | **str**| The webhook url where the request needs to sent. | 
 **x_hub_signature** | **str**| Ingram Micro creates a signature token by use of a secret key + Event ID. The algorithm to generate the secret ley is given at link https://developer.ingrammicro.com/reseller/article/how-use-webhook-secret-key. Use the event Id in the below sample along with your secret key to generate the key. Alternatively, to send try this out, use a random text to see how it works. | 
 **availability_async_notification_request** | [**AvailabilityAsyncNotificationRequest**](AvailabilityAsyncNotificationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

