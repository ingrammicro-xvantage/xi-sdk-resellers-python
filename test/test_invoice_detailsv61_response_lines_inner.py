# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.invoice_detailsv61_response_lines_inner import InvoiceDetailsv61ResponseLinesInner

class TestInvoiceDetailsv61ResponseLinesInner(unittest.TestCase):
    """InvoiceDetailsv61ResponseLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61ResponseLinesInner:
        """Test InvoiceDetailsv61ResponseLinesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61ResponseLinesInner`
        """
        model = InvoiceDetailsv61ResponseLinesInner()
        if include_optional:
            return InvoiceDetailsv61ResponseLinesInner(
                ingram_line_number = '',
                customer_line_number = '0',
                ingram_part_number = '',
                upc = '',
                vendor_part_number = '',
                customer_part_number = '',
                vendor_name = '',
                product_description = '',
                unit_weight = 1.337,
                quantity = 56,
                unit_price = 1.337,
                unit_of_measure = '',
                currency_code = '',
                extended_price = 1.337,
                tax_percentage = 1.337,
                tax_rate = 1.337,
                tax_amount = 1.337,
                serial_numbers = [
                    xi.sdk.resellers.models.invoice_detailsv6_1_response_lines_inner_serial_numbers_inner.InvoiceDetailsv6_1Response_lines_inner_serialNumbers_inner(
                        serial_number = '', )
                    ],
                quantity_ordered = 56,
                quantity_shipped = 56
            )
        else:
            return InvoiceDetailsv61ResponseLinesInner(
        )
        """

    def testInvoiceDetailsv61ResponseLinesInner(self):
        """Test InvoiceDetailsv61ResponseLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
