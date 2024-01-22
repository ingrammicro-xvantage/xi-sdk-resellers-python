# xi.sdk.resellers.OrdersV6Api

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_orderdetails_v6**](OrdersV6Api.md#get_orderdetails_v6) | **GET** /resellers/v6/orders/{ordernumber} | Get Order Details v6


# **get_orderdetails_v6**
> OrderDetailResponse get_orderdetails_v6(ordernumber, im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, ingram_order_date=ingram_order_date, vendor_number=vendor_number, simulate_status=simulate_status, is_iml=is_iml, region_code=region_code)

Get Order Details v6

Use your Ingram Micro sales order number to search for existing orders or retrieve existing order details.  The sales order number, IM-CustomerNumber, IM-CountryCode, IM-SenderID and IM-CorrelationID are required parameters.  In a case when the IM sales order number is repeated, you can refine the result by providing for additional filtering.  Use the \"simulateStatus\" query parameter to test the GET order response for various order statuses. This parameter is only available in the sandbox to help with development and testing of the GET order endpoint.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers
from xi.sdk.resellers.models.order_detail_response import OrderDetailResponse
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
    api_instance = xi.sdk.resellers.OrdersV6Api(api_client)
    ordernumber = '20-RD3QV' # str | The Ingram Micro sales order number.
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany. (optional)
    ingram_order_date = 'Wed May 13 00:00:00 UTC 2020' # date | The date and time in UTC format that the order was created. (optional)
    vendor_number = 'vendor_number_example' # str | Vendor Number. (optional)
    simulate_status = 'simulate_status_example' # str | Order response for various order statuses. Not for use in production. (optional)
    is_iml = True # bool | True/False only for IML customers. (optional)
    region_code = 'region_code_example' # str | Region code for sandbox testing - Not for use in production. (optional)

    try:
        # Get Order Details v6
        api_response = api_instance.get_orderdetails_v6(ordernumber, im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, ingram_order_date=ingram_order_date, vendor_number=vendor_number, simulate_status=simulate_status, is_iml=is_iml, region_code=region_code)
        print("The response of OrdersV6Api->get_orderdetails_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV6Api->get_orderdetails_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordernumber** | **str**| The Ingram Micro sales order number. | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany. | [optional] 
 **ingram_order_date** | **date**| The date and time in UTC format that the order was created. | [optional] 
 **vendor_number** | **str**| Vendor Number. | [optional] 
 **simulate_status** | **str**| Order response for various order statuses. Not for use in production. | [optional] 
 **is_iml** | **bool**| True/False only for IML customers. | [optional] 
 **region_code** | **str**| Region code for sandbox testing - Not for use in production. | [optional] 

### Return type

[**OrderDetailResponse**](OrderDetailResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

