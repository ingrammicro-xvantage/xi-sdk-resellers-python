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

from xi.sdk.resellers.models.invoice_search_response import InvoiceSearchResponse

class TestInvoiceSearchResponse(unittest.TestCase):
    """InvoiceSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceSearchResponse:
        """Test InvoiceSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceSearchResponse`
        """
        model = InvoiceSearchResponse()
        if include_optional:
            return InvoiceSearchResponse(
                records_found = 56,
                page_size = 56,
                page_number = 56,
                invoices = [
                    xi.sdk.resellers.models.invoice_search_response_invoices_inner.InvoiceSearchResponse_invoices_inner(
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
                        invoice_amount_incl_tax = '', )
                    ],
                next_page = ''
            )
        else:
            return InvoiceSearchResponse(
        )
        """

    def testInvoiceSearchResponse(self):
        """Test InvoiceSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
