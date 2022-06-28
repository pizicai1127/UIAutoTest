#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_all_group
# @Author: yanglun@tezign.com
# @Date  : 2022/2/25
# @Desc  :  
"""

import pytest
import allure
from pages.assets.AllCollectionPage import AllCollectionPage
from common.file_method import FileMethod


class TestAllCollection:
    """
    全部素材组下测试用例集
    """

    @allure.title("取消新建素材组")
    def test_group_new_cancel(self, login_sys):
        """
        取消新建素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        selector = group_page.group_new_cancel()
        assert group_page._is_visible(selector) is False

    @allure.title("全部素材组下-新建素材组")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("group_name", ['UI自动化测试-YL'])
    def test_group_new(self, group_name, login_sys):
        """
        测试新建素材组-不带封面图
        @param group_name:
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        # 进入素材组路由
        group_page.goto_group()
        # 新建素材组
        selector = group_page.group_new(group_name)
        assert group_page._text_content(selector).strip() == "全部"

    @allure.title("全部素材组下-搜索素材/素材组")
    @pytest.mark.parametrize('text', ['UI自动化测试'])
    def test_group_search_text(self, text, login_sys):
        """
        全部下搜索框直接输入内容搜索
        @param text:
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        selector = group_page.group_search_text(text)
        assert group_page._text_content(selector).strip() == "全部"

    @allure.title("全部素材组下-搜索框内删除搜索内容")
    @pytest.mark.parametrize('text', ['UI自动化测试'])
    def test_group_search_backspace(self, text, login_sys):
        """
        全部下模拟backspace删除输入内容
        @param text:
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        selector = group_page.group_search_backspace(text)
        assert group_page._text_content(selector).strip() == "全部"

    @allure.title("全部素材组下-清除搜索框输入内容")
    @pytest.mark.parametrize('text', ['UI自动化测试'])
    def test_group_search_clear(self, text, login_sys):
        """
        全部下清除搜索输入内容
        @param text:
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        selector = group_page.group_search_clear(text)
        assert group_page._text_content(selector).strip() == ""

    @allure.title("全部素材组下-列表视图")
    @pytest.mark.flaky(reruns=1)
    def test_group_list_view(self, login_sys):
        """
        全部下-素材组列表视图
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        selector = group_page.group_list_view()
        assert group_page._text_content(selector) == "素材组名称"

    @allure.title("全部素材组下-列表视图下进入素材组")
    def test_group_enter_list(self, login_sys):
        """
        列表视图下进入素材组
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        selector = group_page.group_enter_list()
        assert group_page._text_content(selector).strip() == "全部"

    @allure.title("全部素材组下-平铺视图")
    @pytest.mark.flaky(reruns=1)
    def test_group_view_tile(self, login_sys):
        """
        全部下-素材组平铺视图
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        selector = group_page.group_tile_view()
        assert group_page._is_visible(selector) is True

    @allure.title("全部素材组下-平铺视图下进入素材组")
    def test_group_enter(self, login_sys):
        """
        平铺视图下进入素材组内
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        selector = group_page.read_yaml_element("collection_all_level")
        assert group_page._text_content(selector).strip() == "全部"

    @allure.title("全部素材组下-收藏素材组")
    def test_group_collect(self, login_sys):
        """
        收藏素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.group_collect()
        ele = group_page.read_yaml_element("collect_successful_toast")
        assert group_page._text_content(ele) == "你已成功收藏该素材组"

    @allure.title("全部素材组下-取消收藏素材组")
    def test_group_collect_cancel(self, login_sys):
        """
        全部素材组下-取消收藏素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.group_collect()
        ele = group_page.read_yaml_element("right_cancel_collect")
        assert group_page._text_content(ele) == "你已取消收藏该素材组"

    @allure.title("全部素材组下-素材组排序")
    def test_group_sort(self, login_sys):
        """
        全部下素材组排序
        @param login_sys:
        @return:
        """
        sort_dict = {
            'sort_recent': '最近打开',
            'sort_asset_hot': '素材热度',
            'sort_history_hot': '历史总活跃',
            'sort_name': '名称排序',
            'sort_create_time': '创建时间',
            'sort_update_time': '更新时间',
        }
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        for key, value in sort_dict.items():
            selector = group_page.read_yaml_element(key)
            group_page.group_sort(selector)
            ele = group_page.read_yaml_element("sort_text")
            assert group_page._text_content(ele) == value

    @allure.title("鼠标右键-新建素材组")
    def test_right_mouse_new_group(self, login_sys):
        """
        鼠标右键-新建素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        selector = group_page.right_mouse_new_group()
        assert group_page._text_content(selector).strip() == "全部"

    @allure.title("鼠标右键-新标签页打开")
    def test_right_mouse_new_tab(self, login_sys):
        """
        鼠标右键-新标签页打开
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_new_tab()
        assert True

    @allure.title("鼠标右键-编辑信息")
    def test_right_mouse_edit(self, login_sys):
        """
        鼠标右键-编辑信息
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        text = group_page.right_mouse_edit()
        assert text == "右键-编辑素材组"

    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    @allure.title("鼠标右键-编辑上传封面图")
    def test_group_cover_picture(self, login_sys, file_path):
        """
        鼠标右键-编辑上传封面图
        @param login_sys:
        @param file_path:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        url = group_page.group_cover_picture(file_path)
        assert 'tezign' in url

    @allure.title("鼠标右键-删除封面图")
    def test_group_cover_picture_clear(self, login_sys):
        """
        鼠标右键-删除封面图
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        url = group_page.group_cover_picture_clear()
        assert 'tezign' not in url

    @allure.title("鼠标右键-订阅素材组")
    def test_right_mouse_subscribe(self, login_sys):
        """
        鼠标右键-订阅素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_subscribe()
        ele = group_page.read_yaml_element("right_subscribed_toast")
        assert group_page._text_content(ele) == "订阅成功，每周三10:00将邮件通知更新"

    @allure.title("鼠标右键-取消订阅素材组")
    def test_right_mouse_subscribe_cancel(self, login_sys):
        """
        鼠标右键-取消订阅素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_subscribe()
        ele = group_page.read_yaml_element("right_cancel_subscribe")
        assert group_page._text_content(ele) == "取消成功"

    @allure.title("鼠标右键-收藏素材组")
    def test_right_mouse_collect(self, login_sys):
        """
        鼠标右键-收藏素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_collect()
        ele = group_page.read_yaml_element("right_collected_toast")
        assert group_page._text_content(ele) == "你已成功收藏该素材组"

    @allure.title("鼠标右键-取消收藏素材组")
    def test_right_mouse_collect_cancel(self, login_sys):
        """
        鼠标右键-取消收藏素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_collect()
        ele = group_page.read_yaml_element("right_cancel_collect")
        assert group_page._text_content(ele) == "你已取消收藏该素材组"

    @allure.title("鼠标右键-分享空素材组")
    def test_right_mouse_share(self, login_sys):
        """
        鼠标右键-分享空素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_share()
        ele = group_page.read_yaml_element("right_share_blank_group_toast")
        assert group_page._text_content(ele) == "请先添加素材"

    @allure.title("鼠标右键-复制素材组至自身")
    def test_right_mouse_copy_to_self(self, login_sys):
        """
        鼠标右键-复制素材组至自身
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_copy_to_self()
        ele = group_page.read_yaml_element("copy_to_self_toast")
        assert group_page._text_content(ele) == "不能复制到自身或其子素材组内"

    @allure.title("鼠标右键-移动素材组至全部下")
    def test_right_mouse_move_to_all(self, login_sys):
        """
        鼠标右键-移动素材组至全部下
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_move_to_all()
        ele = group_page.read_yaml_element("copy_move_successful")
        assert group_page._text_content(ele) == "操作成功"

    @allure.title("鼠标右键-下载空素材组")
    def test_right_mouse_download_blank_group(self, login_sys):
        """
        鼠标右键-下载空素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_download_blank_group()
        ele = group_page.read_yaml_element("right_download_toast")
        assert group_page._text_content(ele) == "当前选中了0个素材，请重新选择"

    @allure.title("鼠标右键-删除素材组")
    def test_right_mouse_delete(self, login_sys):
        """
        鼠标右键-删除素材组
        @param login_sys:
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.right_mouse()
        group_page.right_mouse_delete()
        ele = group_page.read_yaml_element("right_delete_toast")
        assert "已删除" in group_page._text_content(ele)

    @allure.title("鼠标右键-排序升序")
    def test_group_asc(self, login_sys):
        """
        排序升序
        @return:
        """
        group_page = AllCollectionPage(login_sys)
        group_page.goto_group()
        group_page.group_group_asc()
        assert True

    @allure.title("鼠标右键-排序降序")
    @pytest.mark.usefixtures()
    def test_group_desc(self, data_init):
        """
        排序降序
        @return:
        """
        data_init.group_sort_desc()
        assert True


if __name__ == '__main__':
    pytest.main(['-vs', 'test_all_group.py::TestAllCollection::test_group_new_cancel'])










