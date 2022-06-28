# # -*- coding: utf-8 -*-
# # @Time : 2022/2/10 10:45 上午
# # @Author : liuzhijie
# # @File : conftest.py
#
#
# import pytest
# from playwright.sync_api import Page
#
# from conf.confs import url_myCollectionPage, group_name, group_description
# from pages.assets.MyCollectionPage import MyCollectionPage
#
# @pytest.fixture(scope='class',autouse=True)
# def collection_reset(page: Page):
#     print('-----测试开始-----')
#     yield
#     collectionObject = MyCollectionPage(page)
#     # collectionObject.group_detele(group_name)
#     print('-----数据清除完毕-----')
#
# @pytest.fixture(scope='function')
# def collection_init(page: Page, asset_group):
#     """
#     进入我收藏的页面
#     """
#     collectionObject = MyCollectionPage(page)
#     collectionObject._go(url_myCollectionPage)
#
#     yield collectionObject
#
#
import os
import time

import pytest
from playwright.sync_api import Browser
from conf.confs import Host2, url_assetGroupPage, account_LZJ, password_LZJ
from pages.assets.MyCollectionPage import MyCollectionPage
from pages.user_center.login_page import LoginPage
from common.logger import logger

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

@pytest.fixture(scope='function')
def my_collection_page_init(login_init):
    """
    进入素材组-我的收藏页面
    """
    assetGroupObject = MyCollectionPage(login_init)
    assetGroupObject._go(url_assetGroupPage)
    print('-----进入素材组-我的收藏页面-----')
    selector = assetGroupObject.read_yaml_element("notice_close_button")
    while assetGroupObject._is_visible(selector) is True:
        assetGroupObject._click(selector)
    yield assetGroupObject

