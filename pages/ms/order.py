#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : order.py

from pages.basepage import BasePage
import pytest

class Order(BasePage):
    market_elements = [
        {
            # 下单元素
            "Shopping_icon": "//div[@class=\'ant-row sku_list_content_box___2jSku\']/div[1]/div/div[2]/button",
            # 第1个sku的购物车图标
            "numbers": "//input[@role=\'spinbutton\']",  # 数目输入栏
            "increase": "//div[@class=\"ant-input-number-handler-wrap\"]/span[1]",  # 数目增加按钮
            "reduce": "//div[@class=\"ant-input-number-handler-wrap\"]/span[2]",  # 数目减少按钮
            "Add_to_cart": "//button[text()=\'加入购物车\']",  # 加入购物车按钮
            "Shopping_icon5": "//div[@class=\'ant-row sku_list_content_box___2jSku\']/div[5]/div/div[2]/button",
            # 第5个sku的购物车图标
            "Order_immediately": "text = 立即下单",  # 立即下单按钮
            "order_cancel": "//button[text()=\'取 消\']",  # 取消下单按钮
            "order_confirm": "//button[text()=\'确定下单\']",  # 确定下单按钮
            "project_name": "//input[@placeholder=\"请输入文字，最多30个汉字\"]",  # 下单弹框的项目名称
            "project_overview": "//div[contains(@placeholder,\"为了便于为您\")]",  # 下单弹框的项目概述
            "Supplemental_Information": "//div[text()=\"补充信息\"]",  # 下单弹框的补充信息线
            "delivery_time": "//input[@placeholder=\"选填\"]",  # 下单弹框的交付时间
            "time_today": "//a[text()=\"Today\"]",  # 下单弹框的交付时间选择今天
            "budget": "//input[starts-with(@placeholder,\"选填，可在项目\")]",  # 预算
            "Add_attachment": "//div[@class=\"input-wrap\"]",  # 添加附件资料
            "order_ensure": ":nth-match(:text(\"确定下单\"), 2)",  # 下单内容弹框的确认下单按钮
            "Successfully_order": "//div[text()=\"下单成功\"]"  # 下单成功弹框的名字
        },
        {
            "one_click_order": "//button[text()=\"一键下单\"]",  # 右上角的一键下单按钮
            "Shopping_icon2": "//div[@class=\'ant-row sku_list_content_box___2jSku\']/div[3]/div/div[2]/button",
            # 第3个sku的购物车图
            "Shopping_trolley": "//button[text()=\"购物车\"]",  # 右上角的购物车按钮
            "Modify_card": "//span[@class=\"edit___3c7VT\"]",  # 修改购物车
            "numbers2": "//input[@max=\"99999\"]",  # 购物车数目输入框
            "Modify_confirm": "//button[text()=\'确认修改\']"  # 确认修改按钮

        }
    ]

    def order01(self):  # 下单方式一：特赞内容SKU下单
        date = self.market_elements
        # 鼠标hover到购物车图标
        self.page.hover(date[0]["Shopping_icon"])
        self.page.click(date[0]["Shopping_icon"])

        self.page.wait_for_timeout(1000)

        self.page.click(date[0]["increase"])  # 数目增加按钮
        self.page.click(date[0]["reduce"])  # 数目减少按钮
        self.page.fill(date[0]["numbers"], "11")  # 数目输入数字11
        self.page.click(date[0]["Order_immediately"])  # 点击立即下单

        self.page.fill(date[0]["project_name"], "立即下单测试")  # 填写项目名称
        self.page.fill(date[0]["project_overview"], "测试项目概述")  # 填写项目概述
        # 填写补充信息
        self.page.click(date[0]["Supplemental_Information"])  # 打开补充信息
        self.page.click(date[0]["delivery_time"])
        self.page.click(date[0]["time_today"])  # 时间选择今天
        self.page.fill(date[0]["budget"], "1100")  # 预算填写1100
        # loginFirst.click(date[0]["Add_attachment"])  # 添加附件，同步代码后需要上传服务器的文件路径
        # loginFirst.set_input_files(
        #     "div[role=\"dialog\"]:has-text(\"补充资料添加附件资料\")",
        #     "/Users/cuiguoen/Downloads/018b3f5cb5e56ba801208f8bcfa313.jpg@1280w_1l_2o_100sh.jpg")   # 添加附件
        self.page.click(date[0]['order_confirm'])  # 确定下单

        assert1 = self.page.text_content(date[0]["Successfully_order"])
        # 通过移动鼠标到空白处点击，关闭下单成功弹窗
        self.page.hover(date[0]['Successfully_order'])
        self.page.mouse.move(100, 0)
        self.page.mouse.click(100, 0)
        self.page.reload()

        self.page.hover(date[0]["Shopping_icon5"])
        self.page.click(date[0]["Shopping_icon5"])
        self.page.fill(date[0]["numbers"], "55")  # 数目输入数字55
        self.page.click(date[0]["Add_to_cart"])  # 点击加入购物车
        return assert1

    def order02(self):  # 下单方式二：一键下单
        date2 = self.market_elements
        self.page.reload()
        self.page.click(date2[1]["one_click_order"])  # 点击右上角的一键下单按钮

        # 打开下单弹框，取消下单
        self.page.click(date2[0]["order_cancel"])  # 取消下单
        # 再次打开下单弹框，进行下单
        self.page.click(date2[1]["one_click_order"])
        # 下单内容填写
        self.page.fill(date2[0]["project_name"], "一键下单测试")  # 填写项目名称
        self.page.fill(date2[0]["project_overview"], "测试项目概述22")  # 填写项目概述
        # 填写补充信息
        self.page.click(date2[0]["Supplemental_Information"])  # 打开补充信息
        self.page.click(date2[0]["delivery_time"])
        self.page.click(date2[0]["time_today"])  # 时间选择今天
        self.page.fill(date2[0]["budget"], "2000")  # 预算填写2000
        self.page.click(date2[0]['order_confirm'])  # 确定下单

        assert2 = self.page.text_content(date2[0]["Successfully_order"])
        # 通过移动鼠标到空白处点击，关闭下单成功弹窗
        self.page.hover(date2[0]['Successfully_order'])
        self.page.mouse.move(100, 0)
        self.page.mouse.click(100, 0)
        return assert2

    def order03(self):  # 下单方式三：购物车下单
        date3 = self.market_elements
        self.page.reload()
        self.page.click("//span[text()=\"视频动画\"]")
        self.page.wait_for_timeout(1000)
        # 鼠标hover到购物车图标
        self.page.hover(date3[1]["Shopping_icon2"])
        self.page.click(date3[0]["increase"])  # 数目增加按钮
        self.page.click(date3[0]["reduce"])  # 数目减少按钮
        self.page.fill(date3[0]["numbers"], "3")  # 数目输入数字3
        self.page.click(date3[0]["Add_to_cart"])  # 点击加入购物车

        self.page.hover(date3[1]["Shopping_trolley"])  # hover右上角的购物车按钮
        self.page.click(date3[1]["Modify_card"])  # 修改购物车
        self.page.fill(date3[1]["numbers2"], "33")  # 修改数目
        self.page.click(date3[1]["Modify_confirm"])  # 确认修改
        self.page.wait_for_timeout(1000)
        self.page.hover(date3[1]["Shopping_trolley"])  # hover右上角的购物车按钮
        self.page.click(date3[1]["Shopping_trolley"])

        self.page.click(date3[0]["order_confirm"])  # 确定下单
        # 下单内容填写
        self.page.fill(date3[0]["project_name"], "购物车下单测试")   # 填写项目名称
        self.page.fill(date3[0]["project_overview"], "测试项目概述333")  # 填写项目概述
        # 填写补充信息
        self.page.click(date3[0]["Supplemental_Information"])  # 打开补充信息
        self.page.click(date3[0]["delivery_time"])
        self.page.click(date3[0]["time_today"])  # 时间选择今天
        self.page.fill(date3[0]["budget"], "3000")  # 预算填写3000
        self.page.click(date3[0]['order_ensure'])  # 确定下单

        assert3 = self.page.text_content(date3[0]["Successfully_order"])
        # 通过移动鼠标到空白处点击，关闭下单成功弹窗
        self.page.hover(date3[0]['Successfully_order'])
        self.page.mouse.move(100,0)
        self.page.mouse.click(100,0)
        return assert3
