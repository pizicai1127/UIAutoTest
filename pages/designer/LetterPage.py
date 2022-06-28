#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : LetterPage.py"""

from time import sleep

from pages.designer.DesigerBasePage import DesignerBasePage


class LetterPage(DesignerBasePage):
    selectors = {
        "mail_btn": '.menu-item.type-mailbox',
        "journal_btn": "text = 功能更新日志",
        "mail": "text=站内信",
        "creat_btn": "text=新建案例",

        "money_btn": 'div:nth-child(5)',
        "withdrawal_record": "text=提现记录",
        "transaction_record": "text=交易记录",

        "tools": ".menu-item.type-tools",
        "upload": "text=开始上传",

        "experience_now": "text=立即体验",
        "try_now": "text=立即试用",
        "go_to_see": "text=去看看",
        "go_to_see_btn": "text=UIrush免费的设计、开发、产品素材库设计、开发、产品常用网站导航去看看 >> button",


    }

    # 创意方站内信
    def mail(self):
        # 点击
        self.page.click(LetterPage.selectors['mail_btn'])
        self.page.click(LetterPage.selectors['journal_btn'])
        self.page.click(LetterPage.selectors['mail'])
        self.page.click(LetterPage.selectors['mail_btn'])

    # 创意方资金管理
    def moneycase(self):
        self.page.click(LetterPage.selectors['money_btn'])
        self.page.click(LetterPage.selectors['withdrawal_record'])
        self.page.click(LetterPage.selectors['transaction_record'])

    # 创意方工具箱
    def tools(self):
        self.page.click(LetterPage.selectors['tools'])
        self._wait(2)

        with self.page.expect_popup() as popup_info:
            self.page.click(LetterPage.selectors['upload'])
            self._wait(2)
        page1 = popup_info.value
        page1.close()

        with self.page.expect_popup() as popup_info:
            self.page.click(LetterPage.selectors['try_now'])
            self._wait(2)
        page2 = popup_info.value
        page2.close()

        with self.page.expect_popup() as popup_info:
            self.page.click(LetterPage.selectors['go_to_see'])
            self._wait(2)
        page3 = popup_info.value
        page3.close()

        with self.page.expect_popup() as popup_info:
            self.page.click(LetterPage.selectors['go_to_see_btn'])
            self._wait(2)
        page4 = popup_info.value
        page4.close()
