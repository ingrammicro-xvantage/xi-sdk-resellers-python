# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_links_inner import OrderDetailB2BLinesInnerLinksInner

class TestOrderDetailB2BLinesInnerLinksInner(unittest.TestCase):
    """OrderDetailB2BLinesInnerLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerLinksInner:
        """Test OrderDetailB2BLinesInnerLinksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerLinksInner`
        """
        model = OrderDetailB2BLinesInnerLinksInner()
        if include_optional:
            return OrderDetailB2BLinesInnerLinksInner(
                topic = '',
                href = '',
                type = ''
            )
        else:
            return OrderDetailB2BLinesInnerLinksInner(
        )
        """

    def testOrderDetailB2BLinesInnerLinksInner(self):
        """Test OrderDetailB2BLinesInnerLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
