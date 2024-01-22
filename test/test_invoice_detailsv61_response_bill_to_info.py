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

from xi.sdk.resellers.models.invoice_detailsv61_response_bill_to_info import InvoiceDetailsv61ResponseBillToInfo

class TestInvoiceDetailsv61ResponseBillToInfo(unittest.TestCase):
    """InvoiceDetailsv61ResponseBillToInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61ResponseBillToInfo:
        """Test InvoiceDetailsv61ResponseBillToInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61ResponseBillToInfo`
        """
        model = InvoiceDetailsv61ResponseBillToInfo()
        if include_optional:
            return InvoiceDetailsv61ResponseBillToInfo(
                contact = '',
                company_name = '',
                address_line1 = '',
                address_line2 = '',
                address_line3 = '',
                city = '',
                state = '',
                postal_code = '',
                country_code = '',
                phone_number = '',
                email = ''
            )
        else:
            return InvoiceDetailsv61ResponseBillToInfo(
        )
        """

    def testInvoiceDetailsv61ResponseBillToInfo(self):
        """Test InvoiceDetailsv61ResponseBillToInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
