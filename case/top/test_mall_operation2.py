#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : ${DATE} ${TIME}
# @Author : cuiguoen
# @File : ${NAME}.py


import pytest
from pages.top.mall_operation2 import SKU_TPU2


class TestSKU_TPU2:
    # 商城运营菜单下的


    @pytest.mark.p0
    def test_metaData(self, topLogin):
        # MetaData菜单
        page = SKU_TPU2(topLogin)
        text_assert = page.metaData()
        assert text_assert == "服务类型"



    @pytest.mark.p0
    def test_solution_disposition(self, topLogin):
        # 商城Solution配置的菜单
        page = SKU_TPU2(topLogin)
        text_assert2 = page.solution_disposition()

    @pytest.mark.p0
    def test_calendar_disposition(self, topLogin):
        # 营销日历配置的菜单
        page = SKU_TPU2(topLogin)
        text_assert3 = page.calendar_disposition()



