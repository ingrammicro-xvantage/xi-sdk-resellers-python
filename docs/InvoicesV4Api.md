# xi-sdk-python.InvoicesV4Api

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v4_invoicedetails**](InvoicesV4Api.md#post_v4_invoicedetails) | **POST** /invoices/v4/invoicedetails | Get Invoice Details


# **post_v4_invoicedetails**
> InvoiceDetailResponse post_v4_invoicedetails(invoice_detail_request=invoice_detail_request)

Get Invoice Details

A real-time request that allows the customer to query Ingram Micro for Invoice information for a specific open or shipped order (in the past 9 months). Orders are searched using Ingram Micro Sales Order Number.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi-sdk-python
from xi-sdk-python.models.invoice_detail_request import InvoiceDetailRequest
from xi-sdk-python.models.invoice_detail_response import InvoiceDetailResponse
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
    api_instance = xi-sdk-python.InvoicesV4Api(api_client)
    invoice_detail_request = {"servicerequest":{"requestpreamble":{"isocountrycode":"US","customernumber":"20-222222"},"invoicedetailrequest":{"invoicenumber":"30-13649-13","customerponumber":"DH-200732"}}} # InvoiceDetailRequest |  (optional)

    try:
        # Get Invoice Details
        api_response = api_instance.post_v4_invoicedetails(invoice_detail_request=invoice_detail_request)
        print("The response of InvoicesV4Api->post_v4_invoicedetails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesV4Api->post_v4_invoicedetails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_detail_request** | [**InvoiceDetailRequest**](InvoiceDetailRequest.md)|  | [optional] 

### Return type

[**InvoiceDetailResponse**](InvoiceDetailResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

