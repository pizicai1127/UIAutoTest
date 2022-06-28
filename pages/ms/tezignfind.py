#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : tezignfind.py

import pytest
from pages.basepage import BasePage

class Find(BasePage):
    find_elements = [
        {
            # '特赞发现'页的导航栏及下方元素
            "tezignfind": "//div[text() = \'特赞发现\']",
            "Cases_Christmas": "//div[text() = \'精选案例合集｜圣诞节\']",  # 精选案例合集｜圣诞节
            "See_all1": "//div[text() = \'精选案例合集｜圣诞节\']/following-sibling::div[1]",  # "精选案例合集｜圣诞节"旁边的"查看全部"按钮
            "Cases_National": "//div[text() = \'精选案例合集｜国潮\']",  # 精选案例合集｜国潮
            "See_all2": "//div[text() = \'精选案例合集｜国潮\']/following-sibling::div[1]",  # 国潮旁边的"查看全部"按钮
            "Creative_Institute": "//div[text()=\'特赞创意研究院\']",  # 特赞创意研究院
            "See_all3": "//div[text()=\'营销干货/白皮书\']/following-sibling::div[1]",
            "school": "//div[text()=\'特赞学院\']",  # 特赞学院
            "See_all4": "//div[text()=\'视频/直播学习社区\']/following-sibling::div[1]",
            "Creative_people": "//div[text()= \'特赞创意人\']",  # 特赞创意人
            "See_details": "//button[text()=\'查看详情\']",  # 特赞创意人下方的"查看详情"按钮
        },
        {
            "searchInput": "//input[@placeholder=\'搜索服务或案例\']",  # 搜索输入框
            # 各种类的案例标签
            "category": "//div[text()=\'品类\']",
            "feast": "//div[text()=\'节日\']",
            "hotspot": "//div[text()=\'热点\']",
            "Internet": "//button[text()=\'互联网\']",
            "Game": "//button[text()=\'游戏\']",
            "Spring_Festival": "//button[text()=\'春节\']",
            "National_tide": "//button[text()=\'国潮\']",
            "favorite": "//div[@class=\"ant-row\"]/div[1]/descendant::i",  # 第一个收藏按钮icon
            "case_first": "//div[@class=\"ant-row\"]/div[1]",  # 第一个案例
            "Brand_service": "//p[text()=\'服务品牌\']",  # "服务品牌"标签
            "retweete1": "//img[@class=\'icon_share_green___1QeHR\']",  # 转发icon之一
            "retweete2": "//img[@class=\''icon_share___2R0Rd\']",  # 转发icon之二
            "Click_Copy": "//button[text()=\'点击复制\']"  # 点击复制按钮
        },
    ]

    def tezignfind(self):  # '特赞发现'页
        date = self.find_elements
        self.page.click(date[0]["tezignfind"])  # 切换到'特赞发现'页
        assert1 = self.page.text_content(date[0]["Cases_Christmas"])
        # 通过点击按钮打开一个新的浏览器标签页时,在新页面操作需要用这个方法context.expect_page()：
        # with context.expect_page() as new_page_info:
        #     page.click(date[0]["See_all1"])
        # new_page1 = new_page_info.value
        #或者使用page.popup()方法
        #通过点击按钮打开一个新的浏览器标签页时,在新页面操作需要用这个方法：
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[0]["See_all1"])
        new_page1 = new_page_info.value

        new_page1.is_visible("//div[text()=\'特赞主题玩法——圣诞\']")
        assert2 = new_page1.text_content("//div[text()=\'线下装置活动\']")

        # 精选案例合集｜国潮
        assert3 = self.page.text_content(date[0]["Cases_National"])
        # 通过点击按钮打开一个新的浏览器标签页时,在新页面操作需要用这个方法：
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[0]["See_all2"])
        new_page2 = new_page_info.value
        assert4 = new_page2.text_content("text = 特赞*国潮案例")

        # 特赞创意研究院
        assert5 = self.page.text_content(date[0]["Creative_Institute"])
        # 通过点击按钮打开一个新的浏览器标签页时,在新页面操作需要用这个方法：
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[0]["See_all3"])
        new_page3 = new_page_info.value
        assert6 = new_page3.text_content("text = 实用、前沿的营销策略白皮书")

        # 特赞学院
        assert7 = self.page.text_content(date[0]["school"])
        # 通过点击按钮打开一个新的浏览器标签页时,在新页面操作需要用这个方法：
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[0]["See_all4"])
        new_page4 = new_page_info.value
        assert8 = new_page4.text_content("text = 专业、真诚的在线知识分享平台")

        # 特赞创意人
        assert9 = self.page.text_content(date[0]["Creative_people"])
        # 通过点击按钮打开一个新的浏览器标签页时,在新页面操作需要用这个方法：
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[0]["See_details"])
        new_page4 = new_page_info.value
        assert10 = new_page4.text_content("text = 特有想象力")
        return assert1,assert2,assert3,assert4,assert5,assert6,assert7,assert8,assert9,assert10

    def tezignfind_search(self):  # 搜索案例与sku
        date = self.find_elements
        self.page.click(date[0]["tezignfind"])  # 切换到'特赞发现'页
        # 搜索
        self.page.fill(date[1]['searchInput'],'3D')
        self.page.click(date[1]['searchInput'])
        self.page.keyboard.press('Enter')  # 按下"Enter"健进行搜索

        self.page.click("//div[text() = \'展开全部\']")
        assert11 = self.page.text_content("//div[text() = \'3D类长图文\']")
        assert12 = self.page.text_content("text = 产品3D模型影像")
        return assert11,assert12

    def tezignfind_case(self):  # 案例操作
        date = self.find_elements
        self.page.click(date[0]["tezignfind"])  # 切换到'特赞发现'页
        # 点击各个案例分类
        self.page.click(date[1]["category"])
        assert14 = self.page.text_content(date[1]["Game"])

        self.page.click(date[1]["feast"])
        assert15 = self.page.text_content(date[1]["Spring_Festival"])

        self.page.click(date[1]["hotspot"])
        assert16 = self.page.text_content(date[1]["National_tide"])
        #点赞与取消点赞
        self.page.click(date[1]["favorite"])
        assert17 = self.page.text_content("//span[text()=\'点赞成功\']")
        self.page.click(date[1]["favorite"])
        assert18 = self.page.text_content("//span[text()=\'取消点赞\']")
        # 打开案例详情
        with self.page.expect_popup() as new_page_info:
            self.page.click(date[1]['case_first'])
        new_page = new_page_info.value

        assert19 = new_page.text_content(date[1]["Brand_service"])
        # 转发案例
        new_page.click(date[1]["retweete1"])
        assert20 = new_page.text_content("//div[text()=\'分享链接已生成\']")
        new_page.click(date[1]["Click_Copy"])

        return assert14,assert15,assert16,assert17,assert18,assert19,assert20
