#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/14 11:16 上午
# @Author : cuiguoen
# @File : official_website.py

import pytest
from pages.basepage import BasePage

class Official_website(BasePage):
    # 官网消息&招聘 菜单
    top_elements = [
        {
            "Official_website": "//span[text()=\'官网消息&招聘\']",
            "news_list": "//span[text()=\'消息列表\']",
            "news_status": "//span[text()=\'已发布\']",
            "button_view": "//tbody/tr[1]//a",
            "title": "//div[text()=\'消息管理 - 站内站外消息管理 - 详情\']",
            "button_create": "//button[text() = \'新建消息\']",
            "input_name": "//input[@placeholder=\"请输入消息主题\"]",
            "button_save": "//button[text() = \'保 存\']",
            "input_title": "//input[@placeholder=\"邮件主题\"]",
            "inside_news": "//span[text()=\'站内信\']",
            "button_save2": "//button[text() = \'保存至草稿\']",
            "button_delete": "//tbody/tr[1]//a[text()=\'删除\']",
            "button_ensure": "//button[text() = \'确 定\']",
        },
        {
            "Website_Announcements": "//span[text()=\'网站公告\']",
            "button_create": "//button[text()=\'新建\']",
            "input_content,": "//input[placeholder=\"内容300字以内\"]",
            "Distribution_channels": "//span[text()=\'企业客户前台\']",
            "button_cancel": "//button[text() = \'取 消\']",
            "ad": "//span[text() = \'公告\']",
        },
        {
            "Customer_message": "//span[text()=\'客户留言\']",

            "Message_status": "//span[text()=\'已关闭\']",
            "input_name": "//input[@placeholder=\"公司名称/客户姓名/电话/邮箱\"]",
            "button_inquire": "//button[text() = \'查询\']",
            "button_add": "//tbody/tr[1]/td[1]//span[text() = \'添加\']",
            "input_remark": "//input[@placeholder=\"请控制在1000字以内\"]",
            "button_save": "//button[text() = \'保 存\']",
        },
    ]


    @pytest.mark.p0
    def news_list(self):
        # 消息列表 菜单
        date = self.top_elements
        self.page.click(date[0]['Official_website'])
        self.page.click(date[0]['news_list'])
        self.page.click(date[0]['news_status'])
        self.page.click(date[0]['button_view'])
        self.page.is_visible(date[0]['title'])
        self.page.go_back()


    @pytest.mark.p0
    def website_Announcements(self):
        # 网站公告 菜单
        date = self.top_elements
        self.page.click(date[1]['Website_Announcements'])
        self.page.click(date[1]['button_create'])
        self.page.click(date[1]['button_cancel'])
        self.page.click(date[1]['ad'])

    @pytest.mark.p0
    def customer_message(self):
        # 客户留言 菜单
        date = self.top_elements
        self.page.click(date[2]['Customer_message'])

        self.page.click(date[2]['Message_status'])
        self.page.click(date[2]['button_inquire'])
        self.page.click(date[2]['button_add'])
        self.page.fill(date[2]['input_remark'], '费洛伊德test')
        self.page.click(date[2]['button_save'])




