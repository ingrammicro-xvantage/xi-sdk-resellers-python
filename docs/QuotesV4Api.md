# xi.sdk.resellers.python.QuotesV4Api

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v4_quotedetails**](QuotesV4Api.md#post_v4_quotedetails) | **POST** /quotes/v1/quotedetails | Get Quote Details
[**post_v4_quotesearch**](QuotesV4Api.md#post_v4_quotesearch) | **POST** /quotes/v1/quotes | Get Quote List


# **post_v4_quotedetails**
> QuoteDetailsResponse post_v4_quotedetails(quote_details_request=quote_details_request)

Get Quote Details

A real-time request to delete a previously accepted order must be submitted before the order is released to Ingram Micro’s warehouse. After release the order is no longer eligible for deletion. Order delete transaction submitted after the order is released will be rejected and will not be applied. *Direct ship orders cannot be deleted. Contact your sales rep for assistance.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.quote_details_request import QuoteDetailsRequest
from xi.sdk.resellers.python.models.quote_details_response import QuoteDetailsResponse
from xi.sdk.resellers.python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.python.Configuration(
    host = "https://api.ingrammicro.com:443/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.python.QuotesV4Api(api_client)
    quote_details_request = {"servicerequest":{"requestpreamble":{"isocountrycode":"US","customerumber":"20-222222"},"OrderDeleteRequestDetails":{"entryDate":"2019-01-22","orderBranch":"20","orderNumber":"RC62Z"}}} # QuoteDetailsRequest |  (optional)

    try:
        # Get Quote Details
        api_response = api_instance.post_v4_quotedetails(quote_details_request=quote_details_request)
        print("The response of QuotesV4Api->post_v4_quotedetails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesV4Api->post_v4_quotedetails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_details_request** | [**QuoteDetailsRequest**](QuoteDetailsRequest.md)|  | [optional] 

### Return type

[**QuoteDetailsResponse**](QuoteDetailsResponse.md)

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

# **post_v4_quotesearch**
> QuoteListResponse post_v4_quotesearch(quote_list_request=quote_list_request)

Get Quote List

A real-time request that allows the customer to query Ingram Micro for detailed information for a specific open or shipped order. Orders are searched using Ingram Micro Sales Order Number.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.quote_list_request import QuoteListRequest
from xi.sdk.resellers.python.models.quote_list_response import QuoteListResponse
from xi.sdk.resellers.python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.python.Configuration(
    host = "https://api.ingrammicro.com:443/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.python.QuotesV4Api(api_client)
    quote_list_request = {"servicerequest":{"requestpreamble":{"isocountrycode":"US","customernumber":"20-222222"},"orderdetailrequest":{"ordernumber":"20-B2V9H"}}} # QuoteListRequest |  (optional)

    try:
        # Get Quote List
        api_response = api_instance.post_v4_quotesearch(quote_list_request=quote_list_request)
        print("The response of QuotesV4Api->post_v4_quotesearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesV4Api->post_v4_quotesearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_list_request** | [**QuoteListRequest**](QuoteListRequest.md)|  | [optional] 

### Return type

[**QuoteListResponse**](QuoteListResponse.md)

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

