#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/11 2:51 下午
# @File : PersonalCenterPage.py
from pages.express.ExpressBasePage import ExpressBasePage


class PersonalCenterPage(ExpressBasePage):
    selectors = {
        # 头像
        "head_portrait": "#root > header > div > div.expressNavBarInnerRight___1UBSq > div > div > i > svg",
        # 我的项目
        "my_project": "body > div:nth-child(11) > div > div > ul > li:nth-child(2) > div",
        # 我的点赞
        "my_fabulous": "body > div:nth-child(11) > div > div > ul > li:nth-child(3) > div",
        # 我收到的内容
        "my_context": "body > div:nth-child(11) > div > div > ul > li:nth-child(4) > div",
        # 账号设置
        "account_setting": "body > div:nth-child(11) > div > div > ul > li:nth-child(6) > div",
        # 帮助
        "help_btn": "body > div:nth-child(11) > div > div > ul > li:nth-child(7) > div",
        # 点击案例合集
        "case_btn": "#root > div > div > div > div > div.list___1JrC5 > div > div > div > div:nth-child(1) > div > div.content___26Fiw > div.bottom___2BKx7 > span",
        # 我收到的内容面包屑
        "accept_context": "text=我收到的内容",
        # 我的点赞
        "my_fabulous_btn": "#root > div > div > div > div > div.ant-radio-group.ant-radio-group-outline > label:nth-child(1) > span:nth-child(2)",
        # 是我的点赞案例
        "my_fabulous_case": "#root > div > div > div > div > div.list___1JrC5 > div > div > div > div:nth-child(1) > div > div.content___3i9oc > div.bottom___2-Gtv",

        "inquiry_btn": "text=立即咨询",

        "cancel_btn": "text=取 消",

        "setting_btn": 'text=账号信息设置',

        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",

    }

    def my_content(self):
        # 鼠标悬浮头像
        self.page.hover(PersonalCenterPage.selectors['head_portrait'])
        # # 点击我的项目
        # self.page.click(PersonalCenterPage.selectors['my_project'])
        # 点击我收到的内容
        self.page.click(PersonalCenterPage.selectors['my_context'])

        # # 点击帮助
        # self.page.click(PersonalCenterPage.selectors['help_btn'])
        self._wait(1)
        # 点击我收到的内容第一个
        self.page.click(PersonalCenterPage.selectors['case_btn'])
        self._wait(1)
        # 点击面包屑返回
        self.page.click(PersonalCenterPage.selectors['accept_context'])
        self._wait(1)
        # 点击我的点赞Tab
        self.page.click(PersonalCenterPage.selectors['my_fabulous_btn'])
        # 点击我的点赞案例
        with self.page.expect_popup() as popup_info:
            self.page.click(PersonalCenterPage.selectors['my_fabulous_case'])
            self._wait(2)
        page1 = popup_info.value
        page1.click(PersonalCenterPage.selectors['inquiry_btn'])
        page1.click(PersonalCenterPage.selectors['cancel_btn'])

    def my_fabulous(self):
        # 鼠标悬浮头像
        self.page.hover(PersonalCenterPage.selectors['head_portrait'])
        # 点击我的点赞
        self.page.click(PersonalCenterPage.selectors['my_fabulous'])

    def account_setting(self):
        # 鼠标悬浮头像
        self.page.hover(PersonalCenterPage.selectors['head_portrait'])
        # 点击账号设置
        self.page.click(PersonalCenterPage.selectors['account_setting'])
        # 点击账号设置
        with self.page.expect_popup() as popup_info:
            self.page.click(PersonalCenterPage.selectors['setting_btn'])
        page2 = popup_info.value
        page2.close()
