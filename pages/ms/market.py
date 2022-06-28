#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : market.py

import pytest
from pages.basepage import BasePage

class Market(BasePage):
    market_elements = [
        {
            # 导航栏
            "marketplace": "//div[text() = \'创意商城\']",
            "tezignfind": "//div[text() = \'特赞发现\']",
            "calander": "//div[text() = \'营销日历\']",
            "mycollet": "//div[text() = \'我的收藏\']",
            "myproject": "//div[text() = \'我的项目\']"
    },
        {
            # 创意商城页上方的元素
            "searchInput": "//input[contains(@class,\'input\')]",  # 搜索输入框
            "hotSearch1": "//div[text()=\'短视频\']",  # 热门搜索
            "calanderTab": "//span[@class=\'calendar_icon_text___1pbJX\']"  # 查看完整日历

        },
        {
            # 特赞内容货架
            "excellent_IP": "//span[text() = \'精品 IP\']",
            "Marketing_scenarios": "//span[text() = \'营销场景\']"
        },
        {
            # 特赞内容SKU
            "content_SKU": "//div[text() = \'特赞内容 SKU\']",
            "Flat_illustration": "//span[text() = \'平面插画\']",
            "New_media": "//span[text() = \'新媒体\']",
            "Video_animations": "//span[text() = \'视频动画\']"
        },
    ]




    def market_search(self):
        # 关键字搜索
        date = self.market_elements
        self.page.fill(date[1]['searchInput'],'动画')

        self.page.click("//button[text() = \'搜索\']")
        # 搜索结果页 ，点击"展开全部"
        self.page.wait_for_timeout(1000)
        # self.page.click("//div[text() = \'展开全部\']")
        text_assert1 = self.page.text_content("//div[text() = \'动画后期\']")

        # 热门搜索
        self.page.go_back()  # 回到上一页
        self.page.click(date[1]['hotSearch1'])
        self.page.click("//div[text() = \'展开全部\']")
        text_assert2 = self.page.text_content("//div[text() = \'短视频拍摄\']")

        # 切换特赞内容货架
        self.page.go_back()  # 回到上一页
        self.page.click(date[2]['excellent_IP'])
        text_assert3 = self.page.text_content("//p[text() = \'预发测试2个\']")
        self.page.click(date[2]['Marketing_scenarios'])
        text_assert4 = self.page.text_content("//p[text() = \'平面玩法再升级\']")

        return text_assert1,text_assert2,text_assert3,text_assert4

    def refresh(self):  # sku下拉刷新与切换tab
        date = self.market_elements

        self.page.click(date[3]['Flat_illustration'])
        # 页面下滑，展示更多sku，通过Keyboard.press操作实现
        self.page.click(date[3]['content_SKU'])
        for i in range(30):
            self.page.keyboard.press("ArrowDown")

        content1 = self.page.text_content("//div[text() = \'海报动态效果\']")
        # 切换特赞内容SKU各tab页
        self.page.click(date[3]['New_media'])
        content2 = self.page.text_content("//div[text() = \'AR\']")
        self.page.click(date[3]['Video_animations'])
        content3 = self.page.text_content("//div[text() = \'动画后期\']")

        return content1,content2,content3




'''
if __name__ == '__main__':
   # 使用pytest.main来运行测试，--headful是有界面运行，删掉，就是无头模式
   # 这里可以看出playwright的有头指的是要启动浏览器，无头模式就是不看到浏览器运行
    pytest.main(['-v','--headful'])
'''