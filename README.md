# xi.sdk.resellers
For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.DealsApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    im_application_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany
    im_environment = 'prodChicago' # str | Environment name.
    deal_id = '12345678' # str | Unique deal ID.

    try:
        # Deals Details
        api_response = api_instance.get_resellers_v6_dealsdetails(im_customer_number, im_country_code, im_correlation_id, im_application_id, im_environment, deal_id)
        print("The response of DealsApi->get_resellers_v6_dealsdetails:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DealsApi->get_resellers_v6_dealsdetails: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.ingrammicro.com:443*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DealsApi* | [**get_resellers_v6_dealsdetails**](docs/DealsApi.md#get_resellers_v6_dealsdetails) | **GET** /resellers/v6/deals/{dealId} | Deals Details
*DealsApi* | [**get_resellers_v6_dealssearch**](docs/DealsApi.md#get_resellers_v6_dealssearch) | **GET** /resellers/v6/deals/search | Deals Search
*FreightEstimateApi* | [**post_freightestimate**](docs/FreightEstimateApi.md#post_freightestimate) | **POST** /resellers/v6/freightestimate | Freight Estimate
*InvoicesApi* | [**get_invoicedetails_v6_1**](docs/InvoicesApi.md#get_invoicedetails_v6_1) | **GET** /resellers/v6.1/invoices/{invoiceNumber} | Get Invoice Details v6.1
*InvoicesApi* | [**get_resellers_v6_invoicesearch**](docs/InvoicesApi.md#get_resellers_v6_invoicesearch) | **GET** /resellers/v6/invoices | Search your invoice
*InvoicesV6Api* | [**get_invoicedetails_v6**](docs/InvoicesV6Api.md#get_invoicedetails_v6) | **GET** /resellers/v6/invoices/{invoicenumber} | Get Invoice Details v6
*OrderStatusApi* | [**resellers_v1_webhooks_orderstatusevent_post**](docs/OrderStatusApi.md#resellers_v1_webhooks_orderstatusevent_post) | **POST** /resellers/v1/webhooks/orderstatusevent | Order Status
*OrdersApi* | [**delete_ordercancel**](docs/OrdersApi.md#delete_ordercancel) | **DELETE** /resellers/v6/orders/{OrderNumber} | Cancel your Order
*OrdersApi* | [**get_orderdetails_v6_1**](docs/OrdersApi.md#get_orderdetails_v6_1) | **GET** /resellers/v6.1/orders/{ordernumber} | Get Order Details v6.1
*OrdersApi* | [**get_resellers_v6_ordersearch**](docs/OrdersApi.md#get_resellers_v6_ordersearch) | **GET** /resellers/v6/orders/search | Search your Orders
*OrdersApi* | [**post_createorder_v6**](docs/OrdersApi.md#post_createorder_v6) | **POST** /resellers/v6/orders | Create your Order
*OrdersApi* | [**put_ordermodify**](docs/OrdersApi.md#put_ordermodify) | **PUT** /resellers/v6/orders/{orderNumber} | Modify your Order
*OrdersV6Api* | [**get_orderdetails_v6**](docs/OrdersV6Api.md#get_orderdetails_v6) | **GET** /resellers/v6/orders/{ordernumber} | Get Order Details v6
*ProductCatalogApi* | [**get_reseller_v6_productdetail**](docs/ProductCatalogApi.md#get_reseller_v6_productdetail) | **GET** /resellers/v6/catalog/details/{ingramPartNumber} | Product Details
*ProductCatalogApi* | [**get_reseller_v6_productsearch**](docs/ProductCatalogApi.md#get_reseller_v6_productsearch) | **GET** /resellers/v6/catalog | Search Products
*ProductCatalogApi* | [**post_priceandavailability**](docs/ProductCatalogApi.md#post_priceandavailability) | **POST** /resellers/v6/catalog/priceandavailability | Price and Availability
*QuoteToOrderApi* | [**post_quote_to_order_v6**](docs/QuoteToOrderApi.md#post_quote_to_order_v6) | **POST** /resellers/v6/q2o/orders | Quote To Order
*QuotesApi* | [**get_quotessearch_v6**](docs/QuotesApi.md#get_quotessearch_v6) | **GET** /resellers/v6/quotes/search | Quote Search
*QuotesApi* | [**get_reseller_v6_validate_quote**](docs/QuotesApi.md#get_reseller_v6_validate_quote) | **GET** /resellers/v6/q2o/validatequote | Validate Quote
*QuotesApi* | [**get_resellers_v6_quotes**](docs/QuotesApi.md#get_resellers_v6_quotes) | **GET** /resellers/v6/quotes/{quoteNumber} | Get Quote Details
*RenewalsApi* | [**get_resellers_v6_renewalsdetails**](docs/RenewalsApi.md#get_resellers_v6_renewalsdetails) | **GET** /resellers/v6/renewals/{renewalId} | Renewals Details
*RenewalsApi* | [**post_renewalssearch**](docs/RenewalsApi.md#post_renewalssearch) | **POST** /resellers/v6/renewals/search | Renewals Search
*ReturnsApi* | [**get_resellers_v6_returnsdetails**](docs/ReturnsApi.md#get_resellers_v6_returnsdetails) | **GET** /resellers/v6/returns/{caseRequestNumber} | Returns Details
*ReturnsApi* | [**get_resellers_v6_returnssearch**](docs/ReturnsApi.md#get_resellers_v6_returnssearch) | **GET** /resellers/v6/returns/search | Returns Search
*ReturnsApi* | [**post_returnscreate**](docs/ReturnsApi.md#post_returnscreate) | **POST** /resellers/v6/returns/create | Returns Create
*StockUpdateApi* | [**resellers_v1_webhooks_availabilityupdate_post**](docs/StockUpdateApi.md#resellers_v1_webhooks_availabilityupdate_post) | **POST** /resellers/v1/webhooks/availabilityupdate | Stock Update


## Documentation For Models

 - [AddressType](docs/AddressType.md)
 - [AvailabilityAsyncNotificationRequest](docs/AvailabilityAsyncNotificationRequest.md)
 - [AvailabilityAsyncNotificationRequestResourceInner](docs/AvailabilityAsyncNotificationRequestResourceInner.md)
 - [AvailabilityAsyncNotificationRequestResourceInnerLinksInner](docs/AvailabilityAsyncNotificationRequestResourceInnerLinksInner.md)
 - [DealsDetailsResponse](docs/DealsDetailsResponse.md)
 - [DealsDetailsResponseProductsInner](docs/DealsDetailsResponseProductsInner.md)
 - [DealsSearchResponse](docs/DealsSearchResponse.md)
 - [DealsSearchResponseDealsInner](docs/DealsSearchResponseDealsInner.md)
 - [Error](docs/Error.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorResponseDTO](docs/ErrorResponseDTO.md)
 - [ErrorResponseErrorsInner](docs/ErrorResponseErrorsInner.md)
 - [ErrorResponseErrorsInnerFieldsInner](docs/ErrorResponseErrorsInnerFieldsInner.md)
 - [Fields](docs/Fields.md)
 - [FreightRequest](docs/FreightRequest.md)
 - [FreightRequestLinesInner](docs/FreightRequestLinesInner.md)
 - [FreightRequestShipToAddressInner](docs/FreightRequestShipToAddressInner.md)
 - [FreightResponse](docs/FreightResponse.md)
 - [FreightResponseFreightEstimateResponse](docs/FreightResponseFreightEstimateResponse.md)
 - [FreightResponseFreightEstimateResponseDistributionInner](docs/FreightResponseFreightEstimateResponseDistributionInner.md)
 - [FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner](docs/FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner.md)
 - [FreightResponseFreightEstimateResponseLinesInner](docs/FreightResponseFreightEstimateResponseLinesInner.md)
 - [GetResellerV6ValidateQuote400Response](docs/GetResellerV6ValidateQuote400Response.md)
 - [GetResellerV6ValidateQuote400ResponseFieldsInner](docs/GetResellerV6ValidateQuote400ResponseFieldsInner.md)
 - [GetResellerV6ValidateQuote500Response](docs/GetResellerV6ValidateQuote500Response.md)
 - [InvoiceDetailRequest](docs/InvoiceDetailRequest.md)
 - [InvoiceDetailRequestServicerequest](docs/InvoiceDetailRequestServicerequest.md)
 - [InvoiceDetailRequestServicerequestInvoicedetailrequest](docs/InvoiceDetailRequestServicerequestInvoicedetailrequest.md)
 - [InvoiceDetailRequestServicerequestRequestpreamble](docs/InvoiceDetailRequestServicerequestRequestpreamble.md)
 - [InvoiceDetailResponse](docs/InvoiceDetailResponse.md)
 - [InvoiceDetailResponseServiceresponse](docs/InvoiceDetailResponseServiceresponse.md)
 - [InvoiceDetailResponseServiceresponseInvoicedetailresponse](docs/InvoiceDetailResponseServiceresponseInvoicedetailresponse.md)
 - [InvoiceDetailResponseServiceresponseInvoicedetailresponseExtendedspecsInner](docs/InvoiceDetailResponseServiceresponseInvoicedetailresponseExtendedspecsInner.md)
 - [InvoiceDetailResponseServiceresponseInvoicedetailresponseMiscfeelineInner](docs/InvoiceDetailResponseServiceresponseInvoicedetailresponseMiscfeelineInner.md)
 - [InvoiceDetailResponseServiceresponseResponsepreamble](docs/InvoiceDetailResponseServiceresponseResponsepreamble.md)
 - [InvoiceDetailsv61Response](docs/InvoiceDetailsv61Response.md)
 - [InvoiceDetailsv61ResponseBillToInfo](docs/InvoiceDetailsv61ResponseBillToInfo.md)
 - [InvoiceDetailsv61ResponseFxRateInfo](docs/InvoiceDetailsv61ResponseFxRateInfo.md)
 - [InvoiceDetailsv61ResponseLinesInner](docs/InvoiceDetailsv61ResponseLinesInner.md)
 - [InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner](docs/InvoiceDetailsv61ResponseLinesInnerSerialNumbersInner.md)
 - [InvoiceDetailsv61ResponsePaymentTermsInfo](docs/InvoiceDetailsv61ResponsePaymentTermsInfo.md)
 - [InvoiceDetailsv61ResponseShipToInfo](docs/InvoiceDetailsv61ResponseShipToInfo.md)
 - [InvoiceDetailsv61ResponseSummary](docs/InvoiceDetailsv61ResponseSummary.md)
 - [InvoiceDetailsv61ResponseSummaryForeignFxTotals](docs/InvoiceDetailsv61ResponseSummaryForeignFxTotals.md)
 - [InvoiceDetailsv61ResponseSummaryLines](docs/InvoiceDetailsv61ResponseSummaryLines.md)
 - [InvoiceDetailsv61ResponseSummaryMiscChargesInner](docs/InvoiceDetailsv61ResponseSummaryMiscChargesInner.md)
 - [InvoiceDetailsv61ResponseSummaryTotals](docs/InvoiceDetailsv61ResponseSummaryTotals.md)
 - [InvoiceSearchResponse](docs/InvoiceSearchResponse.md)
 - [InvoiceSearchResponseInvoicesInner](docs/InvoiceSearchResponseInvoicesInner.md)
 - [MultiSKUPriceAndStockRequest](docs/MultiSKUPriceAndStockRequest.md)
 - [MultiSKUPriceAndStockRequestServicerequest](docs/MultiSKUPriceAndStockRequestServicerequest.md)
 - [MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest](docs/MultiSKUPriceAndStockRequestServicerequestPriceandstockrequest.md)
 - [MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem](docs/MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem.md)
 - [MultiSKUPriceAndStockRequestServicerequestRequestpreamble](docs/MultiSKUPriceAndStockRequestServicerequestRequestpreamble.md)
 - [MultiSKUPriceAndStockResponse](docs/MultiSKUPriceAndStockResponse.md)
 - [MultiSKUPriceAndStockResponseServiceresponse](docs/MultiSKUPriceAndStockResponseServiceresponse.md)
 - [MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse](docs/MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse.md)
 - [MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInner](docs/MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInner.md)
 - [MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner](docs/MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponseDetailsInnerWarehousedetailsInner.md)
 - [MultiSKUPriceAndStockResponseServiceresponseResponsepreamble](docs/MultiSKUPriceAndStockResponseServiceresponseResponsepreamble.md)
 - [OrderCreateRequest](docs/OrderCreateRequest.md)
 - [OrderCreateRequestAdditionalAttributesInner](docs/OrderCreateRequestAdditionalAttributesInner.md)
 - [OrderCreateRequestEndUserInfo](docs/OrderCreateRequestEndUserInfo.md)
 - [OrderCreateRequestLinesInner](docs/OrderCreateRequestLinesInner.md)
 - [OrderCreateRequestLinesInnerAdditionalAttributesInner](docs/OrderCreateRequestLinesInnerAdditionalAttributesInner.md)
 - [OrderCreateRequestLinesInnerEndUserInfoInner](docs/OrderCreateRequestLinesInnerEndUserInfoInner.md)
 - [OrderCreateRequestLinesInnerWarrantyInfoInner](docs/OrderCreateRequestLinesInnerWarrantyInfoInner.md)
 - [OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner](docs/OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner.md)
 - [OrderCreateRequestResellerInfo](docs/OrderCreateRequestResellerInfo.md)
 - [OrderCreateRequestShipToInfo](docs/OrderCreateRequestShipToInfo.md)
 - [OrderCreateRequestShipmentDetails](docs/OrderCreateRequestShipmentDetails.md)
 - [OrderCreateRequestVmf](docs/OrderCreateRequestVmf.md)
 - [OrderCreateResponse](docs/OrderCreateResponse.md)
 - [OrderCreateResponseEndUserInfo](docs/OrderCreateResponseEndUserInfo.md)
 - [OrderCreateResponseOrdersInner](docs/OrderCreateResponseOrdersInner.md)
 - [OrderCreateResponseOrdersInnerAdditionalAttributesInner](docs/OrderCreateResponseOrdersInnerAdditionalAttributesInner.md)
 - [OrderCreateResponseOrdersInnerLinesInner](docs/OrderCreateResponseOrdersInnerLinesInner.md)
 - [OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner](docs/OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner.md)
 - [OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner](docs/OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner.md)
 - [OrderCreateResponseOrdersInnerLinksInner](docs/OrderCreateResponseOrdersInnerLinksInner.md)
 - [OrderCreateResponseOrdersInnerMiscellaneousChargesInner](docs/OrderCreateResponseOrdersInnerMiscellaneousChargesInner.md)
 - [OrderCreateResponseOrdersInnerRejectedLineItemsInner](docs/OrderCreateResponseOrdersInnerRejectedLineItemsInner.md)
 - [OrderCreateResponseShipToInfo](docs/OrderCreateResponseShipToInfo.md)
 - [OrderDeleteRequest](docs/OrderDeleteRequest.md)
 - [OrderDeleteRequestServicerequest](docs/OrderDeleteRequestServicerequest.md)
 - [OrderDeleteRequestServicerequestOrderDeleteRequestDetails](docs/OrderDeleteRequestServicerequestOrderDeleteRequestDetails.md)
 - [OrderDeleteRequestServicerequestRequestpreamble](docs/OrderDeleteRequestServicerequestRequestpreamble.md)
 - [OrderDeleteResponse](docs/OrderDeleteResponse.md)
 - [OrderDeleteResponseServiceresponse](docs/OrderDeleteResponseServiceresponse.md)
 - [OrderDeleteResponseServiceresponseResponsepreamble](docs/OrderDeleteResponseServiceresponseResponsepreamble.md)
 - [OrderDetailB2B](docs/OrderDetailB2B.md)
 - [OrderDetailB2BAdditionalAttributesInner](docs/OrderDetailB2BAdditionalAttributesInner.md)
 - [OrderDetailB2BBillToInfo](docs/OrderDetailB2BBillToInfo.md)
 - [OrderDetailB2BEndUserInfo](docs/OrderDetailB2BEndUserInfo.md)
 - [OrderDetailB2BLinesInner](docs/OrderDetailB2BLinesInner.md)
 - [OrderDetailB2BLinesInnerAdditionalAttributesInner](docs/OrderDetailB2BLinesInnerAdditionalAttributesInner.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInner](docs/OrderDetailB2BLinesInnerEstimatedDatesInner.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery](docs/OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange](docs/OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInnerShip](docs/OrderDetailB2BLinesInnerEstimatedDatesInnerShip.md)
 - [OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange](docs/OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange.md)
 - [OrderDetailB2BLinesInnerLinksInner](docs/OrderDetailB2BLinesInnerLinksInner.md)
 - [OrderDetailB2BLinesInnerMultipleShipmentsInner](docs/OrderDetailB2BLinesInnerMultipleShipmentsInner.md)
 - [OrderDetailB2BLinesInnerScheduleLinesInner](docs/OrderDetailB2BLinesInnerScheduleLinesInner.md)
 - [OrderDetailB2BLinesInnerServiceContractInfo](docs/OrderDetailB2BLinesInnerServiceContractInfo.md)
 - [OrderDetailB2BLinesInnerServiceContractInfoContractInfo](docs/OrderDetailB2BLinesInnerServiceContractInfoContractInfo.md)
 - [OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo](docs/OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo.md)
 - [OrderDetailB2BLinesInnerServiceContractInfoSubscriptions](docs/OrderDetailB2BLinesInnerServiceContractInfoSubscriptions.md)
 - [OrderDetailB2BLinesInnerShipmentDetailsInner](docs/OrderDetailB2BLinesInnerShipmentDetailsInner.md)
 - [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner](docs/OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner.md)
 - [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner](docs/OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner.md)
 - [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner](docs/OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner.md)
 - [OrderDetailB2BMiscellaneousChargesInner](docs/OrderDetailB2BMiscellaneousChargesInner.md)
 - [OrderDetailB2BShipToInfo](docs/OrderDetailB2BShipToInfo.md)
 - [OrderDetailRequest](docs/OrderDetailRequest.md)
 - [OrderDetailRequestServicerequest](docs/OrderDetailRequestServicerequest.md)
 - [OrderDetailRequestServicerequestOrderdetailrequest](docs/OrderDetailRequestServicerequestOrderdetailrequest.md)
 - [OrderDetailResponse](docs/OrderDetailResponse.md)
 - [OrderDetailResponseBillToInfo](docs/OrderDetailResponseBillToInfo.md)
 - [OrderDetailResponseEndUserInfo](docs/OrderDetailResponseEndUserInfo.md)
 - [OrderDetailResponseLinesInner](docs/OrderDetailResponseLinesInner.md)
 - [OrderDetailResponseLinesInnerAdditionalAttributesInner](docs/OrderDetailResponseLinesInnerAdditionalAttributesInner.md)
 - [OrderDetailResponseLinesInnerLinksInner](docs/OrderDetailResponseLinesInnerLinksInner.md)
 - [OrderDetailResponseLinesInnerShipmentDetailsInner](docs/OrderDetailResponseLinesInnerShipmentDetailsInner.md)
 - [OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails](docs/OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails.md)
 - [OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner](docs/OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner.md)
 - [OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInnerSerialNumbersInner](docs/OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInnerSerialNumbersInner.md)
 - [OrderDetailResponseMiscellaneousChargesInner](docs/OrderDetailResponseMiscellaneousChargesInner.md)
 - [OrderDetailResponseShipToInfo](docs/OrderDetailResponseShipToInfo.md)
 - [OrderModifyRequest](docs/OrderModifyRequest.md)
 - [OrderModifyRequestAdditionalAttributesInner](docs/OrderModifyRequestAdditionalAttributesInner.md)
 - [OrderModifyRequestLinesInner](docs/OrderModifyRequestLinesInner.md)
 - [OrderModifyRequestServicerequest](docs/OrderModifyRequestServicerequest.md)
 - [OrderModifyRequestServicerequestOrdermodifyrequest](docs/OrderModifyRequestServicerequestOrdermodifyrequest.md)
 - [OrderModifyRequestServicerequestOrdermodifyrequestHeaderdata](docs/OrderModifyRequestServicerequestOrdermodifyrequestHeaderdata.md)
 - [OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner](docs/OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner.md)
 - [OrderModifyRequestServicerequestOrdermodifyrequestShipto](docs/OrderModifyRequestServicerequestOrdermodifyrequestShipto.md)
 - [OrderModifyRequestServicerequestRequestpreamble](docs/OrderModifyRequestServicerequestRequestpreamble.md)
 - [OrderModifyRequestShipToInfo](docs/OrderModifyRequestShipToInfo.md)
 - [OrderModifyResponse](docs/OrderModifyResponse.md)
 - [OrderModifyResponseLinesInner](docs/OrderModifyResponseLinesInner.md)
 - [OrderModifyResponseLinesInnerAdditionalAttributesInner](docs/OrderModifyResponseLinesInnerAdditionalAttributesInner.md)
 - [OrderModifyResponseLinesInnerShipmentDetails](docs/OrderModifyResponseLinesInnerShipmentDetails.md)
 - [OrderModifyResponseRejectedLineItemsInner](docs/OrderModifyResponseRejectedLineItemsInner.md)
 - [OrderModifyResponseServiceresponse](docs/OrderModifyResponseServiceresponse.md)
 - [OrderModifyResponseServiceresponseOrdermodifyresponse](docs/OrderModifyResponseServiceresponseOrdermodifyresponse.md)
 - [OrderModifyResponseServiceresponseResponsepreamble](docs/OrderModifyResponseServiceresponseResponsepreamble.md)
 - [OrderModifyResponseShipToInfo](docs/OrderModifyResponseShipToInfo.md)
 - [OrderSearchRequest](docs/OrderSearchRequest.md)
 - [OrderSearchRequestServicerequest](docs/OrderSearchRequestServicerequest.md)
 - [OrderSearchRequestServicerequestOrderLookupRequest](docs/OrderSearchRequestServicerequestOrderLookupRequest.md)
 - [OrderSearchRequestServicerequestOrderLookupRequestCustomerOrderNumber](docs/OrderSearchRequestServicerequestOrderLookupRequestCustomerOrderNumber.md)
 - [OrderSearchRequestServicerequestOrderLookupRequestOrderNumber](docs/OrderSearchRequestServicerequestOrderLookupRequestOrderNumber.md)
 - [OrderSearchRequestServicerequestRequestpreamble](docs/OrderSearchRequestServicerequestRequestpreamble.md)
 - [OrderSearchResponse](docs/OrderSearchResponse.md)
 - [OrderSearchResponseOrdersInner](docs/OrderSearchResponseOrdersInner.md)
 - [OrderSearchResponseOrdersInnerLinks](docs/OrderSearchResponseOrdersInnerLinks.md)
 - [OrderSearchResponseOrdersInnerSubOrdersInner](docs/OrderSearchResponseOrdersInnerSubOrdersInner.md)
 - [OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner](docs/OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner.md)
 - [OrderStatusAsyncNotificationRequest](docs/OrderStatusAsyncNotificationRequest.md)
 - [OrderStatusAsyncNotificationRequestResourceInner](docs/OrderStatusAsyncNotificationRequestResourceInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinesInner](docs/OrderStatusAsyncNotificationRequestResourceInnerLinesInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner](docs/OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner](docs/OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner](docs/OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner.md)
 - [OrderStatusAsyncNotificationRequestResourceInnerLinksInner](docs/OrderStatusAsyncNotificationRequestResourceInnerLinksInner.md)
 - [PostQuoteToOrderV6400Response](docs/PostQuoteToOrderV6400Response.md)
 - [PostQuoteToOrderV6400ResponseFieldsInner](docs/PostQuoteToOrderV6400ResponseFieldsInner.md)
 - [PostRenewalssearch400Response](docs/PostRenewalssearch400Response.md)
 - [PriceAndAvailabilityRequest](docs/PriceAndAvailabilityRequest.md)
 - [PriceAndAvailabilityRequestAdditionalAttributesInner](docs/PriceAndAvailabilityRequestAdditionalAttributesInner.md)
 - [PriceAndAvailabilityRequestAvailabilityByWarehouseInner](docs/PriceAndAvailabilityRequestAvailabilityByWarehouseInner.md)
 - [PriceAndAvailabilityRequestProductsInner](docs/PriceAndAvailabilityRequestProductsInner.md)
 - [PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner](docs/PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner.md)
 - [PriceAndAvailabilityResponseInner](docs/PriceAndAvailabilityResponseInner.md)
 - [PriceAndAvailabilityResponseInnerAvailability](docs/PriceAndAvailabilityResponseInnerAvailability.md)
 - [PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner](docs/PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner.md)
 - [PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner](docs/PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner.md)
 - [PriceAndAvailabilityResponseInnerDiscountsInner](docs/PriceAndAvailabilityResponseInnerDiscountsInner.md)
 - [PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner](docs/PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner.md)
 - [PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner](docs/PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner.md)
 - [PriceAndAvailabilityResponseInnerPricing](docs/PriceAndAvailabilityResponseInnerPricing.md)
 - [PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner](docs/PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner.md)
 - [PriceAndAvailabilityResponseInnerServiceFeesInner](docs/PriceAndAvailabilityResponseInnerServiceFeesInner.md)
 - [ProductDetailResponse](docs/ProductDetailResponse.md)
 - [ProductDetailResponseAdditionalInformation](docs/ProductDetailResponseAdditionalInformation.md)
 - [ProductDetailResponseAdditionalInformationProductWeightInner](docs/ProductDetailResponseAdditionalInformationProductWeightInner.md)
 - [ProductDetailResponseCiscoFields](docs/ProductDetailResponseCiscoFields.md)
 - [ProductDetailResponseIndicators](docs/ProductDetailResponseIndicators.md)
 - [ProductDetailResponseTechnicalSpecificationsInner](docs/ProductDetailResponseTechnicalSpecificationsInner.md)
 - [ProductLineType](docs/ProductLineType.md)
 - [ProductLineTypeSerialnumberdetailsInner](docs/ProductLineTypeSerialnumberdetailsInner.md)
 - [ProductLineTypeTrackingnumberdetailsInner](docs/ProductLineTypeTrackingnumberdetailsInner.md)
 - [ProductSearchRequest](docs/ProductSearchRequest.md)
 - [ProductSearchRequestServicerequest](docs/ProductSearchRequestServicerequest.md)
 - [ProductSearchRequestServicerequestProductsearchrequest](docs/ProductSearchRequestServicerequestProductsearchrequest.md)
 - [ProductSearchRequestServicerequestProductsearchrequestSearchcriteria](docs/ProductSearchRequestServicerequestProductsearchrequestSearchcriteria.md)
 - [ProductSearchRequestServicerequestRequestpreamble](docs/ProductSearchRequestServicerequestRequestpreamble.md)
 - [ProductSearchResponse](docs/ProductSearchResponse.md)
 - [ProductSearchResponseCatalogInner](docs/ProductSearchResponseCatalogInner.md)
 - [ProductSearchResponseCatalogInnerLinksInner](docs/ProductSearchResponseCatalogInnerLinksInner.md)
 - [QuoteDetails](docs/QuoteDetails.md)
 - [QuoteDetailsQuoteDetailResponse](docs/QuoteDetailsQuoteDetailResponse.md)
 - [QuoteDetailsQuoteDetailResponseResponsePreamble](docs/QuoteDetailsQuoteDetailResponseResponsePreamble.md)
 - [QuoteDetailsQuoteDetailResponseRetrieveQuoteResponse](docs/QuoteDetailsQuoteDetailResponseRetrieveQuoteResponse.md)
 - [QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseAccountInfo](docs/QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseAccountInfo.md)
 - [QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseContactInfo](docs/QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseContactInfo.md)
 - [QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser](docs/QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser.md)
 - [QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes](docs/QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes.md)
 - [QuoteDetailsRequest](docs/QuoteDetailsRequest.md)
 - [QuoteDetailsRequestQuoteProductsRequest](docs/QuoteDetailsRequestQuoteProductsRequest.md)
 - [QuoteDetailsRequestQuoteProductsRequestRequestpreamble](docs/QuoteDetailsRequestQuoteProductsRequestRequestpreamble.md)
 - [QuoteDetailsRequestQuoteProductsRequestRetrieveQuoteProductsRequest](docs/QuoteDetailsRequestQuoteProductsRequestRetrieveQuoteProductsRequest.md)
 - [QuoteDetailsResponse](docs/QuoteDetailsResponse.md)
 - [QuoteDetailsResponseAdditionalAttributesInner](docs/QuoteDetailsResponseAdditionalAttributesInner.md)
 - [QuoteDetailsResponseEndUserInfo](docs/QuoteDetailsResponseEndUserInfo.md)
 - [QuoteDetailsResponseProductsInner](docs/QuoteDetailsResponseProductsInner.md)
 - [QuoteDetailsResponseProductsInnerPrice](docs/QuoteDetailsResponseProductsInnerPrice.md)
 - [QuoteDetailsResponseQuoteDetailResponse](docs/QuoteDetailsResponseQuoteDetailResponse.md)
 - [QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse](docs/QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse.md)
 - [QuoteDetailsResponseResellerInfo](docs/QuoteDetailsResponseResellerInfo.md)
 - [QuoteListResponse](docs/QuoteListResponse.md)
 - [QuoteListResponseQuoteSearchResponse](docs/QuoteListResponseQuoteSearchResponse.md)
 - [QuoteListResponseQuoteSearchResponseQuoteListInner](docs/QuoteListResponseQuoteSearchResponseQuoteListInner.md)
 - [QuoteListResponseQuoteSearchResponseResponsePreamble](docs/QuoteListResponseQuoteSearchResponseResponsePreamble.md)
 - [QuoteProductList](docs/QuoteProductList.md)
 - [QuoteProductListPrice](docs/QuoteProductListPrice.md)
 - [QuoteSearchResponse](docs/QuoteSearchResponse.md)
 - [QuoteSearchResponseQuotesInner](docs/QuoteSearchResponseQuotesInner.md)
 - [QuoteToOrderDetailsDTO](docs/QuoteToOrderDetailsDTO.md)
 - [QuoteToOrderDetailsDTOAdditionalAttributesInner](docs/QuoteToOrderDetailsDTOAdditionalAttributesInner.md)
 - [QuoteToOrderDetailsDTOEndUserInfoInner](docs/QuoteToOrderDetailsDTOEndUserInfoInner.md)
 - [QuoteToOrderDetailsDTOLinesInner](docs/QuoteToOrderDetailsDTOLinesInner.md)
 - [QuoteToOrderDetailsDTOShipToInfoInner](docs/QuoteToOrderDetailsDTOShipToInfoInner.md)
 - [QuoteToOrderDetailsDTOVmfadditionalAttributesInner](docs/QuoteToOrderDetailsDTOVmfadditionalAttributesInner.md)
 - [QuoteToOrderResponse](docs/QuoteToOrderResponse.md)
 - [RenewalsDetailsResponse](docs/RenewalsDetailsResponse.md)
 - [RenewalsDetailsResponseAdditionalAttributesInner](docs/RenewalsDetailsResponseAdditionalAttributesInner.md)
 - [RenewalsDetailsResponseEndUserInfoInner](docs/RenewalsDetailsResponseEndUserInfoInner.md)
 - [RenewalsDetailsResponseProductsInner](docs/RenewalsDetailsResponseProductsInner.md)
 - [RenewalsDetailsResponseReferenceNumberInner](docs/RenewalsDetailsResponseReferenceNumberInner.md)
 - [RenewalsSearchRequest](docs/RenewalsSearchRequest.md)
 - [RenewalsSearchRequestDataType](docs/RenewalsSearchRequestDataType.md)
 - [RenewalsSearchRequestDataTypeEndDate](docs/RenewalsSearchRequestDataTypeEndDate.md)
 - [RenewalsSearchRequestDataTypeExpirationDate](docs/RenewalsSearchRequestDataTypeExpirationDate.md)
 - [RenewalsSearchRequestDataTypeInvoiceDate](docs/RenewalsSearchRequestDataTypeInvoiceDate.md)
 - [RenewalsSearchRequestDataTypeStartDate](docs/RenewalsSearchRequestDataTypeStartDate.md)
 - [RenewalsSearchRequestStatus](docs/RenewalsSearchRequestStatus.md)
 - [RenewalsSearchRequestStatusOpporutinyStatus](docs/RenewalsSearchRequestStatusOpporutinyStatus.md)
 - [RenewalsSearchResponse](docs/RenewalsSearchResponse.md)
 - [RenewalsSearchResponseRenewalsInner](docs/RenewalsSearchResponseRenewalsInner.md)
 - [RenewalsSearchResponseRenewalsInnerLinksInner](docs/RenewalsSearchResponseRenewalsInnerLinksInner.md)
 - [ReturnsCreateRequest](docs/ReturnsCreateRequest.md)
 - [ReturnsCreateRequestListInner](docs/ReturnsCreateRequestListInner.md)
 - [ReturnsCreateRequestListInnerShipFromInfoInner](docs/ReturnsCreateRequestListInnerShipFromInfoInner.md)
 - [ReturnsCreateResponse](docs/ReturnsCreateResponse.md)
 - [ReturnsCreateResponseReturnsClaimsInner](docs/ReturnsCreateResponseReturnsClaimsInner.md)
 - [ReturnsDetailsResponse](docs/ReturnsDetailsResponse.md)
 - [ReturnsDetailsResponseProductsInner](docs/ReturnsDetailsResponseProductsInner.md)
 - [ReturnsSearchResponse](docs/ReturnsSearchResponse.md)
 - [ReturnsSearchResponseReturnsClaimsInner](docs/ReturnsSearchResponseReturnsClaimsInner.md)
 - [ReturnsSearchResponseReturnsClaimsInnerLinksInner](docs/ReturnsSearchResponseReturnsClaimsInnerLinksInner.md)
 - [ValidateQuoteResponse](docs/ValidateQuoteResponse.md)
 - [ValidateQuoteResponseLinesInner](docs/ValidateQuoteResponseLinesInner.md)
 - [ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner](docs/ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner.md)
 - [ValidateQuoteResponseVmfAdditionalAttributesInner](docs/ValidateQuoteResponseVmfAdditionalAttributesInner.md)


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


## Author
-[Ingram Micro Xvantage](https://github.com/ingrammicro-xvantage)

## Contact

For any inquiries or support, please feel free to contact us at:

- Email: [xi_support@ingrammicro.com](xi_support@ingrammicro.com)


