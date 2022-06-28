#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : conftest
# @Author: yanglun@tezign.com
# @Date  : 2022/2/18
# @Desc  :  全部素材组测试用例集
"""

import pytest
from conf.confs import Host2, account_lsm, password
import time
from pages.user_center.login_page import LoginPage
from playwright.sync_api import Browser
import os
from common.logger import logger
from pages.assets.AllCollectionPage import AllCollectionPage


@pytest.fixture(scope="class", autouse=True)
def login_sys(browser: Browser):
    """
    登录初始化
    @return:
    """
    cookie_file = 'state_lsm.json'
    if os.path.exists(cookie_file):
        context = browser.new_context(storage_state=cookie_file)
        page = context.new_page()
    else:
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        login.login(Host2, account_lsm, password)
        time.sleep(2)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.info(e)

@pytest.fixture(scope="class")
def data_init(login_sys):
    """
    数据初始化，删除全部下新建的素材组
    @return:
    """
    collection_page = AllCollectionPage(login_sys)
    collection_page.goto_group()
    yield collection_page
    try:
        # 删除测试新建的素材组
        collection_page.group_enter()
        collection_page.group_delete()
    except Exception as e:
        logger.error(e)






