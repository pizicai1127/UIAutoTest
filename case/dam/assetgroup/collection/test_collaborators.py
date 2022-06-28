#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_collaborators
# @Author: yanglun@tezign.com
# @Date  : 2022/3/10
# @Desc  :  
"""

import pytest
import allure
from pages.assets.CollaboratorsPage import CollaboratorsPage


class TestCollaboratorsPage:
    """
    素材组协作者测试用例集
    """

    @allure.title("进入协作者页面")
    @pytest.mark.flaky(reruns=1)
    def test_enter_collaborators(self, login_sys):
        """
        测试进入协作者页面
        @param login_sys:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        ele = collaborators_page.read_yaml_element("partner_win_title")
        assert collaborators_page._text_content(ele) == '(权限互斥时，赋予该成员最高权限)'

    @allure.title("搜索协作者")
    @pytest.mark.parametrize("text", (["杨伦", "yanglun@tezign.com",
                                       "内容基建", "A维度"]))
    def test_search_collaborators(self, login_sys, text):
        """
        测试协作者页面搜索协作者
        @param login_sys:
        @param text:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        collaborators_page.search_collaborators(text)
        ele = collaborators_page.read_yaml_element("dept_dimension")
        assert collaborators_page._text_content(ele) in ("成员", "部门/维度")

    @allure.title("树列表收起和展开")
    def test_dep_tree_arrow(self, login_sys):
        """
        测试树列表收起和展开
        @param login_sys:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        collaborators_page.dep_tree_arrow()
        ele = collaborators_page.read_yaml_element("tree_dept_dime_button")
        assert collaborators_page._is_visible(ele) is False

    @allure.title("添加协作者-部门")
    def test_add_dept(self, login_sys):
        """
        添加协作者-部门
        @param login_sys:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        collaborators_page.add_dept()
        ele = collaborators_page.read_yaml_element("add_dept")
        assert collaborators_page._is_check(ele)

    @allure.title("添加协作者-人员")
    def test_add_staff(self, login_sys):
        """
        添加协作者-人员
        @param login_sys:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        collaborators_page.add_staff()
        ele = collaborators_page.read_yaml_element("tree_first_staff")
        assert collaborators_page._is_check(ele)

    @allure.title("添加协作者-取消添加")
    def test_add_collaborators_cancel(self, login_sys):
        """
        添加协作者-取消添加
        @param login_sys:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        collaborators_page.add_collaborators_cancel()
        assert True

    @allure.title("添加协作者-确认添加")
    def test_add_collaborators_confirm(self, login_sys):
        """
        添加协作者-确认添加
        @param login_sys:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        collaborators_page.add_staff()
        selector = collaborators_page.add_collaborators_confirm()
        assert int(collaborators_page._text_content(selector)[-1]) >= 2

    @allure.title("添加的协作者切换权限至可以分享")
    def test_attach_auth(self, login_sys):
        """
        给添加的协作者切换权限
        @param login_sys:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        collaborators_page.attach_auth()
        collaborators_page.enter_collaborators()
        ele = collaborators_page.read_yaml_element("auth_share_text")
        assert collaborators_page._text_content(ele) == "可以分享"

    @allure.title("移除素材组协作者")
    def test_remove_collaborators(self, login_sys):
        """
        测试移除素材组协作者
        @param login_sys:
        @return:
        """
        collaborators_page = CollaboratorsPage(login_sys)
        collaborators_page.goto_group()
        collaborators_page.group_enter()
        collaborators_page.enter_collaborators()
        collaborators_page.remove_collaborators()
        ele = collaborators_page.read_yaml_element("collaborator_num")
        assert collaborators_page._text_content(ele) == "添加协作者"


if __name__ == '__main__':
    pytest.main(['-vs', 'test_collaborators.py::TestCollaboratorsPage::test_remove_collaborators'])
