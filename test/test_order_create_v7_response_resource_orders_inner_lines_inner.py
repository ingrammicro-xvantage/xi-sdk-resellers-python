# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_v7_response_resource_orders_inner_lines_inner import OrderCreateV7ResponseResourceOrdersInnerLinesInner

class TestOrderCreateV7ResponseResourceOrdersInnerLinesInner(unittest.TestCase):
    """OrderCreateV7ResponseResourceOrdersInnerLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateV7ResponseResourceOrdersInnerLinesInner:
        """Test OrderCreateV7ResponseResourceOrdersInnerLinesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateV7ResponseResourceOrdersInnerLinesInner`
        """
        model = OrderCreateV7ResponseResourceOrdersInnerLinesInner()
        if include_optional:
            return OrderCreateV7ResponseResourceOrdersInnerLinesInner(
                sub_order_number = '',
                ingram_line_number = '',
                customer_line_number = '',
                line_status = '',
                ingram_part_number = '',
                unit_price = 1.337,
                extended_unit_price = 1.337,
                quantity_ordered = 56,
                quantity_confirmed = 56,
                quantity_back_ordered = 56,
                notes = '',
                shipment_details = [
                    xi.sdk.resellers.models.order_create_v7_response_resource_orders_inner_lines_inner_shipment_details_inner.OrderCreateV7Response_resource_orders_inner_lines_inner_shipmentDetails_inner(
                        carrier_code = '', 
                        carrier_name = '', 
                        ship_from_warehouse_id = '', 
                        ship_from_location = '', )
                    ]
            )
        else:
            return OrderCreateV7ResponseResourceOrdersInnerLinesInner(
        )
        """

    def testOrderCreateV7ResponseResourceOrdersInnerLinesInner(self):
        """Test OrderCreateV7ResponseResourceOrdersInnerLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
