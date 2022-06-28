#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : test_mypro.py

import pytest
from pages.ms.myproduct import Mypro
from pages.basepage import BasePage

class TestMypro:

    @pytest.mark.p1
    def test_mypro_all(self, loginVMS):  # 我的项目
        page = Mypro(loginVMS[0])
        page.mypro_all()

        assert page._text_content("//span[text()=\'需求名称\']") == "需求名称"

    @pytest.mark.p1
    def test_mypro_assess(self, loginVMS):   # 编辑评估中的项目
        page = Mypro(loginVMS[0])
        text_assert1 = page.mypro_assess()

        assert text_assert1[0] == "评估中"
        assert text_assert1[1] == "更新成功"
        assert text_assert1[2] == "更新项目详情"


    @pytest.mark.p1
    def test_mypro_recalled(self,loginVMS):
        # 项目撤回
        page = Mypro(loginVMS[0])
        text_assert2 = page.mypro_recalled()

        assert text_assert2[0] == "是否确认撤回项目"
        assert text_assert2[1] == "撤回成功"
        assert text_assert2[2] == "已承接"
        assert text_assert2[3] == "需求名称"
        assert text_assert2[4] == "需求名称"
        assert text_assert2[5] == "已撤销"



'''
if __name__ == '__main__':
   # 使用pytest.main来运行测试，--headful是有界面运行，删掉，就是无头模式
   # 这里可以看出playwright的有头指的是要启动浏览器，无头模式就是不看到浏览器运行
    pytest.main(['-v','--headful'])
'''