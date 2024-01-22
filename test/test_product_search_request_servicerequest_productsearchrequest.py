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

from xi.sdk.resellers.models.product_search_request_servicerequest_productsearchrequest import ProductSearchRequestServicerequestProductsearchrequest

class TestProductSearchRequestServicerequestProductsearchrequest(unittest.TestCase):
    """ProductSearchRequestServicerequestProductsearchrequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductSearchRequestServicerequestProductsearchrequest:
        """Test ProductSearchRequestServicerequestProductsearchrequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductSearchRequestServicerequestProductsearchrequest`
        """
        model = ProductSearchRequestServicerequestProductsearchrequest()
        if include_optional:
            return ProductSearchRequestServicerequestProductsearchrequest(
                searchcriteria = xi.sdk.resellers.models.product_search_request_servicerequest_productsearchrequest_searchcriteria.productSearchRequest_servicerequest_productsearchrequest_searchcriteria(
                    vendor = '', 
                    vendorpartnumber = 'WKB-1500GB', 
                    partdescription = 'WRLS ERGO KEYBOARD & MOUSE', 
                    upc = '783750005524', 
                    customerpartnumber = '', )
            )
        else:
            return ProductSearchRequestServicerequestProductsearchrequest(
        )
        """

    def testProductSearchRequestServicerequestProductsearchrequest(self):
        """Test ProductSearchRequestServicerequestProductsearchrequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
