#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 6:27 下午
# @Author : cuiguoen
# @File : member_management.py


import pytest
from pages.basepage import BasePage

class Member_management(BasePage):
    # 后台成员管理 菜单
    top_elements = [
        {
            "Member_management": "//span[text()=\'后台成员管理\']",
            "role_list": "//span[text()=\'角色列表\']",
            "experience_account": "//div[text()=\'体验账号\']",
            "button_create": "//button[text()=\"创建角色\"]",
            "button_cancel": "//button[text()=\"取 消\"]",
            "operate": "//div[text()=\"操作\"]",
        },
        {
            "Account_grouping": "//span[text()=\'Account分组\']",
            "group_name": "//td[text()=\"吴天红\"]",
            "edit": "//tbody/tr[1]//span[text()=\"编辑\"]",
            "button_add": "//button[text()=\"添加\"]",
        },

    ]

    @pytest.mark.p0
    def role_list(self):
        # 角色列表 菜单
        date = self.top_elements
        self.page.click(date[0]['Member_management'])
        self.page.click(date[0]['role_list'])
        self.page.click(date[0]['experience_account'])
        self.page.click(date[0]['button_create'])
        self.page.click(date[0]['button_cancel'])
        self.page.click(date[0]['operate'])


    @pytest.mark.p0
    def account_grouping(self):
        # Account分组 菜单
        date = self.top_elements
        self.page.click(date[1]['Account_grouping'])
        self.page.click(date[1]['group_name'])
        self.page.click(date[1]['edit'])
        self.page.click(date[1]['button_add'])
        self.page.reload()







