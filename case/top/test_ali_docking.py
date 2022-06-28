#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_ali_docking.py


import pytest
from pages.top.ali_docking import Alidocking

class TestAlidocking:

    @pytest.mark.p0
    def test_demand_orders(self, topLogin):
        # 需求订单 菜单
        page = Alidocking(topLogin)
        text_assert = page.demand_orders()
        assert text_assert == "需求名称"


    @pytest.mark.p0
    def test_set_configuration(self, topLogin):
        # 套餐配置 菜单
        page = Alidocking(topLogin)
        text_assert2 = page.set_configuration()


    @pytest.mark.p0
    def test_category_configuration(self, topLogin):
        # 品类配置 菜单
        page = Alidocking(topLogin)
        text_assert3 = page.category_configuration()
        assert text_assert3 == "编辑品类 ryna测试"