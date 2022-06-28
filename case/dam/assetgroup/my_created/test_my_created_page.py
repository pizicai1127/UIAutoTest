# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/3/8 11:39 上午
# @File:test_my_created_page.py

import pytest
from pages.assets.MyCreaterPage import MyCreatedPage
import allure


class TestMyCreatedPage:

    # @pytest.mark.parametrize('created_name', ['ry自动化测试'])
    # def test_created_group(self, created_name, login_i):
    #     """
    #     新建素材库
    #     @rtype: created_name
    #     """
    #     created_group = MyCreatedPage(login_i)
    #     created_group.goto_created()
    #     created_group.created_group(created_name)
    #     # 获取断言内容
    #     asset_content = created_group._get_url()
    #     # 断言
    #     url = "https://asset-stage.tezign.com/dam_enterprise/group"
    #     assert url in asset_content

    @allure.title("我创建的页面")
    def test_created_page(self,login_i):
        """
        我创建的页面
        @rtype: object
        """
        created_page = MyCreatedPage(login_i)
        created_page.goto_created()
        asset_content = created_page._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise/group"
        assert url in asset_content

    @allure.title("我创建的-搜索框直接输入内容搜索")
    @pytest.mark.parametrize('text', ['ry自动化测试'])
    def test_created_search_text(self, text, login_i):
        """
        我创建的-搜索框直接输入内容搜索
        @param text:
        @param login_i:
        @return:
        """
        created_page = MyCreatedPage(login_i)
        created_page.goto_created()
        created_page.created_search(text)
        ele = created_page.read_yaml_element("created_search_all")
        assert created_page._text_content(ele).strip() == "全部"

    @allure.title("视图-平铺模式")
    def test_created_tile_mode(self,login_i):
        """
        视图-平铺模式
        @rtype: object
        """
        title_mode = MyCreatedPage(login_i)
        title_mode.goto_created()
        title_mode.created_arrangement_tile_mode()
        ele = title_mode.read_yaml_element("created_in_group")
        assert title_mode._is_visible(ele) == True

    @allure.title("视图-列表模式")
    def test_created_list_mode(self,login_i):
        """
        视图-列表模式
        @rtype: login_i
        """
        list_mode = MyCreatedPage(login_i)
        list_mode.goto_created()
        list_mode.created_arrangement_list_mode()
        ele = list_mode.read_yaml_element("created_group_name")
        assert list_mode._text_content(ele) == "素材组名称"

    # 我创建的-平铺模式-进入素材详情
    @allure.title("我创建的-平铺模式-进入素材详情")
    def test_created_title_detail(self, login_i):
        created = MyCreatedPage(login_i)
        created.goto_created()
        created.created_arrangement_tile_mode()
        created.created_ingroup()  # 先跳转到素材组下
        created.created_ingroup()  # 再打开第一个素材
        asset_content = created._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise"
        assert url in asset_content

    # 我创建的-列表模式-进入素材详情
    @allure.title("我创建的-列表模式-进入素材详情")
    def test_created_list_detail(self, login_i):
        created = MyCreatedPage(login_i)
        created.goto_created()
        created.created_arrangement_list_mode()
        created.created_in_Lgroup()
        created.created_in_Lgroup()
        asset_content = created._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise"
        assert url in asset_content

    @allure.title("我创建的-所有排序方式")
    def test_created_sort(self,login_i):
        """
        我创建的-所有排序方式
        @rtype: object
        """
        created_sort_dict={
            'created_sort_updatetime': '更新时间',
            'created_sort_recent': '最近打开',
            'created_sort_hot': '素材热度',
            'created_sort_history_hot': '历史总活跃',
            'created_sort_group_name': '名称排序',
            'created_sort_create_time': '创建时间'
        }
        created_sort_page = MyCreatedPage(login_i)
        created_sort_page.goto_created()
        for key, value in created_sort_dict.items():
            selector = created_sort_page.read_yaml_element(key)
            created_sort_page.created_sort(selector)
            ele = created_sort_page.read_yaml_element("created_sort_text")
            assert created_sort_page._text_content(ele) == value

    # 我创建的-平铺模式-收藏
    @allure.title("我创建的-平铺模式-收藏")
    def test_created_collect(self, login_i):
        created_collect = MyCreatedPage(login_i)
        created_collect.goto_created()
        created_collect.created_arrangement_tile_mode()
        created_collect.created_collect()
        ele = created_collect.read_yaml_element("created_collect_toast")
        assert created_collect._text_content(ele) == '你已成功收藏该素材组'

    # 我创建的-平铺模式-取消收藏
    @allure.title("我创建的-平铺模式-取消收藏")
    def test_created_collect_cancel(self, login_i):
        created_collect = MyCreatedPage(login_i)
        created_collect.goto_created()
        created_collect.created_arrangement_tile_mode()
        created_collect.created_collect()
        ele = created_collect.read_yaml_element("created_collect_toast")
        assert created_collect._text_content(ele) == '你已取消收藏该素材组'

    # def test_in_group(self, login_i):
    #     in_group = MyCreatedPage(login_i)
    #     in_group.goto_created()
    #     in_group.created_ingroup()
    #     url = "https://asset-stage.tezign.com/dam_enterprise/group"
    #     assert url in in_group._get_url()

    # def test_created_delete(self, login_i):
    #     """
    #     删除测试的素材库数据
    #     @rtype: object
    #     """
    #     created_delete = MyCreatedPage(login_i)
    #     created_delete.goto_created()
    #     created_delete.created_ingroup()
    #     created_delete.created_group_delete()
    #     # 获取断言内容
    #     asset_content = created_delete._get_url()
    #     # 断言
    #     url = "https://asset-stage.tezign.com/dam_enterprise/group"
    #     assert url in asset_content


if __name__ == '__main__':
    pytest.main(['-vs', 'test_my_created_page.py::TestMyCreatedPage'])

