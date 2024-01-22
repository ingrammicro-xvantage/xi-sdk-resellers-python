# coding: utf-8

"""
    Reseller API

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi.sdk.resellers.models.order_create_response_orders_inner_rejected_line_items_inner import OrderCreateResponseOrdersInnerRejectedLineItemsInner

class TestOrderCreateResponseOrdersInnerRejectedLineItemsInner(unittest.TestCase):
    """OrderCreateResponseOrdersInnerRejectedLineItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateResponseOrdersInnerRejectedLineItemsInner:
        """Test OrderCreateResponseOrdersInnerRejectedLineItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateResponseOrdersInnerRejectedLineItemsInner`
        """
        model = OrderCreateResponseOrdersInnerRejectedLineItemsInner()
        if include_optional:
            return OrderCreateResponseOrdersInnerRejectedLineItemsInner(
                customer_linenumber = '',
                ingram_part_number = '',
                vendor_part_number = '',
                quantity_ordered = 56,
                reject_code = '',
                reject_reason = ''
            )
        else:
            return OrderCreateResponseOrdersInnerRejectedLineItemsInner(
        )
        """

    def testOrderCreateResponseOrdersInnerRejectedLineItemsInner(self):
        """Test OrderCreateResponseOrdersInnerRejectedLineItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
