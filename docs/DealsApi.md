# xi.sdk.resellers.python.DealsApi

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resellers_v6_dealsdetails**](DealsApi.md#get_resellers_v6_dealsdetails) | **GET** /resellers/v6/deals/{dealId} | Deals Details
[**get_resellers_v6_dealssearch**](DealsApi.md#get_resellers_v6_dealssearch) | **GET** /resellers/v6/deals/search | Deals Search


# **get_resellers_v6_dealsdetails**
> DealsDetailsResponse get_resellers_v6_dealsdetails(im_customer_number, im_country_code, im_correlation_id, deal_id, im_sender_id=im_sender_id)

Deals Details

The Deals Details API will retrieve all the details related to the specific deal id.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.deals_details_response import DealsDetailsResponse
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
    api_instance = xi.sdk.resellers.python.DealsApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    deal_id = '12345678' # str | Unique deal ID.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)

    try:
        # Deals Details
        api_response = api_instance.get_resellers_v6_dealsdetails(im_customer_number, im_country_code, im_correlation_id, deal_id, im_sender_id=im_sender_id)
        print("The response of DealsApi->get_resellers_v6_dealsdetails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealsApi->get_resellers_v6_dealsdetails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **deal_id** | **str**| Unique deal ID. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 

### Return type

[**DealsDetailsResponse**](DealsDetailsResponse.md)

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

# **get_resellers_v6_dealssearch**
> DealsSearchResponse get_resellers_v6_dealssearch(im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, end_user=end_user, vendor=vendor, deal_id=deal_id)

Deals Search

The Deals Search API, by default, will retrieve all the deals that are associated with the customer’s account. The customer will be able to search deals using the End-user name, Vendor name, or DealID. 

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.deals_search_response import DealsSearchResponse
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
    api_instance = xi.sdk.resellers.python.DealsApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)
    end_user = 'EnduserCompany' # str | The end user/customer's name. (optional)
    vendor = 'Cisco' # str | The vendor's name. (optional)
    deal_id = '12345678' # str | Deal/Special bid number. (optional)

    try:
        # Deals Search
        api_response = api_instance.get_resellers_v6_dealssearch(im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, end_user=end_user, vendor=vendor, deal_id=deal_id)
        print("The response of DealsApi->get_resellers_v6_dealssearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealsApi->get_resellers_v6_dealssearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 
 **end_user** | **str**| The end user/customer&#39;s name. | [optional] 
 **vendor** | **str**| The vendor&#39;s name. | [optional] 
 **deal_id** | **str**| Deal/Special bid number. | [optional] 

### Return type

[**DealsSearchResponse**](DealsSearchResponse.md)

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

