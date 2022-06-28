#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 6:01 下午
# @Author : cuiguoen
# @File : mall_operation2.py



import pytest
from pages.basepage import BasePage


class SKU_TPU2(BasePage):
    # 商城运营菜单下的
    top_elements = [
        {
            "Mall_operation": "//span[text()=\'商城运营\']",
            "MetaData": "//span[text()=\'MetaData\']",
            "input_type": "//input[@placeholder=\"请输入Metadata 类型\"]",
            "input_value": "//input[@placeholder=\"请输入 Metadata 值\"]",
            "button_inquire": "//button[text() = \'查询\']",
        },
        {
            "Solution_disposition": "//span[text()=\'商城Solution配置\']",
            "button_edit": "//tbody/tr[1]/td[7]/div/div[1]/button",
            "input_title1": "//*[@id=\"rc-root\"]/div/div[2]/div/div[3]/div[2]/div[2]/input",
            "input_describe": "//input[@placeholder=\"请输入简短的一句话描述\"]",
            "button_ensure": "//button[text()=\"保存\"]",
        },
        {
            "Calendar_disposition": "//span[text()=\'营销日历配置\']",
            "is_Published": "//span[text()=\'已发布\']",
            "button_check": "//tbody/tr[1]/td[1]/a",
            "button_add": "//button[text() = '添加']",
            "input_name": "//input[@placeholder=\"请输入事件名称\"]",
            "input_date": "//input[@placeholder=\"请选择日期\"]",
            "today": "//a[text()=\'今天\']",
            "input_remark": "//input[@placeholder=\"请控制在200字以内\"]",
            "status": "//span[text()=\'关闭\']",
            "create_save": "//button[text() = '保 存']",
            "button_delete": "//button[text() =\'删除\']",
        },
    ]

    @pytest.mark.p0
    def metaData(self):
        # MetaData菜单
        date = self.top_elements
        self.page.click(date[0]['Mall_operation'])
        self.page.click(date[0]['MetaData'])
        self.page.fill(date[0]['input_type'], '服务')
        self.page.fill(date[0]['input_value'], '服务')
        self.page.click(date[0]['button_inquire'])
        assert1 = self.page.text_content("//td[text()=\"服务类型\"]")
        return assert1



    @pytest.mark.p0
    def solution_disposition(self):
        # 商城Solution配置的菜单
        date = self.top_elements
        self.page.click(date[1]['Solution_disposition'])
        self.page.click(date[1]['button_edit'])  # 选择第一个Solution编辑
        self.page.fill(date[1]['input_title1'], "预发测试封面标题test")
        self.page.fill(date[1]['input_describe'], "中国发展起来")
        self.page.click(date[1]['button_ensure'])
        self.page.reload()

    @pytest.mark.p0
    def calendar_disposition(self):
        # 营销日历配置的菜单
        date = self.top_elements
        self.page.click(date[2]['Calendar_disposition'])
        self.page.click(date[2]['is_Published'])

        # 添加日历事件
        self.page.click(date[2]['button_check'])
        self.page.click(date[2]['button_add'])
        self.page.fill(date[2]['input_name'],"test1")
        self.page.click(date[2]['input_date'])
        self.page.click(date[2]['today'])
        self.page.fill(date[2]['input_remark'], "test_remark")
        self.page.click(date[2]['status'])
        self.page.click(date[2]['create_save'])
        self.page.reload()
        self.page.click(date[2]['button_delete'])


