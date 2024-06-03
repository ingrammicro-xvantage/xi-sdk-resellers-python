# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_request import OrderCreateRequest

class TestOrderCreateRequest(unittest.TestCase):
    """OrderCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRequest:
        """Test OrderCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRequest`
        """
        model = OrderCreateRequest()
        if include_optional:
            return OrderCreateRequest(
                customer_order_number = '',
                end_customer_order_number = '',
                bill_to_address_id = '',
                special_bid_number = '',
                notes = '',
                accept_back_order = True,
                reseller_info = xi.sdk.resellers.models.order_create_request_reseller_info.OrderCreateRequest_resellerInfo(
                    reseller_id = '', 
                    company_name = '', 
                    contact = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = 56, 
                    email = '', ),
                vmf = xi.sdk.resellers.models.order_create_request_vmf.OrderCreateRequest_vmf(
                    vend_auth_number = '', ),
                ship_to_info = xi.sdk.resellers.models.order_create_request_ship_to_info.OrderCreateRequest_shipToInfo(
                    address_id = '', 
                    contact = '', 
                    company_name = '', 
                    name1 = '', 
                    name2 = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    address_line4 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                end_user_info = xi.sdk.resellers.models.order_create_request_end_user_info.OrderCreateRequest_endUserInfo(
                    end_user_id = '', 
                    contact = '', 
                    company_name = '', 
                    name1 = '', 
                    name2 = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    address_line4 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                lines = [
                    xi.sdk.resellers.models.order_create_request_lines_inner.OrderCreateRequest_lines_inner(
                        customer_line_number = '', 
                        ingram_part_number = '', 
                        quantity = 56, 
                        special_bid_number = '', 
                        notes = '', 
                        unit_price = 1.337, 
                        end_user_price = 1.337, 
                        additional_attributes = [
                            xi.sdk.resellers.models.order_create_request_lines_inner_additional_attributes_inner.OrderCreateRequest_lines_inner_additionalAttributes_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], 
                        warranty_info = [
                            xi.sdk.resellers.models.order_create_request_lines_inner_warranty_info_inner.OrderCreateRequest_lines_inner_warrantyInfo_inner(
                                direct_line_link = '', 
                                warranty_line_link = '', 
                                hardware_line_link = '', 
                                serial_info = [
                                    xi.sdk.resellers.models.order_create_request_lines_inner_warranty_info_inner_serial_info_inner.OrderCreateRequest_lines_inner_warrantyInfo_inner_serialInfo_inner(
                                        dateof_purchase = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        ship_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        primary_serial_number = '', 
                                        secondary_serial_number = '', )
                                    ], )
                            ], 
                        end_user_info = [
                            xi.sdk.resellers.models.order_create_request_lines_inner_end_user_info_inner.OrderCreateRequest_lines_inner_endUserInfo_inner(
                                end_user_type = '', 
                                end_user_id = '', 
                                contact = '', 
                                company_name = '', 
                                name1 = '', 
                                name2 = '', 
                                address_line1 = '', 
                                address_line2 = '', 
                                address_line3 = '', 
                                address_line4 = '', 
                                city = '', 
                                state = '', 
                                postal_code = '', 
                                country_code = '', 
                                phone_number = 1.337, 
                                email = '', )
                            ], )
                    ],
                shipment_details = xi.sdk.resellers.models.order_create_request_shipment_details.OrderCreateRequest_shipmentDetails(
                    carrier_code = '', 
                    freight_account_number = '', 
                    ship_complete = '', 
                    requested_delivery_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    signature_required = True, 
                    shipping_instructions = '', ),
                additional_attributes = [
                    xi.sdk.resellers.models.order_create_request_additional_attributes_inner.OrderCreateRequest_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ]
            )
        else:
            return OrderCreateRequest(
                customer_order_number = '',
        )
        """

    def testOrderCreateRequest(self):
        """Test OrderCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
