# xi.sdk.resellers.AsyncOrderCreateApi

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_async_order_create_v7**](AsyncOrderCreateApi.md#post_async_order_create_v7) | **POST** /resellers/v7/orders | Async Order Create


# **post_async_order_create_v7**
> AsyncOrderCreateResponse post_async_order_create_v7(im_customer_number, im_country_code, im_correlation_id, async_order_create_dto, im_sender_id=im_sender_id)

Async Order Create

This API will allow customers to perform both standard ordering and quote to order functionality via a single API enabling them to have a single endpoint to cater to all types of orders.  This approach will standardize the ordering flow for customers where they will get the response for all orders on to their webhooks.  It provides the much-awaited async ordering flow for Reseller API where large orders can also be placed via a single API with guaranteed delivery. 

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.async_order_create_dto import AsyncOrderCreateDTO
from xi.sdk.resellers.models.async_order_create_response import AsyncOrderCreateResponse
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
    api_instance = xi.sdk.resellers.AsyncOrderCreateApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems.
    async_order_create_dto = {"quoteNumber":"QUO-14551943-D2Y9L9","customerOrderNumber":"12345","enduserOrderNumber":"","billToAddressId":"XYZ","endUserInfo":{"companyName":"ABC TECH","contact":"44045678","addressLine1":"Texas","addressLine2":"4","addressLine3":"","city":"","state":"","postalCode":"","countryCode":"US","email":"abc@gmail.com","phoneNumber":"445678901"},"shipToInfo":{"addressId":"12345","companyName":"","contact":"","addressLine1":"Texas","addressLine2":"4","addressLine3":"","city":"","state":"","postalCode":"","countryCode":"US","email":"abc@gmail.com"},"additionalAttributes":[{"attributeName":"VEND_AUTH_NBR_FLG","attributeValue":"ABC1234"}],"vmfAdditionalAttributes":[{"attributeName":"","attributeValue":"","attributeDescription":""}],"lines":[{"customerLineNumber":"12","ingramPartNumber":"YN6231","quantity":"2","vmfAdditionalAttributesLines":[{"attributeName":"","attributeValue":"","attributeDescription":""}]}]} # AsyncOrderCreateDTO | 
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. (optional)

    try:
        # Async Order Create
        api_response = api_instance.post_async_order_create_v7(im_customer_number, im_country_code, im_correlation_id, async_order_create_dto, im_sender_id=im_sender_id)
        print("The response of AsyncOrderCreateApi->post_async_order_create_v7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsyncOrderCreateApi->post_async_order_create_v7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems. | 
 **async_order_create_dto** | [**AsyncOrderCreateDTO**](AsyncOrderCreateDTO.md)|  | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. | [optional] 

### Return type

[**AsyncOrderCreateResponse**](AsyncOrderCreateResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

