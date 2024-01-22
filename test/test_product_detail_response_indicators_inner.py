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

from xi.sdk.resellers.models.product_detail_response_indicators_inner import ProductDetailResponseIndicatorsInner

class TestProductDetailResponseIndicatorsInner(unittest.TestCase):
    """ProductDetailResponseIndicatorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductDetailResponseIndicatorsInner:
        """Test ProductDetailResponseIndicatorsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductDetailResponseIndicatorsInner`
        """
        model = ProductDetailResponseIndicatorsInner()
        if include_optional:
            return ProductDetailResponseIndicatorsInner(
                has_warranty = True,
                is_new_product = True,
                has_return_limits = True,
                is_back_order_allowed = True,
                is_shipped_from_partner = True,
                is_replacement_product = True,
                is_directship = True,
                is_downloadable = True,
                is_digital_type = True,
                sku_type = '',
                has_std_special_price = True,
                has_acop_special_price = True,
                has_acop_quantity_break = True,
                has_std_web_discount = True,
                has_special_bid = True,
                is_exportable_to_country = True,
                is_discontinued_product = True,
                is_refurbished_product = True,
                is_returnable_product = True,
                is_ingram_ship = True,
                is_enduser_required = True,
                is_heavy_weight = True,
                has_ltl = True,
                is_clearance_product = True,
                has_bundle = True,
                is_oversize_product = True,
                is_preorder_product = True,
                is_license_product = True,
                is_directship_orderable = True,
                is_service_sku = True,
                is_configurable = True
            )
        else:
            return ProductDetailResponseIndicatorsInner(
        )
        """

    def testProductDetailResponseIndicatorsInner(self):
        """Test ProductDetailResponseIndicatorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
