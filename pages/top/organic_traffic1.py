#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/14 11:23 上午
# @Author : cuiguoen
# @File : organic_traffic1.py.py

import pytest
from pages.basepage import BasePage

class Organic1(BasePage):
    # 自然流量菜单下的前半部分
    top_elements = [
        {
            "Organic_traffic": "//span[text()=\'自然流量\']",
            "Normal_projects": "//span[text()=\'普通项目\']",
            "button_reset": "//button[text() = \'重置\']",
            "in_progress": "//span[text()=\'项目进行中\']",
            "button_inquire": "//button[text() = \'查询\']",
            "one_project": "//tbody/tr[1]/td[1]/span[1]",  # 第一个项目
            "quote_list": "//div[text()= \'报价列表\']",
            "Show_open": "//span[text()=\'展 开\']",
            "quote_detail": "//div[text()= \'报价明细记录\']",
            "contract_management": "//div[text()= \'合同管理\']",
            "project_management": "//div[text()= \'项目管理\']",
            "operation_logs": "//div[text()= \'操作日志\']",
            "sides_evaluation": "//div[text()= \'双方评价\']",
            "transaction_details": "//div[text()= \'交易详情\']",
            "visit_notes": "//div[text()= \'回访备注\']",
            "add_notes": "//button[text() = \'添加回访记录\']",
        },
        {
            "contracts_list": "//span[text()=\'合同列表\']",
            "reviewing": "//span[text()=\'审阅中\']",
            "input_name": "//input[@placeholder=\"输入项目名称搜索\"]",
            "button_inquire": "//button[text() = \'查询\']",
            "View_details": "//tbody/tr[1]/td[6]/a",
        },
        {
            "Invoice_request": "//span[text()=\'发票申请\']",
            "Invoice_closed": "//span[text()=\'已关闭\']",
            "button_inquire": "//button[text() = \'查询\']",
            "button_mark": "//button[text() = \'标记为处理中\']",
        },
        {
            "promo_code": "//span[text()=\'发布优惠码\']",
            "create_preferential": "//button[text() = \'新建优惠\']",
            "input_name": "//input[@placeholder=\"优惠码名称,仅支持英文、数字、下划线\"]",
            "minus_fee": "//input[@placeholder=\"减去的费用\"]",
            "start_day": "//div[text()=\"开始日期 *\"]/following-sibling::div[1]//input",
            "today": "//a[text()=\'今天\']",
            "end_day": "//div[text()=\"截止日期 *\"]/following-sibling::div[1]//input",
            "button_remark": "//input[@placeholder=\"请注明申请人、使用场景, 如: 奶黄包申请、VIP客户专用\"]",
            "button_cancel": "//button[text() = \'取 消\']",
            "View_details": "//tbody/tr[1]/td[9]/div/button",  # 查看详情按钮
        },
        {
            "Penalty_appeal": "//span[text()=\'交易行为扣分申诉\']",
            "search_key": " //div[text() =\'选择申诉创意方，支持关键词搜索\']",
            "designer1": "//li[text()=\'李林\']",
            "button_agree": "//span[text()=\'同意\']",
            "button_inquire": "//button[text() = \'查询\']",
            "designer_name": "//tbody/tr[1]/td[1]/span",
            "project_name": "//tbody/tr[1]/td[2]",
        },
        {
            "Discount_code": "//span[text()=\'服务费优惠码\']",
            "button_create": "//button[text()=\'新建优惠\']",
            "input_name": "//input[@placeholder=\"请输入搜索关键字\"]",
            "input_discount": "//input[@placeholder=\"请输入 0~100 的折扣比例\"]",
            "button_cancel": "//button[text()=\'取 消\']",
        },
        {
            "Natural_customer": "//span[text()=\'自然流量客户\']",
            "input_name": "//input[@placeholder=\"客户用户名/邮箱/手机/编号\"]",
            "button_search": "//button[text()=\'搜索\']",
            "button_view": "//button[text()=\'查看详情\']",
            "Proxy_login": "//tbody/tr[1]//button[text()=\"代理登录\"]",
        },
        {
            "Benefit_Editing": "//span[text()=\'权益编辑\']",
            "select_associate": "//div[text()=\'选择关联项目\']",
            "select1": "//li[text()=\"99元\"]",
            "select_status": "//div[text()=\'请选择\']",
            "status1": "//li[text()=\"生效\"]",
            "input_nubmers": "//input[@placeholder=\"请输入使用的次数\"]",
            "button_inquire": "//button[text() = \'查询\']",
        },
    ]

    @pytest.mark.p0
    def normal_projects(self):
        # 普通项目菜单
        date = self.top_elements
        self.page.click(date[0]['Organic_traffic'])
        self.page.click(date[0]['Normal_projects'])
        self.page.click(date[0]['button_reset'])
        self.page.click(date[0]['in_progress'])
        self.page.click(date[0]['button_inquire'])
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[0]['one_project'])
        new_page = new_page_info.value
        new_page.click(date[0]['quote_list'])
        new_page.click(date[0]['Show_open'])
        new_page.click(date[0]['quote_detail'])

        new_page.click(date[0]['contract_management'])
        new_page.click(date[0]['project_management'])
        new_page.click(date[0]['operation_logs'])
        new_page.click(date[0]['sides_evaluation'])
        new_page.click(date[0]['transaction_details'])
        new_page.click(date[0]['visit_notes'])
        new_page.click(date[0]['add_notes'])
        new_page.close()


    @pytest.mark.p0
    def contracts_list(self):
        # 合同列表菜单
        date = self.top_elements
        self.page.click(date[1]['contracts_list'])
        self.page.click(date[1]['reviewing'])
        self.page.fill(date[1]['input_name'],"测试")
        self.page.click(date[1]['button_inquire'])
        self.page.click(date[1]['View_details'])
        assert2 = self.page.text_content("//div[text() = \"合同管理详情\"]")
        return assert2

    @pytest.mark.p0
    def invoice_request(self):
        # 发票申请菜单
        date = self.top_elements
        self.page.click(date[2]['Invoice_request'])
        self.page.click(date[2]['Invoice_closed'])
        self.page.click(date[2]['button_inquire'])
        self.page.click(date[2]['button_mark'])

    @pytest.mark.p0
    def promo_code(self):
        # 发布优惠码 菜单
        date = self.top_elements
        self.page.click(date[3]['promo_code'])
        # 新建优惠
        self.page.click(date[3]['create_preferential'])
        self.page.fill(date[3]['input_name'],"test001")
        self.page.fill(date[3]['minus_fee'], "99")
        self.page.click(date[3]['start_day'])
        self.page.click(date[3]['today'])
        self.page.click(date[3]['end_day'])
        self.page.click(date[3]['today'])
        self.page.fill(date[3]['button_remark'], "test备注")
        self.page.click(date[3]['button_cancel'])
        self.page.click(date[3]['View_details'])


    @pytest.mark.p0
    def penalty_appeal(self):
        # 交易行为扣分申诉 菜单
        date = self.top_elements
        self.page.click(date[4]['Penalty_appeal'])
        self.page.click(date[4]['search_key'])
        self.page.click(date[4]['designer1'])
        self.page.click(date[4]['button_agree'])
        self.page.click(date[4]['button_inquire'])
        self.page.reload()
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[4]['designer_name'])
        new_page = new_page_info.value
        assert3 = new_page.text_content("//div[text() = \"创意方详情\"]")
        new_page.close()
        return assert3

    @pytest.mark.p0
    def discount_code(self):
        # 服务费优惠码 菜单
        date = self.top_elements
        self.page.click(date[5]['Discount_code'])
        self.page.click(date[5]['button_create'])
        self.page.fill(date[5]['input_name'],"test")
        self.page.fill(date[5]['input_discount'], "90")
        self.page.click(date[5]['button_cancel'])
        assert4 = self.page.text_content("//div[text()= \"服务费优惠券\"]")
        return assert4

    @pytest.mark.p0
    def natural_customer(self):
        # 自然流量客户 菜单
        date = self.top_elements
        self.page.click(date[6]['Natural_customer'])
        self.page.fill(date[6]['input_name'],"贵妃奶黄包")
        self.page.click(date[6]['button_search'])
        self.page.click(date[6]['button_view'])
        self.page.go_back()

    @pytest.mark.p0
    def benefit_editing(self):
        # 权益编辑 菜单
        date = self.top_elements
        self.page.click(date[7]['Benefit_Editing'])
        self.page.click(date[7]['select_associate'])
        self.page.click(date[7]['select1'])
        self.page.click(date[7]['select_status'])
        self.page.click(date[7]['status1'])
        self.page.fill(date[7]['input_nubmers'],"100")
        self.page.click(date[7]['button_inquire'])

