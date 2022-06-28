#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_case_creatives1.py

import pytest
from pages.top.case_creatives1 import Share_list

class TestShare_list:
    # 分享列表管理菜单

    @pytest.mark.p0
    def test_case_lists (self, topLogin):
        # 案例分享列表
        page = Share_list(topLogin)
        text_assert = page.case_lists()
        assert text_assert == "新建案例分享列表"


    @pytest.mark.p0
    def test_designer_lists(self, topLogin):
        # 创意方分享列表
        page = Share_list(topLogin)
        text_assert2 = page.designer_lists()
        assert text_assert2 == "新建创意方分享列表"








