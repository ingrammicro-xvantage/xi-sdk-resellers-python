# xi.sdk.resellers.InvoicesApi

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoicedetails_v6_1**](InvoicesApi.md#get_invoicedetails_v6_1) | **GET** /resellers/v6.1/invoices/{invoiceNumber} | Get Invoice Details v6.1
[**get_resellers_v6_invoicesearch**](InvoicesApi.md#get_resellers_v6_invoicesearch) | **GET** /resellers/v6/invoices | Search your invoice


# **get_invoicedetails_v6_1**
> InvoiceDetailsv61Response get_invoicedetails_v6_1(invoice_number, im_customer_number, im_country_code, im_correlation_id, im_application_id, customer_type=customer_type, include_serial_numbers=include_serial_numbers)

Get Invoice Details v6.1

Use your Ingram Micro invoice number to search for existing invoices or retrieve existing invoice details.

The invoice number, IM-CustomerNumber, IM-CountryCode, IM-ApplicationId and IM-CorrelationID are required parameters.

.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.invoice_detailsv61_response import InvoiceDetailsv61Response
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
    api_instance = xi.sdk.resellers.InvoicesApi(api_client)
    invoice_number = '335238411' # str | The Ingram Micro invoice number.
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    im_application_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany.
    customer_type = 'invoice' # str | it should be invoice or order (optional)
    include_serial_numbers = false # bool | if serial in the response send as true or else false (optional)

    try:
        # Get Invoice Details v6.1
        api_response = api_instance.get_invoicedetails_v6_1(invoice_number, im_customer_number, im_country_code, im_correlation_id, im_application_id, customer_type=customer_type, include_serial_numbers=include_serial_numbers)
        print("The response of InvoicesApi->get_invoicedetails_v6_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoicedetails_v6_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_number** | **str**| The Ingram Micro invoice number. | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **im_application_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany. | 
 **customer_type** | **str**| it should be invoice or order | [optional] 
 **include_serial_numbers** | **bool**| if serial in the response send as true or else false | [optional] 

### Return type

[**InvoiceDetailsv61Response**](InvoiceDetailsv61Response.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resellers_v6_invoicesearch**
> InvoiceSearchResponse get_resellers_v6_invoicesearch(im_application_id, im_customer_number, im_country_code, im_correlation_id, payment_terms_net_date=payment_terms_net_date, invoice_date=invoice_date, invoice_due_date=invoice_due_date, order_date=order_date, order_from_date=order_from_date, order_to_date=order_to_date, order_number=order_number, delivery_number=delivery_number, invoice_number=invoice_number, invoice_status=invoice_status, invoice_type=invoice_type, customer_order_number=customer_order_number, end_customer_order_number=end_customer_order_number, special_bid_number=special_bid_number, invoice_from_due_date=invoice_from_due_date, invoice_to_due_date=invoice_to_due_date, invoice_from_date=invoice_from_date, invoice_to_date=invoice_to_date, page_size=page_size, page_number=page_number, orderby=orderby, direction=direction, serial_number=serial_number)

Search your invoice

Search your Ingram Micro invoices. This endpoint searches by multiple invoice parameters and supports pagination of results.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.invoice_search_response import InvoiceSearchResponse
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
    api_instance = xi.sdk.resellers.InvoicesApi(api_client)
    im_application_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    payment_terms_net_date = '2021-04-23' # str | Search by payment terms net date(yyyy-MM-dd). (optional)
    invoice_date = '2021-04-23' # str | Search by invoice date(yyyy-MM-dd). (optional)
    invoice_due_date = '2021-04-23' # str | Search by invoice date from(yyyy-MM-dd). (optional)
    order_date = '2021-04-23' # str | Search by OrderDate date(yyyy-MM-dd). (optional)
    order_from_date = '2021-04-23' # str | Search by OrderFromDate date(yyyy-MM-dd). (optional)
    order_to_date = '2021-04-23' # str | Search by OrderToDate date(yyyy-MM-dd). (optional)
    order_number = '2021-04-23' # str | Search by order number (optional)
    delivery_number = '335238411' # str | Search by delivery number. (optional)
    invoice_number = 'invoice_number_example' # str | The Ingram Micro invoice number. (optional)
    invoice_status = 'invoice_status_example' # str | Ingram Micro invoice status. (optional)
    invoice_type = 'invoice_type_example' # str | Ingram Micro InvoiceType. (optional)
    customer_order_number = 'customer_order_number_example' # str | Ingram Micro CustomerOrderNumber. (optional)
    end_customer_order_number = 'end_customer_order_number_example' # str | Ingram Micro EndCustomerOrderNumber. (optional)
    special_bid_number = 'special_bid_number_example' # str | Ingram Micro SpecialBidNumber. (optional)
    invoice_from_due_date = '2021-04-23' # str | Search by invoice due date from(yyyy-MM-dd). (optional)
    invoice_to_due_date = '2021-04-23' # str | Search by invoice due date to(yyyy-MM-dd). (optional)
    invoice_from_date = ['invoice_from_date_example'] # List[str] | Search by invoice date from(yyyy-MM-dd). (optional)
    invoice_to_date = ['invoice_to_date_example'] # List[str] | Search by invoice date To(yyyy-MM-dd). (optional)
    page_size = 56 # int | Number of records required in the call - max records 100 per page. (optional)
    page_number = 56 # int | The page number reference. (optional)
    orderby = 'InvoiceDate' # str | Column name with which we want to sort. (optional)
    direction = 'desc' # str | asc or desc , along with orderby column result set will be sorted. (optional)
    serial_number = 'serial_number_example' # str | Serial number of the product. (optional)

    try:
        # Search your invoice
        api_response = api_instance.get_resellers_v6_invoicesearch(im_application_id, im_customer_number, im_country_code, im_correlation_id, payment_terms_net_date=payment_terms_net_date, invoice_date=invoice_date, invoice_due_date=invoice_due_date, order_date=order_date, order_from_date=order_from_date, order_to_date=order_to_date, order_number=order_number, delivery_number=delivery_number, invoice_number=invoice_number, invoice_status=invoice_status, invoice_type=invoice_type, customer_order_number=customer_order_number, end_customer_order_number=end_customer_order_number, special_bid_number=special_bid_number, invoice_from_due_date=invoice_from_due_date, invoice_to_due_date=invoice_to_due_date, invoice_from_date=invoice_from_date, invoice_to_date=invoice_to_date, page_size=page_size, page_number=page_number, orderby=orderby, direction=direction, serial_number=serial_number)
        print("The response of InvoicesApi->get_resellers_v6_invoicesearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_resellers_v6_invoicesearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_application_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **payment_terms_net_date** | **str**| Search by payment terms net date(yyyy-MM-dd). | [optional] 
 **invoice_date** | **str**| Search by invoice date(yyyy-MM-dd). | [optional] 
 **invoice_due_date** | **str**| Search by invoice date from(yyyy-MM-dd). | [optional] 
 **order_date** | **str**| Search by OrderDate date(yyyy-MM-dd). | [optional] 
 **order_from_date** | **str**| Search by OrderFromDate date(yyyy-MM-dd). | [optional] 
 **order_to_date** | **str**| Search by OrderToDate date(yyyy-MM-dd). | [optional] 
 **order_number** | **str**| Search by order number | [optional] 
 **delivery_number** | **str**| Search by delivery number. | [optional] 
 **invoice_number** | **str**| The Ingram Micro invoice number. | [optional] 
 **invoice_status** | **str**| Ingram Micro invoice status. | [optional] 
 **invoice_type** | **str**| Ingram Micro InvoiceType. | [optional] 
 **customer_order_number** | **str**| Ingram Micro CustomerOrderNumber. | [optional] 
 **end_customer_order_number** | **str**| Ingram Micro EndCustomerOrderNumber. | [optional] 
 **special_bid_number** | **str**| Ingram Micro SpecialBidNumber. | [optional] 
 **invoice_from_due_date** | **str**| Search by invoice due date from(yyyy-MM-dd). | [optional] 
 **invoice_to_due_date** | **str**| Search by invoice due date to(yyyy-MM-dd). | [optional] 
 **invoice_from_date** | [**List[str]**](str.md)| Search by invoice date from(yyyy-MM-dd). | [optional] 
 **invoice_to_date** | [**List[str]**](str.md)| Search by invoice date To(yyyy-MM-dd). | [optional] 
 **page_size** | **int**| Number of records required in the call - max records 100 per page. | [optional] 
 **page_number** | **int**| The page number reference. | [optional] 
 **orderby** | **str**| Column name with which we want to sort. | [optional] 
 **direction** | **str**| asc or desc , along with orderby column result set will be sorted. | [optional] 
 **serial_number** | **str**| Serial number of the product. | [optional] 

### Return type

[**InvoiceSearchResponse**](InvoiceSearchResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InvoiceSearchResponse to be returned |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

