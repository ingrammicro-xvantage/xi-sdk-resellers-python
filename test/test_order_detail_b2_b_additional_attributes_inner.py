# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_additional_attributes_inner import OrderDetailB2BAdditionalAttributesInner

class TestOrderDetailB2BAdditionalAttributesInner(unittest.TestCase):
    """OrderDetailB2BAdditionalAttributesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BAdditionalAttributesInner:
        """Test OrderDetailB2BAdditionalAttributesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BAdditionalAttributesInner`
        """
        model = OrderDetailB2BAdditionalAttributesInner()
        if include_optional:
            return OrderDetailB2BAdditionalAttributesInner(
                attribute_name = '',
                attribute_value = ''
            )
        else:
            return OrderDetailB2BAdditionalAttributesInner(
        )
        """

    def testOrderDetailB2BAdditionalAttributesInner(self):
        """Test OrderDetailB2BAdditionalAttributesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
