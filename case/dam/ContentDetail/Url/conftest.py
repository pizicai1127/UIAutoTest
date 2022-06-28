# -*- coding: utf-8 -*- 
# @Time : 2022/2/9 2:42 下午 
# @Author : liuzhijie
# @File : conftest.py

import os
import time
from common.logger import logger
import pytest
from playwright.sync_api import Browser
from conf.confs import url_assetPage, asset_test_data, Host2, url_import_baidu, \
    url_assetGroupPage, account_LZJ_007, password_LZJ_007
from pages.assets.AfterSearchPage import AfterSearchPage
from pages.assets.AssetGroupPage import AssetGroupPage
from pages.assets.ContentDetailPage import ContentDetailPage
from pages.assets.AssetPage import AssetPage
from pages.user_center.login_page import LoginPage


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
        login.login(Host2, account_LZJ_007, password_LZJ_007)
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
    进入素材库页面
    """
    assetObject = AssetPage(login_init)
    groupObject = AssetGroupPage(login_init)
    after_searchObject = AfterSearchPage(login_init)
    assetObject._go(url_assetPage)
    print('-----进入素材库页面-----')
    selector = assetObject.read_yaml_element("notice_close_button")
    while assetObject._is_visible(selector) is True:
        assetObject._click(selector)
    yield assetObject
    # 数据清除
    try:
        assetObject._go(url_assetPage)
        selector = assetObject.read_yaml_element("asset_name_first")
        if '百度一下' in assetObject._text_content(selector):
            assetObject.asset_hover()
            assetObject.asset_more_button()
            assetObject.asset_more_delete_content()
            print('-----数据清除完毕-----')
        groupObject._go(url_assetGroupPage)
        groupObject.group_search_text('UI自动化测试')
        groupObject._wait(2)
        selector = assetObject.read_yaml_element("search_group_name_first")
        if groupObject._is_visible(selector) is True:
            after_searchObject._hover(selector)
            after_searchObject.search_delete_group()
    except Exception as err:
        raise err


@pytest.fixture(scope='class')
def detail_url_init(login_init, asset_init):
    """
    进入素材详情页
    """
    asset_init._go(url_assetPage)
    asset_init.upload_url(url_import_baidu)
    ContentDetail = ContentDetailPage(login_init)
    ContentDetail.into_detail_page()
    print('-----进入素材详情页-----')
    yield ContentDetail


@pytest.fixture(scope='class')
def asset_more_init(login_init, asset_init):
    """
    上传素材，进行右键操作
    """
    asset_init.upload_file()
    yield asset_init

