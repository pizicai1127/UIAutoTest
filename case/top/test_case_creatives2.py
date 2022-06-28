#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_case_creatives2.py


import pytest
from pages.top.case_creatives2 import Case_search

class TestCase_search:
    # 案例搜索菜单

    @pytest.mark.p0
    def test_case_search (self, topLogin):
        # 案例搜索菜单
        page = Case_search(topLogin)
        text_assert1 = page.case_search()



    @pytest.mark.p0
    def test_designers_library (self, topLogin):
        # 创意方库菜单
        page = Case_search(topLogin)
        text_assert2 = page.designers_library()
        assert text_assert2 == "搜你感兴趣的创意方"







