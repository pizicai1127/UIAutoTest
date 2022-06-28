#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/6/9 10:58 上午
# @File : test_signature.py
import pytest

from pages.topmanage.SignaturePage import SignaturePage


class TestSignature:
    shuju = [{
        "input_name": "测试",
        "input_name_btn": "测试销售机会25",
        "requirements_description": "销售机会描述",
        "input_estimate_price": "10",
        "input_cost": "1",
        "proposal": "提案",
        "proposal_btn": "最终提案",
        'input_sale_name': "测试",
        'sale_amount_of_money': "100",

    }]

    # 签单搜索
    @pytest.mark.parametrize("data", shuju)
    def test_signature_search(self, top_login, data):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/home")
        page.signature_search(data["input_name"])

    # 点击签单展开选项异常提醒
    def test_exception_reminder(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["exception_reminder_assert"]
        page.exception_reminder()
        assert page._text_content(selector) == '共1454个签单业务总额：154,374,115.60签单总额：154,374,115.60'

    # 点击签单展开选项关联项目状态
    def test_associated_item_status(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["associated_item_not_associated_assert"]
        page.associated_item_status()
        assert page._text_content(selector) == '共2639个签单业务总额：144,433,226.42签单总额：127,983,435.42'

    # 点击签单展开选项签单凭证审核
    def test_signing_voucher_approval(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["signing_voucher_approval_assert"]
        page.signing_voucher_approval()
        assert page._text_content(selector) == '共4278个签单业务总额：336,380,244.38签单总额：319,930,453.38'

    # 点击签单展开选项，交付状态
    def test_delivery_status(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["delivery_status_assert"]
        page.delivery_status()
        assert page._text_content(selector) == '共197个签单业务总额：29,668,534.24签单总额：29,608,534.24'

    # 点击签单展开选项，开票状态
    def test_invoicing_status(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["invoicing_status_assert"]
        page.invoicing_status()
        assert page._text_content(selector) == '共2944个签单业务总额：195,551,850.30签单总额：179,122,059.30'

    # 点击签单展开选项，创意方结款状态
    def test_payment_status(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["payment_status_assert"]
        page.payment_status()
        assert page._text_content(selector) == '共3047个签单业务总额：193,746,530.26签单总额：177,296,739.26'

    # 点击签单展开选项，收款状态
    def test_collection_status(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["collection_status_assert"]
        page.collection_status()
        assert page._text_content(selector) == '共2998个签单业务总额：193,183,291.66签单总额：176,733,500.66'

    # 点击签单展开选项，关联案例
    def test_related_cases(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["related_cases_assert"]
        page.related_cases()
        assert page._text_content(selector) == '共425个签单业务总额：73,812,172.95签单总额：73,803,932.95'

    # 点击签单展开选项，校准状态
    def test_calibration_status(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["calibration_status_assert"]
        page.calibration_status()
        assert page._text_content(selector) == '共4277个签单业务总额：336,367,524.38签单总额：319,917,733.38'

    # 点击签单展开选项，收入金额变更时间
    def test_change_time_of_revenue_amount(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["change_time_of_revenue_amount_assert"]
        page.change_time_of_revenue_amount()
        # assert page._text_content(selector) == '共1个签单业务总额：12,000.00签单总额：12,000.00'

    # 点击来源搜索
    def test_source(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["source_assert"]
        page.source()
        assert page._text_content(selector) == '共113个签单业务总额：14,204,025.39签单总额：14,204,025.39'

    # 点击客户、部门搜索
    def test_customer_department(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["customer_department_assert"]
        page.customer_department()
        assert page._text_content(selector) == '共1个签单业务总额：151,000.00签单总额：151,000.00'

    #   选择开票时间
    def test_invoicing_time(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["invoicing_time_assert"]
        page.invoicing_time()
        assert page._text_content(selector) == '共0个签单业务总额：0.00签单总额：0.00'

    # 签单时间
    def test_signature_time(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["change_time_of_revenue_amount_assert"]
        page.change_time_of_revenue_amount()
        # assert page._text_content(selector) == '共0个签单业务总额：0.00签单总额：0.00'

    # 签单上级客户
    def test_parent_customer(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["parent_customer_assert"]
        page.parent_customer()
        assert page._text_content(selector) == '共3个签单业务总额：1,013,721.00签单总额：1,013,721.00'

    # 搜索交付时间
    def test_delivery_time(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["change_time_of_revenue_amount_assert"]
        page.delivery_time()
        assert page._text_content(selector) == '共1个签单业务总额：12,000.00签单总额：12,000.00'

    # 搜索业务类型
    def test_business_type(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["business_type_assert"]
        page.business_type()
        assert page._text_content(selector) == '共1个签单业务总额：100.00签单总额：100.00'

    #  搜索销售人员
    def test_salesman(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        selector = SignaturePage.selectors["business_type_assert"]
        page._wait(0.5)
        page.salesman()
        assert page._text_content(selector) == '共6个签单业务总额：1,038,541.00签单总额：1,038,541.00'

    #  签单列表，操作
    def test_operation(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        page.operation()

    # 点击签单进入详情页面
    def test_signature_detail(self, top_login):
        page = SignaturePage(top_login)
        page.goto("https://top.tezign.com/#/app/businessDetail")
        page.signature_detail()
