#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : test_favorite.py

import pytest
from pages.ms.favorite import Favorite
from pages.basepage import BasePage

class TestFavorite:

    @pytest.mark.p1
    def test_favorite(self, loginVMS):  # 案例操作
        page = Favorite(loginVMS[0])
        page.Content_case()
        assert page._text_content("//div[text()=\'绝密！阿黄的每日放送！\']") == "绝密！阿黄的每日放送！"

        page.Thumbsup_case()
        assert page._text_content("//div[text()=\'当大疆Osmo遇到Kuka机器人\']") == "当大疆Osmo遇到Kuka机器人"


