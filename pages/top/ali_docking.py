#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : ali_docking.py


import pytest
from pages.basepage import BasePage

class Alidocking(BasePage):
    top_elements = [
        {
            "Ali_docking": "//span[text()=\'阿里对接\']",
            "Demand_orders": "//span[text()=\'需求订单\']",
            "input_name": "//div[@class=\"_1Kt8r\"]/div[1]/div[1]//input[1]",
            "input_people": "//div[@class=\"_1Kt8r\"]/div[2]/div[1]//input[1]",
            "button_search": "//button[text()=\'搜 索\']",
            "process_demand": "//span[text()=\'处理需求\']",
            "modify_amount": "//span[text()=\'修改金额\']",
            "input_amount": "//input[@placeholder=\"请输入修改后的金额（元）\"]",
            "button_ensure": "//button[text()=\"确 定\"]",
        },
        {
            "Set_configuration": "//span[text()=\'套餐配置\']",
            "button_create": "//button[text()=\'新建套餐\']",
            "input_name": "//input[@placeholder=\"请输入套餐名称\"]",
            "input_describe": "//textarea[@placeholder=\"请输入套餐描述\"]",
            "add_materiel": "//a[text()=\"+增加物料\"]",
            "choose_materiel": "//span[@class=\"ant-cascader-picker-label\"]",
            "choose1": "//li[@title=\"文案撰写\"]",
            "choose2": "//li[@title=\"slogan\"]",
            "choose3": "//li[@title=\"复杂\"]",
            "button_save": "//span[text()=\"保 存\"]",
            "input_word": "//input[@placeholder=\"请输入套餐名称或描述的关键字\"]",
            "icon_search": "//span[@class=\"ant-input-suffix\"]",
            "icon_delete": "//a[text()=\"删除\"]",
            "button_ensure": "//button[text()=\"确 定\"]",
        },
        {
            "Category_configuration": "//span[text()=\'品类配置\']",
            "Edit_parent": "//tr[@data-row-key=\"34\"]//button[text()=\'编辑父品类\']",
            "input_name": "//input[@placeholder=\"请填写品类名称\"]",
            "button_ensure": "//button[text()=\"确 定\"]",
            "create_subcategory": "//tr[@data-row-key=\"34\"]//button[text()=\'新建子品类\']",
            "icon_pull": "//tr[@data-row-key=\"34\"]/td[1]/div[1]",
            "icon_delete": "//a[text()=\"删除\"]",
        },
    ]



    @pytest.mark.p0
    def demand_orders(self):
        # 需求订单 菜单
        date = self.top_elements
        self.page.click(date[0]['Ali_docking'])
        self.page.click(date[0]['Demand_orders'])
        self.page.fill(date[0]['input_name'],"ceshiali")
        self.page.fill(date[0]['input_people'], "测试哈哈23")
        self.page.click(date[0]['button_search'])
        assert1 = self.page.text_content("//label[text() = \'需求名称\']")
        return assert1


    @pytest.mark.p0
    def set_configuration(self):
        # 套餐配置 菜单
        date = self.top_elements
        self.page.click(date[1]['Set_configuration'])
        self.page.click(date[1]['button_create'])
        self.page.fill(date[1]['input_name'], 'test套餐')
        self.page.fill(date[1]['input_describe'], 'test套餐')
        self.page.click(date[1]['add_materiel'])
        self.page.click(date[1]['choose_materiel'])
        self.page.click(date[1]['choose1'])
        self.page.click(date[1]['choose2'])
        self.page.click(date[1]['choose3'])
        self.page.click(date[1]['button_save'])

        self.page.fill(date[1]['input_word'], 'test套餐')
        self.page.click(date[1]['icon_search'])
        self.page.click(date[1]['icon_delete'])
        self.page.click(date[1]['button_ensure'])
        self.page.reload()


    @pytest.mark.p0
    def category_configuration(self):
        # 品类配置 菜单
        date = self.top_elements
        self.page.click(date[2]['Category_configuration'])
        self.page.reload()
        self.page.wait_for_timeout(2000)
        # 编辑父品类
        self.page.click(date[2]['Edit_parent'])
        self.page.fill(date[2]['input_name'],'ryna测试')
        assert3 = self.page.text_content("//div[@id=\"rcDialogTitle0\"]")
        self.page.click(date[2]['button_ensure'])
        self.page.reload()
        # 新建子品类
        self.page.click(date[2]['create_subcategory'])
        self.page.fill(date[2]['input_name'], 'test品类名称')
        self.page.click(date[2]['button_ensure'])
        self.page.reload()
        # 删除子品类
        self.page.click(date[2]['icon_pull'])
        if self.page.is_visible(date[2]['icon_delete']):
            self.page.click(date[2]['icon_delete'])
            self.page.click(date[2]['button_ensure'])
        else:
            print('no subcategories')

        return assert3