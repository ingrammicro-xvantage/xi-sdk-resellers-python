# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.get_accesstoken400_response import GetAccesstoken400Response

class TestGetAccesstoken400Response(unittest.TestCase):
    """GetAccesstoken400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccesstoken400Response:
        """Test GetAccesstoken400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccesstoken400Response`
        """
        model = GetAccesstoken400Response()
        if include_optional:
            return GetAccesstoken400Response(
                message = ''
            )
        else:
            return GetAccesstoken400Response(
        )
        """

    def testGetAccesstoken400Response(self):
        """Test GetAccesstoken400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
