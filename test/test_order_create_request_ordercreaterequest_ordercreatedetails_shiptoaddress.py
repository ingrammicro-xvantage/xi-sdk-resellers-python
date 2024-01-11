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

from xi-sdk-resellers-python.models.order_create_request_ordercreaterequest_ordercreatedetails_shiptoaddress import OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress

class TestOrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress(unittest.TestCase):
    """OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress:
        """Test OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress`
        """
        model = OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress()
        if include_optional:
            return OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress(
                attention = '“Mr. Customer”',
                addressline1 = '“Ingram Micro”',
                addressline2 = '3351 Michelson Dr',
                addressline3 = 'Ste 100 or ship to phone number',
                city = 'Irvine',
                state = 'CA',
                postalcode = '92712',
                countrycode = 'US'
            )
        else:
            return OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress(
                addressline1 = '“Ingram Micro”',
                addressline2 = '3351 Michelson Dr',
                city = 'Irvine',
                state = 'CA',
                postalcode = '92712',
        )
        """

    def testOrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress(self):
        """Test OrderCreateRequestOrdercreaterequestOrdercreatedetailsShiptoaddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()