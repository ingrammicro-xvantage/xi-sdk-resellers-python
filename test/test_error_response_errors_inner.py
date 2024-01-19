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

from xi.sdk.resellers.models.error_response_errors_inner import ErrorResponseErrorsInner

class TestErrorResponseErrorsInner(unittest.TestCase):
    """ErrorResponseErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponseErrorsInner:
        """Test ErrorResponseErrorsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponseErrorsInner`
        """
        model = ErrorResponseErrorsInner()
        if include_optional:
            return ErrorResponseErrorsInner(
                id = '',
                type = '',
                message = '',
                fields = [
                    xi.sdk.resellers.models.error_response_errors_inner_fields_inner.ErrorResponse_errors_inner_fields_inner(
                        field = '', 
                        value = '', 
                        message = '', )
                    ]
            )
        else:
            return ErrorResponseErrorsInner(
        )
        """

    def testErrorResponseErrorsInner(self):
        """Test ErrorResponseErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
