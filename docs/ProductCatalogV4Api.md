# xi.sdk.resellers.ProductCatalogV4Api

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v4_multiskupriceandstock**](ProductCatalogV4Api.md#post_v4_multiskupriceandstock) | **POST** /products/v4/multiskupriceandstock | Product availability for upto 50 SKUs
[**post_v4_productsearch**](ProductCatalogV4Api.md#post_v4_productsearch) | **POST** /products/v4/productsearch | Real-time Product Search


# **post_v4_multiskupriceandstock**
> MultiSKUPriceAndStockResponse post_v4_multiskupriceandstock(multi_sku_price_and_stock_request=multi_sku_price_and_stock_request)

Product availability for upto 50 SKUs

Find price and availability of up to 50 SKUs in a single request. As you increase the number of items in the request response time will be extended. This transaction must not be used as a continuous cyclical call to populate availability and pricing for your full catalog. Customers that perform this activity will lose access to price and availability.  Ingram can provide a Price catalog file and an Inventory file in flat file format, which can be obtained through FTP download. Please contact 1800-616-4665 or Electronic.Services@ingrammicro.com for more information on these files.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers
from xi.sdk.resellers.models.multi_sku_price_and_stock_request import MultiSKUPriceAndStockRequest
from xi.sdk.resellers.models.multi_sku_price_and_stock_response import MultiSKUPriceAndStockResponse
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.ProductCatalogV4Api(api_client)
    multi_sku_price_and_stock_request = {  
   "servicerequest":{
        "requestpreamble":{  
         "customernumber":"20-222222",
         "isocountrycode":"US"
      },
      "priceandstockrequest":{  
         "showwarehouseavailability":"True",
         "extravailabilityflag":"Y",
         "item":[  
           {"ingrampartnumber":"TB6489","quantity":1}
         ],
         "includeallsystems":false
      }
   }
} # MultiSKUPriceAndStockRequest |  (optional)

    try:
        # Product availability for upto 50 SKUs
        api_response = api_instance.post_v4_multiskupriceandstock(multi_sku_price_and_stock_request=multi_sku_price_and_stock_request)
        print("The response of ProductCatalogV4Api->post_v4_multiskupriceandstock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogV4Api->post_v4_multiskupriceandstock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_sku_price_and_stock_request** | [**MultiSKUPriceAndStockRequest**](MultiSKUPriceAndStockRequest.md)|  | [optional] 

### Return type

[**MultiSKUPriceAndStockResponse**](MultiSKUPriceAndStockResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v4_productsearch**
> ProductSearchResponse post_v4_productsearch(product_search_request=product_search_request)

Real-time Product Search

A real time search that provides the Ingram Micro part number using the manufacturer part number.  This API is helpful to eliminate any errors when a manufactuer has the same part number and Ingram Micro has had to create multiple sku numbers 

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers
from xi.sdk.resellers.models.product_search_request import ProductSearchRequest
from xi.sdk.resellers.models.product_search_response import ProductSearchResponse
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.ProductCatalogV4Api(api_client)
    product_search_request = {"servicerequest":{"requestpreamble":{"customernumber":"20-222222","isocountrycode":"US"},"productsearchrequest":{"searchcriteria":{"ingrampartnumber":"TSXML3"}}}} # ProductSearchRequest |  (optional)

    try:
        # Real-time Product Search
        api_response = api_instance.post_v4_productsearch(product_search_request=product_search_request)
        print("The response of ProductCatalogV4Api->post_v4_productsearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogV4Api->post_v4_productsearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_search_request** | [**ProductSearchRequest**](ProductSearchRequest.md)|  | [optional] 

### Return type

[**ProductSearchResponse**](ProductSearchResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

