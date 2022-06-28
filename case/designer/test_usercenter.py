#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : test_usercenter.py"""

import pytest

from pages.designer.UserCenterPage import MyPage


class TestMyCenter:
    shuju = [{

        "input_style": "特赞风格"

    }
    ]

    def test_mycase(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/welcome")
        page = MyPage(test_login[0])
        page.mycase()

    @pytest.mark.parametrize("data", shuju)
    def test_mycenter(self, test_login, data):
        test_login[0].goto("https://www.tezign.com/designer/#/welcome")
        page = MyPage(test_login[0])
        test_login[0].goto("https://www.tezign.com/designer/#/welcome")
        page.my_information(data["input_style"])
