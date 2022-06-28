#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/28 10:45 上午
# @File : NoticePage.py.py
from pages.customer.CustomerBasePage import CustomerBasePage


class NoticePage(CustomerBasePage):
    selectors = {
        "head_portrait_btn": '#rc-root > div.default-layout > div.navbar-wrapper > div.navbar > div.bar-body > '
                             'div.bar-user > img',
        "setting_btn": "text=偏好设置",
        "save_btn": "#rc-root > div.default-layout > div.layout-body > div > div > div.view-body > div > div > "
                    "div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > "
                    "div > div.account-card > div.card-bar.clear-fix > button",

        "mail_btn": "#rc-root > div.default-layout > div.navbar-wrapper > div.navbar > div.bar-body > div.bar-menu > "
                    "div.menu-item.type-mailbox > div.item-icon",
        "mail": ".icon-tz-letter-hover",
        "project_dynamics_btn": "#rc-root > div.default-layout > div.navbar-wrapper > div.navbar > div.bar-body > "
                                "div.bar-menu > div:nth-child(1) > div.item-icon ",
        "checkbox_btn":'input[type="checkbox"]',

    }
    """
    第一步：查看偏好设置
    第二步：查看站内信
    第二步：查看项目动态
    """
    def make_settings(self):
        self.page.click(NoticePage.selectors['head_portrait_btn'])
        self.page.click(NoticePage.selectors['setting_btn'])
        self.page.click(NoticePage.selectors['save_btn'])

    def mail(self):
        self.page.click(NoticePage.selectors['mail_btn'])
        self.page.click(NoticePage.selectors['mail'])

    def project_dynamics(self):
        self.page.click(NoticePage.selectors['project_dynamics_btn'])
        self.page.uncheck(NoticePage.selectors['checkbox_btn'])
        self.page.check(NoticePage.selectors['checkbox_btn'])