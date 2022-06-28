# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/3/11 11:05 上午
# @File:test_my_cooperation_page.py

import pytest
from pages.assets.MyCooperationPage import MyCooperationPage


class TestMyCooperationPage:

    def test_cooperation_page(self, login_i):
        """
        与我协作的页面
        @rtype: object
        """
        cooperation_page = MyCooperationPage(login_i)
        cooperation_page.goto_cooperation()
        asset_content = cooperation_page._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise/group"
        assert url in asset_content

    @pytest.mark.parametrize('text', ['ry自动化测试'])
    def test_cooperation_search_text(self, text, login_i):
        """
        与我协作的-搜索框直接输入内容搜索
        @param text:
        @param login_i:
        @return:
        """
        cooperation_page = MyCooperationPage(login_i)
        cooperation_page.goto_cooperation()
        cooperation_page.cooperation_search(text)
        ele = cooperation_page.read_yaml_element("cooperation_search_all")
        assert cooperation_page._text_content(ele).strip() == "全部"

    def test_cooperation_tile_mode(self, login_i):
        """
        视图-平铺模式
        @rtype: object
        """
        title_mode = MyCooperationPage(login_i)
        title_mode.goto_cooperation()
        title_mode.cooperation_arrangement_tile_mode()
        ele = title_mode.read_yaml_element("cooperation_in_group")
        assert title_mode._text_content(ele) != ''

    def test_cooperation_list_mode(self, login_i):
        """
        视图-列表模式
        @rtype: login_i
        """
        list_mode = MyCooperationPage(login_i)
        list_mode.goto_cooperation()
        list_mode.cooperation_arrangement_list_mode()
        ele = list_mode.read_yaml_element("cooperation_group_name")
        assert list_mode._text_content(ele) == "素材组名称"

    # 我创建的-平铺模式-进入素材详情
    def test_cooperation_title_detail(self, login_i):
        cooperation = MyCooperationPage(login_i)
        cooperation.goto_cooperation()
        cooperation.cooperation_arrangement_tile_mode()
        cooperation.cooperation_in_group()  # 先跳转到素材组下
        cooperation.cooperation_in_group()  # 再打开第一个素材
        asset_content = cooperation._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise"
        assert url in asset_content

    # 我创建的-列表模式-进入素材详情
    def test_cooperation_list_detail(self, login_i):
        cooperation = MyCooperationPage(login_i)
        cooperation.goto_cooperation()
        cooperation.cooperation_arrangement_list_mode()
        cooperation.cooperation_Lgroup()
        cooperation.cooperation_Lgroup()
        asset_content = cooperation._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise"
        assert url in asset_content

    def test_cooperation_sort(self, login_i):
        """
        与我协作的-所有排序方式
        @rtype: object
        """
        cooperation_sort_dict = {
            'cooperation_sort_updatetime': '更新时间',
            'cooperation_sort_recent': '最近打开',
            'cooperation_sort_hot': '素材热度',
            'cooperation_sort_history_hot': '历史总活跃',
            'cooperation_sort_group_name': '名称排序',
            'cooperation_sort_create_time': '创建时间'
        }
        cooperation_sort_page = MyCooperationPage(login_i)
        cooperation_sort_page.goto_cooperation()
        for key, value in cooperation_sort_dict.items():
            selector = cooperation_sort_page.read_yaml_element(key)
            cooperation_sort_page.cooperation_sort(selector)
            ele = cooperation_sort_page.read_yaml_element("cooperation_sort_text")
            assert cooperation_sort_page._text_content(ele) == value

    # 与我协作的-平铺模式-收藏
    def test_cooperation_collect(self, login_i):
        cooperation_collect = MyCooperationPage(login_i)
        cooperation_collect.goto_cooperation()
        cooperation_collect.cooperation_arrangement_tile_mode()
        cooperation_collect.cooperation_collect()
        ele = cooperation_collect.read_yaml_element("cooperation_collect_toast")
        assert cooperation_collect._text_content(ele) == '你已成功收藏该素材组'

    # 我创建的-平铺模式-取消收藏
    def test_cooperation_collect_cancel(self, login_i):
        cooperation_collect = MyCooperationPage(login_i)
        cooperation_collect.goto_cooperation()
        cooperation_collect.cooperation_arrangement_tile_mode()
        cooperation_collect.cooperation_collect()
        ele = cooperation_collect.read_yaml_element("cooperation_collect_toast")
        assert cooperation_collect._text_content(ele) == '你已取消收藏该素材组'


if __name__ == '__main__':
    pytest.main(['-vs', 'test_my_cooperation_page.py::TestMyCooperationPage'])
