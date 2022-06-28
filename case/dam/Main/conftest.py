# -*- coding: utf-8 -*- 
# @Time : 2022/2/17 4:36 下午 
# @Author : liuzhijie
# @File : conftest.py
import os
import time
import pytest
from playwright.sync_api import Browser
from common.logger import logger
from conf.confs import Host2, account_LZJ_005, password_LZJ_005, url_assetPage, url_assetGroupPage
from pages.assets.AfterSearchPage import AfterSearchPage
from pages.assets.AssetGroupPage import AssetGroupPage
from pages.assets.AssetPage import AssetPage
from pages.user_center.login_page import LoginPage


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
        login.login(Host2, account_LZJ_005, password_LZJ_005)
        time.sleep(2)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.error(e)




# 关闭公告
@pytest.fixture()
def main_init(login_init):
    # 进入素材库页面
    assetObject = AssetPage(login_init)
    groupObject = AssetGroupPage(login_init)
    after_searchObject = AfterSearchPage(login_init)
    assetObject._go(url_assetPage)
    assetObject._wait(2)
    selector = assetObject.read_yaml_element("notice_close_button")
    while assetObject._is_visible(selector) is True:
        assetObject._click(selector)
        assetObject._wait(1)
    yield assetObject
    # 数据清除
    try:
        assetObject._go(url_assetPage)
        assetObject.asset_my_create()
        selector = assetObject.read_yaml_element("asset_name_first")
        if assetObject._is_visible(selector) is True:
            if 'UI自动化' in assetObject._text_content(selector) or 'test_file' in assetObject._text_content(selector):
                assetObject.asset_hover()
                assetObject.asset_more_button()
                assetObject.asset_more_delete()
        groupObject._go(url_assetGroupPage)
        groupObject.group_search_text('UI自动化测试')
        groupObject._wait(2)
        selector = assetObject.read_yaml_element("search_group_name_first")
        if groupObject._is_visible(selector) is True:
            after_searchObject._hover(selector)
            after_searchObject.search_delete_group()
            print('-----数据清除完毕-----')
    except Exception as err:
        raise err