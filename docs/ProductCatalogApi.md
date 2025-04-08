# xi.sdk.resellers.ProductCatalogApi

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reseller_v6_productdetail**](ProductCatalogApi.md#get_reseller_v6_productdetail) | **GET** /resellers/v6/catalog/details/{ingramPartNumber} | Product Details
[**get_reseller_v6_productdetailcmp**](ProductCatalogApi.md#get_reseller_v6_productdetailcmp) | **GET** /resellers/v6/catalog/details | Product Details
[**get_reseller_v6_productsearch**](ProductCatalogApi.md#get_reseller_v6_productsearch) | **GET** /resellers/v6/catalog | Search Products
[**post_priceandavailability**](ProductCatalogApi.md#post_priceandavailability) | **POST** /resellers/v6/catalog/priceandavailability | Price and Availability


# **get_reseller_v6_productdetail**
> ProductDetailResponse get_reseller_v6_productdetail(ingram_part_number, im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id)

Product Details

Search all the product-related details using a unique Ingram Part Number. Currently, this API is available in the USA, India, and Netherlands.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.product_detail_response import ProductDetailResponse
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
    api_instance = xi.sdk.resellers.ProductCatalogApi(api_client)
    ingram_part_number = '6YE881' # str | Ingram Micro unique part number for the product
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems
    im_sender_id = 'MyCompany' # str | Sender Identification text (optional)

    try:
        # Product Details
        api_response = api_instance.get_reseller_v6_productdetail(ingram_part_number, im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id)
        print("The response of ProductCatalogApi->get_reseller_v6_productdetail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->get_reseller_v6_productdetail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingram_part_number** | **str**| Ingram Micro unique part number for the product | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems | 
 **im_sender_id** | **str**| Sender Identification text | [optional] 

### Return type

[**ProductDetailResponse**](ProductDetailResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reseller_v6_productdetailcmp**
> ProductDetailResponse get_reseller_v6_productdetailcmp(im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, plan_name=plan_name, plan_id=plan_id, vendor_part_number=vendor_part_number)

Product Details

Search all the product-related details.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.product_detail_response import ProductDetailResponse
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
    api_instance = xi.sdk.resellers.ProductCatalogApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems
    im_sender_id = 'MyCompany' # str | Sender Identification text (optional)
    plan_name = 'plan_name_example' # str | Name of the subscription plan (optional)
    plan_id = 'plan_id_example' # str | Id of the subscription plan.   <span style='color:red'>To search for details of subscription products, customer must pass either vendorPartNumber, planName or planId.</span> (optional)
    vendor_part_number = 'vendor_part_number_example' # str | Vendor’s part number for the product. (optional)

    try:
        # Product Details
        api_response = api_instance.get_reseller_v6_productdetailcmp(im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, plan_name=plan_name, plan_id=plan_id, vendor_part_number=vendor_part_number)
        print("The response of ProductCatalogApi->get_reseller_v6_productdetailcmp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->get_reseller_v6_productdetailcmp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems | 
 **im_sender_id** | **str**| Sender Identification text | [optional] 
 **plan_name** | **str**| Name of the subscription plan | [optional] 
 **plan_id** | **str**| Id of the subscription plan.   &lt;span style&#x3D;&#39;color:red&#39;&gt;To search for details of subscription products, customer must pass either vendorPartNumber, planName or planId.&lt;/span&gt; | [optional] 
 **vendor_part_number** | **str**| Vendor’s part number for the product. | [optional] 

### Return type

[**ProductDetailResponse**](ProductDetailResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reseller_v6_productsearch**
> ProductSearchResponse get_reseller_v6_productsearch(im_customer_number, im_correlation_id, im_country_code, page_number=page_number, page_size=page_size, im_sender_id=im_sender_id, type=type, has_discounts=has_discounts, vendor=vendor, vendor_part_number=vendor_part_number, accept_language=accept_language, vendor_number=vendor_number, keyword=keyword, category=category, skip_authorisation=skip_authorisation, group_name=group_name, plan_id=plan_id, show_group_info=show_group_info)

Search Products

Search the Ingram Micro product catalog by providing any of the information in the keyword(Ingram part number / vendor part number/ product description / UPC

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.product_search_response import ProductSearchResponse
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
    api_instance = xi.sdk.resellers.ProductCatalogApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems
    im_country_code = 'US' # str | Two-character ISO country code.
    page_number = 56 # int | Current page number. Default is 1 (optional)
    page_size = 56 # int | Number of records required in the call - max records 100 per page (optional)
    im_sender_id = 'MyCompany' # str | Sender Identification text (optional)
    type = 'type_example' # str | The SKU type of product. One of Physical, Digital, or Any. (optional)
    has_discounts = 'true' # str | Specifies if there are discounts available for the product. (optional)
    vendor = ['vendor_example'] # List[str] | The name of the vendor/manufacturer of the product. (optional)
    vendor_part_number = ['vendor_part_number_example'] # List[str] | The vendors part number for the product. (optional)
    accept_language = 'en' # str | Header to the API calls, the content will help us identify the response language. (optional) (default to 'en')
    vendor_number = 'vendor_number_example' # str | Vendor number of the product (optional)
    keyword = ['keyword_example'] # List[str] | Keyword search,can be ingram part number or vendor part number or product title or vendor nameKeyword search. Can be Ingram Micro part number, vender part number, product title, or vendor name. (optional)
    category = 'Accessories' # str | The category of the product. Example: Displays. (optional)
    skip_authorisation = 'true' # str | This parameter is True when you want Skip the authorization, so template will work like current B2b template. (optional)
    group_name = 'Microsoft Defender for Endpoint P2 (NCE COM MTH)' # str | Name of the Product Group (optional)
    plan_id = '471490' # str | ID of the plan (optional)
    show_group_info = true # bool | In case of value true, below Group related information will displayed without the plan info. Group Name, Group Description, Number of plans, link in the group. A link will be provided if customer want to see all the plans in that group. (optional)

    try:
        # Search Products
        api_response = api_instance.get_reseller_v6_productsearch(im_customer_number, im_correlation_id, im_country_code, page_number=page_number, page_size=page_size, im_sender_id=im_sender_id, type=type, has_discounts=has_discounts, vendor=vendor, vendor_part_number=vendor_part_number, accept_language=accept_language, vendor_number=vendor_number, keyword=keyword, category=category, skip_authorisation=skip_authorisation, group_name=group_name, plan_id=plan_id, show_group_info=show_group_info)
        print("The response of ProductCatalogApi->get_reseller_v6_productsearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->get_reseller_v6_productsearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **page_number** | **int**| Current page number. Default is 1 | [optional] 
 **page_size** | **int**| Number of records required in the call - max records 100 per page | [optional] 
 **im_sender_id** | **str**| Sender Identification text | [optional] 
 **type** | **str**| The SKU type of product. One of Physical, Digital, or Any. | [optional] 
 **has_discounts** | **str**| Specifies if there are discounts available for the product. | [optional] 
 **vendor** | [**List[str]**](str.md)| The name of the vendor/manufacturer of the product. | [optional] 
 **vendor_part_number** | [**List[str]**](str.md)| The vendors part number for the product. | [optional] 
 **accept_language** | **str**| Header to the API calls, the content will help us identify the response language. | [optional] [default to &#39;en&#39;]
 **vendor_number** | **str**| Vendor number of the product | [optional] 
 **keyword** | [**List[str]**](str.md)| Keyword search,can be ingram part number or vendor part number or product title or vendor nameKeyword search. Can be Ingram Micro part number, vender part number, product title, or vendor name. | [optional] 
 **category** | **str**| The category of the product. Example: Displays. | [optional] 
 **skip_authorisation** | **str**| This parameter is True when you want Skip the authorization, so template will work like current B2b template. | [optional] 
 **group_name** | **str**| Name of the Product Group | [optional] 
 **plan_id** | **str**| ID of the plan | [optional] 
 **show_group_info** | **bool**| In case of value true, below Group related information will displayed without the plan info. Group Name, Group Description, Number of plans, link in the group. A link will be provided if customer want to see all the plans in that group. | [optional] 

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
**200** | a ProductSearchv6ResponseElement to be returned |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Sender Identification text . <br>  |
**400** | Bad Request |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Sender Identification text . <br>  |
**404** | No Content |  -  |
**500** | Internal Server Error |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Sender Identification text . <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_priceandavailability**
> List[PriceAndAvailabilityResponseInner] post_priceandavailability(include_availability, include_pricing, im_customer_number, im_country_code, im_correlation_id, include_product_attributes=include_product_attributes, im_sender_id=im_sender_id, price_and_availability_request=price_and_availability_request)

Price and Availability

The PriceAndAvailability API, will retrieve Pricing, Availability, discounts, Inventory Location, Reserve Inventory for the products upto 50 products. 

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.price_and_availability_request import PriceAndAvailabilityRequest
from xi.sdk.resellers.models.price_and_availability_response_inner import PriceAndAvailabilityResponseInner
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
    api_instance = xi.sdk.resellers.ProductCatalogApi(api_client)
    include_availability = True # bool | Pass boolean value as input, if true the response will contain warehouse availability details, if false the response will not hold warehouse availability details
    include_pricing = True # bool | Pass boolean value as input, if true the response will contain Pricing details of the Product, if false the response will not hold Pricing details.
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    include_product_attributes = True # bool | Pass boolean value as input, if true the response will contain detailed attributes related to the Product, if false or not sent the response will contain very few Product details. (optional)
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)
    price_and_availability_request = {"products":[{"ingramPartNumber":"123512"}]} # PriceAndAvailabilityRequest |  (optional)

    try:
        # Price and Availability
        api_response = api_instance.post_priceandavailability(include_availability, include_pricing, im_customer_number, im_country_code, im_correlation_id, include_product_attributes=include_product_attributes, im_sender_id=im_sender_id, price_and_availability_request=price_and_availability_request)
        print("The response of ProductCatalogApi->post_priceandavailability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->post_priceandavailability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_availability** | **bool**| Pass boolean value as input, if true the response will contain warehouse availability details, if false the response will not hold warehouse availability details | 
 **include_pricing** | **bool**| Pass boolean value as input, if true the response will contain Pricing details of the Product, if false the response will not hold Pricing details. | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **include_product_attributes** | **bool**| Pass boolean value as input, if true the response will contain detailed attributes related to the Product, if false or not sent the response will contain very few Product details. | [optional] 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 
 **price_and_availability_request** | [**PriceAndAvailabilityRequest**](PriceAndAvailabilityRequest.md)|  | [optional] 

### Return type

[**List[PriceAndAvailabilityResponseInner]**](PriceAndAvailabilityResponseInner.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**207** | Multi Status |  -  |
**400** | Bad Request |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

