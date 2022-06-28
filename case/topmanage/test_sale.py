#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/6/9 6:47 下午
# @File : test_sale.py
import allure
import pytest

from pages.topmanage.SalePage import SalePage


class TestSale:
    shuju = [{
        "select_company_name": "阿里公司",
        "input_name_btn": "测试销售机会25",
        "requirements_description": "销售机会描述",
        "input_estimate_price": "10",
        "input_cost": "1",
        "proposal": "提案",
        "proposal_btn": "最终提案",
        'input_sale_name': "测试",
        'sale_amount_of_money': "100",
        "explain": "输入备注",
        'lose_describe': "输单描述输单描述",

    }]

    # 搜索关联报价单
    def test_relate_quotation(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/mypanel")
        selector = SalePage.selectors["select_business_department_search_result_assert"]
        page.relate_quotation()
        # assert page._text_content(selector) == '共 4 个 进行中 销售机会 | 销售机会总额（元）：2,423.00详'
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 搜索关联的SKU
    def test_relate_sku(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        selector = SalePage.selectors["select_business_department_search_result_assert"]
        page.relate_sku()
        # assert page._text_content(selector) == '共 1 个 进行中 销售机会 | 销售机会总额（元）：100.00详'
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 销售机会搜索
    def test_crm_sale_search(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_sale_search()

    # 销售金额搜索
    @pytest.mark.parametrize("data", shuju)
    def test_sale_amount_of_money(self, top_login, data):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.sale_amount_of_money(data["sale_amount_of_money"])

    # 销售机会名称搜索
    @pytest.mark.parametrize("data", shuju)
    def test_select_sale(self, top_login, data):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        # page._wait(1)
        page.select_sale(data["input_sale_name"])

    # 查看pipeline视图
    def test_pipeline(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/")
        page.pipeline()

    # 查看pipeline填写规则
    def test_filling_rules(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.filling_rules()

    # 搜索客户部门
    def test_department(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.department()

    # 搜索客户部门
    def test_my_department(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        selector = SalePage.selectors["select_business_department_search_result_assert"]
        page.my_department()
        assert page._text_content(selector) == '共 0 个 进行中 销售机会 | 销售机会总额（元）：0.00详'
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 搜索销售阶段
    def test_sales_phase(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        selector = SalePage.selectors["select_business_department_search_result_assert"]
        page.sales_phase()
        # assert page._text_content(selector) == '共 2 个 进行中 销售机会 | 销售机会总额（元）：2,100.00详'
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 搜索是否pending
    def test_pending(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        selector = SalePage.selectors["select_business_department_search_result_assert"]
        page.pending()
        # assert page._text_content(selector) == '共 17 个 进行中 销售机会 | 销售机会总额（元）：1,297,654.00详'
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 搜索创建时间
    def test_start_time(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        selector = SalePage.selectors["select_business_department_search_result_assert"]
        page.start_time()
        # assert page._text_content(selector) == '共 0 个 进行中 销售机会 | 销售机会总额（元）：0.00详'
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    def test_approval(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.approval()

    # 搜索预估交付时间
    def test_delivery_time(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        selector = SalePage.selectors["select_business_department_search_result_assert"]
        page.delivery_time()
        assert page._text_content(selector) == '共 0 个 进行中 销售机会 | 销售机会总额（元）：0.00详'
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 取消创建销售机会
    def test_crm_cancel(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_cancel()

    # 创建销售机会
    @pytest.mark.parametrize("data", shuju)
    def test_crm_create(self, top_login, data):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_create(data["select_company_name"], data["input_name_btn"], data["requirements_description"],
                        data['input_estimate_price'], data["input_cost"])

    # 在销售机会详情页面，发布记录
    @pytest.mark.parametrize("data", shuju)
    def test_fast_record(self, top_login, data):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        selector = SalePage.selectors["publish_success_assert"]
        page.fast_record(data["explain"])

    # 在销售机会详情页面，点击销售建议
    def test_sales_advice(self, top_login,):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        # selector = SalePage.selectors["associated_quotation_btn_assert"]
        page.sales_advice()
        # assert page._get_attribute(SalePage.selectors["associated_quotation_btn_assert"], "value") == "创建/关联报价单"

    # 在销售机会详情页面，点击知识库
    def test_knowledge_base(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.knowledge_base()

    # 在销售机会详情页面，点击基本资料，记录信息，团队成员
    def test_sale_detail_record(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.sale_detail_record()
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 在销售机会详情页面，点击记录信息
    def test_message_record(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.message_record()
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 在销售机会详情页面，点击团队成员
    def test_team(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.team()
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 在销售机会详情页面，点击基本资料
    def test_basic_information(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.basic_information()
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 在销售机会详情页面，点击基本资料各个编辑按钮
    def test_basic_information_detail(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.basic_information_detail()
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 在销售机会详情页面，点击pipeline填写规则
    def test_pipeline_filling_rules(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.pipeline_filling_rules()

    # 取消绑定的brief
    def test_crm_brief(self, top_login, ):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_brief()

    # 编辑销售机会
    @pytest.mark.parametrize("data", shuju)
    def test_crm_edit_brief(self, top_login, data):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_edit_brief(data["proposal"], data["proposal_btn"])

    # 解绑报价单
    def test_crm_edit_quotation(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_edit_quotation()

    # 删除销售机会
    def test_crm_edit_operation(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_edit_operation()

    # 创建销售机会，然后输单
    @pytest.mark.parametrize("data", shuju)
    def test_crm_create_lose(self, top_login, data):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_create(data["select_company_name"], data["input_name_btn"], data["requirements_description"],
                        data['input_estimate_price'], data["input_cost"])
        page.crm_create_lose(data['lose_describe'])
        page.goto("https://top.tezign.com/#/app/salesOpportunity")

    # 删除输单的销售机会
    def test_delete_lose(self, top_login):
        page = SalePage(top_login)
        page.goto("https://top.tezign.com/#/app/salesOpportunity")
        page.crm_edit_operation()