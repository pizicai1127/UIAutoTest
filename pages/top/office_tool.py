#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/14 11:07 上午
# @Author : cuiguoen
# @File : office_tool.py.py

import pytest
from pages.basepage import BasePage

class Office_tool(BasePage):
    # 中台工具 菜单
    top_elements = [
        {
            "Office_tool": "//span[text()=\'中台工具\']",
            "NPS_questionnaire": "//span[text()=\'NPS问卷\']",
            "button_create": "//button[text() = \'新建\']",
            "input_name": "//input[@placeholder=\"NPS调查问卷名称\"]",
            "button_cancel": "//button[text() = \'取 消\']",
            "button_update": "//tbody/tr[1]//a[text()=\"更新\"]",
        },
        {
            "verification_code": "//span[text()=\'查询验证码\']",
            "input_name": "//input[@placeholder=\"输入注册时用的手机号码\"]",
            "button_inquire": "//button[text() = \'查询\']",
            "button_reset": "//button[text() = \'重置\']",
        },

    ]



    @pytest.mark.p0
    def NPS_questionnaire(self):
        # NPS问卷 菜单
        date = self.top_elements
        self.page.click(date[0]['Office_tool'])
        self.page.click(date[0]['NPS_questionnaire'])
        self.page.click(date[0]['button_create'])
        self.page.fill(date[0]['input_name'], 'test')
        self.page.click(date[0]['button_cancel'])
        self.page.click(date[0]['button_update'])
        self.page.click(date[0]['button_cancel'])

    @pytest.mark.p0
    def verification_code(self):
        # 查询验证码 菜单
        date = self.top_elements
        self.page.click(date[1]['verification_code'])
        self.page.fill(date[1]['input_name'], '13817885701')
        self.page.click(date[1]['button_inquire'])
        self.page.click(date[1]['button_reset'])

