#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/7 11:22 上午
# @File : test_enterprise_project.py
import pytest

from pages.topmanage.EnterpriseProjectPage import EnterpriseProjectPage


class TestEnterpriseProject:
    shuju = [{
        "personnel": "top",
        "keyword": "测试",
        "case_order_textarea": "测试项目项目概述",
        "quantity": "2",
        "xiaomi": "小米",
        "budget": "3",
        "mailbox": "12345698@qq.com",

    }]

    def test_enterprise_project_state(self, top_login):
        page = EnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.enterprise_project_state()
        # page._wait(2)

    def test_enterprise_project_source(self, top_login):
        page = EnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.enterprise_project_source()

    def test_cooperation_mode(self, top_login):
        page = EnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.cooperation_mode()

    @pytest.mark.parametrize("data", shuju)
    def test_business_personnel(self, top_login, data):
        page = EnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.business_personnel(data["personnel"],)

    @pytest.mark.parametrize("data", shuju)
    def test_keyword_search(self, top_login, data):
        page = EnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.keyword_search(data["keyword"],)

    def test_paging(self, top_login):
        page = EnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.paging()