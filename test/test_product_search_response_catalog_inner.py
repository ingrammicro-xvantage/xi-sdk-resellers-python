# coding: utf-8

"""
    Reseller API Documentation

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi.sdk.resellers.python.models.product_search_response_catalog_inner import ProductSearchResponseCatalogInner

class TestProductSearchResponseCatalogInner(unittest.TestCase):
    """ProductSearchResponseCatalogInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductSearchResponseCatalogInner:
        """Test ProductSearchResponseCatalogInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductSearchResponseCatalogInner`
        """
        model = ProductSearchResponseCatalogInner()
        if include_optional:
            return ProductSearchResponseCatalogInner(
                description = '',
                category = '',
                sub_category = '',
                product_type = '',
                ingram_part_number = '',
                vendor_part_number = '',
                upc_code = '',
                vendor_name = '',
                end_user_required = '',
                has_discounts = '',
                type = '',
                discontinued = '',
                new_product = '',
                direct_ship = '',
                has_warranty = '',
                links = [
                    xi.sdk.resellers.python.models.product_search_response_catalog_inner_links_inner.ProductSearch_Response_catalog_inner_links_inner(
                        topic = '', 
                        href = '', 
                        type = '', )
                    ],
                extra_description = '',
                replacement_sku = '',
                authorized_to_purchase = ''
            )
        else:
            return ProductSearchResponseCatalogInner(
        )
        """

    def testProductSearchResponseCatalogInner(self):
        """Test ProductSearchResponseCatalogInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
