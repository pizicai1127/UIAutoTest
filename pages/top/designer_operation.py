#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 5:17 下午
# @Author : cuiguoen
# @File : designer_operation.py.py


import pytest
from pages.basepage import BasePage

class Designer(BasePage):
    # 创意方运营 菜单,有创意方详情页
    top_elements = [
        {
            "designer_operation": "//span[text()=\'创意方运营\']",
            "Satisfaction_survey": "//span[text()=\'创意方满意度调研\']",
            "Not_initiated": "//span[text()=\'未发起\']",
            "input_name": "//input[@placeholder=\"请输入创意方名称搜索\"]",
            "button_search": "//button[text() = \'搜索\']",
            "Commented": "//span[text()=\'已备注\']",
            "input_comment": "//textarea[@placeholder=\"请输入备注\"]",
            "button_ensure": "//button[text()= \'确 定\']",
        },
        {
            "invite_list": "//span[text()=\'特赞邀请列表\']",
            "Not_registered": "//span[text()=\'未注册\']",
            "Full_occupancy": "//span[text()=\'完整入驻激活流程\']",
            "Minimum_number": "//span[text()=\'最低报价案例数门槛（5个）\']",
            "button_inquire": "//button[text()= \'查询\']",
            "Create_invitation": "//button[text()= \'新建邀请\']",
            "input_name": "//input[@placeholder=\"请输入创意方姓名\"]",
            "input_email": "//input[@placeholder=\"请输入创意方邮箱\"]",
            "input_commment": "//textarea[@placeholder=\"您可以在这里补充对该创意方的业务评语\"]",
            "Source_type": "//div[text()=\'请选择来源渠道类型\']",
            "type1": "//li[text()=\'社交人脉\']",
            "button_ensure": "//button[text()= \'确 定\']",
            "button_delete": "//div[@class=\"ant-table-fixed-right\"]//tbody/tr[1]/td/p/span[2]",
            "delete_ensure": "//div[text()= \'删 除\']",
        },
        {
            "invite_designer": "//span[text()=\'创意方邀请列表\']",
            "View_details": "//tbody/tr[1]//button",
            "name1": "//tbody/tr[1]/td[2]/span[1]",
        },
        {
            "designer_verify": "//span[text()=\'创意方审核\']",
            "input_name": "//input[@placeholder=\"创意方姓名/曾用名/公司名称/电话/邮箱\"]",
            "source1": "//span[text()=\'Web端\']",
            "upgrade_passed": "//span[text()=\'升级已通过\']",
            "black_list": "//span[text()= \'否\']",
            "RateCard": "//span[text()= \'完整及草稿\']",
            "button_search": "//button[text() = \'搜 索\']",
            "button_view": "//button[text() = \'查看详情\']",
            "inside_cases": "//div[text() = \'站内案例\']",
            "outside_cases": "//div[text() = \'站外案例\']",
            "button_update": "//button[text() = \'更新盗用状态\']",
            "Behance": "//div[text() = \'Behance\']",
            "Charges": "//div[text() = \'服务收费标准\']",
            "button_reset": "//button[text() = \'重置\']",
            "Quote_history": "//div[text() = \'报价记录\']",
            "portray": "//div[text() = \'画像\']",
            "qualification": "//div[text() = \'资质认证\']",
            "Talent_group": "//div[text() = \'人才组\']",
            "rights": "//div[text() = \'权益\']",
            "Registrant_Information": "//h3[text() = \'注册人信息\']",
            "Quotation_number": "//h3[text() = \'报价次数／金额无限制\']",
            "Agent_login":"//button[text()= \'代理登录\']",
            "My_cases": "//h3[text() = \'我的案例\']",
        },
        {
            "Personal_authentication": "//span[text()=\'创意方个人实名认证\']",
            "identity_card": "//span[text()=\'身份证\']",
            "passed": "//span[text()=\'已通过\']",
            "input_name": "//input[@placeholder=\"创意方姓名/电话/邮箱\"]",
            "button_search": "//button[text() = \'搜索\']",
            "button_view": "//a[text()= \'查看详情\']",
            "Certification_details": "//span[text()=\'实名认证 - 详情\']",
            "button_edit": "//button[text() = \'编辑\']",
            "input_name2": "//input[@placeholder=\"真实姓名\"]",
            "button_ensure": "//button[text() = \'确 定\']",
        },
        {
            "company_authentication": "//span[text()=\'创意方公司实名认证\']",
            "three_certificates": "//span[text()=\'是\']",
            "passed": "//span[text()=\'已通过\']",
            "input_name": "//input[@placeholder=\"创意方姓名/电话/邮箱\"]",
            "button_search": "//button[text() = \'搜索\']",
            "button_view": "//a[text()= \'查看详情\']",
            "Certification_details": "//span[text()=\'实名认证 - 详情\']",
            "button_edit": "//button[text() = \'编辑\']",
            "Business_name": "//input[@placeholder=\"企业名称\"]",
            "button_ensure": "//button[text() = \'确 定\']",
        },
        {
            "tax_change": "//span[text()=\'创意方票税变更申请\']",
            "passed": "//span[text()=\'已通过\']",
            "button_search": "//button[text() = \'查询\']",
            "designer1": "//div[text()=\'cui\']",
            "designer_view": "//div[text()=\'创意方详情\']",
        },
        {
            "quote_go": "//span[text()=\'报价GO二维码\']",
            "input_channel": "//input[@placeholder=\"填写渠道\"]",
            "button_ensure": "//button[text() = \'生成小程序码\']",
        },
    ]



    @pytest.mark.p0
    def demand_orders(self):
        # 创意方满意度调研 菜单
        date = self.top_elements
        self.page.click(date[0]['designer_operation'])
        self.page.click(date[0]['Satisfaction_survey'])
        self.page.click(date[0]['Not_initiated'])
        self.page.fill(date[0]['input_name'], '罗宇科')
        self.page.click(date[0]['button_search'])
        self.page.click(date[0]['Commented'])


    @pytest.mark.p0
    def invite_list(self):
        # 特赞邀请列表 菜单
        date = self.top_elements
        self.page.click(date[1]['invite_list'])
        self.page.click(date[1]['Not_registered'])
        self.page.click(date[1]['Full_occupancy'])
        self.page.click(date[1]['Minimum_number'])
        self.page.click(date[1]['button_inquire'])
        self. page.reload()
        self.page.wait_for_timeout(2000)
        # 新建邀请
        self. page.click(date[1]['Create_invitation'])
        self.page.fill(date[1]['input_name'], 'test009')
        self.page.fill(date[1]['input_email'], 'test009@qq.com')
        self.page.fill(date[1]['input_commment'], 'test009')
        self.page.click(date[1]['Source_type'])
        self.page.click(date[1]['type1'])
        self.page.click(date[1]['button_ensure'])
        # 删除新建的
        self.page.reload()
        self.page.click(date[1]['button_delete'])
        self.page.click(date[1]['delete_ensure'])
        self.page.wait_for_timeout(2000)
        self.page.click(date[1]['invite_list'])
        self.page.click(date[1]['Not_registered'])
        self.page.click(date[1]['Full_occupancy'])


    @pytest.mark.p0
    def invite_designer(self):
        # 创意方邀请列表 菜单
        date = self.top_elements
        self.page.click(date[2]['invite_designer'])
        self.page.click(date[2]['View_details'])
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[2]['name1'])
        new_page = new_page_info.value
        new_page.is_visible("//div[text() = \'创意方详情\']")
        new_page.close()

    @pytest.mark.p0
    def designer_verify(self):
        # 创意方审核 菜单,创意方详情页
        date = self.top_elements
        self.page.click(date[3]['designer_verify'])
        self. page.fill(date[3]['input_name'], '广州市森尼奥广告有限公司')
        self.page.click(date[3]['source1'])
        self.page.click(date[3]['upgrade_passed'])
        self.page.click(date[3]['black_list'])
        #page.click(date[3]['RateCard'])
        self.page.click(date[3]['button_search'])
        # 创意方-详情
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[3]['button_view'])
        new_page = new_page_info.value
        new_page.is_visible(date[3]["Registrant_Information"])
        new_page.click(date[3]['inside_cases'])
        new_page.click(date[3]['button_update'])
        new_page.click(date[3]['outside_cases'])
        new_page.click(date[3]['Behance'])
        new_page.click(date[3]['Charges'])
        new_page.click(date[3]['button_reset'])
        new_page.click(date[3]['Quote_history'])
        new_page.click(date[3]['portray'])
        new_page.click(date[3]['qualification'])
        new_page.click(date[3]['Talent_group'])
        new_page.click(date[3]['rights'])
        new_page.is_visible(date[3]["Quotation_number"])
        new_page.close()

    @pytest.mark.p0
    def personal_authentication(self):
        # 创意方个人实名认证 菜单
        date = self.top_elements
        self.page.click(date[4]['Personal_authentication'])
        self.page.click(date[4]['identity_card'])
        self.page.click(date[4]['passed'])
        self.page.fill(date[4]['input_name'], '15700000001')
        self.page.click(date[4]['button_search'])
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[4]['button_view'])
        new_page = new_page_info.value
        new_page.is_visible(date[4]["Certification_details"])

        new_page.close()

    @pytest.mark.p0
    def company_authentication(self):
        # 创意方公司实名认证 菜单
        date = self.top_elements
        self.page.click(date[5]['company_authentication'])
        self.page.click(date[5]['three_certificates'])
        self.page.click(date[5]['passed'])
        self.page.fill(date[5]['input_name'], '15700001261')
        self.page.click(date[5]['button_search'])

    @pytest.mark.p0
    def test_tax_change(self):
        # 创意方票税变更申请 菜单
        date = self.top_elements
        self.page.click(date[6]['tax_change'])
        self.page.click(date[6]['passed'])
        self.page.click(date[6]['button_search'])
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[6]['designer1'])
        new_page = new_page_info.value
        new_page.is_visible(date[6]["designer_view"])
        new_page.close()

    @pytest.mark.p0
    def test_quote_go(self):
        # 报价GO二维码 菜单
        date = self.top_elements
        self.page.click(date[7]['quote_go'])
        self.page.fill(date[7]['input_channel'], 'weixin')
        self.page.click(date[7]['button_ensure'])
