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

from xi-sdk-resellers-python.models.product_search_request_servicerequest import ProductSearchRequestServicerequest

class TestProductSearchRequestServicerequest(unittest.TestCase):
    """ProductSearchRequestServicerequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductSearchRequestServicerequest:
        """Test ProductSearchRequestServicerequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductSearchRequestServicerequest`
        """
        model = ProductSearchRequestServicerequest()
        if include_optional:
            return ProductSearchRequestServicerequest(
                requestpreamble = xi-sdk-resellers-python.models.product_search_request_servicerequest_requestpreamble.productSearchRequest_servicerequest_requestpreamble(
                    isocountrycode = '', 
                    customernumber = '', 
                    vendornumber = '', ),
                productsearchrequest = xi-sdk-resellers-python.models.product_search_request_servicerequest_productsearchrequest.productSearchRequest_servicerequest_productsearchrequest(
                    searchcriteria = xi-sdk-resellers-python.models.product_search_request_servicerequest_productsearchrequest_searchcriteria.productSearchRequest_servicerequest_productsearchrequest_searchcriteria(
                        vendor = '', 
                        vendorpartnumber = 'WKB-1500GB', 
                        partdescription = 'WRLS ERGO KEYBOARD & MOUSE', 
                        upc = '783750005524', 
                        customerpartnumber = '', ), )
            )
        else:
            return ProductSearchRequestServicerequest(
        )
        """

    def testProductSearchRequestServicerequest(self):
        """Test ProductSearchRequestServicerequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
