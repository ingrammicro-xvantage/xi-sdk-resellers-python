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

from xi.sdk.resellers.python.models.product_search_response_serviceresponse_productsearchresponse_inner import ProductSearchResponseServiceresponseProductsearchresponseInner

class TestProductSearchResponseServiceresponseProductsearchresponseInner(unittest.TestCase):
    """ProductSearchResponseServiceresponseProductsearchresponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductSearchResponseServiceresponseProductsearchresponseInner:
        """Test ProductSearchResponseServiceresponseProductsearchresponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductSearchResponseServiceresponseProductsearchresponseInner`
        """
        model = ProductSearchResponseServiceresponseProductsearchresponseInner()
        if include_optional:
            return ProductSearchResponseServiceresponseProductsearchresponseInner(
                responseflag = '',
                partnumbers = [
                    xi.sdk.resellers.python.models.product_search_response_serviceresponse_productsearchresponse_inner_partnumbers_inner.productSearchResponse_serviceresponse_productsearchresponse_inner_partnumbers_inner(
                        ingrampartnumber = '', 
                        manufacturerpartnumber = '', 
                        upccode = '', 
                        productdescription = '', 
                        currency = '', 
                        haswarranty = '', )
                    ]
            )
        else:
            return ProductSearchResponseServiceresponseProductsearchresponseInner(
        )
        """

    def testProductSearchResponseServiceresponseProductsearchresponseInner(self):
        """Test ProductSearchResponseServiceresponseProductsearchresponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
