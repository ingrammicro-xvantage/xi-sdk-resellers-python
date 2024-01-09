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

from xi-sdk-python.models.multi_sku_price_and_stock_response import MultiSKUPriceAndStockResponse

class TestMultiSKUPriceAndStockResponse(unittest.TestCase):
    """MultiSKUPriceAndStockResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultiSKUPriceAndStockResponse:
        """Test MultiSKUPriceAndStockResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultiSKUPriceAndStockResponse`
        """
        model = MultiSKUPriceAndStockResponse()
        if include_optional:
            return MultiSKUPriceAndStockResponse(
                serviceresponse = xi-sdk-python.models.multi_sku_price_and_stock_response_serviceresponse.multiSKUPriceAndStockResponse_serviceresponse(
                    responsepreamble = xi-sdk-python.models.price_and_availability_response_serviceresponse_responsepreamble.priceAndAvailabilityResponse_serviceresponse_responsepreamble(
                        responsestatus = '', 
                        responsemessage = '', 
                        statuscode = '', ), 
                    priceandstockresponse = xi-sdk-python.models.multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse.multiSKUPriceAndStockResponse_serviceresponse_priceandstockresponse(
                        details = [
                            xi-sdk-python.models.multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner.multiSKUPriceAndStockResponse_serviceresponse_priceandstockresponse_details_inner(
                                itemstatus = '', 
                                statusmessage = '', 
                                ingrampartnumber = '', 
                                vendorpartnumber = '', 
                                globalskuid = '', 
                                customerprice = '', 
                                partdescription1 = '', 
                                partdescription2 = '', 
                                vendornumber = '', 
                                vendorname = '', 
                                cpucode = '', 
                                class = 'A-Stocked product in all IM warehouses', 
                                skustatus = '', 
                                mediacpu = '', 
                                categorysubcategory = '', 
                                retailprice = 1.337, 
                                newmedia = '', 
                                enduserrequired = 'Y-End user data required', 
                                backorderflag = 'Y- Can be backordered', 
                                skuauthorized = '', 
                                extendedvendorpartnumber = '', 
                                warehousedetails = [
                                    xi-sdk-python.models.multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner.multiSKUPriceAndStockResponse_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner(
                                        warehouseid = '10-Mira Loma CA', 
                                        warehousedescription = '', 
                                        availablequantity = 56, 
                                        onorderquantity = 56, 
                                        onholdquantity = '', 
                                        etadate = '', )
                                    ], )
                            ], ), )
            )
        else:
            return MultiSKUPriceAndStockResponse(
        )
        """

    def testMultiSKUPriceAndStockResponse(self):
        """Test MultiSKUPriceAndStockResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
