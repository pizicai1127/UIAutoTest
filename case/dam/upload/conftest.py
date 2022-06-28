#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : conftest
# @Author: yanglun@tezign.com
# @Date  : 2022/4/18
# @Desc  :
"""


import pytest
from conf.confs import Host2, account_ssm, password
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
    cookie_file = 'state_ssm.json'
    if os.path.exists(cookie_file):
        context = browser.new_context(storage_state=cookie_file)
        page = context.new_page()
    else:
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        login.login(Host2, account_ssm, password)
        time.sleep(2)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.error(e)