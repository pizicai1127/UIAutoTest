#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : favorite.py
import pytest
from pages.basepage import BasePage

class Favorite(BasePage):
    find_elements = [
        {
            # '我的收藏'页的元素
            "mycollet": "//div[text() = \'我的收藏\']",
            "Content_received": "//span[text() = \'收到的内容\']",
            "Thumbsup_case": "//span[text() = \'点赞的案例\']",
            "Content_case": "//div[text()=\'绝密！阿黄的每日放送！\']",  # 收到的案例合集
            "like_case": "//div[text()=\'当大疆Osmo遇到Kuka机器人\']",  # 点赞的案例内容
        },
    ]

    def Content_case(self):
        date = self.find_elements
        self.page.click(date[0]["mycollet"])  # 切换到'我的收藏'页
        self.page.click(date[0]["Content_received"])

    def Thumbsup_case(self):
        date = self.find_elements
        self.page.click(date[0]["Thumbsup_case"])


