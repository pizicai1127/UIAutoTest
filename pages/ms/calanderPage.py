#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : calanderPage.py

import pytest
from pages.basepage import BasePage

class CalanderPage(BasePage):
    find_elements = [
        {
            # '营销日历'页的元素
            "calander": "//div[text() = \'营销日历\']",
            "create_calander": "//button[text() = \'新建日历\']",
            "input_name": "//input[@placeholder=\'输入自定义日历名称\']",
            "select_color": "//button[text() = \'选颜色\']",
            "three_color": "//div[@class = \'color-list\']/div[3]",  # 选择第三个颜色
            "OK_button": "//button[text()= \'OK\']",
            "ensure_button": "//button[text()= \'确定\']",
            "Create_vent": "//div[@class=\"rbc-month-view\"]/div[5]/div/div[5]",  # 新建自定义事件
            "Drop_selection": "//div[@class=\'tz-scroll-inner\']/descendant::span[2]",  # 下拉选择
            "coco": "//li[text()=\'coco\']",  # 下拉选择，选择coco的日历
            "event_name": "//input[@placeholder=\'输入名称\']",  # 事件名称
            "describe": "//div[@class=\'public-DraftStyleDefault-block public-DraftStyleDefault-ltr\']",  # 描述
            "select_button": "//div[@class=\'trc_calendar_main___3lPw9\']/ul[1]/descendant::i[6]",  # 选项卡
            "ensure_button2": "//div[@class=\"ant-modal-footer\"]/button[2]",
            "edit_button": "//li[text()=\'编辑\']",
            "delete_button": "//li[text()=\'删除\']",
            "ensure_button3": "//div[text()= \'确定\']",
            "subscribe": "//div[text() = \'特赞日历\']/following-sibling::span[1]",  # 订阅日历
            "select_button2": "//div[@class=\'trc_calendar_main___3lPw9\']/ul[2]/descendant::i[2]",  # 选项卡2
            "cancel_button": "//li[text()=\'取消订阅\']",  # 取消订阅按钮
        },
    ]

    def calander_create(self):
        date = self.find_elements
        self.page.click(date[0]["calander"])  # 切换到'营销日历'页
        # 新建日历
        self.page.click(date[0]["create_calander"])
        self.page.fill(date[0]["input_name"],"一个测试日历哦")
        self.page.click(date[0]["select_color"])
        self. page.click(date[0]["three_color"])
        self.page.click(date[0]["OK_button"])
        self.page.click(date[0]["ensure_button"])
        # 新建自定义事件
        # self.page.click(date[0]["Create_vent"])
        # self.page.click(date[0]["Drop_selection"])
        # self.page.hover(date[0]["coco"])
        # self.page.click(date[0]["coco"])  # 下拉选择，选择coco的日历
        # self.page.fill(date[0]["event_name"], "这是事件名称")
        # self.page.fill(date[0]["describe"], "这是描述正文")
        # self.page.click("//div[text()=\"新建自定义事件\"]")
        # self.page.click(date[0]["ensure_button2"])
        # self.assert page.text_content("text = 新建自定义事件成功") == "新建自定义事件成功"
        # 编辑日历
        self.page.hover(date[0]["select_button"])
        self.page.wait_for_timeout(1000)
        self.page.click(date[0]["edit_button"])
        self. page.fill(date[0]["input_name"],"编辑一下测试日历")
        self. page.click(date[0]["ensure_button"])


    def calander_delete(self):
        # 删除日历
        date = self.find_elements
        self.page.hover(date[0]["select_button"])
        self.page.wait_for_timeout(1000)
        self. page.click(date[0]["delete_button"])
        self. page.click(date[0]["ensure_button3"])


    def calander_subscribe(self):
        # 订阅\取消日历
        date = self.find_elements
        self.page.wait_for_timeout(1000)
        self.page.click(date[0]["subscribe"])


    def calander_cancel(self):
        date = self.find_elements
        self. page.wait_for_timeout(1000)
        self.page.click(date[0]["select_button2"])
        self.page.click(date[0]["cancel_button"])



'''
if __name__ == '__main__':
   # 使用pytest.main来运行测试，--headful是有界面运行，删掉，就是无头模式
   # 这里可以看出playwright的有头指的是要启动浏览器，无头模式就是不看到浏览器运行
    pytest.main(['-v','--headful'])
'''