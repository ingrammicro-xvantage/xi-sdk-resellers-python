# xi.sdk.resellers
For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.


## Requirements.

Python 3.7+

## Installation & Usage
### pip install
If you want to install from PyPI:
```sh
pip install xi.sdk.resellers
```

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python.git`)


Then import the package:
```python
import xi.sdk.resellers
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import xi.sdk.resellers
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Quickstart on creating an application can be found [here](getting-started.md)
Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import xi.sdk.resellers
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
    except ApiException as e:
        print("Exception when calling AccesstokenApi->get_accesstoken: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.ingrammicro.com:443*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccesstokenApi* | [**get_accesstoken**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/AccesstokenApi.md#get_accesstoken) | **GET** /oauth/oauth20/token | Accesstoken
*DealsApi* | [**get_resellers_v6_dealsdetails**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/DealsApi.md#get_resellers_v6_dealsdetails) | **GET** /resellers/v6/deals/{dealId} | Deals Details
*DealsApi* | [**get_resellers_v6_dealssearch**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/DealsApi.md#get_resellers_v6_dealssearch) | **GET** /resellers/v6/deals/search | Deals Search
*FreightEstimateApi* | [**post_freightestimate**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightEstimateApi.md#post_freightestimate) | **POST** /resellers/v6/freightestimate | Freight Estimate
*InvoicesApi* | [**get_invoicedetails_v6_1**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoicesApi.md#get_invoicedetails_v6_1) | **GET** /resellers/v6.1/invoices/{invoiceNumber} | Get Invoice Details v6.1
*InvoicesApi* | [**get_resellers_v6_invoicesearch**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoicesApi.md#get_resellers_v6_invoicesearch) | **GET** /resellers/v6/invoices | Search your invoice
*OrderStatusApi* | [**resellers_v1_webhooks_orderstatusevent_post**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderStatusApi.md#resellers_v1_webhooks_orderstatusevent_post) | **POST** /resellers/v1/webhooks/orderstatusevent | Order Status
*OrdersApi* | [**delete_ordercancel**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrdersApi.md#delete_ordercancel) | **DELETE** /resellers/v6/orders/{OrderNumber} | Cancel your Order
*OrdersApi* | [**get_orderdetails_v6_1**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrdersApi.md#get_orderdetails_v6_1) | **GET** /resellers/v6.1/orders/{ordernumber} | Get Order Details v6.1
*OrdersApi* | [**get_resellers_v6_ordersearch**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrdersApi.md#get_resellers_v6_ordersearch) | **GET** /resellers/v6/orders/search | Search your Orders
*OrdersApi* | [**post_createorder_v6**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrdersApi.md#post_createorder_v6) | **POST** /resellers/v6/orders | Create your Order
*OrdersApi* | [**post_createorder_v7**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrdersApi.md#post_createorder_v7) | **POST** /resellers/v7/orders | Create your Order v7
*OrdersApi* | [**put_ordermodify**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrdersApi.md#put_ordermodify) | **PUT** /resellers/v6/orders/{orderNumber} | Modify your Order
*OrdersApi* | [**vendor_required_info**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrdersApi.md#vendor_required_info) | **POST** /resellers/v7/vendorrequiredinfo | Vendor Required Info
*ProductCatalogApi* | [**get_reseller_v6_productdetail**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductCatalogApi.md#get_reseller_v6_productdetail) | **GET** /resellers/v6/catalog/details/{ingramPartNumber} | Product Details
*ProductCatalogApi* | [**get_reseller_v6_productdetailcmp**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductCatalogApi.md#get_reseller_v6_productdetailcmp) | **GET** /resellers/v6/catalog/details | Product Details
*ProductCatalogApi* | [**get_reseller_v6_productsearch**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductCatalogApi.md#get_reseller_v6_productsearch) | **GET** /resellers/v6/catalog | Search Products
*ProductCatalogApi* | [**post_priceandavailability**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductCatalogApi.md#post_priceandavailability) | **POST** /resellers/v6/catalog/priceandavailability | Price and Availability
*QuotesApi* | [**get_quotessearch_v6**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuotesApi.md#get_quotessearch_v6) | **GET** /resellers/v6/quotes/search | Quote Search
*QuotesApi* | [**get_reseller_v6_validate_quote**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuotesApi.md#get_reseller_v6_validate_quote) | **GET** /resellers/v6/q2o/validatequote | Validate Quote
*QuotesApi* | [**get_resellers_v6_quotes**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuotesApi.md#get_resellers_v6_quotes) | **GET** /resellers/v6/quotes/{quoteNumber} | Get Quote Details
*RenewalsApi* | [**get_resellers_v6_renewalsdetails**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsApi.md#get_resellers_v6_renewalsdetails) | **GET** /resellers/v6/renewals/{renewalId} | Renewals Details
*RenewalsApi* | [**post_renewalssearch**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsApi.md#post_renewalssearch) | **POST** /resellers/v6/renewals/search | Renewals Search
*ReturnsApi* | [**get_resellers_v6_returnsdetails**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsApi.md#get_resellers_v6_returnsdetails) | **GET** /resellers/v6/returns/{caseRequestNumber} | Returns Details
*ReturnsApi* | [**get_resellers_v6_returnssearch**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsApi.md#get_resellers_v6_returnssearch) | **GET** /resellers/v6/returns/search | Returns Search
*ReturnsApi* | [**post_returnscreate**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsApi.md#post_returnscreate) | **POST** /resellers/v6/returns/create | Returns Create
*StockUpdateApi* | [**resellers_v1_webhooks_availabilityupdate_post**](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/StockUpdateApi.md#resellers_v1_webhooks_availabilityupdate_post) | **POST** /resellers/v1/webhooks/availabilityupdate | Stock Update


## Documentation For Models

 - [AccesstokenResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/AccesstokenResponse.md)
 - [AvailabilityAsyncNotificationRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/AvailabilityAsyncNotificationRequest.md)
 - [AvailabilityAsyncNotificationRequestResourceInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/AvailabilityAsyncNotificationRequestResourceInner.md)
 - [AvailabilityAsyncNotificationRequestResourceInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/AvailabilityAsyncNotificationRequestResourceInnerLinksInner.md)
 - [DealsDetailsResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/DealsDetailsResponse.md)
 - [DealsDetailsResponseProductsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/DealsDetailsResponseProductsInner.md)
 - [DealsSearchResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/DealsSearchResponse.md)
 - [DealsSearchResponseDealsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/DealsSearchResponseDealsInner.md)
 - [Error](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/Error.md)
 - [ErrorResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ErrorResponse.md)
 - [ErrorResponseDTO](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ErrorResponseDTO.md)
 - [ErrorResponseErrorsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ErrorResponseErrorsInner.md)
 - [ErrorResponseErrorsInnerFieldsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ErrorResponseErrorsInnerFieldsInner.md)
 - [Fields](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/Fields.md)
 - [FreightRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightRequest.md)
 - [FreightRequestLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightRequestLinesInner.md)
 - [FreightRequestShipToAddress](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightRequestShipToAddress.md)
 - [FreightResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightResponse.md)
 - [FreightResponseFreightEstimateResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightResponseFreightEstimateResponse.md)
 - [FreightResponseFreightEstimateResponseDistributionInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightResponseFreightEstimateResponseDistributionInner.md)
 - [FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner.md)
 - [FreightResponseFreightEstimateResponseLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/FreightResponseFreightEstimateResponseLinesInner.md)
 - [GetAccesstoken400Response](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/GetAccesstoken400Response.md)
 - [GetAccesstoken500Response](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/GetAccesstoken500Response.md)
 - [GetAccesstoken500ResponseFault](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/GetAccesstoken500ResponseFault.md)
 - [GetAccesstoken500ResponseFaultDetail](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/GetAccesstoken500ResponseFaultDetail.md)
 - [GetResellerV6ValidateQuote400Response](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/GetResellerV6ValidateQuote400Response.md)
 - [GetResellerV6ValidateQuote400ResponseFieldsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/GetResellerV6ValidateQuote400ResponseFieldsInner.md)
 - [InvoiceDetailsv61Response](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61Response.md)
 - [InvoiceDetailsv61ResponseBillToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseBillToInfo.md)
 - [InvoiceDetailsv61ResponseFxRateInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseFxRateInfo.md)
 - [InvoiceDetailsv61ResponseLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseLinesInner.md)
 - [InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner.md)
 - [InvoiceDetailsv61ResponsePaymentTermsInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponsePaymentTermsInfo.md)
 - [InvoiceDetailsv61ResponseShipToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseShipToInfo.md)
 - [InvoiceDetailsv61ResponseSummary](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseSummary.md)
 - [InvoiceDetailsv61ResponseSummaryForeignFxTotals](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseSummaryForeignFxTotals.md)
 - [InvoiceDetailsv61ResponseSummaryLines](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseSummaryLines.md)
 - [InvoiceDetailsv61ResponseSummaryMiscChargesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseSummaryMiscChargesInner.md)
 - [InvoiceDetailsv61ResponseSummaryTotals](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceDetailsv61ResponseSummaryTotals.md)
 - [InvoiceSearchResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceSearchResponse.md)
 - [InvoiceSearchResponseInvoicesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/InvoiceSearchResponseInvoicesInner.md)
 - [OrderCreateRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequest.md)
 - [OrderCreateRequestAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestAdditionalAttributesInner.md)
 - [OrderCreateRequestEndUserInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestEndUserInfo.md)
 - [OrderCreateRequestLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestLinesInner.md)
 - [OrderCreateRequestLinesInnerAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestLinesInnerAdditionalAttributesInner.md)
 - [OrderCreateRequestLinesInnerEndUserInfoInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestLinesInnerEndUserInfoInner.md)
 - [OrderCreateRequestLinesInnerWarrantyInfoInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestLinesInnerWarrantyInfoInner.md)
 - [OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner.md)
 - [OrderCreateRequestResellerInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestResellerInfo.md)
 - [OrderCreateRequestShipToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestShipToInfo.md)
 - [OrderCreateRequestShipmentDetails](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestShipmentDetails.md)
 - [OrderCreateRequestVmf](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateRequestVmf.md)
 - [OrderCreateResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponse.md)
 - [OrderCreateResponseEndUserInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseEndUserInfo.md)
 - [OrderCreateResponseOrdersInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseOrdersInner.md)
 - [OrderCreateResponseOrdersInnerAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseOrdersInnerAdditionalAttributesInner.md)
 - [OrderCreateResponseOrdersInnerLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseOrdersInnerLinesInner.md)
 - [OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner.md)
 - [OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner.md)
 - [OrderCreateResponseOrdersInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseOrdersInnerLinksInner.md)
 - [OrderCreateResponseOrdersInnerMiscellaneousChargesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseOrdersInnerMiscellaneousChargesInner.md)
 - [OrderCreateResponseOrdersInnerRejectedLineItemsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseOrdersInnerRejectedLineItemsInner.md)
 - [OrderCreateResponseShipToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateResponseShipToInfo.md)
 - [OrderCreateV7Request](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7Request.md)
 - [OrderCreateV7RequestAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestAdditionalAttributesInner.md)
 - [OrderCreateV7RequestEndUserInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestEndUserInfo.md)
 - [OrderCreateV7RequestLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestLinesInner.md)
 - [OrderCreateV7RequestLinesInnerAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestLinesInnerAdditionalAttributesInner.md)
 - [OrderCreateV7RequestLinesInnerEndUserInfoInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestLinesInnerEndUserInfoInner.md)
 - [OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner.md)
 - [OrderCreateV7RequestResellerInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestResellerInfo.md)
 - [OrderCreateV7RequestShipToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestShipToInfo.md)
 - [OrderCreateV7RequestShipmentDetails](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestShipmentDetails.md)
 - [OrderCreateV7RequestVmfAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7RequestVmfAdditionalAttributesInner.md)
 - [OrderCreateV7Response](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7Response.md)
 - [OrderCreateV7Response201](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7Response201.md)
 - [OrderCreateV7ResponseResource](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7ResponseResource.md)
 - [OrderCreateV7ResponseResourceOrdersInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7ResponseResourceOrdersInner.md)
 - [OrderCreateV7ResponseResourceOrdersInnerLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7ResponseResourceOrdersInnerLinesInner.md)
 - [OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner.md)
 - [OrderCreateV7ResponseResourceShipToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderCreateV7ResponseResourceShipToInfo.md)
 - [OrderDetailB2B](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2B.md)
 - [OrderDetailB2BAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BAdditionalAttributesInner.md)
 - [OrderDetailB2BBillToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BBillToInfo.md)
 - [OrderDetailB2BEndUserInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BEndUserInfo.md)
 - [OrderDetailB2BLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInner.md)
 - [OrderDetailB2BLinesInnerAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerAdditionalAttributesInner.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerEstimatedDatesInner.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInnerShip](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerEstimatedDatesInnerShip.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange.md)
 - [OrderDetailB2BLinesInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerLinksInner.md)
 - [OrderDetailB2BLinesInnerMultipleShipmentsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerMultipleShipmentsInner.md)
 - [OrderDetailB2BLinesInnerScheduleLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerScheduleLinesInner.md)
 - [OrderDetailB2BLinesInnerServiceContractInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerServiceContractInfo.md)
 - [OrderDetailB2BLinesInnerServiceContractInfoContractInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerServiceContractInfoContractInfo.md)
 - [OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo.md)
 - [OrderDetailB2BLinesInnerServiceContractInfoSubscriptions](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerServiceContractInfoSubscriptions.md)
 - [OrderDetailB2BLinesInnerShipmentDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerShipmentDetailsInner.md)
 - [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner.md)
 - [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner.md)
 - [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner.md)
 - [OrderDetailB2BMiscellaneousChargesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BMiscellaneousChargesInner.md)
 - [OrderDetailB2BShipToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderDetailB2BShipToInfo.md)
 - [OrderModifyRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyRequest.md)
 - [OrderModifyRequestAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyRequestAdditionalAttributesInner.md)
 - [OrderModifyRequestLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyRequestLinesInner.md)
 - [OrderModifyRequestShipToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyRequestShipToInfo.md)
 - [OrderModifyResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyResponse.md)
 - [OrderModifyResponseLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyResponseLinesInner.md)
 - [OrderModifyResponseLinesInnerAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyResponseLinesInnerAdditionalAttributesInner.md)
 - [OrderModifyResponseLinesInnerShipmentDetails](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyResponseLinesInnerShipmentDetails.md)
 - [OrderModifyResponseRejectedLineItemsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyResponseRejectedLineItemsInner.md)
 - [OrderModifyResponseShipToInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderModifyResponseShipToInfo.md)
 - [OrderSearchResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderSearchResponse.md)
 - [OrderSearchResponseOrdersInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderSearchResponseOrdersInner.md)
 - [OrderSearchResponseOrdersInnerLinks](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderSearchResponseOrdersInnerLinks.md)
 - [OrderSearchResponseOrdersInnerSubOrdersInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderSearchResponseOrdersInnerSubOrdersInner.md)
 - [OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner.md)
 - [OrderStatusAsyncNotificationRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderStatusAsyncNotificationRequest.md)
 - [OrderStatusAsyncNotificationRequestResourceInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderStatusAsyncNotificationRequestResourceInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderStatusAsyncNotificationRequestResourceInnerLinesInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/OrderStatusAsyncNotificationRequestResourceInnerLinksInner.md)
 - [PostCreateorderV7400Response](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PostCreateorderV7400Response.md)
 - [PostCreateorderV7400ResponseFieldsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PostCreateorderV7400ResponseFieldsInner.md)
 - [PostCreateorderV7500Response](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PostCreateorderV7500Response.md)
 - [PostRenewalssearch400Response](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PostRenewalssearch400Response.md)
 - [PriceAndAvailabilityRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityRequest.md)
 - [PriceAndAvailabilityRequestAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityRequestAdditionalAttributesInner.md)
 - [PriceAndAvailabilityRequestAvailabilityByWarehouseInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityRequestAvailabilityByWarehouseInner.md)
 - [PriceAndAvailabilityRequestProductsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityRequestProductsInner.md)
 - [PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner.md)
 - [PriceAndAvailabilityResponseInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInner.md)
 - [PriceAndAvailabilityResponseInnerAvailability](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerAvailability.md)
 - [PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner.md)
 - [PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner.md)
 - [PriceAndAvailabilityResponseInnerDiscountsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerDiscountsInner.md)
 - [PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner.md)
 - [PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner.md)
 - [PriceAndAvailabilityResponseInnerPricing](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerPricing.md)
 - [PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner.md)
 - [PriceAndAvailabilityResponseInnerServiceFeesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerServiceFeesInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerBillingPeriod](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerBillingPeriod.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerGroupsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerGroupsInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerFeesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerFeesInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner.md)
 - [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerSubscriptionPeriodInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/PriceAndAvailabilityResponseInnerSubscriptionPriceInnerSubscriptionPeriodInner.md)
 - [ProductDetailResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponse.md)
 - [ProductDetailResponseAdditionalInformation](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseAdditionalInformation.md)
 - [ProductDetailResponseAdditionalInformationProductWeightInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseAdditionalInformationProductWeightInner.md)
 - [ProductDetailResponseCiscoFields](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseCiscoFields.md)
 - [ProductDetailResponseIndicators](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseIndicators.md)
 - [ProductDetailResponseSubscriptionDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseSubscriptionDetailsInner.md)
 - [ProductDetailResponseSubscriptionDetailsInnerBillingPeriod](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseSubscriptionDetailsInnerBillingPeriod.md)
 - [ProductDetailResponseSubscriptionDetailsInnerGroupsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseSubscriptionDetailsInnerGroupsInner.md)
 - [ProductDetailResponseSubscriptionDetailsInnerOptionsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseSubscriptionDetailsInnerOptionsInner.md)
 - [ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductDetailResponseSubscriptionDetailsInnerSubscriptionPeriodInner.md)
 - [ProductSearchResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductSearchResponse.md)
 - [ProductSearchResponseCatalogInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductSearchResponseCatalogInner.md)
 - [ProductSearchResponseCatalogInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductSearchResponseCatalogInnerLinksInner.md)
 - [ProductSearchResponseSubscriptionCatalogInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductSearchResponseSubscriptionCatalogInner.md)
 - [ProductSearchResponseSubscriptionCatalogInnerPlansInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductSearchResponseSubscriptionCatalogInnerPlansInner.md)
 - [ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductSearchResponseSubscriptionCatalogInnerPlansInnerLinksInner.md)
 - [ProductSearchResponseSubscriptionCatalogInnerPlansInnerSubscriptionPeriodSummaryInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ProductSearchResponseSubscriptionCatalogInnerPlansInnerSubscriptionPeriodSummaryInner.md)
 - [QuoteDetailsResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponse.md)
 - [QuoteDetailsResponseAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseAdditionalAttributesInner.md)
 - [QuoteDetailsResponseEndUserInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseEndUserInfo.md)
 - [QuoteDetailsResponseProductsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseProductsInner.md)
 - [QuoteDetailsResponseProductsInnerBillDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseProductsInnerBillDetailsInner.md)
 - [QuoteDetailsResponseProductsInnerPrice](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseProductsInnerPrice.md)
 - [QuoteDetailsResponseProductsInnerPriceDiscountsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseProductsInnerPriceDiscountsInner.md)
 - [QuoteDetailsResponseProductsInnerPriceExtraFeesDetailsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseProductsInnerPriceExtraFeesDetailsInner.md)
 - [QuoteDetailsResponseResellerInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseResellerInfo.md)
 - [QuoteDetailsResponseShippingInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteDetailsResponseShippingInfo.md)
 - [QuoteSearchResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteSearchResponse.md)
 - [QuoteSearchResponseQuotesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteSearchResponseQuotesInner.md)
 - [QuoteSearchResponseQuotesInnerLinks](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/QuoteSearchResponseQuotesInnerLinks.md)
 - [RenewalsDetailsResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsDetailsResponse.md)
 - [RenewalsDetailsResponseAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsDetailsResponseAdditionalAttributesInner.md)
 - [RenewalsDetailsResponseEndUserInfo](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsDetailsResponseEndUserInfo.md)
 - [RenewalsDetailsResponseProductsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsDetailsResponseProductsInner.md)
 - [RenewalsDetailsResponseReferenceNumber](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsDetailsResponseReferenceNumber.md)
 - [RenewalsSearchRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchRequest.md)
 - [RenewalsSearchRequestDateType](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchRequestDateType.md)
 - [RenewalsSearchRequestDateTypeEndDate](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchRequestDateTypeEndDate.md)
 - [RenewalsSearchRequestDateTypeExpirationDate](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchRequestDateTypeExpirationDate.md)
 - [RenewalsSearchRequestDateTypeInvoiceDate](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchRequestDateTypeInvoiceDate.md)
 - [RenewalsSearchRequestDateTypeStartDate](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchRequestDateTypeStartDate.md)
 - [RenewalsSearchRequestStatus](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchRequestStatus.md)
 - [RenewalsSearchRequestStatusOpporutinyStatus](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchRequestStatusOpporutinyStatus.md)
 - [RenewalsSearchResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchResponse.md)
 - [RenewalsSearchResponseRenewalsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchResponseRenewalsInner.md)
 - [RenewalsSearchResponseRenewalsInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/RenewalsSearchResponseRenewalsInnerLinksInner.md)
 - [ReturnsCreateRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsCreateRequest.md)
 - [ReturnsCreateRequestListInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsCreateRequestListInner.md)
 - [ReturnsCreateRequestListInnerShipFromInfoInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsCreateRequestListInnerShipFromInfoInner.md)
 - [ReturnsCreateResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsCreateResponse.md)
 - [ReturnsCreateResponseReturnsClaimsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsCreateResponseReturnsClaimsInner.md)
 - [ReturnsDetailsResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsDetailsResponse.md)
 - [ReturnsDetailsResponseProductsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsDetailsResponseProductsInner.md)
 - [ReturnsSearchResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsSearchResponse.md)
 - [ReturnsSearchResponseReturnsClaimsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsSearchResponseReturnsClaimsInner.md)
 - [ReturnsSearchResponseReturnsClaimsInnerLinksInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ReturnsSearchResponseReturnsClaimsInnerLinksInner.md)
 - [ValidateQuoteResponse](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ValidateQuoteResponse.md)
 - [ValidateQuoteResponseLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ValidateQuoteResponseLinesInner.md)
 - [ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner.md)
 - [ValidateQuoteResponseVmfAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/ValidateQuoteResponseVmfAdditionalAttributesInner.md)
 - [VendorRequiredInfoRequest](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/VendorRequiredInfoRequest.md)
 - [VendorRequiredInfoRequestProductsInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/VendorRequiredInfoRequestProductsInner.md)
 - [VendorRequiredInforesponseInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/VendorRequiredInforesponseInner.md)
 - [VendorRequiredInforesponseInnerResponseMessagesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/VendorRequiredInforesponseInnerResponseMessagesInner.md)
 - [VendorRequiredInforesponseInnerVmfAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/VendorRequiredInforesponseInnerVmfAdditionalAttributesInner.md)
 - [VendorRequiredInforesponseInnerVmfAdditionalAttributesInnerAdditionalAttributesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/VendorRequiredInforesponseInnerVmfAdditionalAttributesInnerAdditionalAttributesInner.md)
 - [VendorRequiredInforesponseInnerVmfAdditionalAttributesInnerAdditionalAttributesInnerChoicesInner](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/tree/main/docs/VendorRequiredInforesponseInnerVmfAdditionalAttributesInnerAdditionalAttributesInnerChoicesInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="application"></a>
### application

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **write**: allows modifying resources
 - **read**: allows reading resources
 - **description**: 


## Documentation For Authorization


Authentication schemes defined for the API:
### application

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: https://api.ingrammicro.com:443/oauth/oauth20/token?grant_type=client_credentials&client_id={ClientId}&client_secret={clientSecret}
- **Method**: Get
- **Scopes**: 
  - write: allows modifying resources
  - read: allows reading resources
 

## Author
-[Ingram Micro Xvantage](https://github.com/ingrammicro-xvantage)

## Contact

For any inquiries or support, please feel free to contact us at:

- Email: xi_support@ingrammicro.com

- If you encounter any issues, such as bugs or feature requests, we encourage you to [create a GitHub issue](https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/issues/new) in our repository.