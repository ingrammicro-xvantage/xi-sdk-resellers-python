# coding: utf-8

"""
    Reseller API Documentation - United States

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi-sdk-python.models.multi_sku_price_and_stock_request_servicerequest import MultiSKUPriceAndStockRequestServicerequest

class TestMultiSKUPriceAndStockRequestServicerequest(unittest.TestCase):
    """MultiSKUPriceAndStockRequestServicerequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultiSKUPriceAndStockRequestServicerequest:
        """Test MultiSKUPriceAndStockRequestServicerequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultiSKUPriceAndStockRequestServicerequest`
        """
        model = MultiSKUPriceAndStockRequestServicerequest()
        if include_optional:
            return MultiSKUPriceAndStockRequestServicerequest(
                requestpreamble = xi-sdk-python.models.multi_sku_price_and_stock_request_servicerequest_requestpreamble.multiSKUPriceAndStockRequest_servicerequest_requestpreamble(
                    isocountrycode = 'US', 
                    customernumber = '20-222222', ),
                priceandstockrequest = xi-sdk-python.models.multi_sku_price_and_stock_request_servicerequest_priceandstockrequest.multiSKUPriceAndStockRequest_servicerequest_priceandstockrequest(
                    showwarehouseavailability = '', 
                    extravailabilityflag = '', 
                    includeallsystems = True, 
                    item = xi-sdk-python.models.multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item.multiSKUPriceAndStockRequest_servicerequest_priceandstockrequest_item(
                        index = 56, 
                        ingrampartnumber = '', 
                        vendorpartnumber = '', 
                        upc = '', 
                        customerpartnumber = '', 
                        warehouseidlist = '', ), )
            )
        else:
            return MultiSKUPriceAndStockRequestServicerequest(
        )
        """

    def testMultiSKUPriceAndStockRequestServicerequest(self):
        """Test MultiSKUPriceAndStockRequestServicerequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
