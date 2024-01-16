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

from xi.sdk.resellers.python.models.invoice_detailsv61_response_summary_misc_charges_inner import InvoiceDetailsv61ResponseSummaryMiscChargesInner

class TestInvoiceDetailsv61ResponseSummaryMiscChargesInner(unittest.TestCase):
    """InvoiceDetailsv61ResponseSummaryMiscChargesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61ResponseSummaryMiscChargesInner:
        """Test InvoiceDetailsv61ResponseSummaryMiscChargesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61ResponseSummaryMiscChargesInner`
        """
        model = InvoiceDetailsv61ResponseSummaryMiscChargesInner()
        if include_optional:
            return InvoiceDetailsv61ResponseSummaryMiscChargesInner(
                charge_description = '',
                misc_charge_line_count = 56,
                misc_charge_line_total = 1.337,
                charge_line_reference = '',
                is_non_misc = ''
            )
        else:
            return InvoiceDetailsv61ResponseSummaryMiscChargesInner(
        )
        """

    def testInvoiceDetailsv61ResponseSummaryMiscChargesInner(self):
        """Test InvoiceDetailsv61ResponseSummaryMiscChargesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
