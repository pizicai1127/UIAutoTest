#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/1 4:16 下午
# @File : conftest.py

import pytest
from playwright.sync_api import Playwright

from common.logger import logger
"""
from pages.express.ContextSkuPage import ContextSkuPage
@pytest.fixture(scope='session', autouse=True)
def test_login(playwright: Playwright):
    browser = playwright.chromium.launch(slow_mo=800, headless=False)
    context = browser.new_context(storage_state="state.json", ignore_https_errors=True)
    page = context.new_page()
    page1 = ContextSkuPage(page)
    page1.goto("https://express.tezign.com/platform/market")
    sleep(2)
    page1.information()
    yield page, page1
    , headless=False
    , viewport={"width": 1500,"height": 1500}
    """


@pytest.fixture(scope='session', autouse=True)
def top_login(playwright: Playwright):
    top_cookies = [
        {
            'name': 'transfer_token',
            'value': '7b3f85303efa4fe4a6111fdf1ce8272f',
            'domain': '.musetransfer.com',
            'path': '/'
        },
        {
            'name': 'transfer_uid',
            'value': '6',
            'domain': '.musetransfer.com',
            'path': '/'
        },
        {
            'name': 'guid',
            'value': '1536649860701257728',
            'domain': '.musetransfer.com',
            'path': '/'
        },
    ]

    browser = playwright.chromium.launch(slow_mo=550)
    """
    登录
    """
    context = browser.new_context(ignore_https_errors=True)
    context.add_cookies(cookies=top_cookies)
    page = context.new_page()
    yield page


