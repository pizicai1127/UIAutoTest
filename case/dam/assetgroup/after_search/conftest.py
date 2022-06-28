# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/3/18 1:08 下午
# @File:conftest.py
import pytest
from playwright.sync_api import Browser
import os
from pages.user_center.login_page import LoginPage
from conf.confs import Host2, account_RY, password_RY
from common.logger import logger
from pages.assets.AfterSearchPage import AfterSearchPage


@pytest.fixture(scope='class', autouse=True)
def login_i(browser: Browser):
    """
    登录初始化
    @return:
    """
    cookie_file = 'state-ry.json'
    if os.path.exists(cookie_file):
        context = browser.new_context(storage_state=cookie_file)
        page = context.new_page()
    else:
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        login.login(Host2, account_RY, password_RY)
        page.wait_for_timeout(1000)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.error(e)


@pytest.fixture(scope='class')
def search_i(login_i):
    """
    进入素材组页面
    @rtype: login_i
    """
    search = AfterSearchPage(login_i)
    search.goto_search()
    print('-------进入全部素材组的页面------')
    yield search
