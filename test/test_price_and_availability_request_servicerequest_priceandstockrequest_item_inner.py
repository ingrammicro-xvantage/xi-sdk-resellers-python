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

from xi-sdk-resellers-python.models.price_and_availability_request_servicerequest_priceandstockrequest_item_inner import PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner

class TestPriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner(unittest.TestCase):
    """PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner:
        """Test PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner`
        """
        model = PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner()
        if include_optional:
            return PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner(
                index = 56,
                ingrampartnumber = '',
                vendorpartnumber = '',
                upc = '',
                customerpartnumber = '',
                warehouseidlist = [
                    ''
                    ],
                extendedvendorpartnumber = '',
                quantity = 1.337,
                enduserid = '',
                govtprogramtype = '',
                govtendusertype = '',
                specialbidnumber = ''
            )
        else:
            return PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner(
        )
        """

    def testPriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner(self):
        """Test PriceAndAvailabilityRequestServicerequestPriceandstockrequestItemInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
