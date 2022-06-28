#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/24 5:01 下午
# @File : MyInformationPage.py
from time import sleep

from pages.customer.CustomerBasePage import CustomerBasePage


class MyInformationPage(CustomerBasePage):
    selectors = {
        "my_information": '#rc-root > div.default-layout > div.navbar-wrapper > div.navbar > div.bar-body > '
                          'div.bar-user > '
                          'div > div.card-body > div:nth-child(1) > span.action-text',
        "company_profile": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > div > "
                           "div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > "
                           "div:nth-child(1) > "
                           "div:nth-child(2)",
        "my_evaluation": '#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > div > '
                         'div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > '
                         'div:nth-child(1) > div:nth-child(3)',
        "imformation": '#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > div > '
                       'div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child('
                       '1) > div:nth-child(1)',
        "head_portrait_btn": '#rc-root > div.default-layout > div.navbar-wrapper > div.navbar > div.bar-body > '
                             'div.bar-user > img',
        "evaluation": "text=我撰写的评价",
        "comments_received": "text=我的评价",
        "view_items_to_be_evaluated": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > "
                                      "div > div > "
                                      "div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant"
                                      "-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > "
                                      "div.spin-wrap.size-large > div.spin-container > div > div.container-bar > div "
                                      "> div.flex-1.border-left.pl-30 > span",
        "close_btn": "body > div.wait-list-view > div > i",
        "company_name_edit": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > "
                             "div > "
                             "div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card"
                             "-content> div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.account-card > div > "
                             "div:nth-child(1) > div.col-8 > div > i",
        "input_company_name": 'input[placeholder="请填写公司名称"]',
        "save_btn": "text=保存",
        "cancel_btn": "text=取消",
        "introduction_edit": '#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > div '
                             '> div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card'
                             '-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.account-card > div > '
                             'div:nth-child(2) > div.col-8 > div > i',
        "introduction_name": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > div "
                             "> div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card"
                             "-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.account-card > div > "
                             "div:nth-child(2) > div.col-8 > div > div.form-input.mb-10 > textarea",
        "company_network_edit": '#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > '
                                'div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant'
                                '-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.account-card '
                                '> div > div:nth-child(3) > div.col-8 > div > i',
        "network_name": 'input[placeholder="请填写公司网址"]',
        "company_real_name_authentication_btn": '#rc-root > div.default-layout > div.layout-body > div > div > '
                                                'div.view-body > div > div > '
                                                'div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top'
                                                '-content.ant-tabs-card-content > '
                                                'div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.account-card > '
                                                'div > div:nth-child(4) > div.col-8 > div > '
                                                'div.cert-info.display-flex.flex-align-items-center > p',
        "three_syndromes": 'div[role="tab"]:has-text("非三证合一")',
        "social_information": 'div[role="tab"]:has-text("统一社会信息用代码")',
        "account_settings_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > "
                                "div > "
                                "div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card"
                                "-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.account-card > "
                                "div.info-setting > i",
        "name_btn": "text=取消",
        "name_edit_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > div > "
                         "div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card"
                         "-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.account-card > div.card-body "
                         "> div:nth-child(1) > div.col-8 > div > i",
        "input_name_btn": 'input[placeholder="请填写你的姓名"]',
        "position_edit_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > div "
                             "> div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card"
                             "-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.account-card > "
                             "div.card-body > div:nth-child(2) > div.col-8 > div > i",
        "input_position_btn": 'input[placeholder="请填写职位信息"]',
        "presonal_real_name_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div "
                                  "> div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant"
                                  "-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > "
                                  "div.account-card > div.card-body > div:nth-child(3) > div.col-8 > div > "
                                  "div.cert-info.display-flex.flex-align-items-center > p",

    }

    def information(self):
        # 点击我的头像
        self.page.click(MyInformationPage.selectors['head_portrait_btn'])
        # 点击我的资料
        self.page.click(MyInformationPage.selectors['my_information'])
        # 点击公司简介
        self.page.click(MyInformationPage.selectors['company_profile'])
        # 点击我的评价
        self.page.click(MyInformationPage.selectors['my_evaluation'])
        # 点击个人资料
        self.page.click(MyInformationPage.selectors['imformation'])

    def my_evaluation(self):
        # 点击我的评价
        self.page.click(MyInformationPage.selectors['my_evaluation'])
        # 点击我写评价
        self.page.click(MyInformationPage.selectors['evaluation'])
        # 点击我收到的评价
        self.page.click(MyInformationPage.selectors['comments_received'])

    def to_be_evaluated(self):
        # 点击我的评价
        self.page.click(MyInformationPage.selectors['my_evaluation'])
        # 点击待评价项目
        self.page.click(MyInformationPage.selectors['view_items_to_be_evaluated'])
        # 点击关闭按钮
        self.page.click(MyInformationPage.selectors['close_btn'])

    def company_name(self, input_company_name_empty, input_company_name):
        # 点击公司简介
        self.page.click(MyInformationPage.selectors['company_profile'])
        # 点击公司名称编辑按钮
        self.page.click(MyInformationPage.selectors['company_name_edit'])
        # 点击编辑公司名称，取消按钮
        self.page.click(MyInformationPage.selectors['cancel_btn'])
        self.page.click(MyInformationPage.selectors['company_name_edit'])
        self.page.click(MyInformationPage.selectors['input_company_name'])
        # 删除公司名称
        self.page.fill(MyInformationPage.selectors['input_company_name'], input_company_name_empty)
        # 输入公司名称
        self.page.fill(MyInformationPage.selectors['input_company_name'], input_company_name)
        # 保存公司名称
        self.page.click(MyInformationPage.selectors['save_btn'])

    def company_introduction(self, input_company_introduction_empty, introduction_name):
        # 点击公司简介
        self.page.click(MyInformationPage.selectors['company_profile'])
        # 点击公司简介编辑按钮
        self.page.click(MyInformationPage.selectors['introduction_edit'])
        # 点击编辑公司简介，取消按钮
        self.page.click(MyInformationPage.selectors['cancel_btn'])
        self.page.click(MyInformationPage.selectors['introduction_edit'])
        self.page.click(MyInformationPage.selectors['introduction_name'])
        # 删除公司简介
        self.page.fill(MyInformationPage.selectors['introduction_name'], input_company_introduction_empty)
        # 输入公司简介
        self.page.type(MyInformationPage.selectors['introduction_name'], introduction_name)
        self.page.click(MyInformationPage.selectors['save_btn'])

    def company_network(self, network_name, network_name_empty):
        # 点击公司简介
        self.page.click(MyInformationPage.selectors['company_profile'])
        # 点击公司网址编辑按钮
        self.page.click(MyInformationPage.selectors['company_network_edit'])
        # 点击编辑公司网址，取消按钮
        self.page.click(MyInformationPage.selectors['cancel_btn'])
        self.page.click(MyInformationPage.selectors['company_network_edit'])
        self.page.click(MyInformationPage.selectors['network_name'])
        # 输入公司网址
        self.page.fill(MyInformationPage.selectors['network_name'], network_name)
        # 删除公司网址
        self.page.fill(MyInformationPage.selectors['network_name'], network_name_empty)
        self.page.click(MyInformationPage.selectors['save_btn'])

    def company_real_name_authentication(self):
        # 点击公司简介
        self.page.click(MyInformationPage.selectors['company_profile'])
        # 点击公司实名认证
        self.page.click(MyInformationPage.selectors['company_real_name_authentication_btn'])
        self.page.click(MyInformationPage.selectors['three_syndromes'])
        self.page.click(MyInformationPage.selectors['social_information'])

    def account_settings(self):
        # 点击我的资料
        self.page.click(MyInformationPage.selectors['my_information'])
        with self.page.expect_popup() as popup_info:
            self.page.click(MyInformationPage.selectors['account_settings_btn'])
            sleep(2)
        page1 = popup_info.value
        page1.close()

    def account_name(self, input_name_btn_empty, input_name_btn):
        # 点击我的资料
        self.page.click(MyInformationPage.selectors['my_information'])
        # 点击用户名称编辑按钮
        self.page.click(MyInformationPage.selectors['name_edit_btn'])
        # 点击编辑用户名称，取消按钮
        self.page.click(MyInformationPage.selectors['cancel_btn'])
        self.page.click(MyInformationPage.selectors['name_edit_btn'])
        self.page.click(MyInformationPage.selectors['input_name_btn'])
        # 删除用户名称
        self.page.fill(MyInformationPage.selectors['input_name_btn'], input_name_btn_empty)
        # 输入用户名称
        self.page.fill(MyInformationPage.selectors['input_name_btn'], input_name_btn)
        # 保存用户名称
        self.page.click(MyInformationPage.selectors['save_btn'])

    def position_name(self, input_position_btn_empty, input_position_btn):
        # 点击我的资料
        self.page.click(MyInformationPage.selectors['my_information'])
        # 点击用户名称编辑按钮
        self.page.click(MyInformationPage.selectors['position_edit_btn'])
        # 点击编辑用户职位，取消按钮
        self.page.click(MyInformationPage.selectors['cancel_btn'])
        self.page.click(MyInformationPage.selectors['position_edit_btn'])
        self.page.click(MyInformationPage.selectors['input_position_btn'])
        # 删除用户职位名称
        self.page.fill(MyInformationPage.selectors['input_position_btn'], input_position_btn_empty)
        # 输入用户职位名称
        self.page.fill(MyInformationPage.selectors['input_position_btn'], input_position_btn)
        # 保存用户职位名称
        self.page.click(MyInformationPage.selectors['save_btn'])

    def personal_real_name(self):
        # 点击我的资料
        self.page.click(MyInformationPage.selectors['my_information'])
        # 点击个人实名认证
        self.page.click(MyInformationPage.selectors['presonal_real_name_btn'])