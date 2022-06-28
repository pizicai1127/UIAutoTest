#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File :test_ratecard """

import pytest
from time import sleep

from pages.designer.RatecardPage import RatePage


class Testratecard:
    shuju = [
        {
            "lowest_price": "1",
            "maximum_price": "2",
            "show": "特赞动态说明动态说明",
            "modify_lowest_price": "5",
            "modify_maximum_price": "10",
        }
    ]
    """
    对创意方服务增删改查操作
    """
    @pytest.mark.parametrize("data", shuju)
    def test_ratecard(self, test_login, data):
        page = RatePage(test_login[0])
        page.goto("https://www.tezign.com/designer/#/ratecardList")
        page._wait(1)
        page.ratecard(data["lowest_price"], data["maximum_price"])
        # page._wait(1)
        # page.editratecard(data["modify_lowest_price"], data["modify_maximum_price"])
        # page.service()
        # page.delete_service()
        # page.share()

    # @pytest.mark.run(order=2)
    @pytest.mark.parametrize("data", shuju)
    def test_editratecard(self, test_login, data):
        test_login[0].goto("https://www.tezign.com/designer/#/ratecardList")
        page = RatePage(test_login[0])
        page._wait(2)
        page.editratecard(data["modify_lowest_price"], data["modify_maximum_price"])

    def test_service(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/ratecardList")
        page = RatePage(test_login[0])
        page.service()

    def test_delete_service(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/ratecardList")
        page = RatePage(test_login[0])
        page.delete_service()

    def test_share(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/ratecardList")
        page = RatePage(test_login[0])
        page.share()
