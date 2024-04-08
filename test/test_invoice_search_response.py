# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

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
                        invoiced_amount_due = 1.337, 
                        customer_order_number = '', 
                        end_customer_order_number = '', 
                        order_create_date = '', 
                        invoice_amount_incl_tax = 1.337, 
                        forgntotalamount = 1.337, 
                        gst_invoice_number = '', 
                        isfseccenabled = True, )
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
