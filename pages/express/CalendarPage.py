#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/10 5:01 下午
# @File : CalendarPage.py
from pages.express.ExpressBasePage import ExpressBasePage


class CalendarPage(ExpressBasePage):
    selectors = {
        # 营销日历Tab
        "calendarTab": "#root > header > div > div.expressNavBarInnerLeft___3vZnM > nav > ul > li.navbar-tab.display-block.hot > a",
        # 左上角的创意商城
        "creative_mall": "#root > div > div > div > div.pt-20.pb-20.pl-36.calendar-navigation > div > span:nth-child(1) > span",
        # 右上角周
        "week_btn": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.rbc-calendar > div.display-flex.justify-center.calendar-header > div.position-absolute.r-20 > button.tz-btn.header-week-btn.type-neutral.shape-round",
        # 右上角月
        "month_btn": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.rbc-calendar > div.display-flex.justify-center.calendar-header > div.position-absolute.r-20 > button.tz-btn.header-month-btn.type-neutral.shape-round",
        # 日历下一天按钮
        "calendar_next_btn": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.rbc-calendar > div.display-flex.justify-center.calendar-header > div.display-flex.justify-space-between.mr-10 > button:nth-child(3) > i > svg",
        # 日历上一天按钮
        "calendar_last_btn": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.rbc-calendar > div.display-flex.justify-center.calendar-header > div.display-flex.justify-space-between.mr-10 > button:nth-child(1) > i > svg",
        # 今天按钮
        "today_btn": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.rbc-calendar > div.display-flex.justify-center.calendar-header > div.display-flex.justify-space-between.mr-10 > button.tz-btn.type-primary.shape-round",
        # 日历
        "calendar_btn": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.rbc-calendar > div.display-flex.justify-center.calendar-header > div.display-flex.justify-space-between.mr-10 > span > div > i > svg",
        # 下一年
        "next_year_btn": "body > div:nth-child(11) > div > div > div > div > div > div > div.ant-calendar-month-panel > div > div.ant-calendar-month-panel-header > a.ant-calendar-month-panel-next-year-btn",
        # 上一年
        "last_year_btn": "body > div:nth-child(11) > div > div > div > div > div > div > div.ant-calendar-month-panel > div > div.ant-calendar-month-panel-header > a.ant-calendar-month-panel-prev-year-btn",
        # 今年
        "this_year_btn": "body > div:nth-child(11) > div > div > div > div > div > div > div.ant-calendar-month-panel > div > div.ant-calendar-month-panel-header > a.ant-calendar-month-panel-year-select > span.ant-calendar-month-panel-year-select-content",
        # 十二月
        "december": "body > div:nth-child(11) > div > div > div > div > div > div > div.ant-calendar-month-panel > div > div.ant-calendar-month-panel-body > table > tbody > tr:nth-child(4) > td:nth-child(3) > a",
        # 特赞日历
        "favorite_calendar_btn": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.sidebar_warp___36oRK > div > ul:nth-child(2) > li:nth-child(1) > div > div",
        # 特赞日历更多按钮
        # "favorite_calendar": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.sidebar_warp___36oRK > div > ul:nth-child(2) > li:nth-child(1) > div > span.item_subscribe___37_KQ > span > i",
        "favorite_calendar": '[aria-label="icon-more"] svg',
        # 取消订阅按钮
        "cancel_subscribe": "text=取消订阅",
        # 可订阅日历，特赞日历
        "tezign_calendar": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.sidebar_warp___36oRK > div > ul:nth-child(4) > li:nth-child(1) > div > div",
        # 可订阅特赞日历
        "subscribe_tezign_calendar": "#root > div > div > div > div.spin-wrap.size-default > div.spin-container > div > div.sidebar_warp___36oRK > div > ul:nth-child(4) > li:nth-child(1) > div > span.item_subscribe___37_KQ > span",

    }

    def calendar(self):
        # 点击营销日历
        self.page.click(CalendarPage.selectors['calendarTab'])
        # 点击创意商城面包屑
        self.page.click(CalendarPage.selectors['creative_mall'])

    def calendar_detail(self):
        # 点击营销日历
        self.page.click(CalendarPage.selectors['calendarTab'])
        # 点击周视图
        self.page.click(CalendarPage.selectors['week_btn'])
        # 点击月视图
        self.page.click(CalendarPage.selectors['month_btn'])
        # 点击下一天
        self.page.click(CalendarPage.selectors['calendar_next_btn'])
        # 点击上一天
        self.page.click(CalendarPage.selectors['calendar_last_btn'])
        # 点击今天
        self.page.click(CalendarPage.selectors['today_btn'])
        # 点击日历
        self.page.click(CalendarPage.selectors['calendar_btn'])
        # self._wait(3)
        # 点击下一年按钮
        self.page.click(CalendarPage.selectors['next_year_btn'])
        # 点击上一年按钮
        self.page.click(CalendarPage.selectors['last_year_btn'])
        # 点击今年
        self.page.click(CalendarPage.selectors['this_year_btn'])
        self.page.click(CalendarPage.selectors['calendarTab'])
        # 点击日历
        self.page.click(CalendarPage.selectors['calendar_btn'])
        # 点击12月
        self.page.click(CalendarPage.selectors['december'])
        self.page.click(CalendarPage.selectors['today_btn'])
        # 点击特赞日历
        self.page.click(CalendarPage.selectors['favorite_calendar_btn'])
        # 特赞日历更多按钮
        self.page.click(CalendarPage.selectors['favorite_calendar'])
        # 取消订阅按钮
        self.page.click(CalendarPage.selectors['cancel_subscribe'])
        # 可订阅日历，订阅特赞日历
        self.page.click(CalendarPage.selectors['tezign_calendar'])
        # 订阅特赞日历
        self.page.click(CalendarPage.selectors['subscribe_tezign_calendar'])

