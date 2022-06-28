#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/3/4 2:59 下午
# @Author: cuiguoen
# @File : test_tezignfind.py

import pytest
from pages.ms.tezignfind import Find

class TestFind:
    @pytest.mark.p1
    def test_tezignfind(self, loginVMS):  # '特赞发现'页
        page = Find(loginVMS[0])
        text_assert = page.tezignfind()

        assert text_assert[0] == "精选案例合集｜圣诞节"
        assert text_assert[1] == "线下装置活动"
        assert text_assert[2] == "精选案例合集｜国潮"
        assert text_assert[3] == "特赞*国潮案例"
        assert text_assert[4] == "特赞创意研究院"
        assert text_assert[5] == "实用、前沿的营销策略白皮书"
        assert text_assert[6] == "特赞学院"
        assert text_assert[7] == "专业、真诚的在线知识分享平台"
        assert text_assert[8] == "特赞创意人"
        assert text_assert[9] == "特有想象力"

    @pytest.mark.p1
    def test_search(self, loginVMS):  # 搜索案例与sku
        page = Find(loginVMS[0])
        text_assert2 = page.tezignfind_search()
        assert text_assert2[0] == "3D类长图文"
        assert text_assert2[1] == "产品3D模型影像"

    @pytest.mark.p1
    def test_case(self, loginVMS):  # 案例操作
        page = Find(loginVMS[0])
        text_assert3 = page.tezignfind_case()

        assert text_assert3[0] == "游戏"
        assert text_assert3[1] == "春节"
        assert text_assert3[2] == "国潮"
        assert text_assert3[3] == "点赞成功"
        assert text_assert3[4] == "取消点赞"
        assert text_assert3[5] == "服务品牌"
        assert text_assert3[6] =="分享链接已生成"

'''
if __name__ == '__main__':
   # 使用pytest.main来运行测试，--headful是有界面运行，删掉，就是无头模式
   # 这里可以看出playwright的有头指的是要启动浏览器，无头模式就是不看到浏览器运行
    pytest.main(['-v','--headful'])
'''