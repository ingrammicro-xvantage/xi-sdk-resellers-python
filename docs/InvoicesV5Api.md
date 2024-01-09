# xi-sdk-python.InvoicesV5Api

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoices**](InvoicesV5Api.md#get_invoices) | **GET** /resellers/v5/invoices/{invoiceNumber} | Get Invoice Details


# **get_invoices**
> InvoiceDetails get_invoices(invoice_number, customer_number, iso_country_code)

Get Invoice Details

View invoice details. This is a request to query invoice details for a specific Ingram Micro order placed in the last 9 months, whether open or shipped.   <strong>invoiceNumber</strong>, <strong>isoCountryCode</strong> and <strong>customerNumber</strong> parameters are required.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi-sdk-python
from xi-sdk-python.models.invoice_details import InvoiceDetails
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
    api_instance = xi-sdk-python.InvoicesV5Api(api_client)
    invoice_number = '20-RCW67-11' # str | Ingram Micro Invoice Number (default to '20-RCW67-11')
    customer_number = '20-222222' # str | Your unique Ingram Micro customer number (default to '20-222222')
    iso_country_code = 'US' # str | ISO 2 char country code (default to 'US')

    try:
        # Get Invoice Details
        api_response = api_instance.get_invoices(invoice_number, customer_number, iso_country_code)
        print("The response of InvoicesV5Api->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesV5Api->get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_number** | **str**| Ingram Micro Invoice Number | [default to &#39;20-RCW67-11&#39;]
 **customer_number** | **str**| Your unique Ingram Micro customer number | [default to &#39;20-222222&#39;]
 **iso_country_code** | **str**| ISO 2 char country code | [default to &#39;US&#39;]

### Return type

[**InvoiceDetails**](InvoiceDetails.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

