# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_response import OrderCreateResponse

class TestOrderCreateResponse(unittest.TestCase):
    """OrderCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateResponse:
        """Test OrderCreateResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateResponse`
        """
        model = OrderCreateResponse()
        if include_optional:
            return OrderCreateResponse(
                customer_order_number = '',
                end_customer_order_number = '',
                bill_to_address_id = '',
                special_bid_number = '',
                order_split = True,
                processed_partially = True,
                purchase_order_total = 1.337,
                ship_to_info = xi.sdk.resellers.models.order_create_response_ship_to_info.OrderCreateResponse_shipToInfo(
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
                end_user_info = xi.sdk.resellers.models.order_create_response_end_user_info.OrderCreateResponse_endUserInfo(
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
                orders = [
                    xi.sdk.resellers.models.order_create_response_orders_inner.OrderCreateResponse_orders_inner(
                        number_of_lines_with_success = 56, 
                        number_of_lines_with_error = 56, 
                        number_of_lines_with_warning = 56, 
                        ingram_order_number = '', 
                        ingram_order_date = '', 
                        notes = '', 
                        order_type = '', 
                        order_total = 1.337, 
                        freight_charges = 1.337, 
                        total_tax = 1.337, 
                        currency_code = '', 
                        lines = [
                            xi.sdk.resellers.models.order_create_response_orders_inner_lines_inner.OrderCreateResponse_orders_inner_lines_inner(
                                sub_order_number = '', 
                                ingram_line_number = '', 
                                customer_line_number = '', 
                                line_status = '', 
                                ingram_part_number = '', 
                                vendor_part_number = '', 
                                unit_price = 1.337, 
                                extended_unit_price = 1.337, 
                                quantity_ordered = 56, 
                                quantity_confirmed = 56, 
                                quantity_back_ordered = 56, 
                                special_bid_number = '', 
                                notes = '', 
                                shipment_details = [
                                    xi.sdk.resellers.models.order_create_response_orders_inner_lines_inner_shipment_details_inner.OrderCreateResponse_orders_inner_lines_inner_shipmentDetails_inner(
                                        carrier_code = '', 
                                        carrier_name = '', 
                                        ship_from_warehouse_id = '', 
                                        ship_from_location = '', 
                                        freight_account_number = '', 
                                        signature_required = '', 
                                        shipping_instructions = '', )
                                    ], 
                                additional_attributes = [
                                    xi.sdk.resellers.models.order_create_response_orders_inner_lines_inner_additional_attributes_inner.OrderCreateResponse_orders_inner_lines_inner_additionalAttributes_inner(
                                        attribute_name = '', 
                                        attribute_value = '', )
                                    ], )
                            ], 
                        miscellaneous_charges = [
                            xi.sdk.resellers.models.order_create_response_orders_inner_miscellaneous_charges_inner.OrderCreateResponse_orders_inner_miscellaneousCharges_inner(
                                sub_order_number = '', 
                                charge_line_reference = '', 
                                charge_description = '', 
                                charge_amount = 1.337, )
                            ], 
                        links = [
                            xi.sdk.resellers.models.order_create_response_orders_inner_links_inner.OrderCreateResponse_orders_inner_links_inner(
                                topic = '', 
                                href = '', 
                                type = '', )
                            ], 
                        rejected_line_items = [
                            xi.sdk.resellers.models.order_create_response_orders_inner_rejected_line_items_inner.OrderCreateResponse_orders_inner_rejectedLineItems_inner(
                                customer_linenumber = '', 
                                ingram_part_number = '', 
                                vendor_part_number = '', 
                                quantity_ordered = 56, 
                                reject_code = '', 
                                reject_reason = '', )
                            ], 
                        additional_attributes = [
                            xi.sdk.resellers.models.order_create_response_orders_inner_additional_attributes_inner.OrderCreateResponse_orders_inner_additionalAttributes_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], )
                    ]
            )
        else:
            return OrderCreateResponse(
        )
        """

    def testOrderCreateResponse(self):
        """Test OrderCreateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
