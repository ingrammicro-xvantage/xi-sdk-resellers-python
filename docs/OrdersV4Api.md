# xi.sdk.resellers.OrdersV4Api

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v4_ordercreate**](OrdersV4Api.md#post_v4_ordercreate) | **POST** /orders/v4/ordercreate | Create a new Order
[**post_v4_orderdelete**](OrdersV4Api.md#post_v4_orderdelete) | **POST** /orders/v4/orderdelete | Delete an Order
[**post_v4_orderdetails**](OrdersV4Api.md#post_v4_orderdetails) | **POST** /orders/v4/orderdetails | Get Order Details
[**post_v4_ordermodify**](OrdersV4Api.md#post_v4_ordermodify) | **POST** /orders/v4/ordermodify | Modify an Existing Order
[**post_v4_ordersearch**](OrdersV4Api.md#post_v4_ordersearch) | **POST** /orders/v4/orderlookup | Order Search


# **post_v4_ordercreate**
> OrderCreateResponse post_v4_ordercreate(order_create_request=order_create_request)

Create a new Order

The order create transaction is a real-time transaction that allows customers to place standard product and direct ship (licensing and warranties) orders with Ingram Micro using API.

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
    api_instance = xi.sdk.resellers.OrdersV4Api(api_client)
    order_create_request = {"ordercreaterequest":{"requestpreamble":{"isocountrycode":"US","customernumber":"20-222222"},"ordercreatedetails":{"systemid":"","customerponumber":"TESTAPI10156","billtosuffix":"000","shiptoaddress":{"attention":"HARRY WELLS","addressline1":"THE COMPUTER STORE","addressline2":"754 LAS PALMAS DR","city":"IRVINE","state":"CA","postalcode":"926022004","countrycode":"US"},"lines":[{"linetype":"P","linenumber":"001","globalskuid":"","quantity":"1","ingrampartnumber":"NE7872"}],"extendedspecs":[{"attributename":"entrymethod","attributevalue":"WEBS"}]}}} # OrderCreateRequest |  (optional)

    try:
        # Create a new Order
        api_response = api_instance.post_v4_ordercreate(order_create_request=order_create_request)
        print("The response of OrdersV4Api->post_v4_ordercreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV4Api->post_v4_ordercreate: %s\n" % e)
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

# **post_v4_orderdelete**
> OrderDeleteResponse post_v4_orderdelete(order_delete_request=order_delete_request)

Delete an Order

A real-time request to delete a previously accepted order must be submitted before the order is released to Ingram Micro’s warehouse. After release the order is no longer eligible for deletion. Order delete transaction submitted after the order is released will be rejected and will not be applied. *Direct ship orders cannot be deleted. Contact your sales rep for assistance.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_delete_request import OrderDeleteRequest
from xi.sdk.resellers.models.order_delete_response import OrderDeleteResponse
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
    api_instance = xi.sdk.resellers.OrdersV4Api(api_client)
    order_delete_request = {"servicerequest":{"requestpreamble":{"isocountrycode":"US","customerumber":"20-222222"},"OrderDeleteRequestDetails":{"entryDate":"2019-01-22","orderBranch":"20","orderNumber":"RC62Z"}}} # OrderDeleteRequest |  (optional)

    try:
        # Delete an Order
        api_response = api_instance.post_v4_orderdelete(order_delete_request=order_delete_request)
        print("The response of OrdersV4Api->post_v4_orderdelete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV4Api->post_v4_orderdelete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_delete_request** | [**OrderDeleteRequest**](OrderDeleteRequest.md)|  | [optional] 

### Return type

[**OrderDeleteResponse**](OrderDeleteResponse.md)

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

# **post_v4_orderdetails**
> OrderDetailResponse post_v4_orderdetails(order_detail_request=order_detail_request)

Get Order Details

A real-time request that allows the customer to query Ingram Micro for detailed information for a specific open or shipped order. Orders are searched using Ingram Micro Sales Order Number.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_detail_request import OrderDetailRequest
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
    api_instance = xi.sdk.resellers.OrdersV4Api(api_client)
    order_detail_request = {"servicerequest":{"requestpreamble":{"isocountrycode":"US","customernumber":"20-222222"},"orderdetailrequest":{"ordernumber":"20-B2V9H"}}} # OrderDetailRequest |  (optional)

    try:
        # Get Order Details
        api_response = api_instance.post_v4_orderdetails(order_detail_request=order_detail_request)
        print("The response of OrdersV4Api->post_v4_orderdetails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV4Api->post_v4_orderdetails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_detail_request** | [**OrderDetailRequest**](OrderDetailRequest.md)|  | [optional] 

### Return type

[**OrderDetailResponse**](OrderDetailResponse.md)

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

# **post_v4_ordermodify**
> OrderModifyResponse post_v4_ordermodify(order_modify_request=order_modify_request)

Modify an Existing Order

The order modify transaction allows for changes to be made after the order creation process but before the order is released to Ingram Micro’s warehouse system.  Order modify transaction submitted after the order is released will be rejected and will not be applied.  Types of modifications allowable: Order release, add comment, and carrier change. NOTE - Direct Ship orders cannot be modified. 

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_modify_request import OrderModifyRequest
from xi.sdk.resellers.models.order_modify_response import OrderModifyResponse
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
    api_instance = xi.sdk.resellers.OrdersV4Api(api_client)
    order_modify_request = xi.sdk.resellers.OrderModifyRequest() # OrderModifyRequest |  (optional)

    try:
        # Modify an Existing Order
        api_response = api_instance.post_v4_ordermodify(order_modify_request=order_modify_request)
        print("The response of OrdersV4Api->post_v4_ordermodify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV4Api->post_v4_ordermodify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_modify_request** | [**OrderModifyRequest**](OrderModifyRequest.md)|  | [optional] 

### Return type

[**OrderModifyResponse**](OrderModifyResponse.md)

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

# **post_v4_ordersearch**
> OrderSearchResponse post_v4_ordersearch(order_search_request=order_search_request)

Order Search

Search your orders using various search parameters

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_search_request import OrderSearchRequest
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
    api_instance = xi.sdk.resellers.OrdersV4Api(api_client)
    order_search_request = xi.sdk.resellers.OrderSearchRequest() # OrderSearchRequest |  (optional)

    try:
        # Order Search
        api_response = api_instance.post_v4_ordersearch(order_search_request=order_search_request)
        print("The response of OrdersV4Api->post_v4_ordersearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersV4Api->post_v4_ordersearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_search_request** | [**OrderSearchRequest**](OrderSearchRequest.md)|  | [optional] 

### Return type

[**OrderSearchResponse**](OrderSearchResponse.md)

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

