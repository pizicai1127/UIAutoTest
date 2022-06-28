#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 4:00 下午
# @Author : cuiguoen
# @File : CRM01.py.py

import pytest
from pages.basepage import BasePage

class CRM(BasePage):
    top_elements =[
        {
            "CRM": "//span[text()=\'CRM/业务管理\']",
            "sales_lea": "//li[@title=\"销售线索\"]",
            "type_c": "//span[text()=\"C\"]",
            "source_type": "//div[text()=\"来源类型\"]",
            "type2": "//li[text()=\'员工推荐\']",
            "reset": "//button[text()=\'重置\']",
            "new_sales": "//button[text()=\'新建销售线索\']",
            "company": "//div[text()=\'选择已有公司\']",
            "company_choose": "//li[text()=\'测试888\']",
            "department": "//div[text()=\'选择已有部门\']",
            "department_choose": "//li[text()=\'A1\']",
            "contact": "//div[text()=\'选择联系人\']",
            "contact_choose": "//li[text()=\'预发测试1\']",
            "demand_type": "//div[@class=\"ant-modal-body\"]/descendant::span[12]",  # 需求类型 选择"M"
            "source_clues": "//div[@class=\"ant-modal-body\"]/div/div[6]/descendant::div[6]",  # 线索来源
            "clues_choose": "//li[text()=\'员工推荐\']",
            "source_details": "//input[@placeholder=\"填写销售/活动/文章/渠道名称\"]",
            "create_button": "//button[text()=\'创建\']",
            "assigned": "//span[text()= \"已分配\"]",
            "my_clues": "//span[text()= \"我的线索\"]",
            "clue_pool": "//span[text()= \"线索公海池\"]",
        },
        {
            "sales_opportunities": "//span[text()= \"销售机会\"]",
            "input_name": "//input[@placeholder=\"请输入机会名称\"]",
            "opportunities_type": "//div[text()= \"请选择业务类型\"]",
            "content_business": "//li[text()=\"Content业务\"]",
            "company": "//div[text()= \"请选择公司/部门名称\"]",
            "company_choose": "//li[text()=\"A1\"]",
            "more_choose": "//button[text()=\'更多筛选\']",
            "input_money": "//input[@placeholder=\"金额（元）\"]",
            "search": "//button[text()=\'搜索\']",
            "reset": "//button[text()=\'重置\']",
            "button_create": "//button[text()=\'新建销售机会\']",
            "enterprise_name": "//div[@class=\"_n29Q3\"]",
            "company_name": "//li[@label=\"阿里公司\"]",
            "input_name2": "//div[@class=\"ant-modal-body\"]/descendant::input[@placeholder=\"请输入机会名称\"]",
            "input_remark": "//textarea[@placeholder=\"请输入备注信息\"]",
            "choose_sku": "//div[@class=\"ant-modal-body\"]/descendant::div[text()=\"请选择SKU类型\"]",  # 客户意向sku
            "sku_num3": "//li[@title=\"动画 / 3D\"]/label/span/input",  # 客户意向sku选择第三个
            "choose_department": "//div[@class=\"ant-modal-body\"]/descendant::div[text()=\"请选择客户部门\"]",
            "department1": "//li[text()=\"阿里部门\"]",
            "choose_contact": "//div[@class=\"ant-modal-body\"]/descendant::div[text()=\"客户首次联系人\"][2]",
            "contact1": "//li[contains(text(),\"阿里测试\")]",
            "input_sales_amount": "//input[@placeholder=\"请输入预估销售金额（元）\"]",
            "input_project_costs": "//input[@placeholder=\"请输入预估项目成本（元）\"]",
            "choose_date": "//input[@placeholder=\"请选择预计成单日期\"]",
            "choose_today": "//a[text()=\"今天\"]",
            "choose_date2": "//input[@placeholder=\"请选择预估交付时间\"]",
            "button_submit": "//button[text()=\'提交\']",
            "more_option": "//tbody[@class=\"ant-table-tbody\"]/tr[1]/td[1]/span[text()='更多']",
            "delete_button": "//button[text()='删除']",
            "ensure": "//div[text()='确 定']",
        },

    ]

    @pytest.mark.p0
    def sales_lead(self):
        # 销售线索
        date = self.top_elements
        self.page.click(date[0]['CRM'])
        self.page.click(date[0]['sales_lea'])
        self.page.click(date[0]['type_c'])
        self.page.click(date[0]['source_type'])
        self.page.click(date[0]['type2'])
        self.page.mouse.move(100, 0)
        self.page.mouse.click(100, 0)
        self.page.click(date[0]['reset'])
        # 新建销售线索
        self.page.reload()
        self.page.click(date[0]['new_sales'])
        self.page.click(date[0]['company'])
        self.page.click(date[0]['company_choose'])
        self.page.click(date[0]['department'])
        self.page.click(date[0]['department_choose'])
        self.page.click(date[0]['contact'])
        self.page.click(date[0]['contact_choose'])
        self.page.click(date[0]['demand_type'])
        self.page.click(date[0]['source_clues'])
        self.page.click(date[0]['clues_choose'])
        self.page.fill(date[0]['source_details'],"这是新建销售线索的来源详情")
        self.page.click(date[0]['create_button'])
        # 切换tab
        self.page.click(date[0]['clue_pool'])
        assert1 = self.page.text_content("//span[text()= \"移入公海原因\"]")
        return assert1

    @pytest.mark.p0
    def sales_opportunities(self):
        # 销售机会
        date = self.top_elements
        self.page.click(date[1]['sales_opportunities'])
        self.page.click(date[1]['reset'])
        self.page.fill(date[1]['input_name'], "测试")
        self.page.click(date[1]['opportunities_type'])
        self.page.click(date[1]['content_business'])
        self.page.click(date[1]['company'])
        self.page.click(date[1]['company_choose'])
        self.page.click(date[1]['more_choose'])
        self.page.fill(date[1]['input_money'], "100")
        self.page.click(date[1]['search'])
        # 新建销售机会
        self.page.click(date[1]['reset'])
        self.page.reload()
        self.page.click(date[1]['button_create'])
        self. page.click(date[1]['enterprise_name'])
        assert2 = self.page.text_content("//span[text()=\'新建销售机会\']")
        self.page.click(date[1]['company_name'])
        self.page.fill(date[1]['input_name2'], "测试新建销售机会_记得删除")
        self.page.fill(date[1]['input_remark'], "测试输入备注信息")
        self.page.click(date[1]['choose_sku'])
        self.page.click(date[1]['sku_num3'])
        self.page.click(date[1]['choose_department'])
        self.page.click(date[1]['department1'])
        self.page.click(date[1]['choose_contact'])
        self.page.click(date[1]['contact1'])
        self.page.fill(date[1]['input_sales_amount'], "108")
        self.page.fill(date[1]['input_project_costs'], "62")
        self.page.click(date[1]['choose_date'])
        self.page.click(date[1]['choose_today'])
        self.page.click(date[1]['choose_date2'])
        self.page.click(date[1]['choose_today'])
        self.page.click(date[1]['button_submit'])

        self.page.reload()
        self.page.wait_for_timeout(2000)
        self.page.click(date[1]['more_option'])
        self.page.click(date[1]['delete_button'])
        self.page.click(date[1]['ensure'])
        return assert2
