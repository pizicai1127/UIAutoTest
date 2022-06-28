#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_personal_panel.py

import pytest
from pages.top.personal_panel import Personal

class TestPersonal:

    @pytest.mark.p0
    def test_my_business(self,topLogin):
        page = Personal(topLogin)
        text_assert = page.my_business()
        assert text_assert[0] == "SQL金额"
        assert text_assert[1] == "签单确认收入"
        assert text_assert[2] == "签单总额"
        assert text_assert[3] == "项目面板执行遇到问题？点击查看业务SOP"
        assert text_assert[4] == "业务标准SOP参考"

    def test_my_collect(self,topLogin):
        page = Personal(topLogin)
        text_assert2 = page.my_collect()
        assert text_assert2 == "案例分享列表"



