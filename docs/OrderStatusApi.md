# xi.sdk.resellers.OrderStatusApi

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resellers_v1_webhooks_orderstatusevent_post**](OrderStatusApi.md#resellers_v1_webhooks_orderstatusevent_post) | **POST** /resellers/v1/webhooks/orderstatusevent | Order Status


# **resellers_v1_webhooks_orderstatusevent_post**
> resellers_v1_webhooks_orderstatusevent_post(targeturl, x_hub_signature, order_status_async_notification_request)

Order Status

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers
from xi.sdk.resellers.models.order_status_async_notification_request import OrderStatusAsyncNotificationRequest
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.OrderStatusApi(api_client)
    targeturl = 'https://59a2dc5368073ab42fd9a92e210a9fdb.m.pipedream.net/' # str | The webhook url where the request needs to sent.
    x_hub_signature = '3LeaTfLE5FLj1FcYflwdwFosH4ADHmMbds6thtirGC3e9lEkF9/1pt4T2fQQGlxf40EznDBER0b60M75K6ZW0A==' # str | Ingram Micro creates a signature token by use of a secret key + Event ID. The algorithm to generate the secret ley is given at link https://developer.ingrammicro.com/reseller/article/how-use-webhook-secret-key. Use the event Id in the below sample along with your secret key to generate the key. Alternatively, to send try this out, use a random text to see how it works.
    order_status_async_notification_request = {"topic":"resellers/orders","event":"im::updated","eventTimeStamp":"2021-11-01T13:02:06.369Z","eventId":"N01CIB9VVFYKR9J6ZW","resource":[{"eventType":"im::order_shipped","orderNumber":"20-RD128","customerOrderNumber":"ZENPO","orderEntryTimeStamp":"2020-04-03T08:54:39-07:00","lines":[{"ingramLineNumber":"001","subOrderNumber":"20-RD128-21","lineStatus":"IM::shipped","ingramPartNumber":"5CX895","vendorPartNumber":"TC57HO-1PEZU4P-NA","requestedQuantity":3,"shippedQuantity":2,"backOrderedQuantity":1,"shipmentDetails":[{"shipmentDate":"2019-11-06","shipFromWarehouseId":"10","warehouseName":"New York","carrierCode":"4M","carrierName":"SMARTPOST-BM","packageDetails":[{"cartonNumber":"","quantityInbox":"","trackingNumber":""}]}],"serialNumberDetails":[{"serialNumber":"123123123"}]}],"links":[{"topic":"orders","href":"/resellers/v5/orders/20-RD128","type":"GET"}]}]} # OrderStatusAsyncNotificationRequest | 

    try:
        # Order Status
        api_instance.resellers_v1_webhooks_orderstatusevent_post(targeturl, x_hub_signature, order_status_async_notification_request)
    except Exception as e:
        print("Exception when calling OrderStatusApi->resellers_v1_webhooks_orderstatusevent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targeturl** | **str**| The webhook url where the request needs to sent. | 
 **x_hub_signature** | **str**| Ingram Micro creates a signature token by use of a secret key + Event ID. The algorithm to generate the secret ley is given at link https://developer.ingrammicro.com/reseller/article/how-use-webhook-secret-key. Use the event Id in the below sample along with your secret key to generate the key. Alternatively, to send try this out, use a random text to see how it works. | 
 **order_status_async_notification_request** | [**OrderStatusAsyncNotificationRequest**](OrderStatusAsyncNotificationRequest.md)|  | 

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

