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

from xi-sdk-resellers-python.models.order_detail_b2_b_lines_inner_multiple_shipments_inner import OrderDetailB2BLinesInnerMultipleShipmentsInner

class TestOrderDetailB2BLinesInnerMultipleShipmentsInner(unittest.TestCase):
    """OrderDetailB2BLinesInnerMultipleShipmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerMultipleShipmentsInner:
        """Test OrderDetailB2BLinesInnerMultipleShipmentsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerMultipleShipmentsInner`
        """
        model = OrderDetailB2BLinesInnerMultipleShipmentsInner()
        if include_optional:
            return OrderDetailB2BLinesInnerMultipleShipmentsInner(
                line_number = '',
                requested_quantity = '',
                confirmed_quantity = '',
                data_type = '',
                date_range = xi-sdk-resellers-python.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship_ship_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_ship_shipDateRange(
                    start_date = '', 
                    end_date = '', ),
                source = '',
                description = '',
                var_date = '',
                delivery_date = ''
            )
        else:
            return OrderDetailB2BLinesInnerMultipleShipmentsInner(
        )
        """

    def testOrderDetailB2BLinesInnerMultipleShipmentsInner(self):
        """Test OrderDetailB2BLinesInnerMultipleShipmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()