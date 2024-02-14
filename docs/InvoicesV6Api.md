# xi.sdk.resellers.InvoicesV6Api

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoicedetails_v6**](InvoicesV6Api.md#get_invoicedetails_v6) | **GET** /resellers/v6/invoices/{invoicenumber} | Get Invoice Details v6


# **get_invoicedetails_v6**
> InvoiceDetailResponse get_invoicedetails_v6(invoicenumber, version, im_customer_number, im_country_code, im_correlation_id, im_application_id, customer_type=customer_type, include_serial_numbers=include_serial_numbers)

Get Invoice Details v6

Use your Ingram Micro invoice number to search for existing invoices or retrieve existing invoice details.  The invoice number, IM-CustomerNumber, IM-CountryCode, IM-ApplicationId and IM-CorrelationID are required parameters.  .

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.invoice_detail_response import InvoiceDetailResponse
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
    api_instance = xi.sdk.resellers.InvoicesV6Api(api_client)
    invoicenumber = '335238411' # str | The Ingram Micro invoice number.
    version = '20-222222' # str | Version of codebase.
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    im_application_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany.
    customer_type = 'invoice' # str | it should be invoice or order (optional)
    include_serial_numbers = false # bool | if serial in the response send as true or else false (optional)

    try:
        # Get Invoice Details v6
        api_response = api_instance.get_invoicedetails_v6(invoicenumber, version, im_customer_number, im_country_code, im_correlation_id, im_application_id, customer_type=customer_type, include_serial_numbers=include_serial_numbers)
        print("The response of InvoicesV6Api->get_invoicedetails_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesV6Api->get_invoicedetails_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoicenumber** | **str**| The Ingram Micro invoice number. | 
 **version** | **str**| Version of codebase. | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **im_application_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany. | 
 **customer_type** | **str**| it should be invoice or order | [optional] 
 **include_serial_numbers** | **bool**| if serial in the response send as true or else false | [optional] 

### Return type

[**InvoiceDetailResponse**](InvoiceDetailResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-ApplicationID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

