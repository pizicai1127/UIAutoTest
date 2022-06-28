#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/11 2:51 下午
# @File : test_pesonal_center.py
from pages.express.PersonalCenterPage import PersonalCenterPage


class TestPersonalCenter:
    def test_my_content(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = PersonalCenterPage(expesss_login)
        page.my_content()

    def test_my_fabulous(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = PersonalCenterPage(expesss_login)
        page.my_fabulous()

    def test_account_setting(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = PersonalCenterPage(expesss_login)
        page.account_setting()