# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/3/8 11:14 上午
# @File:conftest.py
import time
import pytest
from playwright.sync_api import Browser
import os
from pages.user_center.login_page import LoginPage
from conf.confs import Host2, account_RY, password_RY
from common.logger import logger
from pages.assets.MyCreaterPage import MyCreatedPage


@pytest.fixture(scope='class', autouse=True)
def login_i(browser: Browser):
    """
    登录初始化
    @return:
    """
    cookie_file = 'state.json'
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
        logger.info(e)


@pytest.fixture(scope='class')
def created_i(login_i):
    """
    进入素材组-我创建的 页面
    @rtype: object
    """
    mycreated = MyCreatedPage(login_i)
    mycreated.goto_created()
    print('-------进入素材组-我创建的页面------')
    yield mycreated
    # try:
    #     # 删除测试新建的素材组
    #     mycreated.created_ingroup()
    #     mycreated.created_group_delete()
    # except Exception as e:
    #     logger.error(e)
