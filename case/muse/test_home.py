#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/6/15 5:58 下午
# @File : test_home.py

from pages.muse.MusePage import MusePage


class TestMuseHome:
    #  搜索销售人员
    def test_drag_and_drop(self, top_login):
        page = MusePage(top_login)
        page.goto("https://musetransfer.com/")
        # selector = MusePage.selectors["business_type_assert"]
        page._wait(1)
        page.drag_and_drop()


