#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/24 3:17 下午
# @Author  : wmt
# @File    : conftest.py
# @Software: PyCharm
import pytest
from playwright.sync_api import Page
from pages.user_center.login_page import LoginPage, LogoutSys


@pytest.fixture(scope="function")
def login_page_load( page: Page):
    """
    登录页面的前置
    :return:
    """
    #前置

    login_home_page=LoginPage(page)
    yield login_home_page  #yield之前代码是前置，之后的代码就是后置，yield的作用就相当于return

@pytest.fixture(scope="function")
def logout_page_load( page: Page):
    """
    登录页面的前置
    :return:
    """
    #前置
    logout_page=LogoutSys(page)
    yield logout_page  #yield之前代码是前置，之后的代码就是后置，yield的作用就相当于return


