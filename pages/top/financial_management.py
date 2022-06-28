#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 5:28 下午
# @Author : cuiguoen
# @File : financial_management.py



import pytest
from pages.basepage import BasePage

class Financial_management(BasePage):
    # 财务管理 菜单
    top_elements = [
        {
            "Financial_management": "//span[text()=\'财务管理\']",
            "Invoicing_management": "//span[text()=\'收款开票管理\']",
            "input_keyword": "//input[@placeholder=\"请输入签单名称关键词搜索\"]",
            "Invoicing_applications": "//span[text()=\'有\']",
            "Invoicing_status": "//span[text()=\'部分开票\']",
            "Payment_status": "//span[text()=\'部分收款\']",
            "Payment_method": "//span[text()=\'特赞建行868\']",
            "button_search": "//button[text() = \'查询\']",
            "application_management": "//tbody/tr[1]/td[1]/div/button[text()=\"开票申请管理(\"]",
            "application_title": "//div[text()=\'开票申请管理\']",
            "settlement_management": "//tbody/tr[1]/td[1]/div/button[text()=\"收款结算管理\"]",
            "describe1": "//p[text() = \'历史收款记录如下，如需添加收款记录请点击右侧“添加收款”\']",
            "Associate_project": "//tbody/tr[1]/td[1]/div/button[text()=\"查看关联项目\"]",
            "describe2": "//div[text()=\'关联项目\']",
        },
        {
            "Payment_management": "//span[text()=\'付款收票管理\']",
            "input_name": "//input[@placeholder=\"请输入项目名称\"]",
            "is_tickets": "//span[text()=\'无\']",
            "advance_settlement": "//span[text()=\'否\']",
            "button_search": "//button[text() = \'查询\']",
            "button_view": "//button[text() = \'查 看\']",
            "button_close": "//button[text() = \'关闭\']",
            "button_tickets": "//button[text() = \'收 票\']",
        },
        {
            "Cash_management": "//span[text()=\'提现管理\']",
            "payment_status": "//span[text()=\'已打款\']",
            "user_type": "//span[text()=\'企业创意方\']",
            "project_type": "//span[text()=\'企业项目\']",
            "button_search": "//button[text() = \'查询\']",
            "project1": "//span[text() = \'sfvs\']",
            "Contract_management": "//div[text() = \'合同管理\']",
        },
    ]



    @pytest.mark.p0
    def financial_management(self):
        # 收款开票管理 菜单
        date = self.top_elements
        self.page.click(date[0]['Financial_management'])
        self.page.click(date[0]['Invoicing_management'])
        self.page.fill(date[0]['input_keyword'],'支付宝')
        self.page.click(date[0]['Invoicing_applications'])
        self.page.click(date[0]['Invoicing_status'])
        self.page.click(date[0]['Payment_status'])
        self.page.click(date[0]['Payment_method'])
        self.page.click(date[0]['button_search'])
        self.page.click(date[0]['application_management'])
        self.page.is_visible(date[0]['application_title'])
        self.page.reload()
        self.page.fill(date[0]['input_keyword'], '预发测试3')
        self.page.click(date[0]['button_search'])
        self.page.click(date[0]['settlement_management'])
        self.page.is_visible(date[0]['describe1'])
        self.page.reload()
        self.page.fill(date[0]['input_keyword'], '预发测试3')
        self.page.click(date[0]['button_search'])
        self.page.click(date[0]['Associate_project'])
        self.page.is_visible(date[0]['describe2'])
        self.page.reload()

    @pytest.mark.p0
    def payment_management(self):
        # 付款收票管理 菜单
        date = self.top_elements
        self.page.click(date[1]['Payment_management'])
        self.page.fill(date[1]['input_name'], '测试一下看看1')
        self.page.click(date[1]['is_tickets'])
        self.page.click(date[1]['advance_settlement'])
        self.page.click(date[1]['button_search'])
        self.page.click(date[1]['button_view'])
        self.page.click(date[1]['button_close'])
        self.page.click(date[1]['button_tickets'])
        self.page.reload()

    @pytest.mark.p0
    def cash_management(self):
        # 提现管理 菜单
        date = self.top_elements
        self.page.click(date[2]['Cash_management'])
        self.page.click(date[2]['payment_status'])
        # page.click(date[2]['user_type'])
        self.page.click(date[2]['project_type'])
        self.page.click(date[2]['button_search'])
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[2]['project1'])
        new_page = new_page_info.value
        new_page.close()