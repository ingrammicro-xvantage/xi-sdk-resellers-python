# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_response import OrderDetailResponse

class TestOrderDetailResponse(unittest.TestCase):
    """OrderDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponse:
        """Test OrderDetailResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponse`
        """
        model = OrderDetailResponse()
        if include_optional:
            return OrderDetailResponse(
                ingram_order_number = '',
                ingram_order_date = '',
                order_type = '',
                customer_order_number = '',
                end_customer_order_number = '',
                vendor_sales_order_number = '',
                order_status = '',
                order_total = 1.337,
                order_sub_total = 1.337,
                freight_charges = 1.337,
                currency_code = '',
                total_weight = 1.337,
                total_tax = 1.337,
                payment_terms = '',
                notes = '',
                bill_to_info = xi.sdk.resellers.models.order_detail_response_bill_to_info.OrderDetailResponse_billToInfo(
                    contact = '', 
                    company_name = '', 
                    name1 = '', 
                    name2 = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                ship_to_info = xi.sdk.resellers.models.order_detail_response_ship_to_info.OrderDetailResponse_shipToInfo(
                    contact = '', 
                    company_name = '', 
                    name1 = '', 
                    name2 = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                end_user_info = xi.sdk.resellers.models.order_detail_response_end_user_info.OrderDetailResponse_endUserInfo(
                    contact = '', 
                    company_name = '', 
                    name1 = '', 
                    name2 = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                lines = [
                    xi.sdk.resellers.models.order_detail_response_lines_inner.OrderDetailResponse_lines_inner(
                        sub_order_number = '', 
                        ingram_order_line_number = '', 
                        vendor_sales_order_line_number = '', 
                        customer_linenumber = '', 
                        line_status = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        vendor_name = '', 
                        part_description = '', 
                        unit_weight = 1.337, 
                        weight_uom = '', 
                        unit_price = 56, 
                        upc_code = '', 
                        extended_price = 1.337, 
                        tax_amount = 1.337, 
                        currency_code = '', 
                        quantity_ordered = 56, 
                        quantity_confirmed = 56, 
                        quantity_back_ordered = 56, 
                        special_bid_number = '', 
                        requested_delivery_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        promised_delivery_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        line_notes = '', 
                        shipment_details = [
                            xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner.OrderDetailResponse_lines_inner_shipmentDetails_inner(
                                quantity = 56, 
                                estimated_ship_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                shipped_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                estimated_delivery_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                delivered_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                ship_from_warehouse_id = '', 
                                ship_from_location = '', 
                                invoice_number = '', 
                                invoice_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                carrier_details = xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details.OrderDetailResponse_lines_inner_shipmentDetails_inner_carrierDetails(
                                    carrier_code = '', 
                                    carrier_name = '', 
                                    tracking_details = [
                                        xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner.OrderDetailResponse_lines_inner_shipmentDetails_inner_carrierDetails_trackingDetails_inner(
                                            tracking_number = '', 
                                            tracking_url = '', 
                                            package_weight = '', 
                                            carton_number = '', 
                                            quantity_in_box = '', 
                                            serial_numbers = [
                                                xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner_serial_numbers_inner.OrderDetailResponse_lines_inner_shipmentDetails_inner_carrierDetails_trackingDetails_inner_SerialNumbers_inner(
                                                    serial_number = '', )
                                                ], )
                                        ], ), )
                            ], 
                        additional_attributes = [
                            xi.sdk.resellers.models.order_detail_response_lines_inner_additional_attributes_inner.OrderDetailResponse_lines_inner_additionalAttributes_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], 
                        links = [
                            xi.sdk.resellers.models.order_detail_response_lines_inner_links_inner.OrderDetailResponse_lines_inner_links_inner(
                                topic = '', 
                                href = '', 
                                type = '', )
                            ], )
                    ],
                miscellaneous_charges = [
                    xi.sdk.resellers.models.order_detail_response_miscellaneous_charges_inner.OrderDetailResponse_miscellaneousCharges_inner(
                        sub_order_number = '', 
                        charge_line_reference = '', 
                        charge_description = '', 
                        charge_amount = 1.337, )
                    ],
                additional_attributes = [
                    xi.sdk.resellers.models.order_detail_response_lines_inner_additional_attributes_inner.OrderDetailResponse_lines_inner_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ]
            )
        else:
            return OrderDetailResponse(
        )
        """

    def testOrderDetailResponse(self):
        """Test OrderDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
