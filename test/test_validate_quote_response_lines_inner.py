# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.validate_quote_response_lines_inner import ValidateQuoteResponseLinesInner

class TestValidateQuoteResponseLinesInner(unittest.TestCase):
    """ValidateQuoteResponseLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateQuoteResponseLinesInner:
        """Test ValidateQuoteResponseLinesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateQuoteResponseLinesInner`
        """
        model = ValidateQuoteResponseLinesInner()
        if include_optional:
            return ValidateQuoteResponseLinesInner(
                customer_line_number = '11',
                ingram_part_number = 'YN6551',
                quantity = 1,
                vmf_additional_attributes_lines = [
                    xi.sdk.resellers.models.validate_quote_response_lines_inner_vmf_additional_attributes_lines_inner.ValidateQuoteResponse_lines_inner_vmfAdditionalAttributesLines_inner(
                        attribute_name = '', 
                        attribute_value = '', 
                        attribute_description = '', )
                    ]
            )
        else:
            return ValidateQuoteResponseLinesInner(
        )
        """

    def testValidateQuoteResponseLinesInner(self):
        """Test ValidateQuoteResponseLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
