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

from xi-sdk-resellers-python.models.invoice_search_response_invoices_inner import InvoiceSearchResponseInvoicesInner

class TestInvoiceSearchResponseInvoicesInner(unittest.TestCase):
    """InvoiceSearchResponseInvoicesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceSearchResponseInvoicesInner:
        """Test InvoiceSearchResponseInvoicesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceSearchResponseInvoicesInner`
        """
        model = InvoiceSearchResponseInvoicesInner()
        if include_optional:
            return InvoiceSearchResponseInvoicesInner(
                payment_terms_due_date = '',
                erp_order_number = '',
                invoice_number = '',
                invoice_status = '',
                invoice_date = '',
                invoice_due_date = '',
                invoiced_amount_due = '',
                customer_order_number = '',
                order_create_date = '',
                end_customer_order_number = '',
                invoice_amount_incl_tax = ''
            )
        else:
            return InvoiceSearchResponseInvoicesInner(
        )
        """

    def testInvoiceSearchResponseInvoicesInner(self):
        """Test InvoiceSearchResponseInvoicesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
