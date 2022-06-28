#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/1 4:05 下午
# @File : test_home_page.py
import pytest


from pages.express.HomePage import HomePage


class TestHomePage:
    shuju = [{
        "search": "阿里巴巴",
        "case_order": "测试项目名称",
        "case_order_textarea": "测试项目项目概述",
        "quantity": "2",
        "xiaomi": "小米",
        "budget": "3",
        "mailbox": "12345698@qq.com",

    }]

    # def test_information(self, playwright: Playwright):
    #     browser = playwright.chromium.launch(slow_mo=1000, headless=False)
    #     context = browser.new_context(storage_state="state.json", ignore_https_errors=True)
    #     page = context.new_page()
    #     page = ContextSkuPage(page)
    #     page.goto("https://express.tezign.com/platform/market")
    #     sleep(2)
    #     page.information()
    # express首页solution
    def test_home_page(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.home_page()

    # express特赞内容SKU
    def test_home_page_special_content(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.home_page_special_content()

    # express侧边栏
    def test_home_page_sidebar(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.home_page_sidebar()

    # express侧边栏
    def test_home_page_navigation(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.home_page_navigation()

    # 特赞内容操作
    @pytest.mark.parametrize("data", shuju)
    def test_home_page_operation(self, data, expesss_login):
        assert_selectors = "body > div:nth-child(12) > div > div.ant-modal-wrap.ant-modal-centered > div > " \
                         "div.ant-modal-content > div.ant-modal-footer > div > " \
                         "button.tz-btn.type-neutral.shape-round.ghost-text "
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.home_page_operation(data["quantity"],)
        # assert page._is_visible(assert_selectors)

    # 点击首页热门搜索短视频，点赞，取消点赞
    def test_hot_search(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.hot_search()
        assert page._text_content("text= 点赞成功") == "点赞成功"
        assert page._text_content("text= 已取消点赞") == "已取消点赞"

    # 点击首页热门搜索短视频，点击购物车，点击下单,然后取消
    def test_hot_search_shopping_cart(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.hot_search_shopping_cart()

    # 点击首页热门搜索插画，点击购物车，下单
    @pytest.mark.parametrize("data", shuju)
    def test_hot_illustration(self, data, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.hot_illustration(data["quantity"], data["case_order"], data["case_order_textarea"])

    # 点击首页热门搜索平面，点击立即询价，下单
    @pytest.mark.parametrize("data", shuju)
    def test_hot_plane(self, data, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.hot_plane(data["case_order"], data["case_order_textarea"])

    # 点击首页热门搜索海报，点击立查看全部；搜索
    @pytest.mark.parametrize("data", shuju)
    def test_hot_poster(self, data, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.hot_poster(data["xiaomi"], )

    # express搜索,点赞，点击案例进入详情页面，下单
    @pytest.mark.parametrize("data", shuju)
    def test_search(self, data, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = HomePage(expesss_login)
        page.home_page_search(data["search"], data["case_order"], data["case_order_textarea"])
