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

from xi.sdk.resellers.python.models.invoice_detail_response_serviceresponse_invoicedetailresponse import InvoiceDetailResponseServiceresponseInvoicedetailresponse

class TestInvoiceDetailResponseServiceresponseInvoicedetailresponse(unittest.TestCase):
    """InvoiceDetailResponseServiceresponseInvoicedetailresponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailResponseServiceresponseInvoicedetailresponse:
        """Test InvoiceDetailResponseServiceresponseInvoicedetailresponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailResponseServiceresponseInvoicedetailresponse`
        """
        model = InvoiceDetailResponseServiceresponseInvoicedetailresponse()
        if include_optional:
            return InvoiceDetailResponseServiceresponseInvoicedetailresponse(
                customernumber = '',
                invoicenumber = '',
                invoicedate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                invoicetype = '',
                customerordernumber = '',
                customerfreightamount = 1.337,
                customerforeignfrightamt = 1.337,
                totaltaxamount = 1.337,
                totalamount = 1.337,
                shiptosuffix = '',
                billtosuffix = '',
                freightamount = 1.337,
                paymentterms = '',
                orderdate = '',
                carrier = '',
                carrierdescription = '',
                discountamount = 1.337,
                taxtype = '',
                enduserponumber = '',
                freightforwardercode = '',
                creditmemoreasoncode = ''
            )
        else:
            return InvoiceDetailResponseServiceresponseInvoicedetailresponse(
        )
        """

    def testInvoiceDetailResponseServiceresponseInvoicedetailresponse(self):
        """Test InvoiceDetailResponseServiceresponseInvoicedetailresponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
