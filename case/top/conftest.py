#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/7 3:10 下午
# @Author: cuiguoen
# @File : conftest.py.py

import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope='class')
def topLogin(playwright: Playwright):
    top_cookies = [
        {
            'name': 'globalUserId',
            'value': '517711772203876352',
            'domain': 'top.tezign.com',
            'path': '/'
        },
        {
            'name': 'xtoptoken',
            'value': '32089a3bb92f36c9c3798fbf20227fa7',
            'domain': 'top.tezign.com',
            'path': '/'
        },
        {
            'name': 'xtopuid',
            'value': '317',
            'domain': 'top.tezign.com',
            'path': '/'
        },
    ]
    browser = playwright.chromium.launch(headless=True, slow_mo=100)
    context = browser.new_context()
    # 通过添加登陆cookie实现登陆
    context.add_cookies(cookies=top_cookies)

    page = context.new_page()
    page.goto("https://top.tezign.com/")

    yield page
    print("关闭top后台页面")
    context.close()  # 关闭context
    browser.close()  # 关闭browser