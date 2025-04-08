# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_response_orders_inner_miscellaneous_charges_inner import OrderCreateResponseOrdersInnerMiscellaneousChargesInner

class TestOrderCreateResponseOrdersInnerMiscellaneousChargesInner(unittest.TestCase):
    """OrderCreateResponseOrdersInnerMiscellaneousChargesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateResponseOrdersInnerMiscellaneousChargesInner:
        """Test OrderCreateResponseOrdersInnerMiscellaneousChargesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateResponseOrdersInnerMiscellaneousChargesInner`
        """
        model = OrderCreateResponseOrdersInnerMiscellaneousChargesInner()
        if include_optional:
            return OrderCreateResponseOrdersInnerMiscellaneousChargesInner(
                sub_order_number = '',
                charge_line_reference = '',
                charge_description = '',
                charge_amount = 1.337
            )
        else:
            return OrderCreateResponseOrdersInnerMiscellaneousChargesInner(
        )
        """

    def testOrderCreateResponseOrdersInnerMiscellaneousChargesInner(self):
        """Test OrderCreateResponseOrdersInnerMiscellaneousChargesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
