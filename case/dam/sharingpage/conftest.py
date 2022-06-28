#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : conftest
# @Author: yanglun@tezign.com
# @Date  : 2022/4/10
# @Desc  :  
"""


import pytest
from conf.confs import Host2, account_sm, password
import time
from pages.user_center.login_page import LoginPage
from playwright.sync_api import Browser
import os
from common.logger import logger


@pytest.fixture(scope="class")
def login_sys(browser: Browser):
    """
    登录初始化
    @return:
    """
    cookie_file = 'state_sm.json'
    if os.path.exists(cookie_file):
        context = browser.new_context(storage_state=cookie_file)
        page = context.new_page()
    else:
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        login.login(Host2, account_sm, password)
        time.sleep(2)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.error(e)


@pytest.fixture(scope="class")
def new_browser_context(browser: Browser):
    """
    初始化一个浏览器上下文，作为无痕打开分享落地页的页面
    @param browser:
    @return:
    """
    context = browser.new_context()
    page_two = context.new_page()
    yield page_two















