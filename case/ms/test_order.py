#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : test_order.py

import pytest
from pages.basepage import BasePage
from pages.ms.order import Order

class TestOrder:

    @pytest.mark.p1
    def test_order01(self, loginVMS):  # 下单方式一：特赞内容SKU下单
        page = Order(loginVMS[0])
        order_assert = page.order01()

        assert order_assert == "下单成功"
        print("下单成功")

    @pytest.mark.p1
    def test_order02(self,loginVMS):  # 下单方式二：一键下单
        page = Order(loginVMS[0])
        order_assert = page.order02()

        assert order_assert == "下单成功"
        print("下单成功")

    @pytest.mark.p1
    def test_order03(self, loginVMS):  # 下单方式三：购物车下单
        page = Order(loginVMS[0])
        order_assert = page.order03()

        assert order_assert == "下单成功"
        print("下单成功")


'''
if __name__ == '__main__':
   # 使用pytest.main来运行测试，--headful是有界面运行，删掉，就是无头模式
   # 这里可以看出playwright的有头指的是要启动浏览器，无头模式就是不看到浏览器运行
    pytest.main(['-v','--headful'])
'''