# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field
from typing import Optional
from typing_extensions import Annotated
from xi.sdk.resellers.models.freight_request import FreightRequest
from xi.sdk.resellers.models.freight_response import FreightResponse

from xi.sdk.resellers.api_client import ApiClient, RequestSerialized
from xi.sdk.resellers.api_response import ApiResponse
from xi.sdk.resellers.rest import RESTResponseType


class FreightEstimateApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def post_freightestimate(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        im_customer_contact: Annotated[str, Field(strict=True, max_length=64, description="Logged in Users email address contact.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction.")] = None,
        freight_request: Optional[FreightRequest] = None,
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
    ) -> FreightResponse:
        """Freight Estimate

        The freight estimator endpoint will allow customers to understand the freight cost for an order.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param im_customer_contact: Logged in Users email address contact. (required)
        :type im_customer_contact: str
        :param im_sender_id: Unique value used to identify the sender of the transaction.
        :type im_sender_id: str
        :param freight_request:
        :type freight_request: FreightRequest
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

        _param = self._post_freightestimate_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_customer_contact=im_customer_contact,
            im_sender_id=im_sender_id,
            freight_request=freight_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FreightResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
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
    def post_freightestimate_with_http_info(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        im_customer_contact: Annotated[str, Field(strict=True, max_length=64, description="Logged in Users email address contact.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction.")] = None,
        freight_request: Optional[FreightRequest] = None,
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
    ) -> ApiResponse[FreightResponse]:
        """Freight Estimate

        The freight estimator endpoint will allow customers to understand the freight cost for an order.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param im_customer_contact: Logged in Users email address contact. (required)
        :type im_customer_contact: str
        :param im_sender_id: Unique value used to identify the sender of the transaction.
        :type im_sender_id: str
        :param freight_request:
        :type freight_request: FreightRequest
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

        _param = self._post_freightestimate_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_customer_contact=im_customer_contact,
            im_sender_id=im_sender_id,
            freight_request=freight_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FreightResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
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
    def post_freightestimate_without_preload_content(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        im_customer_contact: Annotated[str, Field(strict=True, max_length=64, description="Logged in Users email address contact.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction.")] = None,
        freight_request: Optional[FreightRequest] = None,
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
        """Freight Estimate

        The freight estimator endpoint will allow customers to understand the freight cost for an order.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param im_customer_contact: Logged in Users email address contact. (required)
        :type im_customer_contact: str
        :param im_sender_id: Unique value used to identify the sender of the transaction.
        :type im_sender_id: str
        :param freight_request:
        :type freight_request: FreightRequest
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

        _param = self._post_freightestimate_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_customer_contact=im_customer_contact,
            im_sender_id=im_sender_id,
            freight_request=freight_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FreightResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _post_freightestimate_serialize(
        self,
        im_customer_number,
        im_country_code,
        im_correlation_id,
        im_customer_contact,
        im_sender_id,
        freight_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if im_customer_number is not None:
            _header_params['IM-CustomerNumber'] = im_customer_number
        if im_country_code is not None:
            _header_params['IM-CountryCode'] = im_country_code
        if im_correlation_id is not None:
            _header_params['IM-CorrelationID'] = im_correlation_id
        if im_customer_contact is not None:
            _header_params['IM-CustomerContact'] = im_customer_contact
        if im_sender_id is not None:
            _header_params['IM-SenderID'] = im_sender_id
        # process the form parameters
        # process the body parameter
        if freight_request is not None:
            _body_params = freight_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
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
            resource_path='/resellers/v6/freightestimate',
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


