#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/28 2:26 下午
# @File : test_publish_project.py
import pytest

from pages.customer.PublishProjectPage import PublishProject


class TestPublishProject:
    shuju = [{
        "quantity_btn": "2",
        "project_name": "测试项目名称",
        "target_user": "测试项目目标用户",
        "input_style": "添加风格",
        "project_cycle": "5",
        "budget": "3",
        "mailbox": "12345698@qq.com",

    }]

    # 客户端发布项目
    @pytest.mark.parametrize("data", shuju)
    def test_publish_project(self, test_login_btn, data):
        test_login_btn[0].goto("https://www.tezign.com/client/#/projects")
        page = PublishProject(test_login_btn[0])
        page.publish_project(data["quantity_btn"], data["project_name"], data["target_user"], data["input_style"],
                             data["project_cycle"], data["budget"], data["mailbox"])

    # 客户取消复制项目
    def test_edit_cancel_copy_project(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/projects")
        page = PublishProject(test_login_btn[0])
        page.edit_cancel_copy_project()

    # 客户确认复制项目
    def test_edit_confirm_copy_project(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/projects")
        page = PublishProject(test_login_btn[0])
        page.edit_confirm_copy_project()

    # 客户取消删除项目
    def test_delete_cancel_project(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/projects")
        page = PublishProject(test_login_btn[0])
        page.delete_cancel_project()

    # 客户确定删除项目
    def test_delete_project(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/projects")
        page = PublishProject(test_login_btn[0])
        page.delete_project()
