# # -*- coding: utf-8 -*-
# # @Time : 2022/1/25 2:31 下午
# # @Author : liuzhijie
# # @File : conftest.py
#
# import pytest
# from playwright.sync_api import Page
# from conf.confs import url_collectionPage
# from pages.assets.AssetGroupPage import AssetGroupPage
# from conf.confs import Host2
# from conf.confs import account
# from conf.confs import password
# from pages.user_center.login_page import AssetLoginPage
#
#
#
# @pytest.fixture(scope='function', autouse=True)
# def login_init(page: Page):
#     """
#      正常登录流程测试
#     """
#     # 登陆
#     loginObject = AssetLoginPage(page)
#     loginObject.login(Host2, account, password)
#     print('-----登陆初始化完成-----')
#     yield page
#
# @pytest.fixture(scope='function')
# def asset_init(login_init):
#     """
#     进入素材组页面
#     """
#     assetGroupObject = AssetGroupPage(login_init)
#     assetGroupObject._go(url_collectionPage)
#     print('-----进入素材库页面-----')
#     yield assetGroupObject
#
#
