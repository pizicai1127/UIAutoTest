#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : case_creatives2.py


import pytest
from pages.basepage import BasePage

class Case_search(BasePage):
    # 案例搜索菜单
    top_elements =[
        {
            "Case_Creativer": "//span[text()=\'案例/创意方\']",
            "case_search": "//span[text()=\'案例搜索\']",
            "input_keyword": "//input[@placeholder=\"案例名/描述/行业/风格/品牌相关/营销相关/目标受众等\"]",
            "button_search": "//div[@class=\"_34ey1\"]/button",
            "Drop_down": "//div[text()= \'品牌\']//span",  # 品牌下拉按钮
            "ali_option": "//li[text()= \'阿里巴巴\']",
            "first_case": "//div[@class=\"ant-row\"]/div[1]",  # 第一个案例
            "collect": "//div[@class=\"ant-row\"]/div[1]/div/div/div/div[3]/div[1]",  # 第一个案例的收藏/取消收藏

        },
        {
            "Designers_Library": "//span[text()=\'创意方库\']",
            "recommend_tab": "//div[text()= \'推荐创意方\']",  # 推荐创意方tab
            "input_name": "//input[@placeholder=\'创意方名称/企业名称/电话/邮箱/曾用名/风格/行业/品牌\']",
            "Search_icon": "//span[@class=\"ant-input-suffix\"]",  # 搜索图标
            "designers_tab": "//div[text()= \'创意方库\']",  # 创意方库tab
            "input_name2": "//input[@placeholder=\'可搜索各类创意方名称/SKU/电话/邮箱/风格/行业/品牌等\']",
            "Search_icon2": "//input[@placeholder=\"可搜索各类创意方名称/SKU/电话/邮箱/风格/行业/品牌等\"]/following-sibling::span[1]",
            # 搜索图标
            "favorable_tab": "//div[text()= \'好评优先\']",
        },

    ]

    @pytest.mark.p0
    def case_search(self):
        # 案例搜索菜单
        date = self.top_elements
        self.page.click(date[0]['Case_Creativer'])
        self.page.click(date[0]['case_search'])
        self.page.fill(date[0]['input_keyword'],"测试")
        self.page.click(date[0]['button_search'])
        self.page.click(date[0]['Drop_down'])
        self.page.click(date[0]['ali_option'])
        # 第一个案例的收藏/取消收藏
        self.page.hover(date[0]['first_case'])
        self.page.click(date[0]['collect'])
        self.page.wait_for_timeout(1000)
        self.page.click(date[0]['collect'])


    @pytest.mark.p0
    def designers_library (self):
        # 创意方库菜单
        date = self.top_elements
        self.page.click(date[1]['Designers_Library'])
        self.page.click(date[1]['recommend_tab'])
        assert1 = self.page.text_content("//span[text()=\'搜你感兴趣的创意方\']")
        self.page.fill(date[1]['input_name'],"测试")
        self.page.click(date[1]['Search_icon'])
        self.page.click(date[1]['designers_tab'])
        self.page.fill(date[1]['input_name2'], "测试")
        self.page.click(date[1]['Search_icon2'])
        self.page.click(date[1]['favorable_tab'])
        return assert1







