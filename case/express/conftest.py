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


# @pytest.fixture(scope='session', autouse=True)
# def expesss_login(playwright: Playwright):
#     browser = playwright.chromium.launch(slow_mo=300,  headless=False)
#     """
#     登录
#     """
#     cookie_file = 'state.json'
#     context = browser.new_context(storage_state=cookie_file, ignore_https_errors=True)
#     page = context.new_page()
#     yield page
#     try:
#         context.storage_state(path=cookie_file)
#     except Exception as e:
#         logger.info(e)

@pytest.fixture(scope='session', autouse=True)
def expesss_login(playwright: Playwright):
    top_cookies = [
        {
            'name': 'globalUserId',
            'value': '1498501916393955328',
            'domain': '.express.tezign.com',
            'path': '/'
        },
        {
            'name': 'vmsxtoken',
            'value': '1b6fe1de68bded450d78f290d1810358',
            'domain': 'express.tezign.com',
            'path': '/'
        },
        {
            'name': 'vmsxuid',
            'value': '151812',
            'domain': '.express.tezign.com',
            'path': '/'
        },
    ]

    browser = playwright.chromium.launch(slow_mo=900)
    """
    登录
    """
    context = browser.new_context(ignore_https_errors=True)
    context.add_cookies(cookies=top_cookies)
    page = context.new_page()
    yield page
    # try:
    #     context.storage_state(path=cookie_file)
    # except Exception as e:
    #     logger.info(e)
