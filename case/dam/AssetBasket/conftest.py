import os
import time
import pytest
from playwright.sync_api import Browser
from conf.confs import Host2, url_assetPage, asset_test_data, account_LZJ_002, password_LZJ_002
from pages.assets.AssetBasketPage import AssetBasketPage
from pages.assets.AssetPage import AssetPage
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
        login.login(Host2, account_LZJ_002, password_LZJ_002)
        time.sleep(2)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.error(e)


@pytest.fixture(scope="class")
def asset_init(login_init):
    """
    进入素材库页面,并上传文件
    """
    assetObject = AssetPage(login_init)
    print('-----进入素材库页面-----')
    assetObject._go(url_assetPage)
    assetObject._wait(1)
    selector = assetObject.read_yaml_element("notice_close_button")
    while assetObject._is_visible(selector) is True:
        assetObject._click(selector)
    print('-----上传文件-----')
    assetObject.upload_file()
    assetObject._wait(1)
    yield assetObject
    # 数据清除
    try:
        assetObject._go(url_assetPage)
        selector = assetObject.read_yaml_element("asset_name_first")
        while 'UI自动化' in assetObject._text_content(selector) or 'test_file' in assetObject._text_content(selector):
            assetObject.asset_hover()
            assetObject.asset_more_button()
            assetObject.asset_more_delete()
            assetObject._wait(1)
            print('-----数据清除完毕-----')
    except Exception as err:
        raise err


@pytest.fixture(scope='function')
def asset_basket_init(login_init, asset_init):
    """
    素材篮页面，将素材加入素材篮，并打开素材篮页面
    """
    assetbasketObject = AssetBasketPage(login_init)
    print('-----点击加入素材篮-----')
    assetbasketObject.add_to_basket()
    time.sleep(1)
    assetbasketObject._wait(2)
    print('-----打开素材篮-----')
    assetbasketObject.open_basket()
    yield assetbasketObject

