#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : test_case.py"""
import pytest
from time import sleep

from pages.designer.CasePage import AnliPage


class TestAnli:
    shuju = [
        {
            "anli_name": "测试案例1",
            "case_description": "测试案例描述",
            "fengge_btn": "特赞",
            "background": "背景描述背景描述背景描述背景描述",
            "describe": "修改背景描述背景描述背景描述背景描述",
            "brand": "特赞品牌",
            "describe_background": "修改背景",
            "click_the_input_box": "测试文本输入",
        }

    ]

    # 对创意方案例增删改查
    @pytest.mark.parametrize("data", shuju)
    def test_anliport(self, test_login, data):
        page = AnliPage(test_login[0])
        page.gotoanli("https://www.tezign.com/designer/#/portfolio")
        page._wait(1)
        page.check_element()
        page.anlicase(data["anli_name"], data["case_description"], data["fengge_btn"], data["background"])
        # page.gotoanli("https://www.tezign.com/designer/#/portfolio")
        # page._wait(1)
        # page.editcase(data['describe'], data['brand'], data['describe_background'], data['click_the_input_box'])
        # page.goto("https://www.tezign.com/designer/#/portfolio")
        # page._wait(1)
        # page.deletecase()
        # page._wait(1)

    @pytest.mark.parametrize("data", shuju)
    def test_editcase(self, test_login, data):
        page = AnliPage(test_login[0])
        page.goto("https://www.tezign.com/designer/#/portfolio")
        page._wait(1)
        page.check_element()
        page.editcase(data['describe'], data['brand'], data['describe_background'], data['click_the_input_box'])
        test_login[0].goto("https://www.tezign.com/designer/#/portfolio")
        page._wait(1)

    # 查看创意方案例类型
    def test_case_type(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/portfolio")
        page = AnliPage(test_login[0])
        page.case_type()

    def test_delete_case(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/portfolio")
        page = AnliPage(test_login[0])
        page.deletecase()
