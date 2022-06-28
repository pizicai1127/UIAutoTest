#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : test_market.py

import pytest
from pages.basepage import BasePage
from pages.ms.market import Market

class TestMarket:



    @pytest.mark.p1
    def test_market_search(self,loginVMS):
        # 关键字搜索
        page = Market(loginVMS[0])
        text_assert = page.market_search()

        assert text_assert[0] == "动画后期"
        assert text_assert[1] == "短视频拍摄"
        assert text_assert[2] == "预发测试2个"
        assert text_assert[3] == "平面玩法再升级"

    @pytest.mark.p1
    def test_refresh(self,loginVMS):  # sku下拉刷新与切换tab
        page = Market(loginVMS[0])
        content = page.refresh()

        assert content[0] == "海报动态效果"
        assert content[1]== "AR"
        assert content[2] == "动画后期"




'''
if __name__ == '__main__':
   # 使用pytest.main来运行测试，--headful是有界面运行，删掉，就是无头模式
   # 这里可以看出playwright的有头指的是要启动浏览器，无头模式就是不看到浏览器运行
    pytest.main(['-v','--headful'])
'''