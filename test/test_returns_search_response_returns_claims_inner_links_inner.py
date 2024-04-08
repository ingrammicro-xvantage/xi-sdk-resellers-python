# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.returns_search_response_returns_claims_inner_links_inner import ReturnsSearchResponseReturnsClaimsInnerLinksInner

class TestReturnsSearchResponseReturnsClaimsInnerLinksInner(unittest.TestCase):
    """ReturnsSearchResponseReturnsClaimsInnerLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnsSearchResponseReturnsClaimsInnerLinksInner:
        """Test ReturnsSearchResponseReturnsClaimsInnerLinksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnsSearchResponseReturnsClaimsInnerLinksInner`
        """
        model = ReturnsSearchResponseReturnsClaimsInnerLinksInner()
        if include_optional:
            return ReturnsSearchResponseReturnsClaimsInnerLinksInner(
                topic = '',
                href = '',
                type = ''
            )
        else:
            return ReturnsSearchResponseReturnsClaimsInnerLinksInner(
        )
        """

    def testReturnsSearchResponseReturnsClaimsInnerLinksInner(self):
        """Test ReturnsSearchResponseReturnsClaimsInnerLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
