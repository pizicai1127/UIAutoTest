#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/25 2:25 下午
# @File : test_fund_manager.py
from pages.customer.FundManagementPage import FundManagementPage


class TestFundManager:
    # 客户端资金管理
    def test_fund_manager(self, test_login_btn):
        page = FundManagementPage(test_login_btn[0])
        # page.goto("https://www.tezign.com/client/#/payment")
        page.fund_management()
