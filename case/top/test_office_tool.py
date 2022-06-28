#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_office_tool.py


import pytest
from pages.top.office_tool import Office_tool

class TestOffice_tool:
    # 中台工具 菜单

    @pytest.mark.p0
    def test_NPS_questionnaire(self, topLogin):
        # NPS问卷 菜单
        page = Office_tool(topLogin)
        text_assert = page.NPS_questionnaire()

    @pytest.mark.p0
    def test_verification_code(self, topLogin):
        # 查询验证码 菜单
        page = Office_tool(topLogin)
        text_assert2 = page.verification_code()

