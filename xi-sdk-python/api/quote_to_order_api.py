# coding: utf-8

"""
    Reseller API Documentation - United States

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from typing import Optional

from xi-sdk-python.models.quote_to_order_details_dto import QuoteToOrderDetailsDTO
from xi-sdk-python.models.quote_to_order_response import QuoteToOrderResponse

from xi-sdk-python.api_client import ApiClient
from xi-sdk-python.api_response import ApiResponse
from xi-sdk-python.rest import RESTResponseType


class QuoteToOrderApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def post_quote_to_order_v6(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction accross all the systems.")],
        quote_to_order_details_dto: QuoteToOrderDetailsDTO,
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> QuoteToOrderResponse:
        """Quote To Order

        The “Quote to Order” (QTO) endpoint allows a customer to create an order using the existing quote which is in “Ready to Order” status. A customer can create an order using Configure to order (CTO) quote or a non-configure to order (Non-CTO) quote. Upon successful submission of the order create request, a confirmation message will be returned as an API response. <br > <br >Ingram Micro offers webhooks as a method to send notifications to Resellers once the order creation request is received. All the updates related to Order creation will be pushed as a notification to the customer via a pre-defined callback URL as an HTTP post. <br > <br > **Prerequisite:** Pre-defined callback URL <br > <br > Before creating an order using the quote, it’s recommended to validate the quote using the “Validate Quote” endpoint. Validate Quote endpoint will not only validate the quote but also outline all the mandatory fields required by the vendor at a header level and at the line level which a customer need to pass to the Quote To Order endpoint request.  For a detailed understanding of the “Validate Quote” endpoint, review the “Validate Quote” endpoint documentation. <br ><br > **How it works:** <br ><br > - The customer validates the quote with a quote number from Validate Quote endpoint. <br > - The customer copies all the mandatory fields required by the vendor and adds them to the QTO request body. <br > - The customer provides all the values for Vendor mandatory fields along with other required information for QTO to create an order. <br > - After the order creation request receipt acknowledgment from the QTO endpoint, all further order creation updates will be provided via webhook push notification.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction accross all the systems. (required)
        :type im_correlation_id: str
        :param quote_to_order_details_dto: (required)
        :type quote_to_order_details_dto: QuoteToOrderDetailsDTO
        :param im_sender_id: Unique value used to identify the sender of the transaction.
        :type im_sender_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_quote_to_order_v6_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            quote_to_order_details_dto=quote_to_order_details_dto,
            im_sender_id=im_sender_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "QuoteToOrderResponse",
            '400': "PostQuoteToOrderV6400Response",
            '500': "GetResellerV6ValidateQuote500Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def post_quote_to_order_v6_with_http_info(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction accross all the systems.")],
        quote_to_order_details_dto: QuoteToOrderDetailsDTO,
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[QuoteToOrderResponse]:
        """Quote To Order

        The “Quote to Order” (QTO) endpoint allows a customer to create an order using the existing quote which is in “Ready to Order” status. A customer can create an order using Configure to order (CTO) quote or a non-configure to order (Non-CTO) quote. Upon successful submission of the order create request, a confirmation message will be returned as an API response. <br > <br >Ingram Micro offers webhooks as a method to send notifications to Resellers once the order creation request is received. All the updates related to Order creation will be pushed as a notification to the customer via a pre-defined callback URL as an HTTP post. <br > <br > **Prerequisite:** Pre-defined callback URL <br > <br > Before creating an order using the quote, it’s recommended to validate the quote using the “Validate Quote” endpoint. Validate Quote endpoint will not only validate the quote but also outline all the mandatory fields required by the vendor at a header level and at the line level which a customer need to pass to the Quote To Order endpoint request.  For a detailed understanding of the “Validate Quote” endpoint, review the “Validate Quote” endpoint documentation. <br ><br > **How it works:** <br ><br > - The customer validates the quote with a quote number from Validate Quote endpoint. <br > - The customer copies all the mandatory fields required by the vendor and adds them to the QTO request body. <br > - The customer provides all the values for Vendor mandatory fields along with other required information for QTO to create an order. <br > - After the order creation request receipt acknowledgment from the QTO endpoint, all further order creation updates will be provided via webhook push notification.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction accross all the systems. (required)
        :type im_correlation_id: str
        :param quote_to_order_details_dto: (required)
        :type quote_to_order_details_dto: QuoteToOrderDetailsDTO
        :param im_sender_id: Unique value used to identify the sender of the transaction.
        :type im_sender_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_quote_to_order_v6_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            quote_to_order_details_dto=quote_to_order_details_dto,
            im_sender_id=im_sender_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "QuoteToOrderResponse",
            '400': "PostQuoteToOrderV6400Response",
            '500': "GetResellerV6ValidateQuote500Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def post_quote_to_order_v6_without_preload_content(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction accross all the systems.")],
        quote_to_order_details_dto: QuoteToOrderDetailsDTO,
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Quote To Order

        The “Quote to Order” (QTO) endpoint allows a customer to create an order using the existing quote which is in “Ready to Order” status. A customer can create an order using Configure to order (CTO) quote or a non-configure to order (Non-CTO) quote. Upon successful submission of the order create request, a confirmation message will be returned as an API response. <br > <br >Ingram Micro offers webhooks as a method to send notifications to Resellers once the order creation request is received. All the updates related to Order creation will be pushed as a notification to the customer via a pre-defined callback URL as an HTTP post. <br > <br > **Prerequisite:** Pre-defined callback URL <br > <br > Before creating an order using the quote, it’s recommended to validate the quote using the “Validate Quote” endpoint. Validate Quote endpoint will not only validate the quote but also outline all the mandatory fields required by the vendor at a header level and at the line level which a customer need to pass to the Quote To Order endpoint request.  For a detailed understanding of the “Validate Quote” endpoint, review the “Validate Quote” endpoint documentation. <br ><br > **How it works:** <br ><br > - The customer validates the quote with a quote number from Validate Quote endpoint. <br > - The customer copies all the mandatory fields required by the vendor and adds them to the QTO request body. <br > - The customer provides all the values for Vendor mandatory fields along with other required information for QTO to create an order. <br > - After the order creation request receipt acknowledgment from the QTO endpoint, all further order creation updates will be provided via webhook push notification.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction accross all the systems. (required)
        :type im_correlation_id: str
        :param quote_to_order_details_dto: (required)
        :type quote_to_order_details_dto: QuoteToOrderDetailsDTO
        :param im_sender_id: Unique value used to identify the sender of the transaction.
        :type im_sender_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_quote_to_order_v6_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            quote_to_order_details_dto=quote_to_order_details_dto,
            im_sender_id=im_sender_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "QuoteToOrderResponse",
            '400': "PostQuoteToOrderV6400Response",
            '500': "GetResellerV6ValidateQuote500Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _post_quote_to_order_v6_serialize(
        self,
        im_customer_number,
        im_country_code,
        im_correlation_id,
        quote_to_order_details_dto,
        im_sender_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if im_customer_number is not None:
            _header_params['IM-CustomerNumber'] = im_customer_number
        if im_country_code is not None:
            _header_params['IM-CountryCode'] = im_country_code
        if im_sender_id is not None:
            _header_params['IM-SenderID'] = im_sender_id
        if im_correlation_id is not None:
            _header_params['IM-CorrelationID'] = im_correlation_id
        # process the form parameters
        # process the body parameter
        if quote_to_order_details_dto is not None:
            _body_params = quote_to_order_details_dto


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'application'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/resellers/v6/q2o/orders',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


