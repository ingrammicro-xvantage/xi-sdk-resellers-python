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

from xi-sdk-resellers-python.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship_ship_date_range import OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange

class TestOrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange(unittest.TestCase):
    """OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange:
        """Test OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange`
        """
        model = OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange()
        if include_optional:
            return OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange(
                start_date = '',
                end_date = ''
            )
        else:
            return OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange(
        )
        """

    def testOrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange(self):
        """Test OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
