#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_CRM1.py


import pytest
from pages.top.CRM01 import CRM

class TestCRM:

    @pytest.mark.p0
    def test_sales_lead(self,topLogin):
        # 销售线索
        page = CRM(topLogin)
        text_assert1 = page.sales_lead()
        assert text_assert1 == "移入公海原因"

    @pytest.mark.p0
    def test_sales_opportunities(self, topLogin):
        # 销售机会
        page = CRM(topLogin)
        text_assert2 = page.sales_opportunities()
        assert text_assert2 == "新建销售机会"