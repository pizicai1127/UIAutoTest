#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : ms_login.py

from pages.basepage import BasePage


class LoginPage(BasePage):

    # 登录页 元素
    selectors = {

        "account": "//input[@placeholder=\"邮箱/手机\"]",  # 登录页 -账号输入框
        "password": "//input[@placeholder=\"密码\"]",  # 登录页-，密码输入框
        "checkbox": "//input[@class=\"ant-checkbox-input\"]",  # 登录页面-（我已阅读并同意《用户协议》及隐私政策）
        "login_btn": "//button[text()=\"登录\"]"  # 登录页-登录按钮

    }
    def go_to_tenant(self, tenant_id):
        """输入租户登录地址"""
        # 打开生产租户
        self.page.goto(tenant_id)

    def home_login(self, account, password):
        """用户登录流程"""
        self.page.fill(LoginPage.selectors['account'], account)
        # # 输入密码
        self.page.fill(LoginPage.selectors['password'], password)
        # # 勾选 用户协议
        self.page.click(LoginPage.selectors['checkbox'])
        # # 点击 登录按钮
        self.page.click(LoginPage.selectors['login_btn'])

        # 等待3s
        self.page.wait_for_timeout(3000)
