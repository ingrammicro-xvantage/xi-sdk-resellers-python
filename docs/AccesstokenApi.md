# xi.sdk.resellers.AccesstokenApi

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accesstoken**](AccesstokenApi.md#get_accesstoken) | **GET** /oauth/oauth20/token | Accesstoken


# **get_accesstoken**
> AccesstokenResponse get_accesstoken(grant_type, client_id, client_secret)

Accesstoken

The Authentication endpoint will provide an access token to access the API.

### Example


```python
import xi.sdk.resellers
from xi.sdk.resellers.models.accesstoken_response import AccesstokenResponse
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443"
)


# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.AccesstokenApi(api_client)
    grant_type = 'client_credentials' # str | Keep grant_type as client_credentials only.
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 

    try:
        # Accesstoken
        api_response = api_instance.get_accesstoken(grant_type, client_id, client_secret)
        print("The response of AccesstokenApi->get_accesstoken:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccesstokenApi->get_accesstoken: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Keep grant_type as client_credentials only. | 
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 

### Return type

[**AccesstokenResponse**](AccesstokenResponse.md)

### Authorization

No authorization required

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

