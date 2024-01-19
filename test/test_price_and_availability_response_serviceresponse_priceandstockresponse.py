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

from xi.sdk.resellers.models.price_and_availability_response_serviceresponse_priceandstockresponse import PriceAndAvailabilityResponseServiceresponsePriceandstockresponse

class TestPriceAndAvailabilityResponseServiceresponsePriceandstockresponse(unittest.TestCase):
    """PriceAndAvailabilityResponseServiceresponsePriceandstockresponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityResponseServiceresponsePriceandstockresponse:
        """Test PriceAndAvailabilityResponseServiceresponsePriceandstockresponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityResponseServiceresponsePriceandstockresponse`
        """
        model = PriceAndAvailabilityResponseServiceresponsePriceandstockresponse()
        if include_optional:
            return PriceAndAvailabilityResponseServiceresponsePriceandstockresponse(
                details = [
                    xi.sdk.resellers.models.price_and_availability_response_serviceresponse_priceandstockresponse_details_inner.priceAndAvailabilityResponse_serviceresponse_priceandstockresponse_details_inner(
                        itemstatus = 'SUCCESS', 
                        statusmessage = '', 
                        ingrampartnumber = '', 
                        vendorpartnumber = '', 
                        globalskuid = '', 
                        customerprice = 1.337, 
                        partdescription1 = '', 
                        partdescription2 = '', 
                        vendornumber = '', 
                        vendorname = '', 
                        cpucode = '', 
                        class = 'A', 
                        skustatus = 'ACTIVE', 
                        mediacpu = '', 
                        categorysubcategory = '', 
                        retailprice = 1.337, 
                        newmedia = '', 
                        enduserrequired = 'Y', 
                        backorderflag = 'Y', 
                        skuauthorized = '', 
                        extendedvendorpartnumber = '', 
                        warehousedetails = [
                            xi.sdk.resellers.models.price_and_availability/warehouse_list_type/response.priceAndAvailability.warehouseListType.Response(
                                warehouseid = '', 
                                warehousedescription = '', 
                                availablequantity = 56, 
                                onorderquantity = 56, 
                                onholdquantity = 56, 
                                etadate = '', )
                            ], )
                    ]
            )
        else:
            return PriceAndAvailabilityResponseServiceresponsePriceandstockresponse(
        )
        """

    def testPriceAndAvailabilityResponseServiceresponsePriceandstockresponse(self):
        """Test PriceAndAvailabilityResponseServiceresponsePriceandstockresponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
