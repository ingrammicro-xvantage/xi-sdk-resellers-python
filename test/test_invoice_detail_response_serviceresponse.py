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

from xi-sdk-resellers-python.models.invoice_detail_response_serviceresponse import InvoiceDetailResponseServiceresponse

class TestInvoiceDetailResponseServiceresponse(unittest.TestCase):
    """InvoiceDetailResponseServiceresponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailResponseServiceresponse:
        """Test InvoiceDetailResponseServiceresponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailResponseServiceresponse`
        """
        model = InvoiceDetailResponseServiceresponse()
        if include_optional:
            return InvoiceDetailResponseServiceresponse(
                responsepreamble = xi-sdk-resellers-python.models.invoice_detail_response_serviceresponse_responsepreamble.InvoiceDetailResponse_serviceresponse_responsepreamble(
                    responsestatus = '', 
                    statuscode = '', 
                    responsemessage = '', ),
                invoicedetailresponse = xi-sdk-resellers-python.models.invoice_detail_response_serviceresponse_invoicedetailresponse.invoiceDetailResponse_serviceresponse_invoicedetailresponse(
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
                    creditmemoreasoncode = '', )
            )
        else:
            return InvoiceDetailResponseServiceresponse(
        )
        """

    def testInvoiceDetailResponseServiceresponse(self):
        """Test InvoiceDetailResponseServiceresponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
