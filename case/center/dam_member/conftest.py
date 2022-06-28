#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 4:33 下午
# @Author  : wmt
# @File    : conftest.py
# @Software: PyCharm
import os
import time

import pytest
from playwright.sync_api import Page, Browser
from common import logger
from conf.confs import Host2, account, password, url_dam_member_page, url_dam_external_page
from pages.user_center.dam_exteranl_page import DamExternalPage
from pages.user_center.dam_member_page import DamMemberPage
from pages.user_center.login_page import LoginPage


#@pytest.fixture(scope="function")
# def login_init(browser: Browser):
#     """
#     登录初始化
#     @return:
#     """
#     cookie_file = 'state_wmt.json'
#     if os.path.exists(cookie_file):
#         context = browser.new_context(storage_state=cookie_file)
#         page = context.new_page()
#     else:
#         context = browser.new_context()
#         page = context.new_page()
#         login = LoginPage(page)
#         login.login(Host2, account, password)
#         time.sleep(2)
#     yield page
#     try:
#         # 保存登录验证cookie
#         context.storage_state(path=cookie_file)
#     except Exception as e:
#         logger.info(e)

@pytest.fixture(scope="function")
def login_init(browser: Browser):
    """
    登录初始化
    @return:
    """
    context = browser.new_context()
    page = context.new_page()
    login = LoginPage(page)
    login.login(Host2, account, password)
    time.sleep(2)
    yield page







@pytest.fixture(scope="function")
def dam_member_page_init(login_init):
    """
    进入成员信息页面
    """

    # login_home_page = LoginPage(page)
    # print('-----准备登录dam租户成员信息页面-----')
    # login_home_page.login(url_dam_member_page, account, password)
    # login_home_page._wait(6)

    memberObject = DamMemberPage(login_init)
    memberObject._go(url_dam_member_page)
    memberObject._wait(6)
    yield memberObject


@pytest.fixture(scope="function")
def dam_external_page_init(login_init):
    """
    进入成员信息页面
    """

    # login_home_page = LoginPage(page)
    # print('-----准备登录dam租户成员信息页面-----')
    # login_home_page.login(url_dam_external_page, account, password)
    # login_home_page._wait(6)
    # time.sleep(2)

    externalObject = DamExternalPage(login_init)
    externalObject._go(url_dam_external_page)
    externalObject._wait(6)
    yield externalObject
