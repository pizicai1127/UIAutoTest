#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : conftest.py

import pytest
import os
from playwright.sync_api import Page
from pages.ms.ms_login  import LoginPage
from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright


@pytest.fixture(scope='class')
def loginVMS(playwright: Playwright):
    date ={
            # 管理员账号
            "login_page_url": "https://asset-stage.tezign.com/user/login",  # 租户地址
            "account": "cuiguoen@tezign.com",
            "password": "111111qq",
            "market_url": "https://asset-stage.tezign.com/platform/market"  # 创意商城地址
        }

    browser = playwright.chromium.launch(headless=True, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.go_to_tenant(date["login_page_url"])
    login_page.home_login(date["account"], date["password"])

    # 进入创意商城页面
    login_page.go_to_tenant(date["market_url"])

    # 加入等待时间,这个wait_for_timeout的单位是毫秒
    #page.wait_for_timeout(1000)
    print("进入创意商城页面，开始执行操作")

    yield page,context
    print("关闭创意方商城页面")
    context.close()  # 关闭context
    browser.close()  # 关闭browser




