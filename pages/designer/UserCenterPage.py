#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : MyPage.py"""

from time import sleep

from pages.designer.DesigerBasePage import DesignerBasePage


class MyPage(DesignerBasePage):
    selectors = {
        "my_btn": "#rc-root > div > div.navbar-wrapper > div.navbar > div.bar-body > div.bar-user > img",
        "VIT3_btn": "text=VIT3",
        "VIT2_btn": "text=VIT2",
        "VIT_btn": "text=SVIT",
        "VIT1_btn": 'text=VIT1',
        "open": "text=展开已完成的内容",
        "ensure": "text=保证服务质量，确保按时交付，减少项目终止",
        "to_perfect": "text=去完善",
        "complete_personal_information": "text=补全个人信息",
        "later_certification": "text=稍后认证",
        "improve_personal_experience": "text=完善个人经历",
        "preference_push": "text=设置推送偏好",
        "complement_creative_ability": "text=补全创意能力资料",
        "special_credit": "text = 特赞信用",
        "my_information_btn": "text=我的资料",
        "creative_ability": "text=创意能力",
        "edit_btn": "#rc-root > div > div.layout-body > div > div > div.view-body > div > "
                      "div.ant-tabs.ant-tabs-top.tz-tabs.type-flexible-card.ant-tabs-card.ant-tabs-no-animation > "
                      "div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > "
                      "div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.profile-card.creative-ability > div > "
                      "div.edit-button > span > i",
        "add_style": "text=添加风格",
        "objectification_person": "text=拟物",
        "cancel_simulacrum_btn": "text=拟物 >> svg",
        "input_style": 'text=极简扁平拟物活泼商业磨砂Material Design添加风格 >> input[type="text"]',
        "style_btn": "text = 特赞风格 >> svg",
        "medical_care_btn": "text=医疗",
        "cancel_medical_care_btn": "text=医疗 >> svg",
        "preservation_btn": "text=保 存",
        "personal_experience": "text=个人经历",
        "project_experience": "text=项目经历",
        "learning_experience": "text=学习经历",
        "customer_evaluation": "text=客户评价",
        "my_evaluation_btn": "text=我撰写的评价",

    }

    def my_information(self, input_style):
        # 点击我的资料
        self.page.click(MyPage.selectors['my_btn'])
        self.page.click(MyPage.selectors['my_information_btn'])
        # 创意能力
        self.page.click(MyPage.selectors['creative_ability'])
        self.page.click(MyPage.selectors['edit_btn'])
        # 编辑创意能力，选择拟物，取消拟物，添加风格，取消风格
        self.page.click(MyPage.selectors['objectification_person'])
        self.page.click(MyPage.selectors['cancel_simulacrum_btn'])
        self.page.click(MyPage.selectors['add_style'])
        self.page.click(MyPage.selectors['input_style'])
        self.page.fill(MyPage.selectors['input_style'], input_style)
        self.page.press(MyPage.selectors['input_style'], "Enter")
        self.page.click(MyPage.selectors['style_btn'])
        # 选择医疗，取消医疗
        self.page.click(MyPage.selectors['medical_care_btn'])
        self.page.click(MyPage.selectors['cancel_medical_care_btn'])
        self.page.click(MyPage.selectors['preservation_btn'])

        self.page.click(MyPage.selectors['personal_experience'])
        self.page.click(MyPage.selectors['project_experience'])
        self.page.click(MyPage.selectors['learning_experience'])

        self.page.click(MyPage.selectors['customer_evaluation'])
        self.page.click(MyPage.selectors['my_evaluation_btn'])

    def mycase(self):
        # 点击我的信用
        self.page.click(MyPage.selectors['my_btn'])
        self.page.click(MyPage.selectors['special_credit'])
        self.page.click(MyPage.selectors['VIT3_btn'])
        self._wait(1)
        self.page.click(MyPage.selectors['VIT2_btn'])
        self._wait(1)
        self.page.click(MyPage.selectors['VIT_btn'])
        self._wait(1)
        self.page.click(MyPage.selectors['VIT1_btn'])
        self._wait(1)
        self.page.click(MyPage.selectors['ensure'])
        self._wait(1)
        # 补全个人信息
        self.page.click(MyPage.selectors['complete_personal_information'])
        self.page.goto("https://www.tezign.com/designer/#/services")
        # 补全创意能力资料
        self.page.click(MyPage.selectors['ensure'])
        self._wait(1)
        self.page.click(MyPage.selectors['open'])
        self.page.click(MyPage.selectors['complement_creative_ability'])
        # self.page.click(MyPage.selectors['later_certification'])
        self.page.goto("https://www.tezign.com/designer/#/services")
        # 个人经历
        self.page.click(MyPage.selectors['ensure'])
        self._wait(1)
        self.page.click(MyPage.selectors['open'])
        self.page.click(MyPage.selectors['improve_personal_experience'])
        # self.page.click(MyPage.selectors['later_certification'])
        self.page.goto("https://www.tezign.com/designer/#/services")
        # 设置推送偏好
        self.page.click(MyPage.selectors['ensure'])
        self._wait(1)
        self.page.click(MyPage.selectors['open'])
        self.page.click(MyPage.selectors['preference_push'])
        # self.page.goto("https://www.tezign.com/designer/#/services")
        # page.go_back()返回上一页
        self.page.go_back()
        # 去完善案例
        self.page.click(MyPage.selectors['ensure'])
        self._wait(1)
        self.page.click(MyPage.selectors['to_perfect'])
        self.page.goto("https://www.tezign.com/designer/#/services")
