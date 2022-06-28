#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/7 5:21 下午
# @File : test_new_enterprise_project.py
import pytest

from pages.topmanage.NewEnterpriseProjectPage import NewEnterpriseProjectPage


class TestNewEnterpriseProject:
    shuju = [{
        "project_title": "测试项目",
        "background": "插画海报平面",
        "project_budget": "2",
        "input_customer": "阿里巴巴零售通",
        "budget": "3",
        "quantity": "4",
        "quantity_btn": "5",

    }]

    @pytest.mark.parametrize("data", shuju)
    def test_create_project(self, top_login, data):
        page = NewEnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.create_project(data["project_title"], data["background"], data["project_budget"], data["input_customer"])

    @pytest.mark.parametrize("data", shuju)
    def test_edit_draft_project(self, top_login, data):
        page = NewEnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.edit_draft_project(data["quantity"], data["quantity_btn"], )

    def test_publish_project(self, top_login):
        page = NewEnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.publish_project()

    @pytest.mark.parametrize("data", shuju)
    def test_delete_draft_project(self, top_login, data):
        page = NewEnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.create_project(data["project_title"], data["background"], data["project_budget"], data["input_customer"])
        page.goto("https://top.tezign.com/#/app/proProject/list")
        page.delete_draft_project()

    def test_edit_publish_project(self, top_login):
        page = NewEnterpriseProjectPage(top_login)
        page.goto("https://top.tezign.com/#/app/proProject/list")


# t = TestNewEnterpriseProject()
# t.test_create_project()
# t.test_delete_draft_project()
