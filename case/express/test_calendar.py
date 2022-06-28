#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/10 5:01 下午
# @File : test_calendar.py


from pages.express.CalendarPage import CalendarPage


class TestCalendar:


    def test_calendar(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = CalendarPage(expesss_login)
        page.calendar()

    def test_calendar_detail(self, expesss_login):
        expesss_login.goto("https://express.tezign.com")
        page = CalendarPage(expesss_login)
        page.calendar_detail()
        assert page._text_content("text = 订阅成功") == "订阅成功"
