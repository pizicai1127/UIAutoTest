#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/14 11:46 上午
# @Author : cuiguoen
# @File : personal_panel.py


import pytest
from pages.basepage import BasePage

class Personal(BasePage):
    top_elements = [
        {
            "Personal_panel": "//span[@class=\'menu-name\'][text()=\'个人面板\']",
            "Personal_tab": "//li[@title=\"个人面板\"]",
            "my_business": "//div[text()=\"我的业务\"]",
            "my_collect": "//div[text()=\"我的收藏\"]",
            "my_tp": "//div[text()=\"TP\"]",
        },
        {
            "input_person1": "//div[@class=\"_2yYEX\"]/descendant::ul",  # 上面的业务人员框点击下拉
            "technical1": "//span[@title=\"技术部\"]",  # 选择技术部
            "re_revenue": "//div[@role=\"tab\"][text()=\"确认收入\"]",  # 确认收入tab
            "Sign_order": "//div[@role=\"tab\"][text()=\"签单\"]",  # 签单tab

            "input_person2": "//div[@class=\"_2DsrC\"]/descendant::ul",  # 下面的业务人员框点击下拉
            "technical2": "//span[@title=\"技术部\"]",  # 选择技术部
            "look_sop": "//span[text()=\'执行遇到问题？点击查看业务SOP\']",  # 点击打开业务标准SOP参考弹窗
            "animation_class": "//div[text()=\'动画类\']",  # 动画类tab
            "not_associated": "//div[text()=\'未关联签单项目\']",
            "closed_pro": "//div[text()=\'已完结签单项目\']",
        },
        {
            "all_share": "//div[@class=\"_1qHgP\"]/a",
            "create_caselist": "//button[text()=\'新建案例分享列表\']",  # 点击新建案例分享列表按钮
            "input_title": "//input[@placeholder=\"请输入案例分享列表标题\"]",  # 标题
            "input_describe": "//textarea[@placeholder=\"请输入案例分享列表描述\"]",  # 描述
            "button_create": "//button[text()=\"创建\"]",  # 创建按钮
            "create_designerlist": "//button[text()=\"新建创意方分享列表\"]",
            "input_title2": "//input[@placeholder=\"请输入创意方分享列表标题\"]",
            "input_describe2": "//textarea[@placeholder =\"请输入创意方分享列表描述\"]",
            "my_designers": "//div[text()=\"我收藏的创意方\"]",
            "my_cases": "//div[text()=\"我收藏的案例\"]",
            "list1": "//div[@class=\"_X4KVZ\"]/div[1]/div/div/a[1]",
            "button_delete": "//button[text()=\'删除\']",
            "button_delete2": "//div[text()=\'删 除\']",
            "list2": "//div[@class=\"_X4KVZ\"]/div[2]/div/div/a[1]",
        }
    ]


    @pytest.mark.p0
    def my_business(self):
        date = self.top_elements
        self.page.click(date[0]['Personal_panel'])
        self.page.click(date[0]['Personal_tab'])
        self.page.click(date[1]['input_person1']) # 上面的业务人员框点击下拉
        self.page.click(date[1]['technical1'])
        # 通过移动鼠标到空白处点击，关闭弹窗
        self.page.mouse.move(100, 0)
        self.page.mouse.click(100, 0)
        assert1 = self.page.text_content("//div[text()=\'SQL金额\']")
        self.page.click(date[1]['re_revenue'])
        assert2 = self.page.text_content("//div[text()=\'签单确认收入\']")
        self.page.click(date[1]['Sign_order'])
        assert3 = self.page.text_content("//div[text()=\'签单总额\']")

        # 下面的业务人员框
        self.page.reload()  # 刷新一下页面，方便查找下拉选择技术部
        self.page.click(date[1]['input_person2'])  # 下面的业务人员框点击下拉
        self.page.click(date[1]['technical2'])
        self.page.mouse.move(100, 0)
        self.page.mouse.click(100, 0)
        assert4 = self.page.text_content("//span[text()=\'项目面板\']")
        self.page.click(date[1]['look_sop'])
        self.page.click(date[1]['animation_class'])
        assert5 = self.page.text_content("//div[text()=\'业务标准SOP参考\']")
        self.page.reload()
        self.page.click(date[1]['not_associated'])
        self.page.click(date[1]['closed_pro'])
        return assert1,assert2,assert3,assert4,assert5

    def my_collect(self):
        date = self.top_elements
        self.page.click(date[0]["my_collect"])
        self.page.click(date[2]['all_share'])
        assert6 = self.page.text_content("//div[text()=\'案例分享列表\']")
        self.page.go_back()

        # 新建案例分享列表
        self.page.click(date[2]['create_caselist'])
        self.page.fill(date[2]['input_title'],'新建一个测试的案例分享列表')
        self.page.fill(date[2]['input_describe'],'一个案例列表描述')
        self.page.click(date[2]['button_create'])
        # 新建创意方分享列表
        self.page.click(date[2]['create_designerlist'])
        self.page.fill(date[2]['input_title2'], '新建一个测试的创意方分享列表')
        self.page.fill(date[2]['input_describe2'], '这是一个创意方列表的描述')
        self.page.click(date[2]['button_create'])
        self.page.click(date[2]['my_cases'])
        self.page.click(date[2]['my_designers'])
        # 删除创建的案例分享列表和创意方分享列表
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[2]['list1'])
        new_page = new_page_info.value
        new_page.click(date[2]['button_delete'])
        new_page.close()
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[2]['list2'])
        new_page2 = new_page_info.value
        new_page2.click(date[2]['button_delete'])
        new_page2.close()
        return assert6


