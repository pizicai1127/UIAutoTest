#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : myproduct.py

import pytest
from pages.basepage  import BasePage

class Mypro(BasePage):
    find_elements = [
        {
            # '我的项目'页的元素
            "myproject": "//div[text() = \'我的项目\']",
            "input_day": "//input[@placeholder = \'开始日期\']",
            "start_day": "//input[@class=\"ant-calendar-input \" and @placeholder=\"开始日期\"]",
            "end_day": "//input[@class=\"ant-calendar-input \" and @placeholder=\"结束日期\"]",
            "all_pro": "//button[contains(text(),\'全部\')]",
            "assess_pro": "//button[contains(text(),\'评估中\')]",
            "continue_pro": "//button[contains(text(),\'已承接\')]",
            "delivered_pro": "//button[contains(text(),\'已交付\')]",
            "completeed_pro": "//button[contains(text(),\'已完成\')]",
            "recalled_pro": "//button[contains(text(),\'已撤回\')]",
            "View_button": "//tbody/tr[1]/td/button[text()=\'查看\']",  # 第一个查看按钮
            "Recalled_button": "//tbody/tr[2]/td/button[text()=\'撤回\']",  # 第二个撤回按钮
            "edit_button": "//button[text()=\'编辑\']",
            "project_name": "//input[@placeholder=\"请输入文字，最多30个汉字\"]",  # 下单弹框的项目名称
            "project_overview": "//div[contains(@placeholder,\"为了便于为您\")]",  # 下单弹框的项目概述
            "Supplemental_Information": "//div[text()=\"补充信息\"]",  # 下单弹框的补充信息线
            "delivery_time": "//input[@placeholder=\"选填\"]",  # 下单弹框的交付时间
            "time_today": "//a[text()=\"Today\"]",  # 下单弹框的交付时间选择今天
            "budget": "//input[starts-with(@placeholder,\"选填，可在项目\")]",  # 预算
            "ensure_button": "//button[text()=\'确定\']",
            "Reason_withdrawal": "//textarea[@placeholder=\'请输入文字\']"  # 撤回原因
        },
    ]

    def mypro_all(self):  # 我的项目
        date = self.find_elements
        self.page.click(date[0]["myproject"])  # 切换到'我的项目'页

        self.page.click(date[0]["input_day"])  # 调起日期输入框
        self.page.click(date[0]["start_day"])
        self.page.fill(date[0]["start_day"],"2022-02-20")
        self.page.click(date[0]["end_day"])
        self.page.fill(date[0]["end_day"], "2022-03-20")
        self.page.keyboard.press("Enter")

        self.page.click(date[0]["all_pro"])

    def mypro_assess(self):  # 编辑评估中的项目
        date = self.find_elements
        self.page.click(date[0]["assess_pro"])  # 切换tab
        self.page.click(date[0]["View_button"])
        assert1 = self.page.text_content("//div[text()=\'评估中\']")

        self.page.click(date[0]["edit_button"])  # 编辑项目详情
        self.page.fill(date[0]["project_name"], "更新项目详情")  # 填写项目名称
        self.page.fill(date[0]["project_overview"], "更新一下测试项目概述")  # 填写项目概述
        self.page.click(date[0]["delivery_time"])
        self.page.click(date[0]["time_today"])  # 时间选择今天
        self.page.fill(date[0]["budget"], "1100")  # 预算填写1100
        self.page.click(date[0]["ensure_button"])
        assert2 = self.page.text_content("text = 更新成功")
        assert3 = self.page.text_content("//span[text()=\'更新项目详情\']")
        # 通过移动鼠标到空白处点击，关闭下单成功弹窗
        self.page.mouse.click(100, 0)
        return assert1,assert2,assert3

    def mypro_recalled(self):
        # 项目撤回
        date =  self.find_elements
        self.page.click(date[0]["Recalled_button"])
        assert4 = self.page.text_content("//div[text()=\'是否确认撤回项目\']")
        self.page.fill(date[0]["Reason_withdrawal"],"这是测试撤回原因")
        self.page.click(date[0]["ensure_button"])
        assert5 = self.page.text_content("text = 撤回成功")
        # 切换各个tab
        self.page.click(date[0]["continue_pro"])
        self.page.click(date[0]["View_button"])
        assert6 = self.page.text_content("//div[text()=\'已承接\']")
        self.page.hover("//div[text()=\'已承接\']")
        self.page.mouse.click(100, 0)
        self.page.click(date[0]["delivered_pro"])
        assert7 = self.page.text_content("//span[text()=\'需求名称\']")
        self.page.click(date[0]["completeed_pro"])
        assert8 = self.page.text_content("//span[text()=\'需求名称\']")
        # 已撤回/取消tab，第一个项目是已撤回，此页面列表是按时间倒序排列
        self.page.click(date[0]["recalled_pro"])
        self.page.click(date[0]["View_button"])
        assert9 = self.page.text_content("//div[text()=\'已撤销\']")
        self.page.hover("//div[text()=\'已撤销\']")
        self.page.mouse.click(100, 0)
        return assert4,assert5,assert6,assert7,assert8,assert9

