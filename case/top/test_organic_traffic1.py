#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_organic_traffic1.py


import pytest
from pages.top.organic_traffic1 import Organic1

class TestOrganic1:
    # 自然流量菜单下的前半部分

    @pytest.mark.p0
    def test_normal_projects(self, topLogin):
        # 普通项目菜单
        page = Organic1(topLogin)
        text_assert1 = page.normal_projects()



    @pytest.mark.p0
    def test_contracts_list(self, topLogin):
        # 合同列表菜单
        page = Organic1(topLogin)
        text_assert2 = page.contracts_list()
        assert text_assert2 == "合同管理详情"

    @pytest.mark.p0
    def test_invoice_request(self, topLogin):
        # 发票申请菜单
        page = Organic1(topLogin)
        text_assert3 = page.invoice_request()

    @pytest.mark.p0
    def test_promo_code(self, topLogin):
        # 发布优惠码 菜单
        page = Organic1(topLogin)
        text_assert4 = page.promo_code()



    @pytest.mark.p0
    def test_penalty_appeal(self, topLogin):
        # 交易行为扣分申诉 菜单
        page = Organic1(topLogin)
        text_assert5 = page.penalty_appeal()
        assert text_assert5 == "创意方详情"


    @pytest.mark.p0
    def test_discount_code(self, topLogin):
        # 服务费优惠码 菜单
        page = Organic1(topLogin)
        text_assert6 = page.discount_code()
        assert text_assert6 == "服务费优惠券"

    @pytest.mark.p0
    def test_natural_customer(self, topLogin):
        # 自然流量客户 菜单
        page = Organic1(topLogin)
        text_assert7 = page.natural_customer()

    @pytest.mark.p0
    def test_benefit_editing(self, topLogin):
        # 权益编辑 菜单
        page = Organic1(topLogin)
        text_assert8 = page.benefit_editing()

