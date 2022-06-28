#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_official_website.py


import pytest
from pages.top.official_website import Official_website

class TestOfficial_website:
    # 官网消息&招聘 菜单


    @pytest.mark.p0
    def test_news_list(self, topLogin):
        # 消息列表 菜单
        page = Official_website(topLogin)
        text_assert = page.news_list()

    @pytest.mark.p0
    def test_website_Announcements(self, topLogin):
        # 网站公告 菜单
        page = Official_website(topLogin)
        text_assert = page.website_Announcements()

    @pytest.mark.p0
    def test_customer_message(self, topLogin):
        # 客户留言 菜单
        page = Official_website(topLogin)
        text_assert = page.customer_message()



