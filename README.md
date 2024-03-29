# xi.sdk.resellers
For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.


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
*AccesstokenApi* | [**get_accesstoken**](docs/AccesstokenApi.md#get_accesstoken) | **GET** /oauth/oauth20/token | Accesstoken
*DealsApi* | [**get_resellers_v6_dealsdetails**](docs/DealsApi.md#get_resellers_v6_dealsdetails) | **GET** /resellers/v6/deals/{dealId} | Deals Details
*DealsApi* | [**get_resellers_v6_dealssearch**](docs/DealsApi.md#get_resellers_v6_dealssearch) | **GET** /resellers/v6/deals/search | Deals Search
*FreightEstimateApi* | [**post_freightestimate**](docs/FreightEstimateApi.md#post_freightestimate) | **POST** /resellers/v6/freightestimate | Freight Estimate
*InvoicesApi* | [**get_invoicedetails_v6_1**](docs/InvoicesApi.md#get_invoicedetails_v6_1) | **GET** /resellers/v6.1/invoices/{invoiceNumber} | Get Invoice Details v6.1
*InvoicesApi* | [**get_resellers_v6_invoicesearch**](docs/InvoicesApi.md#get_resellers_v6_invoicesearch) | **GET** /resellers/v6/invoices | Search your invoice
*OrderStatusApi* | [**resellers_v1_webhooks_orderstatusevent_post**](docs/OrderStatusApi.md#resellers_v1_webhooks_orderstatusevent_post) | **POST** /resellers/v1/webhooks/orderstatusevent | Order Status
*OrdersApi* | [**delete_ordercancel**](docs/OrdersApi.md#delete_ordercancel) | **DELETE** /resellers/v6/orders/{OrderNumber} | Cancel your Order
*OrdersApi* | [**get_orderdetails_v6_1**](docs/OrdersApi.md#get_orderdetails_v6_1) | **GET** /resellers/v6.1/orders/{ordernumber} | Get Order Details v6.1
*OrdersApi* | [**get_resellers_v6_ordersearch**](docs/OrdersApi.md#get_resellers_v6_ordersearch) | **GET** /resellers/v6/orders/search | Search your Orders
*OrdersApi* | [**post_createorder_v6**](docs/OrdersApi.md#post_createorder_v6) | **POST** /resellers/v6/orders | Create your Order
*OrdersApi* | [**put_ordermodify**](docs/OrdersApi.md#put_ordermodify) | **PUT** /resellers/v6/orders/{orderNumber} | Modify your Order
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

 - [AccesstokenResponse](docs/AccesstokenResponse.md)
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
 - [GetAccesstoken400Response](docs/GetAccesstoken400Response.md)
 - [GetAccesstoken500Response](docs/GetAccesstoken500Response.md)
 - [GetAccesstoken500ResponseFault](docs/GetAccesstoken500ResponseFault.md)
 - [GetAccesstoken500ResponseFaultDetail](docs/GetAccesstoken500ResponseFaultDetail.md)
 - [GetResellerV6ValidateQuote400Response](docs/GetResellerV6ValidateQuote400Response.md)
 - [GetResellerV6ValidateQuote400ResponseFieldsInner](docs/GetResellerV6ValidateQuote400ResponseFieldsInner.md)
 - [GetResellerV6ValidateQuote500Response](docs/GetResellerV6ValidateQuote500Response.md)
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
 - [OrderModifyRequest](docs/OrderModifyRequest.md)
 - [OrderModifyRequestAdditionalAttributesInner](docs/OrderModifyRequestAdditionalAttributesInner.md)
 - [OrderModifyRequestLinesInner](docs/OrderModifyRequestLinesInner.md)
 - [OrderModifyRequestShipToInfo](docs/OrderModifyRequestShipToInfo.md)
 - [OrderModifyResponse](docs/OrderModifyResponse.md)
 - [OrderModifyResponseLinesInner](docs/OrderModifyResponseLinesInner.md)
 - [OrderModifyResponseLinesInnerAdditionalAttributesInner](docs/OrderModifyResponseLinesInnerAdditionalAttributesInner.md)
 - [OrderModifyResponseLinesInnerShipmentDetails](docs/OrderModifyResponseLinesInnerShipmentDetails.md)
 - [OrderModifyResponseRejectedLineItemsInner](docs/OrderModifyResponseRejectedLineItemsInner.md)
 - [OrderModifyResponseShipToInfo](docs/OrderModifyResponseShipToInfo.md)
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
 - [ProductSearchResponse](docs/ProductSearchResponse.md)
 - [ProductSearchResponseCatalogInner](docs/ProductSearchResponseCatalogInner.md)
 - [ProductSearchResponseCatalogInnerLinksInner](docs/ProductSearchResponseCatalogInnerLinksInner.md)
 - [QuoteDetailsResponse](docs/QuoteDetailsResponse.md)
 - [QuoteDetailsResponseAdditionalAttributesInner](docs/QuoteDetailsResponseAdditionalAttributesInner.md)
 - [QuoteDetailsResponseEndUserInfo](docs/QuoteDetailsResponseEndUserInfo.md)
 - [QuoteDetailsResponseProductsInner](docs/QuoteDetailsResponseProductsInner.md)
 - [QuoteDetailsResponseProductsInnerPrice](docs/QuoteDetailsResponseProductsInnerPrice.md)
 - [QuoteDetailsResponseResellerInfo](docs/QuoteDetailsResponseResellerInfo.md)
 - [QuoteSearchResponse](docs/QuoteSearchResponse.md)
 - [QuoteSearchResponseQuotesInner](docs/QuoteSearchResponseQuotesInner.md)
 - [QuoteSearchResponseQuotesInnerLinks](docs/QuoteSearchResponseQuotesInnerLinks.md)
 - [QuoteToOrderDetailsDTO](docs/QuoteToOrderDetailsDTO.md)
 - [QuoteToOrderDetailsDTOAdditionalAttributesInner](docs/QuoteToOrderDetailsDTOAdditionalAttributesInner.md)
 - [QuoteToOrderDetailsDTOEndUserInfo](docs/QuoteToOrderDetailsDTOEndUserInfo.md)
 - [QuoteToOrderDetailsDTOLinesInner](docs/QuoteToOrderDetailsDTOLinesInner.md)
 - [QuoteToOrderDetailsDTOLinesInnerVmfAdditionalAttributesLinesInner](docs/QuoteToOrderDetailsDTOLinesInnerVmfAdditionalAttributesLinesInner.md)
 - [QuoteToOrderDetailsDTOShipToInfo](docs/QuoteToOrderDetailsDTOShipToInfo.md)
 - [QuoteToOrderDetailsDTOVmfadditionalAttributesInner](docs/QuoteToOrderDetailsDTOVmfadditionalAttributesInner.md)
 - [QuoteToOrderResponse](docs/QuoteToOrderResponse.md)
 - [RenewalsDetailsResponse](docs/RenewalsDetailsResponse.md)
 - [RenewalsDetailsResponseAdditionalAttributesInner](docs/RenewalsDetailsResponseAdditionalAttributesInner.md)
 - [RenewalsDetailsResponseEndUserInfo](docs/RenewalsDetailsResponseEndUserInfo.md)
 - [RenewalsDetailsResponseProductsInner](docs/RenewalsDetailsResponseProductsInner.md)
 - [RenewalsDetailsResponseReferenceNumber](docs/RenewalsDetailsResponseReferenceNumber.md)
 - [RenewalsSearchRequest](docs/RenewalsSearchRequest.md)
 - [RenewalsSearchRequestDateType](docs/RenewalsSearchRequestDateType.md)
 - [RenewalsSearchRequestDateTypeEndDate](docs/RenewalsSearchRequestDateTypeEndDate.md)
 - [RenewalsSearchRequestDateTypeExpirationDate](docs/RenewalsSearchRequestDateTypeExpirationDate.md)
 - [RenewalsSearchRequestDateTypeInvoiceDate](docs/RenewalsSearchRequestDateTypeInvoiceDate.md)
 - [RenewalsSearchRequestDateTypeStartDate](docs/RenewalsSearchRequestDateTypeStartDate.md)
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
 - **description**: 


## Author
-[Ingram Micro Xvantage](https://github.com/ingrammicro-xvantage)

## Contact

For any inquiries or support, please feel free to contact us at:

- Email: [xi_support@ingrammicro.com](xi_support@ingrammicro.com)

