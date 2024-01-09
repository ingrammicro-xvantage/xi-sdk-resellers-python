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

from xi-sdk-python.models.order_detail_response_serviceresponse import OrderDetailResponseServiceresponse

class TestOrderDetailResponseServiceresponse(unittest.TestCase):
    """OrderDetailResponseServiceresponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponseServiceresponse:
        """Test OrderDetailResponseServiceresponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponseServiceresponse`
        """
        model = OrderDetailResponseServiceresponse()
        if include_optional:
            return OrderDetailResponseServiceresponse(
                responsepreamble = xi-sdk-python.models.invoice_detail_response_serviceresponse_responsepreamble.InvoiceDetailResponse_serviceresponse_responsepreamble(
                    responsestatus = '', 
                    statuscode = '', 
                    responsemessage = '', ),
                orderdetailresponse = xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse.orderDetailResponse_serviceresponse_orderdetailresponse(
                    ordernumber = '', 
                    ordertype = '', 
                    customerordernumber = '', 
                    enduserponumber = '', 
                    orderstatus = '', 
                    entrytimestamp = '', 
                    entrymethoddescription = '', 
                    ordertotalvalue = 1.337, 
                    ordersubtotal = 1.337, 
                    freightamount = '', 
                    currencycode = '', 
                    totalweight = '', 
                    totaltax = '', 
                    billtoaddress = xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_billtoaddress.orderDetailResponse_serviceresponse_orderdetailresponse_billtoaddress(
                        suffix = '', 
                        name = '', 
                        attention = '', 
                        addressline1 = '', 
                        addressline2 = '', 
                        addressline3 = '', 
                        city = '', 
                        state = '', 
                        postalcode = '', 
                        countrycode = '', ), 
                    shiptoaddress = xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_shiptoaddress.orderDetailResponse_serviceresponse_orderdetailresponse_shiptoaddress(
                        suffix = '', 
                        attention = '', 
                        name = '', 
                        addressline1 = '', 
                        addressline2 = '', 
                        addressline3 = '', 
                        city = '', 
                        state = '', 
                        postalcode = '', 
                        countrycode = '', ), 
                    enduserinfo = xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_enduserinfo.orderDetailResponse_serviceresponse_orderdetailresponse_enduserinfo(
                        enduserid = '', ), 
                    lines = [
                        xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_lines_inner.orderDetailResponse_serviceresponse_orderdetailresponse_lines_inner(
                            linenumber = '', 
                            globallinenumber = '', 
                            ordersuffix = '', 
                            erpordernumber = '', 
                            linestatus = '', 
                            partnumber = '', 
                            manufacturerpartnumber = '', 
                            vendorname = '', 
                            vendorcode = '', 
                            partdescription1 = '', 
                            partdescription2 = '', 
                            unitweight = '', 
                            unitprice = 1.337, 
                            extendedprice = 1.337, 
                            taxamount = 1.337, 
                            requestedquantity = '', 
                            confirmedquantity = '', 
                            backorderquantity = '', 
                            serialnumberdetails = [
                                xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_lines_inner_serialnumberdetails_inner.orderDetailResponse_serviceresponse_orderdetailresponse_lines_inner_serialnumberdetails_inner(
                                    serialnumber = '', )
                                ], 
                            trackingnumber = [
                                ''
                                ], 
                            shipmentdetails = [
                                xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner.orderDetailResponse_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner(
                                    quantity = 1.337, 
                                    shipmentdate = '', 
                                    shipfromwarehouseid = '', 
                                    warehousename = '', 
                                    invoicenumber = '', 
                                    invoicedate = '', 
                                    status = '', 
                                    statusdescription = '', 
                                    shippeddate = '', 
                                    holdreasoncodedescription = '', 
                                    ponumber = '', 
                                    carriertype = '', 
                                    carriercode = '', 
                                    carriername = '', 
                                    pronumber = '', 
                                    packagedetails = xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner_packagedetails.orderDetailResponse_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner_packagedetails(
                                        packageweight = '', 
                                        cartonnumber = '', 
                                        quantityinbox = '', ), )
                                ], 
                            productextendedspecs = [
                                xi-sdk-python.models.invoice_detail_response_serviceresponse_invoicedetailresponse_extendedspecs_inner.InvoiceDetailResponse_serviceresponse_invoicedetailresponse_extendedspecs_inner(
                                    attributename = '', 
                                    attributevalue = '', )
                                ], 
                            backorderetadate = '', )
                        ], 
                    commentlines = [
                        xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_commentlines_inner.orderDetailResponse_serviceresponse_orderdetailresponse_commentlines_inner(
                            commenttext1 = '', 
                            commenttext2 = '', )
                        ], 
                    miscfeeline = [
                        xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_miscfeeline_inner.orderDetailResponse_serviceresponse_orderdetailresponse_miscfeeline_inner(
                            description = '', 
                            chargeamount = '', )
                        ], 
                    extendedspecs = [
                        xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_extendedspecs_inner.orderDetailResponse_serviceresponse_orderdetailresponse_extendedspecs_inner(
                            attributename = '', 
                            attributevalue = '', )
                        ], )
            )
        else:
            return OrderDetailResponseServiceresponse(
        )
        """

    def testOrderDetailResponseServiceresponse(self):
        """Test OrderDetailResponseServiceresponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
