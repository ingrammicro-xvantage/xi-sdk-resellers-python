# coding: utf-8

"""
    Reseller API Documentation - United States

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi-sdk-python.models.price_and_availability_response_inner_discounts_inner import PriceAndAvailabilityResponseInnerDiscountsInner

class TestPriceAndAvailabilityResponseInnerDiscountsInner(unittest.TestCase):
    """PriceAndAvailabilityResponseInnerDiscountsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityResponseInnerDiscountsInner:
        """Test PriceAndAvailabilityResponseInnerDiscountsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityResponseInnerDiscountsInner`
        """
        model = PriceAndAvailabilityResponseInnerDiscountsInner()
        if include_optional:
            return PriceAndAvailabilityResponseInnerDiscountsInner(
                special_pricing = [
                    xi-sdk-python.models.price_and_availability_response_inner_discounts_inner_special_pricing_inner.PriceAndAvailabilityResponse_inner_discounts_inner_specialPricing_inner(
                        discount_type = 'Special Bid, Promo Discount', 
                        special_bid_numer = '', 
                        special_pricing_discount = 1.337, 
                        special_pricing_effective_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        special_pricing_expiration_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        special_pricing_available_quantity = 56, 
                        special_pricing_min_quantity = 56, 
                        government_discount_type = '', 
                        government_discounted_customer_price = 1.337, )
                    ],
                quantity_discounts = [
                    xi-sdk-python.models.price_and_availability_response_inner_discounts_inner_quantity_discounts_inner.PriceAndAvailabilityResponse_inner_discounts_inner_quantityDiscounts_inner(
                        condition_type = 'Total fee', 
                        currency_code = '', 
                        currency_type = '', 
                        quantity = 56, 
                        amount = 1.337, )
                    ]
            )
        else:
            return PriceAndAvailabilityResponseInnerDiscountsInner(
        )
        """

    def testPriceAndAvailabilityResponseInnerDiscountsInner(self):
        """Test PriceAndAvailabilityResponseInnerDiscountsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
