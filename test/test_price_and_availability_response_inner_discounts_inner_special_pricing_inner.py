# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.price_and_availability_response_inner_discounts_inner_special_pricing_inner import PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner

class TestPriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner(unittest.TestCase):
    """PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner:
        """Test PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner`
        """
        model = PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner()
        if include_optional:
            return PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner(
                discount_type = 'Special Bid, Promo Discount',
                special_bid_numer = '',
                special_pricing_discount = 1.337,
                special_pricing_effective_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                special_pricing_expiration_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                special_pricing_available_quantity = 56,
                special_pricing_min_quantity = 56,
                government_discount_type = '',
                government_discounted_customer_price = 1.337
            )
        else:
            return PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner(
        )
        """

    def testPriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner(self):
        """Test PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
