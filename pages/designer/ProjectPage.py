#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : ProjectPage.py"""

from time import sleep

from pages.designer.DesigerBasePage import DesignerBasePage


class ProjectPage(DesignerBasePage):
    selectors = {
        "quoted_btn": "text=已经报价的项目 (0)",
        "in_progress_btn": "text=正在进行的项目 (1)",
        "closed_btn": "text=已完结的项目 (5)",
        "to_be_responded_btn": 'text=待响应的项目 (0)',
        "click_item": 'h3:has-text("ceshi1")',
        "project_information": 'li:has-text("项目信息")',
        "project_docking": 'li:has-text("项目对接")',
        "contract_management": 'li:has-text("合同管理")',
        "transaction_record": "text=交易记录",

    }

    # 查看创意方案例流程
    def project_case(self):
        # 点击已经报价的项目
        self.page.click(ProjectPage.selectors['quoted_btn'])
        self._wait(1)
        # 点击正在进行的项目
        self.page.click(ProjectPage.selectors['in_progress_btn'])
        self._wait(1)
        # 点击已完结的项目
        self.page.click(ProjectPage.selectors['closed_btn'])
        self._wait(1)
        # 点击待响应的项目
        self.page.click(ProjectPage.selectors['to_be_responded_btn'])
        self._wait(1)
        self.page.click(ProjectPage.selectors['in_progress_btn'])

        with self.page.expect_popup() as popup_info:
            self.page.click(ProjectPage.selectors['click_item'])
        page1 = popup_info.value
        page1.click(ProjectPage.selectors['project_information'])
        page1.click(ProjectPage.selectors['project_docking'])
        page1.click(ProjectPage.selectors['contract_management'])
        page1.close()
