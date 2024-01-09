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

from xi-sdk-python.models.invoice_detailsv61_response_summary_foreign_fx_totals import InvoiceDetailsv61ResponseSummaryForeignFxTotals

class TestInvoiceDetailsv61ResponseSummaryForeignFxTotals(unittest.TestCase):
    """InvoiceDetailsv61ResponseSummaryForeignFxTotals unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61ResponseSummaryForeignFxTotals:
        """Test InvoiceDetailsv61ResponseSummaryForeignFxTotals
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61ResponseSummaryForeignFxTotals`
        """
        model = InvoiceDetailsv61ResponseSummaryForeignFxTotals()
        if include_optional:
            return InvoiceDetailsv61ResponseSummaryForeignFxTotals(
                foreign_currency_code = '',
                foreign_currency_fx_rate = 1.337,
                foreign_total_taxable_amount = '',
                foreign_total_tax_amount = 1.337,
                foreign_invoice_amount_due = ''
            )
        else:
            return InvoiceDetailsv61ResponseSummaryForeignFxTotals(
        )
        """

    def testInvoiceDetailsv61ResponseSummaryForeignFxTotals(self):
        """Test InvoiceDetailsv61ResponseSummaryForeignFxTotals"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
