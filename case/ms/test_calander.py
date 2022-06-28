#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : test_calander.py

import pytest
from pages.ms.calanderPage import CalanderPage
from pages.basepage import BasePage
class TestCalander:

    @pytest.mark.p1
    def test_calander_create(self, loginVMS):  # 我的项目
        page = CalanderPage(loginVMS[0])
        page.calander_create()
        assert page._text_content("text = 编辑自定义日历成功") == "编辑自定义日历成功"

    @pytest.mark.p1
    def test_calander_delete(self,loginVMS):
        page = CalanderPage(loginVMS[0])
        page.calander_delete()
        assert page._text_content("text = 删除自定义日历成功") == "删除自定义日历成功"

    @pytest.mark.p1
    def test_calander_subscribe(self, loginVMS):
        page = CalanderPage(loginVMS[0])
        page.calander_subscribe()
        assert page._text_content("text = 订阅成功") == "订阅成功"

        page.calander_cancel()
        assert page._text_content("text = 已取消订阅") == "已取消订阅"


'''
if __name__ == '__main__':
   # 使用pytest.main来运行测试，--headful是有界面运行，删掉，就是无头模式
   # 这里可以看出playwright的有头指的是要启动浏览器，无头模式就是不看到浏览器运行
    pytest.main(['-v','--headful'])
'''