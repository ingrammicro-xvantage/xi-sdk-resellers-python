# xi.sdk.resellers.FreightEstimateApi

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_freightestimate**](FreightEstimateApi.md#post_freightestimate) | **POST** /resellers/v6/freightestimate | Freight Estimate


# **post_freightestimate**
> FreightResponse post_freightestimate(im_customer_number, im_country_code, im_correlation_id, im_customer_contact, im_sender_id=im_sender_id, freight_request=freight_request)

Freight Estimate

The freight estimator endpoint will allow customers to understand the freight cost for an order.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.freight_request import FreightRequest
from xi.sdk.resellers.models.freight_response import FreightResponse
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.FreightEstimateApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    im_customer_contact = 'John.Doe@reseller.com' # str | Logged in Users email address contact.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. (optional)
    freight_request = {"billToAddressId":"000","shipToAddressId":"200","shipToAddress":{"companyName":"ABC TECH","addressLine1":"17501 W 98TH ST SPC 1833","addressLine2":"string","addressLine3":"string","city":"LENEXA","state":"KS","postalCode":"662191736","countryCode":"US"},"lines":[{"customerLineNumber":"001","ingramPartNumber":"A300-123456","quantity":"1","warehouseId":"20","carrierCode":""},{"customerLineNumber":"002","ingramPartNumber":"A300-789012","quantity":"1","warehouseId":"10","carrierCode":""}]} # FreightRequest |  (optional)

    try:
        # Freight Estimate
        api_response = api_instance.post_freightestimate(im_customer_number, im_country_code, im_correlation_id, im_customer_contact, im_sender_id=im_sender_id, freight_request=freight_request)
        print("The response of FreightEstimateApi->post_freightestimate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreightEstimateApi->post_freightestimate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **im_customer_contact** | **str**| Logged in Users email address contact. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. | [optional] 
 **freight_request** | [**FreightRequest**](FreightRequest.md)|  | [optional] 

### Return type

[**FreightResponse**](FreightResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error: Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

