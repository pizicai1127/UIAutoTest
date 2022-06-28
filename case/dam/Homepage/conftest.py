# -*- coding: utf-8 -*- 
# @Time : 2022/3/16 10:58 上午 
# @Author : liuzhijie
# @File : conftest.py
import os
import time
import pytest
from playwright.sync_api import Browser
from common.logger import logger
from conf.confs import Host2, account_LZJ, password_LZJ, url_homePage
from pages.user_center.login_page import LoginPage
from pages.assets.HomePage import HomePage


@pytest.fixture(scope='class')
def login_init(browser: Browser):
    """
    登录初始化
    @return:
    """
    cookie_file = 'state_lzj.json'
    if os.path.exists(cookie_file):
        context = browser.new_context(storage_state=cookie_file)
        page = context.new_page()
    else:
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        login.login(Host2, account_LZJ, password_LZJ)
        time.sleep(2)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.error(e)


@pytest.fixture()
def home_init(login_init):
    """
    首页初始化
    """
    HomeObject = HomePage(login_init)
    HomeObject._go(url_homePage)
    # 关闭公告
    selector = HomeObject.read_yaml_element("notice_close_button")
    if HomeObject._is_visible(selector) is True:
        HomeObject._click(selector)
    print('-----进入首页-----')
    yield HomeObject