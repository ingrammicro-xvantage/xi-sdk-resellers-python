# xi.sdk.resellers.OrdersV5Api

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_orders_order_number**](OrdersV5Api.md#delete_orders_order_number) | **DELETE** /resellers/v5/Orders/{ordernumber} | Cancel an Existing Order
[**get_orders_search**](OrdersV5Api.md#get_orders_search) | **GET** /resellers/v5/Orders/search | Search your Orders
[**get_v5_orders_details**](OrdersV5Api.md#get_v5_orders_details) | **GET** /resellers/v5/Orders/{ordernumber} | Get Order Details
[**post_v5_orders_create**](OrdersV5Api.md#post_v5_orders_create) | **POST** /resellers/v5/Orders | Create a New Order


# **delete_orders_order_number**
> OrderCancelResponse delete_orders_order_number(ordernumber, customer_number, iso_country_code, entry_date)

Cancel an Existing Order

This endpoint is a request to cancel a previously accepted order. Use your Ingram Micro sales order number to cancel an order.   The <strong>orderNumber, isoCountryCode, customerNumber</strong> and <strong>entryDate</strong> parameters are required.   This call must be submitted <strong>before</strong> the order is released to Ingram Micro’s warehouse. The order cannot be canceled once it is released to the warehouse.   Direct ship orders cannot be canceled. Contact your Ingram Micro sales rep for assistance.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_cancel_response import OrderCancelResponse
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
    api_instance = xi.sdk.resellers.OrdersV5Api(api_client)
    ordernumber = '20-RD128' # str | Ingram Micro sales order number
    customer_number = 'customer_number_example' # str | Your unique Ingram Micro customer number
    iso_country_code = 'iso_country_code_example' # str | 2 chars ISO country code
    entry_date = '2020-04-03' # str | Order entry date (yyyy-mm-dd) (default to '2020-04-03')

    try:
        # Cancel an Existing Order
        api_response = api_instance.delete_orders_order_number(ordernumber, customer_number, iso_country_code, entry_date)
        print("The response of OrdersV5Api->delete_orders_order_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV5Api->delete_orders_order_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordernumber** | **str**| Ingram Micro sales order number | 
 **customer_number** | **str**| Your unique Ingram Micro customer number | 
 **iso_country_code** | **str**| 2 chars ISO country code | 
 **entry_date** | **str**| Order entry date (yyyy-mm-dd) | [default to &#39;2020-04-03&#39;]

### Return type

[**OrderCancelResponse**](OrderCancelResponse.md)

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

# **get_orders_search**
> OrderSearchResponse get_orders_search(customer_number, isocountrycode, ordernumber=ordernumber, customerordernumber=customerordernumber, orderstatus=orderstatus, startcreatetimestamp=startcreatetimestamp, endcreatetimestamp=endcreatetimestamp, pagesize=pagesize, pagenumber=pagenumber)

Search your Orders

Search your Ingram Micro orders. This endpoint searches by multiple order parameters and supports pagination of results. Search using one or more of the parameters below:   <ul><li>ordernumber — Ingram Micro sales order number</li><li>customerordernumber — The PO or order number provided by you when creating an order</li><li>orderstatus — user order status codes for the search, default is set to \"any\"</li><li>startcreatetimestamp and endcreatetimestamp — Order create date range</li></ul>   For pagination, please use these parameters:  <ul><li>pagesize — default 25, max 100</li><li>pagenumber — default 1</li></ul>   Order Status Values:  <ul><li>P – PENDING</li><li>R – RELEASED</li><li>4 – SHIPPED</li><li>I – INVOICED</li><li>V – VOIDED</li></ul>   The search endpoint also returns HATEOAS links for order details and invoice details, if applicable.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_search_response import OrderSearchResponse
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
    api_instance = xi.sdk.resellers.OrdersV5Api(api_client)
    customer_number = '20-222222' # str | Your unique Ingram Micro customer number
    isocountrycode = 'US' # str | 2 char iso country code
    ordernumber = 'ordernumber_example' # str | Ingram sales order number (optional)
    customerordernumber = 'ZENPO1' # str | Search using your PO/Order number (optional)
    orderstatus = 'any' # str | Ingram Micro order status (optional) (default to 'any')
    startcreatetimestamp = '2013-10-20T19:20:30+01:00' # datetime | Search start date/time in UTC format (optional)
    endcreatetimestamp = '2013-10-20T19:20:30+01:00' # datetime | Search end date/time in UTC format (optional)
    pagesize = 56 # int | Number of records required in the call (optional)
    pagenumber = 1 # int | the page number reference (optional) (default to 1)

    try:
        # Search your Orders
        api_response = api_instance.get_orders_search(customer_number, isocountrycode, ordernumber=ordernumber, customerordernumber=customerordernumber, orderstatus=orderstatus, startcreatetimestamp=startcreatetimestamp, endcreatetimestamp=endcreatetimestamp, pagesize=pagesize, pagenumber=pagenumber)
        print("The response of OrdersV5Api->get_orders_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV5Api->get_orders_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_number** | **str**| Your unique Ingram Micro customer number | 
 **isocountrycode** | **str**| 2 char iso country code | 
 **ordernumber** | **str**| Ingram sales order number | [optional] 
 **customerordernumber** | **str**| Search using your PO/Order number | [optional] 
 **orderstatus** | **str**| Ingram Micro order status | [optional] [default to &#39;any&#39;]
 **startcreatetimestamp** | **datetime**| Search start date/time in UTC format | [optional] 
 **endcreatetimestamp** | **datetime**| Search end date/time in UTC format | [optional] 
 **pagesize** | **int**| Number of records required in the call | [optional] 
 **pagenumber** | **int**| the page number reference | [optional] [default to 1]

### Return type

[**OrderSearchResponse**](OrderSearchResponse.md)

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

# **get_v5_orders_details**
> OrderDetailResponse get_v5_orders_details(ordernumber, customernumber, isocountrycode, customerordernumber=customerordernumber, startcreatetimestamp=startcreatetimestamp, endcreatetimestamp=endcreatetimestamp, simulate=simulate)

Get Order Details

Use your Ingram Micro sales order number to search for existing orders or retrieve existing order details.   <b>The sales order number, customer number and isoCountryCode are required parameters.</b>   The sales order number is returned in the Order Create POST response. Ingram Micro recommends that you save this number for future uses.   The IM sales order number can also be retrieved by searching for your existing order using the Order Search GET endpoint. You will need the customer PO number or order number that was provided at the time of order creation.   In a case when the IM sales order number is repeated, you can refine the result by providing customer order number for additional filtering or using the date range to filter orders by creation date.   Use the \"simulate\" query parameter to test the GET order response for various order statuses. This parameter is only available in the sandbox to help with development and testing of the GET order endpoint.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_detail_response import OrderDetailResponse
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
    api_instance = xi.sdk.resellers.OrdersV5Api(api_client)
    ordernumber = '20-RD128' # str | Ingram Micro sales order number
    customernumber = '20-222222' # str | Your unique Ingram Micro customer number (default to '20-222222')
    isocountrycode = 'US' # str | 2 chars ISO country code (default to 'US')
    customerordernumber = 'customerordernumber_example' # str | Your PO/Order Number provide at the time of order creation (optional)
    startcreatetimestamp = 'Sun Mar 15 00:00:00 UTC 2020' # date | Filter start date - format YYYY-MM-DD (optional)
    endcreatetimestamp = '2020-04-20' # str | Filter end date - format YYYY-MM-DD (optional)
    simulate = '' # str | Order response for various order statuses. Not for use in production. (optional)

    try:
        # Get Order Details
        api_response = api_instance.get_v5_orders_details(ordernumber, customernumber, isocountrycode, customerordernumber=customerordernumber, startcreatetimestamp=startcreatetimestamp, endcreatetimestamp=endcreatetimestamp, simulate=simulate)
        print("The response of OrdersV5Api->get_v5_orders_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV5Api->get_v5_orders_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordernumber** | **str**| Ingram Micro sales order number | 
 **customernumber** | **str**| Your unique Ingram Micro customer number | [default to &#39;20-222222&#39;]
 **isocountrycode** | **str**| 2 chars ISO country code | [default to &#39;US&#39;]
 **customerordernumber** | **str**| Your PO/Order Number provide at the time of order creation | [optional] 
 **startcreatetimestamp** | **date**| Filter start date - format YYYY-MM-DD | [optional] 
 **endcreatetimestamp** | **str**| Filter end date - format YYYY-MM-DD | [optional] 
 **simulate** | **str**| Order response for various order statuses. Not for use in production. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_orders_create**
> OrderCreateResponse post_v5_orders_create(order_create_request=order_create_request)

Create a New Order

Instantly create and place orders. The POST API supports stocked SKUs as well as licensing and warranties SKUs.   Every order to be created with this API must complete these validations to be placed and processed:<ul><li>SKU, shipping address, product authorization and stock allocations must clear validation.</li><li>Ingram Micro Sales validates pricing, stock or other processing parameters. Ingram Micro sales may place an order a hold if revision is necessary.</li><li>Credit validation confirms available credit prior to processing an order. If an order does not clear credit validation, the Ingram Micro sales rep or accounts receivable manager will contact you for next steps.</li><li>Warehouse validation selects the location closest to the destination zip code. If the stock is not available in any of the warehouses, Ingram Micro places a backorder in the warehouse closest to the destination zip code.</li></ul>   Ingram Micro recommends that you provide the <strong>ingrampartnumber</strong> for each SKU contained in each order.   When using <strong>vendorpartnumber</strong> to place an order, please use the product search endpoint to find the <strong>ingrampartnumber</strong> for a specific <strong>vendorpartnumber</strong>, and then supply the <strong>ingrampartnumber</strong> to place an order.   <strong>NOTE:</strong> You must have net terms to use the <strong>Ingram Micro Order Create API</strong>. Ingram Micro offers trade credit when using our APIs, and repayment is based on net terms. For example, if your net terms agreement is net-30, you will have 30 days to make a full payment. Ingram Micro does not allow credit card transactions for API ordering.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_create_request import OrderCreateRequest
from xi.sdk.resellers.models.order_create_response import OrderCreateResponse
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
    api_instance = xi.sdk.resellers.OrdersV5Api(api_client)
    order_create_request = {"ordercreaterequest":{"requestpreamble":{"isocountrycode":"US","customernumber":"20-222222"},"ordercreatedetails":{"customerponumber":"CustumerPO-1","shiptoaddress":{"attention":"John Smith","addressline1":"Ingram Micro","addressline2":"3351 Michelson Dr","city":"Long Beach","state":"CA","postalcode":"92612","countrycode":"US"},"carriercode":"OT","lines":[{"linetype":"P","linenumber":"002","quantity":"1","ingrampartnumber":"TSXML3"}],"extendedspecs":[{"attributename":"isdirectshiporder","attributevalue":"false"},{"attributename":"euponumber","attributevalue":"1234"},{"attributename":"commenttext","attributevalue":"Happy Birthday Mom"},{"attributename":"duplicatecustomerordernumbervalidate","attributevalue":"ALLOW"},{"attributename":"commenttext","attributevalue":"///This order must ship on FedEx"},{"attributename":"commenttext","attributevalue":"/// 3rd account# 12345678"}]}}} # OrderCreateRequest |  (optional)

    try:
        # Create a New Order
        api_response = api_instance.post_v5_orders_create(order_create_request=order_create_request)
        print("The response of OrdersV5Api->post_v5_orders_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV5Api->post_v5_orders_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_create_request** | [**OrderCreateRequest**](OrderCreateRequest.md)|  | [optional] 

### Return type

[**OrderCreateResponse**](OrderCreateResponse.md)

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

