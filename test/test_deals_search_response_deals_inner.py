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

from xi.sdk.resellers.models.deals_search_response_deals_inner import DealsSearchResponseDealsInner

class TestDealsSearchResponseDealsInner(unittest.TestCase):
    """DealsSearchResponseDealsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DealsSearchResponseDealsInner:
        """Test DealsSearchResponseDealsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DealsSearchResponseDealsInner`
        """
        model = DealsSearchResponseDealsInner()
        if include_optional:
            return DealsSearchResponseDealsInner(
                deal_id = '',
                version = '',
                end_user = '',
                vendor = '',
                deal_expiry_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                links = [
                    xi.sdk.resellers.models.renewals_search_response_renewals_inner_links_inner.renewalsSearchResponse_renewals_inner_links_inner(
                        topic = '', 
                        href = '', 
                        type = '', )
                    ]
            )
        else:
            return DealsSearchResponseDealsInner(
        )
        """

    def testDealsSearchResponseDealsInner(self):
        """Test DealsSearchResponseDealsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
