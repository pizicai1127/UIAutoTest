#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/4 10:47 上午
# @File : test_special_discovery.py
import pytest

from pages.express.SpecialDiscoveryPage import SpecialDiscoveryPage


class TestSpecialDiscovery:
    shuju = [{
        "input_search": "视频",
        "case_order": "测试项目名称",
        "case_order_textarea": "测试项目项目概述",
        "quantity": "2",
        "xiaomi": "小米",
        "budget": "3",
        "mailbox": "12345698@qq.com",

    }]

    # 点击轮播图
    def test_discovery_page(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = SpecialDiscoveryPage(expesss_login)
        page.discovery_page()

    # 点赞案例
    def test_discovery_page_selected_cases(self, expesss_login):
        expesss_login.goto("https://express.tezign.com/platform/case")
        page = SpecialDiscoveryPage(expesss_login)
        page.discovery_page_selected_cases()
        assert page._text_content("text= 点赞成功") == "点赞成功"
        assert page._text_content("text= 取消点赞") == "取消点赞"

    # 发现页面，点击案例，下单取消
    def test_selected_cases(self, expesss_login):
        expesss_login.goto("https://express.tezign.com/platform/case")
        page = SpecialDiscoveryPage(expesss_login)
        page.selected_cases()

    # 特赞发现，研究院
    def test_creative_research_institute(self, expesss_login):
        expesss_login.goto("https://express.tezign.com/platform/case")
        page = SpecialDiscoveryPage(expesss_login)
        page._wait(3)
        page.creative_research_institute()

    # 特赞发现页，案例分类
    def test_classification(self, expesss_login):
        expesss_login.goto("https://express.tezign.com/platform/case")
        page = SpecialDiscoveryPage(expesss_login)
        page.classification()

    # 特赞发现页，案例二级分类
    def test_classification_second_level(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = SpecialDiscoveryPage(expesss_login)
        page.classification_second_level()

    # 特赞发现页面搜索框
    @pytest.mark.parametrize("data", shuju)
    def test_input_search(self, expesss_login, data):
        expesss_login.goto("https://express.tezign.com")
        page = SpecialDiscoveryPage(expesss_login)
        page.input_search(data["input_search"])
