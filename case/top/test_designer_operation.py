#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_designer_operation.py


import pytest
from pages.top.designer_operation import Designer

class TestDesigner:
    # 创意方运营 菜单,有创意方详情页

    @pytest.mark.p0
    def test_demand_orders(self, topLogin):
        # 创意方满意度调研 菜单
        page = Designer(topLogin)
        text_assert = page.demand_orders()


    @pytest.mark.p0
    def test_invite_list(self, topLogin):
        # 特赞邀请列表 菜单
        page = Designer(topLogin)
        text_assert2 = page.invite_list()

    @pytest.mark.p0
    def test_invite_designer(self, topLogin):
        # 创意方邀请列表 菜单
        page = Designer(topLogin)
        text_assert3 = page.invite_designer()

    @pytest.mark.p0
    def test_designer_verify(self, topLogin):
        # 创意方审核 菜单,创意方详情页
        page = Designer(topLogin)
        text_assert4 = page.designer_verify()


    @pytest.mark.p0
    def test_personal_authentication(self, topLogin):
        # 创意方个人实名认证 菜单
        page = Designer(topLogin)
        text_assert5 = page.personal_authentication()

    @pytest.mark.p0
    def test_company_authentication(self, topLogin):
        # 创意方公司实名认证 菜单
        page = Designer(topLogin)
        text_assert6 = page.company_authentication()

    @pytest.mark.p0
    def test_tax_change(self, topLogin):
        # 创意方票税变更申请 菜单
        page = Designer(topLogin)
        text_assert7 = page.test_tax_change()

    @pytest.mark.p0
    def test_quote_go(self, topLogin):
        # 报价GO二维码 菜单
        page = Designer(topLogin)
        text_assert8 = page.test_quote_go()