# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.validate_quote_response_lines_inner_vmf_additional_attributes_lines_inner import ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner

class TestValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner(unittest.TestCase):
    """ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner:
        """Test ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner`
        """
        model = ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner()
        if include_optional:
            return ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner(
                attribute_name = '',
                attribute_value = '',
                attribute_description = ''
            )
        else:
            return ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner(
        )
        """

    def testValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner(self):
        """Test ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
