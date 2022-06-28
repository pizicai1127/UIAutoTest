#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 2:33 下午
# @Author : cuiguoen
# @File : creatives1.py


import pytest
from pages.basepage import BasePage

class Share_list(BasePage):
    # 分享列表管理菜单
    top_elements =[
        {
            "Case_Creativer": "//span[text()=\'案例/创意方\']",
            "Share_list": "//span[text()=\'分享列表管理\']",
            "create_case_lists": "//button[text() = \'新建案例分享列表\']",
            "input_title": "//input[@placeholder=\"请输入案例分享列表标题\"]",
            "input_detail": "//textarea[@placeholder=\"请输入案例分享列表描述\"]",
            "button_create": "//button[text() = \'创建分享列表\']",
            "choose_title": "//input[@placeholder=\"请输入标题\"]",
            "button_inquire": "//button[text() = \'查询\']",
            "case_list1": "//div[@class=\"panel-content\"]/div/div/div[1]/div/div/div[1]",  # 点击某一个案例分享列表
            "Add_case": "//button[text()=\'添加案例\']",
            "choose_one_case": "//div[@class=\"ant-row\"]/div[1]/div/div[2]/i",  # 添加案例的列表里第一个案例
            "button_ensure": "//button[text() = \'确 定\']",
            "button_delete": "//button[text()=\"删除\"]",
            "ensure_delete": "//div[text()=\"删 除\"]",
        },
        {
            "designers_list": "//div[text()=\'创意方分享列表\']",
            "create_designer_lists": "//button[text() = \'新建创意方分享列表\']",
            "input_title2": "//input[@placeholder=\"请输入创意方分享列表标题\"]",
            "input_detail2": "//textarea[@placeholder=\"请输入创意方分享列表描述\"]",
            "button_create2": "//button[text() = \'创建分享列表\']",
            "button_authorization": "//button[text() = \'授权\']",
            "button_switch": "//button[@role=\"switch\"]",
            "add_classify": "//button[text()=\"添加分类\"]",
            "input_name": "//input[@placeholder=\"请输入分类名称\"]",
            "input_title": "//input[@placeholder=\"请输入分类描述\"]",
            "button_save": "//button[text()=\"保 存\"]",
            "button_delete": "//div[@class=\"body_header_operatorWarp\"]/button[1]",
            "ensure_delete": "//div[text()=\"删 除\"]",
        },

    ]

    @pytest.mark.p0
    def case_lists (self):
        # 案例分享列表
        date = self.top_elements
        self.page.click(date[0]['Case_Creativer'])
        self.page.click(date[0]['Share_list'])
        self.page.click(date[0]['create_case_lists'])
        self.page.fill(date[0]['input_title'],"新建案例分享列表标题test")
        self.page.fill(date[0]['input_detail'], "案例分享列表描述test")
        aseert1 = self.page.text_content("//div[text()=\'新建案例分享列表\']")
        self.page.click(date[0]['button_create'])
        self.page.click(date[0]['Share_list'])
        self.page.fill(date[0]['choose_title'], "案例")
        self.page.click(date[0]['button_inquire'])
        # 点击某一个案例分享列表
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[0]["case_list1"])
        self.new_page = new_page_info.value
        self.new_page.click(date[0]['Add_case'])
        self. new_page.click(date[0]['choose_one_case'])
        self.new_page.click(date[0]['button_ensure'])

        self.new_page.reload()
        self.new_page.click(date[0]['button_delete'])
        self.new_page.click(date[0]['ensure_delete'])
        return aseert1

    @pytest.mark.p0
    def designer_lists(self):
        # 创意方分享列表
        date = self.top_elements
        self.page.click(date[0]['Share_list'])
        self.page.click(date[1]['designers_list'])
        self.page.click(date[1]['create_designer_lists'])
        self.page.fill(date[1]['input_title2'], "新建创意方分享列表标题test2")
        self.page.fill(date[1]['input_detail2'], "新建创意方列表描述test2")
        aseert2 = self.page.text_content("//div[text()=\'新建创意方分享列表\']")
        self.page.click(date[1]['button_create2'])
        self.page.click(date[1]['button_authorization'])
        self.page.click(date[1]['button_switch'])
        self.page.mouse.click(100,0)
        self. page.click(date[1]['add_classify'])
        self.page.fill(date[1]['input_name'], "分类名称test2")
        self.page.fill(date[1]['input_title'], "分类描述test2")
        self.page.click(date[1]['button_save'])
        self.page.click(date[1]['button_delete'])
        self.page.click(date[1]['ensure_delete'])
        return aseert2








