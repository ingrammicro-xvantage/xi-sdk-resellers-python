# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.multi_sku_price_and_stock_request_servicerequest_requestpreamble import MultiSKUPriceAndStockRequestServicerequestRequestpreamble

class TestMultiSKUPriceAndStockRequestServicerequestRequestpreamble(unittest.TestCase):
    """MultiSKUPriceAndStockRequestServicerequestRequestpreamble unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultiSKUPriceAndStockRequestServicerequestRequestpreamble:
        """Test MultiSKUPriceAndStockRequestServicerequestRequestpreamble
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultiSKUPriceAndStockRequestServicerequestRequestpreamble`
        """
        model = MultiSKUPriceAndStockRequestServicerequestRequestpreamble()
        if include_optional:
            return MultiSKUPriceAndStockRequestServicerequestRequestpreamble(
                isocountrycode = 'US',
                customernumber = '20-222222'
            )
        else:
            return MultiSKUPriceAndStockRequestServicerequestRequestpreamble(
                isocountrycode = 'US',
                customernumber = '20-222222',
        )
        """

    def testMultiSKUPriceAndStockRequestServicerequestRequestpreamble(self):
        """Test MultiSKUPriceAndStockRequestServicerequestRequestpreamble"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
