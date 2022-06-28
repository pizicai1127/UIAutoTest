#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/14 11:39 上午
# @Author : cuiguoen
# @File : organic_traffic2.py.py

import pytest
from pages.basepage import BasePage

class Organic2(BasePage):
    # 自然流量菜单下的后半部分
    top_elements = [
        {
            "Organic_traffic": "//span[text()=\'自然流量\']",
            "Benefit_view": "//span[text()=\'权益查看\']",
            "input_name": "//input[@placeholder=\"请输入权益名称\"]",
            "select_associate": "//div[text()=\'请输入关联项目\']",
            "select1": "//li[text()=\"99元\"]",
            "button_inquire": "//button[text() = \'查询\']",
        },
        {
            "approval_rate": "//span[text()=\'项目审核通过率\']",
            "month": "//span[text()=\'月\']",
            "title": "//h1[text() = \'项目审核通过率 - 统计\']",
        },
        {
            "success_rate": "//span[text()=\'项目对接成功率\']",
            "month": "//span[text()=\'月\']",
            "title": "//h1[text() = \'项目对接成功率- 统计\']",
        },
        {
            "Fund_custody": "//span[text()=\'资金托管统计\']",
            "month": "//span[text()=\'月\']",
            "title": "//h1[text() = \'资金托管 - 统计\']",
        },
        {
            "custody_rate": "//span[text()=\'资金托管率\']",
            "month": "//span[text()=\'月\']",
            "title": "//h1[text() = \'资金托管率 - 统计\']",
        },
        {
            "Customer_personal": "//span[text()=\'客户个人实名认证\']",
            "input_name": "//input[@placeholder=\"客户姓名/电话/邮箱\"]",
            "audit_successed": "//span[text()=\'已通过\']",
            "button_search": "//button[text() = \'搜索\']",
            "view_detail": "//a[text() = \'查看详情\']",
            "personal_detail": "//a[text() = \'实名认证 - 详情\']",
        },
        {
            "Customer_company": " // span[text() =\'客户公司实名认证\']",
            "input_name": "//input[@placeholder=\"客户姓名/电话/邮箱\"]",
            "audit_successed": "//span[text()=\'已通过\']",
            "button_search": "//button[text() = \'搜索\']",
            "view_detail": "//a[text() = \'查看详情\']",
            "company_detail": "//a[text() = \'实名认证 - 详情\']",
        },
        {
            "Sensitive_word": " // span[text() =\'敏感词屏蔽\']",
            "input_word": "//input[@placeholder=\"输入敏感词搜索\"]",
            "button_inquire": "//button[text() = \'查询\']",
            "edit": "//span[text()=\'编辑\']",
            "button_ensure": "//button[text() = \'确 定\']",
        },
    ]



    @pytest.mark.p0
    def benefit_view(self):
        # 权益查看 菜单
        date = self.top_elements
        self.page.click(date[0]['Organic_traffic'])
        self.page.click(date[0]['Benefit_view'])
        self.page.fill(date[0]['input_name'],"99大放送")
        self.page.click(date[0]['select_associate'])
        self.page.click(date[0]['select1'])
        self.page.click(date[0]['button_inquire'])

    @pytest.mark.p0
    def bapproval_rate(self):
         # 项目审核通过率 菜单
        date = self.top_elements
        self.page.click(date[1]['approval_rate'])
        self.page.click(date[1]['month'])
        self.page.is_visible(date[1]['title'])

    @pytest.mark.p0
    def success_rate(self):
         # 项目对接成功率 菜单
        date = self.top_elements
        self.page.click(date[2]['success_rate'])
        self.page.click(date[2]['month'])
        self.page.is_visible(date[2]['title'])

    @pytest.mark.p0
    def fund_custody(self):
        # 资金托管统计 菜单
        date = self.top_elements
        self.page.click(date[3]['Fund_custody'])
        self.page.click(date[3]['month'])
        self.page.is_visible(date[3]['title'])

    @pytest.mark.p0
    def custody_rate(self):
        # 资金托管率 菜单
        date = self.top_elements
        self.page.click(date[4]['custody_rate'])
        self.page.click(date[4]['month'])
        self.page.is_visible(date[4]['title'])

    @pytest.mark.p0
    def customer_personal(self):
        # 客户个人实名认证 菜单
        date = self.top_elements
        self.page.click(date[5]['Customer_personal'])
        self.page.fill(date[5]['input_name'],"frank")
        self.page.click(date[5]['audit_successed'])
        self.page.click(date[5]['button_search'])
        self.page.click(date[5]['view_detail'])
        self.page.is_visible(date[5]['personal_detail'])

    @pytest.mark.p0
    def customer_company(self):
        # 客户公司实名认证 菜单
        date = self.top_elements
        self.page.click(date[6]['Customer_company'])
        self.page.fill(date[6]['input_name'], "M广告")
        self.page.click(date[6]['audit_successed'])
        self.page.click(date[6]['button_search'])
        self.page.click(date[6]['view_detail'])
        self.page.is_visible(date[6]['company_detail'])

    @pytest.mark.p0
    def sensitive_word(self):
        # 敏感词屏蔽 菜单
        date = self.top_elements
        self.page.click(date[7]['Sensitive_word'])
        self.page.fill(date[7]['input_word'], "线下")
        self.page.click(date[7]['button_inquire'])
        self.page.click(date[7]['edit'])
        self.page.click(date[7]['button_ensure'])
