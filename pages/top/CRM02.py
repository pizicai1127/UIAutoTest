#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 5:00 下午
# @Author : cuiguoen
# @File : CRM02.py.py



import pytest
from pages.basepage import BasePage

class CRM2(BasePage):
    top_elements =[
        {
            "CRM": "//span[text()=\'CRM/业务管理\']",
            "sales_lea": "//li[@title=\"销售线索\"]",

        },
        {
            "sales_opportunities": "//span[text()= \"销售机会\"]",
        },
        {
            "CRM": "//span[text()=\'CRM/业务管理\']",
            "soso_enquiry": "//span[text()= \"嗖嗖询价/报价🔥\"]",
            "expand_search": "//span[text()= \"展开搜索\"]",  # 搜索
            "quote_record": "//input[@id=\"quoteName\"]",
            "search_button": "//button[text() = \'搜索\']",
            "create_quotation": "//span[text() = \'创建报价单\']",
            "Tezign_option": "//div[text()=\'Tezign\']",
            "Content_option": "//ul[@id=\"item_0$Menu\"]/li[1]",  # 选择Teizgn——Content新建报价单
            "option1": "//span[text()=\"插画主视觉\"]",
            "option1_one": "//div[@class=\"middle-part\"]/descendant::input[1]",
            "ensure": "//button[text() = \'确认\']",
            "quotation_name": "//input[@placeholder=\"输入报价单名称\"]",
            "next_buttom": "//button[text() = \'下一步\']",
            "save_buttom": "//button[text() = \'保存\']",
            "return_buttom": "//button[text() = \' 返回\']",
            "delete_button": "//div[@class=\"ant-table-fixed-right\"]//tbody[@class=\"ant-table-tbody\"]/tr[1]/td/div/button[4]",
            # 删除按钮
            "ensure2": "//div[text() = \'确 定\']",
        },
        {
            "business_signin": "//span[text() = \'业务签单\']",
            "choose_type": "//div[text() = \'选择业务类型\']",
            "type1": "//li[text() = \'campaign签单\']",
            "Reset_filtering": "//button[text() = \'重置筛选\']",
            "vproject1": "//div[@class=\"ant-table-fixed-left\"]/descendant::a[text()='预发测试3']",
            "edit_money": "//button[text()=\"编辑\"]",
            "open_detail": "//div[text()=\'展开详情\']",
            "button_opportunity": "//a[text()=\"查看销售机会\"]",
            "request_invoicing": "//button[text()=\"申请开票\"]",
            "button_advance": "//button[text()=\"提前申请\"]",
            "button_eelivery": "//button[text()=\"前往交付\"]",
        },
        {
            "enterprise_projects": "//span[text() = \'企业项目\']",
            "project_completed": "//span[text() = \'项目完结\']",
            "master_project": "//span[text() = \'一对多主项目\']",
            "button_query": "//button[text() = \'查询\']",
            "project1": "//div[text() = \'大C测试预发1\']",
            "Match_push": "//div[text()=\"人才匹配推送\"]",
            "Enquire": "//button[text()=\"查 询\"]",
            "Invitation_cooperation": "//div[text()=\"邀约与合作\"]",
            "Push_records": "//button[contains(text(),\"推送记录\")]",
            "Sub_project": "//div[text()=\"子项目管理\"]",
            "Account_management": "//div[text()=\"账期管理\"]",
        },
        {
            "enterprise_contacts": "//span[text() = \'企业客户/联系人\']",
            "input_name": "//input[@placeholder=\"请输入\"]",
            "button_search": "//button[text()=\"搜索\"]",
            "button_contact": "//button[text()=\"新建联系人\"]",
            "input_name2": "//input[@placeholder=\"请输入联系人姓名\"]",
            "choose_kp": "//div[text()=\"请选择相关KP\"]",
            "KP1": "//li[text()=\"CEO\"]",
            "choose_enterpris": "//div[text()=\"请选择企业公司\"]",
            "enterpris1": "//li[text()=\"测试888\"]",
            "choose_department": "//div[text()=\"请选择部门\"]",
            "department1": "//li[text()=\"测试888 - A1\"]",
            "button_submit": "//button[text()=\"提交\"]",
            "button_more": "//div[@class=\"ant-table-fixed-right\"]//tbody/tr[1]//span",  # 更多按钮
            "button_delete": "//button[text() = \'删除\']",
        },
        {
            "operational_audits": "//span[text() = \'运营审核审批\']",
            "keyword_search": "//input[@placeholder=\"请输入关键词搜索\"]",
            "department_search": "//input[@placeholder=\"输入关键词搜索\"]",
            "button_yes": "//span[text() = \"是\"]",
            "button_query": "//button[text() = \"查询\"]",
            "quotation_approval": "//div[text() = \"报价审批\"]",
            "client_search": "//div[text()= '客户名称']/following-sibling::div[1]/input",  # 客户名称搜索
            "Exception_alerts": "//span[text() = \'金额不一致\']",  # 异常提醒
            "button_query2": "//div[@aria-hidden=\"false\"]//button[text() = \"查询\"]",
            "Prepayment_approval": "//div[text() = \"预付款审批\"]",
            "Sign_name": "//div[text()=\"签单名称\"]//following-sibling::div/input",  # 签单名称
            "button_query3": "//div[@aria-hidden=\"false\"]//button[text() = \"查询\"]",
            "Credential_auditing": "//div[text() = \"凭证审核\"]",
            "button_sign_audit": "//span[text() = \'签单凭证审核\']",
            "button_proof_delivery": "//span[text() = \'交付凭证审核\']",
            "button_sku_adjusting": "//span[text() = \'SKU校准审核\']",
            "button_query4": "//div[@aria-hidden=\"false\"]//button[text() = \"查询\"]",
            "View_details": "//tr[@data-row-key=\"20\"]/td[8]/div/button",
        },
    ]

    @pytest.mark.p0
    def soso_enquiry(self):
        # 嗖嗖询价/报价
        date = self.top_elements
        self.page.click(date[2]['CRM'])
        self.page.click(date[2]['soso_enquiry'])
        self.page.click(date[2]['expand_search'])
        self.page.fill(date[2]['quote_record'],"测试")
        self.page.click(date[2]['search_button'])
        # 新建报价单
        self.page.hover(date[2]['create_quotation'])
        self.page.hover(date[2]['Tezign_option'])
        self.page.click(date[2]['Content_option'])  # 选择Teizgn——Content新建报价单
        # 选择第一个SKU
        self.page.wait_for_timeout(2000)
        self.page.click(date[2]['option1_one'])
        self.page.click(date[2]['ensure'])
        self.page.fill(date[2]['quotation_name'],"这是一个测试报价单")
        self.page.click(date[2]['next_buttom'])
        self.page.click(date[2]['save_buttom'])
        self.page.wait_for_timeout(3000)
        self.page.click(date[2]['return_buttom'])
        assert1 = self.page.text_content("//div[@class=\"ant-table-scroll\"]/descendant::button[1]")
        # 复制/删除报价单
        self.page.reload()

        self.page.click(date[2]['delete_button'])
        self.page.click(date[2]['ensure2'])
        return assert1

    @pytest.mark.p0
    def business_signing(self):
        # 业务签单
        date = self.top_elements
        self.page.click(date[3]['business_signin'])
        self.page.click(date[3]['choose_type'])
        self.page.click(date[3]['type1'])
        self.page.click(date[3]['Reset_filtering'])
        # 打开一个签单,选择签单名称是"预发测试3"
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[3]['vproject1'])
        new_page = new_page_info.value
        new_page.reload()
        vpro_name = new_page.text_content("//div[@class=\"_Exrvu\"]/strong")
        print(vpro_name)
        assert2 = new_page.text_content("//div[text()=\"收入金额\"]")
        new_page.click(date[3]['edit_money'])
        new_page.click(date[3]['open_detail'])
        new_page.mouse.click(100, 0)


        # 申请开票
        new_page.click(date[3]['request_invoicing'])
        new_page.click(date[3]['button_advance'])
        new_page.reload()
        new_page.click(date[3]['request_invoicing'])
        new_page.click(date[3]['button_eelivery'])

        # 查看销售机会
        with new_page.expect_popup() as new_page_info2:
            new_page.click(date[3]['button_opportunity'])
        new_page2 = new_page_info2.value
        assert3 = new_page2.text_content("//span[text()=\'销售机会详情页\']")
        new_page2.close()
        new_page.close()
        return assert2,assert3


    @pytest.mark.p0
    def enterprise_projects(self):
        # 企业项目
        date = self.top_elements
        self.page.click(date[4]['enterprise_projects'])
        self.page.click(date[4]['project_completed'])
        self.page.click(date[4]['master_project'])
        self.page.click(date[4]['button_query'])
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[4]['project1'])
        new_page = new_page_info.value
        assert4 = new_page.text_content("//span[text() = \'大C测试预发1\']")
        new_page.click(date[4]['Match_push'])
        new_page.click(date[4]['Enquire'])
        new_page.click(date[4]['Invitation_cooperation'])
        new_page.click(date[4]['Push_records'])
        new_page.click(date[4]['Sub_project'])
        new_page.click(date[4]['Account_management'])
        assert5 = new_page.text_content("//span[text() = \'项目完结\']")

        new_page.close()
        return assert4,assert5

    @pytest.mark.p0
    def enterprise_contacts(self):
        # 企业客户/联系人
        date = self.top_elements
        self.page.click(date[5]['enterprise_contacts'])
        self.page.fill(date[5]['input_name'],"测试")
        self.page.click(date[5]['button_search'])
        self.page.click(date[5]['button_contact'])
        self.page.fill(date[5]['input_name2'], "测试姓名")
        self.page.click(date[5]['choose_kp'])
        self.page.click(date[5]['KP1'])
        self. page.click(date[5]['choose_enterpris'])
        self.page.click(date[5]['enterpris1'])
        self.page.click(date[5]['choose_department'])
        self.page.click(date[5]['department1'])
        self.page.click(date[5]['button_submit'])
        self.page.reload()
        self.page.click(date[5]['button_more'])
        self.page.hover(date[5]['button_delete'])
        self.page.click(date[5]['button_delete'])
        self.page.reload()

    @pytest.mark.p0
    def operational_audits(self):
        # 运营审核审批
        date = self.top_elements
        self.page.click(date[6]['operational_audits'])
        self.page.reload()
        self.page.fill(date[6]['keyword_search'], "测试")
        self.page.fill(date[6]['department_search'], "A1")
        self.page.click(date[6]['button_yes'])
        self.page.click(date[6]['button_query'])
        self.page.click(date[6]['quotation_approval'])
        self.page.fill(date[6]['client_search'], "测试")
        self.page.click(date[6]['Exception_alerts'])
        self.page.click(date[6]['button_query2'])
        self.page.click(date[6]['Prepayment_approval'])
        self.page.fill(date[6]['Sign_name'], "天猫")
        self.page.click(date[6]['button_query3'])
        self.page.click(date[6]['Credential_auditing'])
        self.page.click(date[6]['button_proof_delivery'])
        self.page.click(date[6]['button_query4'])
        self.page.click(date[6]['button_sku_adjusting'])
        self.page.click(date[6]['button_query4'])
        self.page.click(date[6]['button_sign_audit'])
        self.page.click(date[6]['button_query4'])
        self.page.click(date[6]['View_details'])
        assert6 = self.page.text_content("//div[text() =\'签单凭证\']")
        self.page.mouse.click(100, 0)
        return assert6