# xi-sdk-resellers-python.QuoteToOrderApi

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_quote_to_order_v6**](QuoteToOrderApi.md#post_quote_to_order_v6) | **POST** /resellers/v6/q2o/orders | Quote To Order


# **post_quote_to_order_v6**
> QuoteToOrderResponse post_quote_to_order_v6(im_customer_number, im_country_code, im_correlation_id, quote_to_order_details_dto, im_sender_id=im_sender_id)

Quote To Order

The “Quote to Order” (QTO) endpoint allows a customer to create an order using the existing quote which is in “Ready to Order” status. A customer can create an order using Configure to order (CTO) quote or a non-configure to order (Non-CTO) quote. Upon successful submission of the order create request, a confirmation message will be returned as an API response. <br > <br >Ingram Micro offers webhooks as a method to send notifications to Resellers once the order creation request is received. All the updates related to Order creation will be pushed as a notification to the customer via a pre-defined callback URL as an HTTP post. <br > <br > **Prerequisite:** Pre-defined callback URL <br > <br > Before creating an order using the quote, it’s recommended to validate the quote using the “Validate Quote” endpoint. Validate Quote endpoint will not only validate the quote but also outline all the mandatory fields required by the vendor at a header level and at the line level which a customer need to pass to the Quote To Order endpoint request.  For a detailed understanding of the “Validate Quote” endpoint, review the “Validate Quote” endpoint documentation. <br ><br > **How it works:** <br ><br > - The customer validates the quote with a quote number from Validate Quote endpoint. <br > - The customer copies all the mandatory fields required by the vendor and adds them to the QTO request body. <br > - The customer provides all the values for Vendor mandatory fields along with other required information for QTO to create an order. <br > - After the order creation request receipt acknowledgment from the QTO endpoint, all further order creation updates will be provided via webhook push notification.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi-sdk-resellers-python
from xi-sdk-resellers-python.models.quote_to_order_details_dto import QuoteToOrderDetailsDTO
from xi-sdk-resellers-python.models.quote_to_order_response import QuoteToOrderResponse
from xi-sdk-resellers-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = xi-sdk-resellers-python.Configuration(
    host = "https://api.ingrammicro.com:443/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi-sdk-resellers-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi-sdk-resellers-python.QuoteToOrderApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems.
    quote_to_order_details_dto = {"quoteNumber":"QUO-14551943-D2Y9L9","customerOrderNumber":"12345","enduserOrderNumber":"","billToAddressId":"XYZ","endUserInfo":{"companyName":"ABC TECH","contact":"44045678","addressLine1":"Texas","addressLine2":"4","addressLine3":"","city":"","state":"","postalCode":"","countryCode":"US","email":"abc@gmail.com","phoneNumber":"445678901"},"shipToInfo":{"addressId":"12345","companyName":"","contact":"","addressLine1":"Texas","addressLine2":"4","addressLine3":"","city":"","state":"","postalCode":"","countryCode":"US","email":"abc@gmail.com"},"additionalAttributes":[{"attributeName":"VEND_AUTH_NBR_FLG","attributeValue":"ABC1234"}],"vmfAdditionalAttributes":[{"attributeName":"","attributeValue":"","attributeDescription":""}],"lines":[{"customerLineNumber":"12","ingramPartNumber":"YN6231","quantity":"2","vmfAdditionalAttributesLines":[{"attributeName":"","attributeValue":"","attributeDescription":""}]}]} # QuoteToOrderDetailsDTO | 
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. (optional)

    try:
        # Quote To Order
        api_response = api_instance.post_quote_to_order_v6(im_customer_number, im_country_code, im_correlation_id, quote_to_order_details_dto, im_sender_id=im_sender_id)
        print("The response of QuoteToOrderApi->post_quote_to_order_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteToOrderApi->post_quote_to_order_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems. | 
 **quote_to_order_details_dto** | [**QuoteToOrderDetailsDTO**](QuoteToOrderDetailsDTO.md)|  | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. | [optional] 

### Return type

[**QuoteToOrderResponse**](QuoteToOrderResponse.md)

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

