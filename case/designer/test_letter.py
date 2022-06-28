#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : test_letter.py"""

import pytest

from pages.designer.LetterPage import LetterPage


class TestLetter:

    # 查看创意方站内信
    def test_letter(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/ratecardList")
        page = LetterPage(test_login[0])
        page.mail()

    # 查看创意方资金管理
    def test_money(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/ratecardList")
        page = LetterPage(test_login[0])
        page.moneycase()

    # 查看创意方工具箱
    def test_tools(self, test_login):
        page = LetterPage(test_login[0])
        page.tools()
