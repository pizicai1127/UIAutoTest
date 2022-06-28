#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 5:33 下午
# @Author : cuiguoen
# @File : mall_operation1.py.py

import pytest
from pages.basepage import BasePage

class SKU_TPU(BasePage):
    # 商城运营菜单下的sku/tpu
    top_elements =[
        {
            "Mall_operation": "//span[text()=\'商城运营\']",
            "SKU_category": "//span[text()=\'SPU品类\']",
            "create_category": "//button[text() = '新增品类']",
            "input_name": "//input[@placeholder= '请填写品类名称']",
            "choose_fa": "//div[@class=\"ant-form-item-control has-success\"]/span/span/i",
            "fa1": "//li[@title=\"视频类\"]",
            "choose_lessee": "//div[text()= \'如果不指定租户，请填写 platform\']",
            "lessee1": "//li[text()=\"platform\"]",
            "button_ensure": "//button[text()=\'确 定\']",
            "button_edit": "//td[text()=\"test新品类\"]/following-sibling::td[4]/div/button",  # 编辑按钮
            "button_cancel": "//button[text()=\'取 消\']",
            "button_delete": "//td[text()=\"test新品类\"]/following-sibling::td[4]/button",  # 删除按钮
            "Standard_SPU": "//div[text()= '标准SPU分类']",
        },
        {
            "SPU_SKU": "//span[text()=\'SPU/SKU\']",
            "input_name1": "//input[@placeholder=\"请输入商品SKU名称\"]",
            "only_on": "//span[text()=\'仅上架\']",
            "button_inquire": "//button[text()=\'查询\']",
            "marketplace_SPU": "//div[text()= \'租户商城SPU\']",
            "input_name2": "//input[@placeholder=\"请输入SPU名称\"]",
            "choose_lessee": "//div[text()= \'选择租户\']",
            "lessee1": "//li[text() = \'platform\']",
            "button_inquire2": "//div[@class=\"ant-col ant-col-18 ant-col-offset-3\"]/button[1]",  # 查询按钮
            "button_reset2": "//div[@class=\"ant-col ant-col-18 ant-col-offset-3\"]/button[2]",  # 重置按钮
            "lite_SPU": "//div[text()= \'Lite商城SKU\']",
            "standard_SPU": "//div[text()= \'标准SPU\']",
            "input_name3": "//input[@placeholder=\"请输入标准SKU名称\"]",
        },
        {
            "TPU": "//span[text()=\'TPU\']",
            "TPU_name": "//input[@placeholder=\"请输入 TPU 名称\"]",
            "TPU_ids": "//input[@placeholder=\"输入英文分号检索多个ID\"]",
            "button_inquire": "//button[text()=\'查询\']",
            "button_create": " // button[text() =\'新建\']",
            "choose_classify": "//div[text()= \'请选择\']",
            "classify1": "//li[text()= \'动画/3D\']",
            "subcategory": "//div[text()=\"子分类*\"]/following-sibling::div[1]",
            "2D": "//li[text()= \'2D动画\']",
            "input_name": "//div[@class=\"ant-table-body\"]//tbody//td[1]/div/textarea",  # TPU名称
            "input_describe": "//div[@class=\"ant-table-body\"]//tbody//td[2]/div/textarea",  # 描述
            "choose_unit": "//div[@class=\"ant-table-body\"]//tbody//td[11]/div/div/div/div",  # 单位
            "unit": "//li[text()= \"套\"]",
            "button_save": "//button[text()= \"保 存\"]",
            "button_delete": "//tbody[@class=\"ant-table-tbody\"]/tr[1]/td[2]/div/button[2]",
            "Yes_button": "//div[text()= \"是\"]",

        }
    ]

    @pytest.mark.p0
    def SKU_category(self):
        # SPU品类菜单
        date = self.top_elements
        self.page.click(date[0]['Mall_operation'])
        self.page.click(date[0]['SKU_category'])
        self.page.click(date[0]['create_category'])
        self.page.fill(date[0]['input_name'],'test新品类')
        self.page.click(date[0]['choose_lessee'])
        self.page.click(date[0]['lessee1'])
        self.page.click(date[0]['button_ensure'])
        self.page.reload()
        '''
        # 删除品类
        page.click(date[0]['button_edit'])
        page.click(date[0]['button_cancel'])
        page.reload()
        page.click(date[0]['button_delete'])
        page.click(date[0]['button_ensure'])
        '''
        self.page.click(date[0]['Standard_SPU'])
        assert1 = self.page.text_content("//td[text()= '海报 / kv']")
        return assert1

    @pytest.mark.p0
    def SPU_SKU(self):
        # SPU/SKU菜单
        date = self.top_elements
        self.page.click(date[1]['SPU_SKU'])
        self.page.fill(date[1]['input_name1'],"视频")
        self.page.click(date[1]['only_on'])
        self.page.click(date[1]['button_inquire'])
        self.page.click(date[1]['marketplace_SPU'])
        self.page.fill(date[1]['input_name2'], "视频")
        self.page.click(date[1]['choose_lessee'])
        self.page.click(date[1]['lessee1'])
        self.page.click(date[1]['button_inquire2'])
        self.page.click(date[1]['button_reset2'])
        self.page.click(date[1]['lite_SPU'])
        self.page.reload()
        self.page.click(date[1]['standard_SPU'])
        self.page.fill(date[1]['input_name3'],"测试")
        self.page.click(date[1]['button_inquire2'])

    @pytest.mark.p0
    def TPU(self):
        # TPU菜单
        date = self.top_elements
        self.page.click(date[2]['TPU'])
        self.page.fill(date[2]['TPU_name'],"测试")
        self.page.fill(date[2]['TPU_ids'], "511")
        self.page.click(date[2]['button_inquire'])
        # 新建tpu
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[2]['button_create'])
        new_page = new_page_info.value
        new_page.click(date[2]['choose_classify'])
        new_page.click(date[2]['classify1'])
        new_page.click(date[2]['subcategory'])
        new_page.click(date[2]['2D'])
        new_page.click(date[2]['input_name'])
        new_page.fill(date[2]['input_name'], "test测试")
        new_page.click(date[2]['input_describe'])
        new_page.fill(date[2]['input_describe'], "test测试描述")
        new_page.click(date[2]['choose_unit'])
        new_page.click(date[2]['unit'])
        new_page.click(date[2]['button_save'])
        # 删除tpu
        new_page.wait_for_timeout(1000)
        if new_page.is_visible(date[2]['button_delete']):
            new_page.click(date[2]['button_delete'])
            new_page.click(date[2]['Yes_button'])
        else:
            print("创建tpu失败")




