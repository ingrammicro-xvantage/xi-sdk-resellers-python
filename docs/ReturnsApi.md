# xi.sdk.resellers.python.ReturnsApi

All URIs are relative to *https://api.ingrammicro.com:443/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resellers_v6_returnsdetails**](ReturnsApi.md#get_resellers_v6_returnsdetails) | **GET** /resellers/v6/returns/{caseRequestNumber} | Returns Details
[**get_resellers_v6_returnssearch**](ReturnsApi.md#get_resellers_v6_returnssearch) | **GET** /resellers/v6/returns/search | Returns Search
[**post_returnscreate**](ReturnsApi.md#post_returnscreate) | **POST** /resellers/v6/returns/create | Returns Create


# **get_resellers_v6_returnsdetails**
> ReturnsDetailsResponse get_resellers_v6_returnsdetails(im_customer_number, im_country_code, im_correlation_id, case_request_number, im_sender_id=im_sender_id)

Returns Details

The Returns Details API will retrieve all the details related to the specific caseRequestNumber.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.returns_details_response import ReturnsDetailsResponse
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
    api_instance = xi.sdk.resellers.python.ReturnsApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    case_request_number = '12345678' # str | A unique return request number.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)

    try:
        # Returns Details
        api_response = api_instance.get_resellers_v6_returnsdetails(im_customer_number, im_country_code, im_correlation_id, case_request_number, im_sender_id=im_sender_id)
        print("The response of ReturnsApi->get_resellers_v6_returnsdetails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsApi->get_resellers_v6_returnsdetails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **case_request_number** | **str**| A unique return request number. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 

### Return type

[**ReturnsDetailsResponse**](ReturnsDetailsResponse.md)

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

# **get_resellers_v6_returnssearch**
> ReturnsSearchResponse get_resellers_v6_returnssearch(im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, case_request_number=case_request_number, invoice_number=invoice_number, return_claim_id=return_claim_id, reference_number=reference_number, ingram_part_number=ingram_part_number, vendor_part_number=vendor_part_number, return_status_in=return_status_in, claim_status_in=claim_status_in, created_on_bt=created_on_bt, modified_on_bt=modified_on_bt, return_reason_in=return_reason_in, page=page, size=size, sort=sort, sorting_column_name=sorting_column_name)

Returns Search

The Returns Search API, by default, will retrieve all the returns that are associated with the customer’s account. The customer will be able to search returns using the query parameters. The Returns Search response will return the following information:  returnClaimId, caseRequestNumber, createdOn, referenceNumber, and returnReason.

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.returns_search_response import ReturnsSearchResponse
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
    api_instance = xi.sdk.resellers.python.ReturnsApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)
    case_request_number = 'case_request_number_example' # str | A unique return request number. (optional)
    invoice_number = 'invoice_number_example' # str | The Invoice number for the order. (optional)
    return_claim_id = 'return_claim_id_example' # str | A unique return claim Id. (optional)
    reference_number = 'reference_number_example' # str | The reference number for the return. (optional)
    ingram_part_number = 'ingram_part_number_example' # str | Unique IngramMicro part number. (optional)
    vendor_part_number = 'vendor_part_number_example' # str | The vendor's part number. (optional)
    return_status_in = 'return_status_in_example' # str | Comma-separated values of pre-defined status. Open, Approved, Partially Approved, Denied, Voided. (optional)
    claim_status_in = 'claim_status_in_example' # str | Comma-separated values of pre-defined status. Open, Approved, Partially Approved, Denied, Voided. (optional)
    created_on_bt = 'created_on_bt_example' # str | The date on which the return request was created.  (optional)
    modified_on_bt = 'modified_on_bt_example' # str | The date on which the return request was last updated. (optional)
    return_reason_in = 'return_reason_in_example' # str | Comma separated Pre-defined value. test, (EW) Express Warehousing, (AR) Account Receivables, (BB) Buy Back, (BE) Stock Balance Exception, (BO) Bill Only, (CE) Credit Dept Use - Credit Exception, (CF) Configuration Fee, (CS ) Customer Service Discretion, (CS1) Customer Service Discretion CS Error, (DE) Defective Exception, (DF) Defective Items, (DI) Direct Credit, (DM) Damaged from Carrier, (DN) Damaged Without Product, (DT) Direct/ Special Order, (DT1) Direct Ship billed, not shipped., (FO) Freight Out, (FX) No-Scan, (IN) Incomplete, (LS) Lost Shipment, (MN) Minimum Order Fee Credit, (OS) Over Shipment, (PR) Pricing Error, (RF) Refusal Credit, (RI) Re-Invoice, (RP) Return For Repair, (RT) Return Not Credited, (RTD) RCN, (SB) Stock Balance, (SD) Sales Discretion, (SH) Incorrect Shipping And Handling, (SS) Short Shipment, (SSK) Short Ship kit, (SW) Sales Writeoff, (TE) Opened Return, (TR) Training Refund, (TX) Tax Credit, (WS) Wrong Sales Sealed, (WW) Wrong Warehouse, (FS) Warehouse Failed Serial# Capture, Latin America Vebdor Credits, Select Source, ITAD - Trade-in Credit, Withholding Tax (optional)
    page = 'page_example' # str | Number of page. (optional)
    size = 'size_example' # str | The submitted pagesize, default is 25 (optional)
    sort = 'sort_example' # str | Refers to the column selected to apply the sorting criteria. (optional)
    sorting_column_name = 'sorting_column_name_example' # str | The column name which will be sorted on. (optional)

    try:
        # Returns Search
        api_response = api_instance.get_resellers_v6_returnssearch(im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, case_request_number=case_request_number, invoice_number=invoice_number, return_claim_id=return_claim_id, reference_number=reference_number, ingram_part_number=ingram_part_number, vendor_part_number=vendor_part_number, return_status_in=return_status_in, claim_status_in=claim_status_in, created_on_bt=created_on_bt, modified_on_bt=modified_on_bt, return_reason_in=return_reason_in, page=page, size=size, sort=sort, sorting_column_name=sorting_column_name)
        print("The response of ReturnsApi->get_resellers_v6_returnssearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsApi->get_resellers_v6_returnssearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 
 **case_request_number** | **str**| A unique return request number. | [optional] 
 **invoice_number** | **str**| The Invoice number for the order. | [optional] 
 **return_claim_id** | **str**| A unique return claim Id. | [optional] 
 **reference_number** | **str**| The reference number for the return. | [optional] 
 **ingram_part_number** | **str**| Unique IngramMicro part number. | [optional] 
 **vendor_part_number** | **str**| The vendor&#39;s part number. | [optional] 
 **return_status_in** | **str**| Comma-separated values of pre-defined status. Open, Approved, Partially Approved, Denied, Voided. | [optional] 
 **claim_status_in** | **str**| Comma-separated values of pre-defined status. Open, Approved, Partially Approved, Denied, Voided. | [optional] 
 **created_on_bt** | **str**| The date on which the return request was created.  | [optional] 
 **modified_on_bt** | **str**| The date on which the return request was last updated. | [optional] 
 **return_reason_in** | **str**| Comma separated Pre-defined value. test, (EW) Express Warehousing, (AR) Account Receivables, (BB) Buy Back, (BE) Stock Balance Exception, (BO) Bill Only, (CE) Credit Dept Use - Credit Exception, (CF) Configuration Fee, (CS ) Customer Service Discretion, (CS1) Customer Service Discretion CS Error, (DE) Defective Exception, (DF) Defective Items, (DI) Direct Credit, (DM) Damaged from Carrier, (DN) Damaged Without Product, (DT) Direct/ Special Order, (DT1) Direct Ship billed, not shipped., (FO) Freight Out, (FX) No-Scan, (IN) Incomplete, (LS) Lost Shipment, (MN) Minimum Order Fee Credit, (OS) Over Shipment, (PR) Pricing Error, (RF) Refusal Credit, (RI) Re-Invoice, (RP) Return For Repair, (RT) Return Not Credited, (RTD) RCN, (SB) Stock Balance, (SD) Sales Discretion, (SH) Incorrect Shipping And Handling, (SS) Short Shipment, (SSK) Short Ship kit, (SW) Sales Writeoff, (TE) Opened Return, (TR) Training Refund, (TX) Tax Credit, (WS) Wrong Sales Sealed, (WW) Wrong Warehouse, (FS) Warehouse Failed Serial# Capture, Latin America Vebdor Credits, Select Source, ITAD - Trade-in Credit, Withholding Tax | [optional] 
 **page** | **str**| Number of page. | [optional] 
 **size** | **str**| The submitted pagesize, default is 25 | [optional] 
 **sort** | **str**| Refers to the column selected to apply the sorting criteria. | [optional] 
 **sorting_column_name** | **str**| The column name which will be sorted on. | [optional] 

### Return type

[**ReturnsSearchResponse**](ReturnsSearchResponse.md)

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

# **post_returnscreate**
> ReturnsCreateResponse post_returnscreate(im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, returns_create_request=returns_create_request)

Returns Create

Return create endpoint will allow customers to create a return request. In order to create a request, the customer must provide either ingramPartNumber or vendorPartNumber along with other required fields listed below. 

### Example

* OAuth Authentication (application):

```python
import time
import os
import xi.sdk.resellers.python
from xi.sdk.resellers.python.models.returns_create_request import ReturnsCreateRequest
from xi.sdk.resellers.python.models.returns_create_response import ReturnsCreateResponse
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
    api_instance = xi.sdk.resellers.python.ReturnsApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)
    returns_create_request = {"list":[{"invoiceNumber":"40-NFERG-11","invoiceDate":"2023-07-18","customerOrderNumber":"","ingramPartNumber":"164B2G","vendorPartNumber":"","serialNumber":"","quantity":"1","primaryReason":"I have not received part or all of my order","secondaryReason":"Received only partial shipment.","notes":"B2BCartCreation20","referenceNumber":"RefNum","billToAddressId":"000","shipFromInfo":{"companyName":"ABC TECH","contact":"STARK","addressLine1":"17501 W 98TH ST SPC 1833","addressLine2":"string","addressLine3":"string","city":"LENEXA","state":"KS","postalCode":"662191736","countryCode":"US","email":"stark@gmail.com","phoneNumber":""},"numberOfBoxes":"1"}]} # ReturnsCreateRequest |  (optional)

    try:
        # Returns Create
        api_response = api_instance.post_returnscreate(im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, returns_create_request=returns_create_request)
        print("The response of ReturnsApi->post_returnscreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsApi->post_returnscreate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 
 **returns_create_request** | [**ReturnsCreateRequest**](ReturnsCreateRequest.md)|  | [optional] 

### Return type

[**ReturnsCreateResponse**](ReturnsCreateResponse.md)

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

