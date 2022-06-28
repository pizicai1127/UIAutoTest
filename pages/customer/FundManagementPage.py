#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/25 2:10 下午
# @File : FundManagementPage.py
from pages.customer.CustomerBasePage import CustomerBasePage


class FundManagementPage(CustomerBasePage):
    selectors = {
        "project_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div > div.wallet-head > "
                       "div.info.info-project > a",
        "back_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div > div.remain-head > "
                    "div.operation",
        "withdrawal_record_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div > div.wallet-body "
                                 "> div.wallet-tab > div:nth-child(2) > a",
        "transaction_record_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div > "
                                  "div.wallet-body > div.wallet-tab > div:nth-child(1) > a",
        "fund_management_btn":"#rc-root > div.default-layout > div.navbar-wrapper > div.navbar > div.bar-body > "
                              "div.bar-menu > div:nth-child(4) > div.item-icon",
    }

    def fund_management(self):
        self.page.click(FundManagementPage.selectors['fund_management_btn'])
        self.page.click(FundManagementPage.selectors['withdrawal_record_btn'])
        self.page.click(FundManagementPage.selectors['transaction_record_btn'])
        self.page.click(FundManagementPage.selectors['project_btn'])
        self.page.click(FundManagementPage.selectors['back_btn'])