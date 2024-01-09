# xi-sdk-python.QuotesV5Api

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v5_quotes_details**](QuotesV5Api.md#get_v5_quotes_details) | **GET** /resellers/v5/quote/{quoteNumber} | Get Quote Details
[**post_v5_quotes_search**](QuotesV5Api.md#post_v5_quotes_search) | **POST** /resellers/v5/quote/search | Search Quotes


# **get_v5_quotes_details**
> QuoteDetails get_v5_quotes_details(quote_number, customer_number, iso_country_code, third_party_source=third_party_source)

Get Quote Details

The quote details API provides all quote details associated with the quote number provided.   The “<strong>quoteNumber</strong>”, “<strong>isoCountryCode</strong>” and “<strong>customerNumber</strong>” parameters are required.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi-sdk-python
from xi-sdk-python.models.quote_details import QuoteDetails
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
    api_instance = xi-sdk-python.QuotesV5Api(api_client)
    quote_number = 'QUO-25576-C8S2W7' # str | Ingram Micro Quote Number (default to 'QUO-25576-C8S2W7')
    customer_number = '20-222222' # str | Your Ingram Micro unique customer number (default to '20-222222')
    iso_country_code = 'US' # str |  (default to 'US')
    third_party_source = 'customer' # str | Unique identifier used to identify the third party source accessing the services (optional) (default to 'customer')

    try:
        # Get Quote Details
        api_response = api_instance.get_v5_quotes_details(quote_number, customer_number, iso_country_code, third_party_source=third_party_source)
        print("The response of QuotesV5Api->get_v5_quotes_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesV5Api->get_v5_quotes_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_number** | **str**| Ingram Micro Quote Number | [default to &#39;QUO-25576-C8S2W7&#39;]
 **customer_number** | **str**| Your Ingram Micro unique customer number | [default to &#39;20-222222&#39;]
 **iso_country_code** | **str**|  | [default to &#39;US&#39;]
 **third_party_source** | **str**| Unique identifier used to identify the third party source accessing the services | [optional] [default to &#39;customer&#39;]

### Return type

[**QuoteDetails**](QuoteDetails.md)

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

# **post_v5_quotes_search**
> QuoteListResponse post_v5_quotes_search(quote_list_request=quote_list_request)

Search Quotes

This endpoint enables the retrieval and filtering of relevant quote list key criteria data, such as quote number, special bid numbers, end user name, status, and date ranges from the Ingram Micro system. By default, the Quotes endpoint retrieves quotes modified or created within the last 30 days.   Observe these additional parameters:<ul><li>Only active quotes are available through this API.</li><li>Quotes older than 365 days are excluded by default.</li><li>You can use date range filters to retrieve quotes older than 30 days and up to 365 days.</li><li>Quotes that are in draft and closed states are excluded, and are not accessible through this API.</li></ul>

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi-sdk-python
from xi-sdk-python.models.quote_list_request import QuoteListRequest
from xi-sdk-python.models.quote_list_response import QuoteListResponse
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
    api_instance = xi-sdk-python.QuotesV5Api(api_client)
    quote_list_request = {"quoteSearchRequest":{"requestPreamble":{"customerNumber":"20-222222","customerContact":"customer@im.com","isoCountryCode":"US"},"retrieveQuoteRequest":{"fromDate":"2019-08-01","toDate":"2019-11-01","pageIndex":1,"recordsPerPage":5,"sorting":"desc","sortingColumnName":"createdon","thirdPartySource":"3RDPIDCONWISE"}}} # QuoteListRequest |  (optional)

    try:
        # Search Quotes
        api_response = api_instance.post_v5_quotes_search(quote_list_request=quote_list_request)
        print("The response of QuotesV5Api->post_v5_quotes_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesV5Api->post_v5_quotes_search: %s\n" % e)
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

