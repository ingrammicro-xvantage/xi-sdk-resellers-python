# xi.sdk.resellers.RenewalsApi

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resellers_v6_renewalsdetails**](RenewalsApi.md#get_resellers_v6_renewalsdetails) | **GET** /resellers/v6/renewals/{renewalId} | Renewals Details
[**post_renewalssearch**](RenewalsApi.md#post_renewalssearch) | **POST** /resellers/v6/renewals/search | Renewals Search


# **get_resellers_v6_renewalsdetails**
> RenewalsDetailsResponse get_resellers_v6_renewalsdetails(im_customer_number, im_country_code, im_correlation_id, renewal_id, im_sender_id=im_sender_id)

Renewals Details

The Renewal Details API endpoint will retrieve all the details related to the renewal. The customer is required to pass renewalId as a path parameter while sending a request.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.renewals_details_response import RenewalsDetailsResponse
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
    api_instance = xi.sdk.resellers.RenewalsApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    renewal_id = '123456' # str | Unique Ingram renewal ID.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)

    try:
        # Renewals Details
        api_response = api_instance.get_resellers_v6_renewalsdetails(im_customer_number, im_country_code, im_correlation_id, renewal_id, im_sender_id=im_sender_id)
        print("The response of RenewalsApi->get_resellers_v6_renewalsdetails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenewalsApi->get_resellers_v6_renewalsdetails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **renewal_id** | **str**| Unique Ingram renewal ID. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 

### Return type

[**RenewalsDetailsResponse**](RenewalsDetailsResponse.md)

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

# **post_renewalssearch**
> RenewalsSearchResponse post_renewalssearch(im_customer_number, im_country_code, im_correlation_id, content_type, im_sender_id=im_sender_id, customer_order_number=customer_order_number, ingram_purchase_order_number=ingram_purchase_order_number, serial_number=serial_number, page=page, size=size, sort=sort, renewals_search_request=renewals_search_request)

Renewals Search

The Renewal Search API, by default, will retrieve all the renewals that are associated with the customer’s account. The customer will be able to search for renewals via basic search or advanced search. Basic search is available thru the query string parameters, whereas the advanced search is available thru the request body schema. 

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.renewals_search_request import RenewalsSearchRequest
from xi.sdk.resellers.models.renewals_search_response import RenewalsSearchResponse
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
    api_instance = xi.sdk.resellers.RenewalsApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    content_type = 'application/json' # str | The media type for JSON Request.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)
    customer_order_number = 'customer_order_number_example' # str | The reseller's unique PO/Order number. (optional)
    ingram_purchase_order_number = 'ingram_purchase_order_number_example' # str | Sales order number. (optional)
    serial_number = 'serial_number_example' # str | A serial number of the product. (optional)
    page = 'page_example' # str | Number of page. (optional)
    size = 'size_example' # str | The submitted pagesize, default is 25. (optional)
    sort = 'sort_example' # str | Refers to the column selected to apply the sorting criteria. (optional)
    renewals_search_request = [{"status":{"OpporutinyStatus":{"value":"Closed","subStatus":"Renewal went direct"}},"dateType":{"startDate":{"customStartDate":"05/27/2023","customEndDate":"06/26/2023"},"endDate":{"customStartDate":"06/26/2023","customEndDate":"07/26/2023"},"invoiceDate":{"customStartDate":"05/27/2023","customEndDate":"06/26/2023"},"expirationDate":{"customStartDate":"06/26/2023","customEndDate":"07/26/2023"}},"vendor":"HP","endUser":"STARK"}] # RenewalsSearchRequest |  (optional)

    try:
        # Renewals Search
        api_response = api_instance.post_renewalssearch(im_customer_number, im_country_code, im_correlation_id, content_type, im_sender_id=im_sender_id, customer_order_number=customer_order_number, ingram_purchase_order_number=ingram_purchase_order_number, serial_number=serial_number, page=page, size=size, sort=sort, renewals_search_request=renewals_search_request)
        print("The response of RenewalsApi->post_renewalssearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenewalsApi->post_renewalssearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **content_type** | **str**| The media type for JSON Request. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 
 **customer_order_number** | **str**| The reseller&#39;s unique PO/Order number. | [optional] 
 **ingram_purchase_order_number** | **str**| Sales order number. | [optional] 
 **serial_number** | **str**| A serial number of the product. | [optional] 
 **page** | **str**| Number of page. | [optional] 
 **size** | **str**| The submitted pagesize, default is 25. | [optional] 
 **sort** | **str**| Refers to the column selected to apply the sorting criteria. | [optional] 
 **renewals_search_request** | [**RenewalsSearchRequest**](RenewalsSearchRequest.md)|  | [optional] 

### Return type

[**RenewalsSearchResponse**](RenewalsSearchResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error: Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

