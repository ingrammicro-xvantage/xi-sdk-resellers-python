# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner_vmf_additional_attributes_lines_inner import AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner

class TestAsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner(unittest.TestCase):
    """AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner:
        """Test AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner`
        """
        model = AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner()
        if include_optional:
            return AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner(
                attribute_name = '',
                attribute_value = ''
            )
        else:
            return AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner(
        )
        """

    def testAsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner(self):
        """Test AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()