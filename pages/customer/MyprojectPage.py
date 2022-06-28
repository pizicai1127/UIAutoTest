#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/21 2:27 下午
# @File : MyprojectPage.py
from pages.customer.CustomerBasePage import CustomerBasePage


class MyProjectPage(CustomerBasePage):
    selectors = {
        "publishing_time_sort_btn": "text=按发布时间排序",
        "update_time_sort_btn": "text=按更新时间排序",
        "project_title_btn": 'h3:has-text("回归测试")',
        "project_information_btn": 'li:has-text("项目信息")',
        "project_docking_btn": 'li:has-text("项目对接")',
        "contract_management_btn": 'li:has-text("合同管理")',
        "contract_setting_btn": 'text=合同设置',
        "fund_payment_btn": 'text=资金支付',
        "project_management_btn": 'li:has-text("项目管理")',
        "project_first_btn": 'div[role="button"]:has-text("1¥3,000.00共有 1 个任务，共需 1 个工作日已确认")',
        "project_second_btn": 'div[role="button"]:has-text("2¥500.00共有 1 个任务，共需 1 个工作日已确认")',
        "evaluate_btn": 'text=项目信息项目对接合同管理项目管理评论 >> :nth-match(i, 5)',
        "input_box_btn": "input[placeholder='输 入']",
        "expression_btn": 'text=目前不支持此种文件类型😀😬😁😂😃😄😅😆😇😉😊🙂🙃😋😌😍😘😗😙😚😜😝😛🤑🤓😎🤗😏😶😐😑😒🙄🤔\ud83d >> i',
        "expression_btn1": '#rc-root > div.default-layout > div.layout-body > div > div.view-side > div > '
                           'div.messager-operation > div > div.pm-emoji > div > div.emoji-wrap.sc-bwzfXH.hVJNYR > '
                           'div:nth-child(1) > div > a:nth-child(34) > span',
    }

    # 项目排序
    def my_project_sort(self):
        self.page.click(MyProjectPage.selectors['publishing_time_sort_btn'])
        self.page.click(MyProjectPage.selectors['update_time_sort_btn'])
        self.page.hover(MyProjectPage.selectors['update_time_sort_btn'])
        self.page.click(MyProjectPage.selectors['publishing_time_sort_btn'])

    # 查看项目
    def view_project_tails(self):
        self.page.click(MyProjectPage.selectors['project_title_btn'])
        self.page.click(MyProjectPage.selectors['project_information_btn'])
        self.page.click(MyProjectPage.selectors['project_docking_btn'])
        self.page.click(MyProjectPage.selectors['contract_management_btn'])
        self.page.click(MyProjectPage.selectors['contract_setting_btn'])
        self.page.click(MyProjectPage.selectors['fund_payment_btn'])
        self.page.click(MyProjectPage.selectors['evaluate_btn'])
        # self.page.click(MyProjectPage.selectors['project_management_btn'])
        # self.page.click(MyProjectPage.selectors['project_first_btn'])
        # self.page.click(MyProjectPage.selectors['project_second_btn'])

    # 进入客户端项目详情页，进行对话
    def input_box(self,input_box):
        self.page.fill(MyProjectPage.selectors['input_box_btn'], input_box)
        self.page.press(MyProjectPage.selectors['input_box_btn'], "Enter")
        self.page.click(MyProjectPage.selectors['expression_btn'])
        self.page.click(MyProjectPage.selectors['expression_btn1'])
        self.page.press(MyProjectPage.selectors['input_box_btn'], "Enter")

