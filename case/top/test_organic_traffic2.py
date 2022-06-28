#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_organic_traffic2.py


import pytest
from pages.top.organic_traffic2 import Organic2

class TestOrganic2:
    # 自然流量菜单下的后半部分

    @pytest.mark.p0
    def test_benefit_view(self, topLogin):
        # 权益查看 菜单
        page = Organic2(topLogin)
        text_assert = page.benefit_view()

    @pytest.mark.p0
    def test_bapproval_rate(self, topLogin):
         # 项目审核通过率 菜单
         page = Organic2(topLogin)
         text_assert2 = page.bapproval_rate()

    @pytest.mark.p0
    def test_success_rate(self, topLogin):
         # 项目对接成功率 菜单
         page = Organic2(topLogin)
         text_assert = page.success_rate()

    @pytest.mark.p0
    def test_fund_custody(self, topLogin):
        # 资金托管统计 菜单
        page = Organic2(topLogin)
        text_assert = page.fund_custody()

    @pytest.mark.p0
    def test_custody_rate(self, topLogin):
        # 资金托管率 菜单
        page = Organic2(topLogin)
        text_assert = page.custody_rate()

    @pytest.mark.p0
    def test_customer_personal(self, topLogin):
        # 客户个人实名认证 菜单

        page = Organic2(topLogin)
        text_assert = page.customer_personal()

    @pytest.mark.p0
    def test_customer_company(self, topLogin):
        # 客户公司实名认证 菜单
        page = Organic2(topLogin)
        text_assert = page.customer_company()

    @pytest.mark.p0
    def test_sensitive_word(self, topLogin):
        # 敏感词屏蔽 菜单
        page = Organic2(topLogin)
        text_assert = page.sensitive_word()