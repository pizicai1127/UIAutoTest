# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/4/20 2:54 下午
# @File:test_life_cycle_mange.py
import pytest
from pages.assets.LifecycleManagePage import LifeCyclePage


class TestLifeCycleMange:
    def test_lifecycle_page(self, login_i):
        """
        进入有效期管理页面
        @rtype: login_i
        """
        lifecycle_page = LifeCyclePage(login_i)
        lifecycle_page.goto_Lifecycle()
        asset_content = lifecycle_page._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise/"
        assert url in asset_content

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_lifecycle_add(self, text, login_i):
        """
        添加有效期规则
        @param text:
        @param login_i:
        @return:
        """
        lifecycle_page = LifeCyclePage(login_i)
        lifecycle_page.goto_Lifecycle()
        lifecycle_page.Lifecycle_add(text)
        ele = lifecycle_page.read_yaml_element("lifecycle_search_first")
        assert lifecycle_page._text_content(ele) == text

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_lifecycle_search(self, text, login_i):
        """
        有效期管理-搜索规则名称或标签
        @param text:
        @param login_i:
        @return:
        """
        lifecycle_page = LifeCyclePage(login_i)
        lifecycle_page.goto_Lifecycle()
        lifecycle_page.lifecycle_search(text)
        ele = lifecycle_page.read_yaml_element("lifecycle_search_first")
        assert lifecycle_page._text_content(ele) == text

    def test_lifecycle_edit(self, login_i):
        """
        有效期管理-编辑-发布成功
        @param login_i:
        @return:
        """
        lifecycle_page = LifeCyclePage(login_i)
        lifecycle_page.goto_Lifecycle()
        lifecycle_page.lifecycle_edit()
        ele = lifecycle_page.read_yaml_element("lifecycle_title")
        lifecycle_page._wait_for_selector(ele)
        assert lifecycle_page._text_content(ele) == '有效期管理'

    def test_lifecycle_related(self, login_i):
        """
        有效期管理-查看关联素材-打开成功
        @param login_i:
        @return:
        """
        lifecycle_page = LifeCyclePage(login_i)
        lifecycle_page.goto_Lifecycle()
        lifecycle_page.lifecycle_related()
        asset_content = lifecycle_page._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise"
        assert url in asset_content

    def test_lifecycle_delete(self, login_i):
        """
        删除
        @param login_i:
        @return:
        """
        lifecycle_page = LifeCyclePage(login_i)
        lifecycle_page.goto_Lifecycle()
        ele = lifecycle_page.read_yaml_element("lifecycle_search_first")
        if lifecycle_page._text_content(ele) == 'ry自动化':
            lifecycle_page.lifecycle_delete()
            ele = lifecycle_page.read_yaml_element("lifecycle_delete_toast")
            lifecycle_page._wait_for_selector(ele)
            assert lifecycle_page._text_content(ele) == '删除成功'
        else:
            pass







