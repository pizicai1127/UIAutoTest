#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_financial_management.py

import pytest
from pages.top.financial_management import Financial_management

class TestFinancial_management:
    # 财务管理 菜单

    @pytest.mark.p0
    def test_financial_management(self, topLogin):
        # 收款开票管理 菜单
        page = Financial_management(topLogin)
        text_assert = page.financial_management()


    @pytest.mark.p0
    def test_payment_management(self, topLogin):
        # 付款收票管理 菜单
        page = Financial_management(topLogin)
        text_assert2 = page.payment_management()

    @pytest.mark.p0
    def test_cash_management(self, topLogin):
        # 提现管理 菜单
        page = Financial_management(topLogin)
        text_assert3 = page.cash_management()
