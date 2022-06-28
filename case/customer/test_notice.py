#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/28 11:28 上午
# @File : test_notice.py
from pages.customer.NoticePage import NoticePage
import pytest


class TestNotice:

    # 查看偏好设置
    def test_makesettings(self,test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/setting")
        page = NoticePage(test_login_btn[0])
        page.make_settings()

    # 查看站内信
    def test_mail(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/setting")
        page = NoticePage(test_login_btn[0])
        page.mail()

    # 查看项目动态
    def test_project_dynamics(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/setting")
        page = NoticePage(test_login_btn[0])
        page.project_dynamics()