#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_group_tree_page
# @Author: yanglun@tezign.com
# @Date  : 2022/4/18
# @Desc  :
"""

import pytest
import allure
from pages.assets.CollectionTreeListPage import CollectionTreeListPage


class TestCollectionTreeList:
    """
    素材组-左侧树列表用例
    """

    @allure.title("空判断-直接点击确认button")
    def test_tree_new_group_error(self, login_sys):
        """
        新建素材组-空判断：直接点击确认按钮
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_new_group_error()
        ele = tree_page.read_yaml_element("tree_blank_assert")
        assert tree_page._text_content(ele) == "此为必填信息"

    @allure.title("取消新建素材组")
    def test_tree_new_group_cancel(self, login_sys):
        """
        新建素材组-取消新建
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_new_group_cancel()
        assert True

    @allure.title("新建素材组-不带封面图")
    @pytest.mark.parametrize('text', ['组织组织-树结构'])
    def test_tree_new_group(self, login_sys, text):
        """
        新建素材组-不带封面图
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_new_group(text)
        ele = tree_page.read_yaml_element("tree_new_group_assert")
        assert tree_page._text_content(ele).strip() == text

    @allure.title("树结构进入素材组")
    def test_tree_enter_group(self, login_sys):
        """
        树结构-进入素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_enter_group()
        ele = tree_page.read_yaml_element("tree_enter_group_assert")
        assert tree_page._text_content(ele).strip() == "全部"

    @allure.title("树结构的展开和收起")
    def test_tree_expand_fold(self, login_sys):
        """
        素材组树结构的展开与收起
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_expand_fold()
        assert True

    @allure.title("面包屑切换素材组")
    def test_tree_bread_crumbs(self, login_sys):
        """
        素材组树结构-面包屑切换
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_bread_crumbs()
        ele = tree_page.read_yaml_element("tree_brand_crumb_assert")
        assert tree_page._text_content(ele).strip() == "全部素材组"

    @allure.title("树结构-新标签页打开素材组")
    def test_tree_open_new_tab(self, login_sys):
        """
        素材组树结构-新标签页打开
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_open_new_tab()
        assert True

    @allure.title("树结构-新建子素材组")
    @pytest.mark.parametrize('text', ['子素材组-树结构'])
    def test_tree_new_sub_group(self, login_sys, text):
        """
        素材组树结构-新建子素材组
        @param login_sys:
        @param text:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_new_sub_group(text)
        ele = tree_page.read_yaml_element("tree_new_sub_group_assert")
        assert tree_page._text_content(ele).strip() == text

    @allure.title("树结构-编辑素材组")
    @pytest.mark.parametrize('text', ['组织组织组织'])
    def test_tree_edit_group(self, login_sys, text):
        """
        素材组树结构-编辑素材组
        @param login_sys:
        @param text:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_edit_group(text)
        ele = tree_page.read_yaml_element("tree_edit_group_assert")
        assert tree_page._text_content(ele).strip() == text

    @allure.title("树结构-订阅素材组")
    def test_tree_subscribe_group(self, login_sys):
        """
        素材组树结构-订阅素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_subscribe_group()
        ele = tree_page.read_yaml_element("tree_subscribe_group_assert")
        assert tree_page._text_content(ele) == "订阅成功，每周三10:00将邮件通知更新"

    @allure.title("树结构-取消订阅素材组")
    def test_tree_cancel_subscribe_group(self, login_sys):
        """
        素材组树结构-取消订阅素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_cancel_subscribe_group()
        ele = tree_page.read_yaml_element("tree_cancel_subscribe_assert")
        assert tree_page._text_content(ele) == "取消成功"

    @allure.title("树结构-收藏素材组")
    def test_tree_collect_group(self, login_sys):
        """
        素材组树结构-收藏素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_collect_group()
        ele = tree_page.read_yaml_element("tree_collect_assert")
        assert tree_page._text_content(ele) == "你已成功收藏该素材组"

    @allure.title("树结构-取消收藏素材组")
    def test_tree_cancel_collect_group(self, login_sys):
        """
        素材组树结构-取消收藏素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_cancel_collect_group()
        ele = tree_page.read_yaml_element("tree_cancel_collect_assert")
        assert tree_page._text_content(ele) == "你已取消收藏该素材组"

    @allure.title("空判断-分享空素材组")
    def test_tree_share_blank_group(self, login_sys):
        """
        素材组树结构-分享素材组-空素材组分享
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_share_blank_group()
        ele = tree_page.read_yaml_element("tree_blank_group_share_assert")
        assert tree_page._text_content(ele) == "暂无权限"

    @allure.title("树结构-分享非空素材组")
    def test_tree_share_group(self, login_sys):
        """
        素材组树结构-分享非空素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_share_group()
        ele = tree_page.read_yaml_element("tree_share_assert")
        assert tree_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"

    @allure.title("空判断-下载空素材组")
    def test_tree_download_blank_group(self, login_sys):
        """
        素材组树结构-下载空素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_download_blank_group()
        ele = tree_page.read_yaml_element("tree_download_blank_assert")
        assert tree_page._text_content(ele) == "当前选中了0个素材，请重新选择"

    @allure.title("素材组树结构-下载非空素材组")
    def test_tree_download_group(self, login_sys):
        """
        素材组树结构-下载非空素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_download_group()
        ele = tree_page.read_yaml_element("tree_download_assert")
        assert tree_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组树结构-取消删除素材组")
    def test_tree_cancel_delete_group(self, login_sys):
        """
        素材组树结构-取消删除素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_cancel_delete_group()
        assert True

    @allure.title("素材组树结构-确认删除素材组")
    def test_tree_delete_group(self, login_sys):
        """
        素材组树结构-删除素材组
        @param login_sys:
        @return:
        """
        tree_page = CollectionTreeListPage(login_sys)
        tree_page.goto_group()
        tree_page.tree_delete_group()
        ele = tree_page.read_yaml_element("tree_delete_toast")
        assert "已删除" in tree_page._text_content(ele).strip()


if __name__ == '__main__':
    pytest.main(['-vs', 'test_group_tree_page.py::TestCollectionTreeList::test_tree_edit_group'])
