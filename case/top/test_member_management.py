#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_member_management.py


import pytest
from pages.top.member_management import Member_management

class TestMember_management:
    # 后台成员管理 菜单

    @pytest.mark.p0
    def test_role_list(self, topLogin):
        # 角色列表 菜单
        page = Member_management(topLogin)
        text_assert = page.role_list()


    @pytest.mark.p0
    def test_account_grouping(self, topLogin):
        # Account分组 菜单
        page = Member_management(topLogin)
        text_assert = page.account_grouping()






