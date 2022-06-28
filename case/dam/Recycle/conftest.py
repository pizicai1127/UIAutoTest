# -*- coding: utf-8 -*- 
# @Time : 2022/4/12 11:50 上午 
# @Author : liuzhijie
# @File : conftest.py
import os
import time
import pytest
from playwright.sync_api import Browser

from pages.assets.AfterSearchPage import AfterSearchPage
from pages.assets.AssetGroupPage import AssetGroupPage
from pages.assets.AssetPage import AssetPage
from pages.assets.RecyclePage import RecyclePage
from pages.user_center.login_page import LoginPage
from conf.confs import url_assetPage, asset_test_data, Host2, account_LZJ_004, password_LZJ_004, url_recyclePage, \
    url_assetGroupPage
from common.logger import logger


@pytest.fixture(scope='module')
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
        login.login(Host2, account_LZJ_004, password_LZJ_004)
        time.sleep(2)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.error(e)


@pytest.fixture(scope='class')
def asset_init(login_init):
    """
    素材库页面
    """
    assetObject = AssetPage(login_init)
    assetObject._go(url_assetPage)
    assetObject._wait(1)
    selector = assetObject.read_yaml_element("notice_close_button")
    while assetObject._is_visible(selector) is True:
        assetObject._click(selector)
    # 上传素材
    assetObject.upload_file()
    # hover 素材
    assetObject.asset_hover()
    # 点击"。。。"按钮
    assetObject.asset_more_button()
    # 删除素材（让素材进入回收站）
    assetObject.asset_more_delete()
    print('-----进入素材库页面-----')

    yield assetObject
    # 数据清除
    try:
        assetObject._go(url_assetPage)
        selector = assetObject.read_yaml_element("asset_name_first")
        if assetObject._text_content(selector) in asset_test_data:
            assetObject.asset_hover()
            assetObject.asset_more_button()
            assetObject.asset_more_delete()
            assetObject._wait(2)
            print('-----数据清除完毕-----')
        else:
            print('-----数据清除完毕-----')
    except Exception as err:
        raise err


@pytest.fixture(scope='class')
def group_init(login_init):
    """
    素材组页面
    """
    groupObject = AssetGroupPage(login_init)
    after_searchObject = AfterSearchPage(login_init)
    groupObject._go(url_assetGroupPage)
    groupObject._wait(1)
    # 新建素材组
    groupObject.group_new('UI自动化测试-回收站-测试组')
    # 删除素材组（让素材进入回收站）
    groupObject.group_delete()
    yield groupObject
    # 数据清除
    groupObject._go(url_assetGroupPage)
    groupObject.group_search_text('UI自动化测试')
    groupObject._wait(2)
    selector = groupObject.read_yaml_element("search_group_name_first")
    if groupObject._is_visible(selector) is True:
        after_searchObject._hover(selector)
        after_searchObject.search_delete_group()


@pytest.fixture(scope='class')
def recycle_init(login_init):
    """
    回收站页面
    """
    recycleObject = RecyclePage(login_init)
    recycleObject._go(url_recyclePage)
    recycleObject._wait(1)
    yield recycleObject