# coding: utf-8

"""
    Reseller API Documentation

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi-sdk-resellers-python.models.order_create_response_orders_inner_lines_inner import OrderCreateResponseOrdersInnerLinesInner

class TestOrderCreateResponseOrdersInnerLinesInner(unittest.TestCase):
    """OrderCreateResponseOrdersInnerLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateResponseOrdersInnerLinesInner:
        """Test OrderCreateResponseOrdersInnerLinesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateResponseOrdersInnerLinesInner`
        """
        model = OrderCreateResponseOrdersInnerLinesInner()
        if include_optional:
            return OrderCreateResponseOrdersInnerLinesInner(
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
                    xi-sdk-resellers-python.models.order_create_response_orders_inner_lines_inner_shipment_details_inner.OrderCreateResponse_orders_inner_lines_inner_shipmentDetails_inner(
                        carrier_code = '', 
                        carrier_name = '', 
                        ship_from_warehouse_id = '', 
                        ship_from_location = '', 
                        freight_account_number = '', 
                        signature_required = '', 
                        shipping_instructions = '', )
                    ],
                additional_attributes = [
                    xi-sdk-resellers-python.models.order_create_response_orders_inner_lines_inner_additional_attributes_inner.OrderCreateResponse_orders_inner_lines_inner_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ]
            )
        else:
            return OrderCreateResponseOrdersInnerLinesInner(
        )
        """

    def testOrderCreateResponseOrdersInnerLinesInner(self):
        """Test OrderCreateResponseOrdersInnerLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
