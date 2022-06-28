#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/21 2:33 下午
# @File : test_my_project.py
import pytest

from pages.customer.MyprojectPage import MyProjectPage


class TestMyProject:
    shuju = [{
        "input_box": "哈哈哈",
    }]

    # 查看客户端排序
    def test_project_sort(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/projects")
        page = MyProjectPage(test_login_btn[0])
        page.my_project_sort()

    # 查看客户端项目
    def test_project_tails(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/projects")
        page = MyProjectPage(test_login_btn[0])
        page.view_project_tails()

    # 进入客户端项目详情页，进行对话
    @pytest.mark.parametrize("data", shuju)
    def test_input_box(self,test_login_btn,data):
        test_login_btn[0].goto("https://www.tezign.com/client/#/projects/84827")
        page = MyProjectPage(test_login_btn[0])
        page.input_box(data["input_box"])
