# xi.sdk.resellers.python.ProductCatalogV5Api

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v5_catalog_productsearch**](ProductCatalogV5Api.md#get_v5_catalog_productsearch) | **GET** /resellers/v5/Catalog | Search Product Catalog
[**multi_sku_price_and_stock**](ProductCatalogV5Api.md#multi_sku_price_and_stock) | **POST** /resellers/v5/Catalog/priceandavailability | Find availability of upto 50 SKUs


# **get_v5_catalog_productsearch**
> ProductSearchResponse get_v5_catalog_productsearch(customer_number, iso_country_code, part_number)

Search Product Catalog

Search the Ingram Micro product catalog using customerNumber, isoCountryCode and partNumber.<ul><li>customerNumber and isoCountryCode fields are required.</li><li>The PartNumber field accepts the following:<ul><li>Ingram part number</li><li>Vendor part number</li><li>Customer part number</li><li>UPC (Universal Product Code)</li></ul></li></ul>

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.product_search_response import ProductSearchResponse
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
    api_instance = xi.sdk.resellers.python.ProductCatalogV5Api(api_client)
    customer_number = '20-222222' # str | Your unique Ingram Micro customer number (default to '20-222222')
    iso_country_code = 'US' # str | 2 chars country code (default to 'US')
    part_number = '1AQ821' # str | Part Number can be ingram part number or vendor part number or customer part number or UPC (default to '1AQ821')

    try:
        # Search Product Catalog
        api_response = api_instance.get_v5_catalog_productsearch(customer_number, iso_country_code, part_number)
        print("The response of ProductCatalogV5Api->get_v5_catalog_productsearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogV5Api->get_v5_catalog_productsearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_number** | **str**| Your unique Ingram Micro customer number | [default to &#39;20-222222&#39;]
 **iso_country_code** | **str**| 2 chars country code | [default to &#39;US&#39;]
 **part_number** | **str**| Part Number can be ingram part number or vendor part number or customer part number or UPC | [default to &#39;1AQ821&#39;]

### Return type

[**ProductSearchResponse**](ProductSearchResponse.md)

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

# **multi_sku_price_and_stock**
> PriceAndAvailabilityResponse multi_sku_price_and_stock(price_and_availability_request=price_and_availability_request)

Find availability of upto 50 SKUs

Search the product catalog for the price and availability for up to 50 SKUs at one time. This endpoint helps to confirm the details just prior to placing a real-time call.<ul><li>You may request visibility for reserve stock if you participate in reserved inventory, in addition to the stock that is open to all the partners. Please see the details in the endpoint model below.</li><li>Follow these guidelines when using this endpoint:<ul><li>This endpoint is not for refreshing the full catalog with availability and pricing information. Ingram Micro applies rate limits on this endpoint. Continuous cyclical calls will error out. Customers that perform this activity may lose access to the endpoint.</li><li>For the full catalog refresh, Ingram Micro can provide a Price and Inventory file in flat file format, made available through FTP download. Please contact your Ingram Micro sales rep for details.</li></ul></li></ul>

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.price_and_availability_request import PriceAndAvailabilityRequest
from xi.sdk.resellers.python.models.price_and_availability_response import PriceAndAvailabilityResponse
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
    api_instance = xi.sdk.resellers.python.ProductCatalogV5Api(api_client)
    price_and_availability_request = {"servicerequest":{"requestpreamble":{"customernumber":"20-222223","isocountrycode":"US"},"priceandstockrequest":{"showwarehouseavailability":"True","extravailabilityflag":"Y","item":[{"ingrampartnumber":"TB6489","quantity":1},{"ingrampartnumber":"1AQ821","quantity":1}],"includeallsystems":false}}} # PriceAndAvailabilityRequest |  (optional)

    try:
        # Find availability of upto 50 SKUs
        api_response = api_instance.multi_sku_price_and_stock(price_and_availability_request=price_and_availability_request)
        print("The response of ProductCatalogV5Api->multi_sku_price_and_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogV5Api->multi_sku_price_and_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_and_availability_request** | [**PriceAndAvailabilityRequest**](PriceAndAvailabilityRequest.md)|  | [optional] 

### Return type

[**PriceAndAvailabilityResponse**](PriceAndAvailabilityResponse.md)

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

