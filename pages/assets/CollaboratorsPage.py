#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : CollaboratorsPage
# @Author: yanglun@tezign.com
# @Date  : 2022/3/10
# @Desc  : 素材组成员协作页面
"""

from pages.basepage import BasePage
from conf.confs import url_myCreatedPage
from common.exception_handle import *


class CollaboratorsPage(BasePage):
    """
    素材组协作者页面
    """

    def goto_group(self):
        """
        进入我创建的素材组页面
        @return:
        """
        self._go(url_myCreatedPage)

    def group_enter(self):
        """
        进入我创建的素材组内
        @return:
        """
        # 进入素材组
        selector = self.read_yaml_element("my_enter_collection")
        self._click(selector)

    @element_not_found_exception
    def enter_collaborators(self):
        """
        进入协作者页面
        @return:
        """
        # 进入协作者页面
        selector = self.read_yaml_element("add_partner")
        self._click(selector)

    @element_not_found_exception
    def search_collaborators(self, text):
        """
        搜索协作者
        @return:
        """
        # 聚焦搜索输入框
        selector = self.read_yaml_element("search_collaborators")
        self._click(selector)
        selector = self.read_yaml_element("search_collaborators")
        self._fill(selector, text)
        self._wait(0.5)

    @element_not_found_exception
    def dep_tree_arrow(self):
        """
        部门/外部联系人树列表下拉列表展开button
        @return:
        """
        selector = self.read_yaml_element("tree_dept_arrow")
        # selector1 = self.read_yaml_element("tree_outer_arrow")
        self._click(selector)
        self._wait(0.5)

    def add_dept(self):
        """
        添加协作者-部门
        @return:
        """
        selector = self.read_yaml_element("tree_dept_dime_button")
        for _ in range(10):
            if self._is_visible(selector):
                self._click(selector)
                break
            else:
                self._wait(1)
        selector = self.read_yaml_element("add_dept")
        self._check(selector)

    def add_staff(self):
        """
        添加协作者-人员
        @return:
        """
        selector = self.read_yaml_element("tree_dept_dime_button")
        for _ in range(10):
            if self._is_visible(selector):
                self._click(selector)
                break
            else:
                self._wait(1)
        selector = self.read_yaml_element("tree_dept")
        self._click(selector)
        selector = self.read_yaml_element("tree_first_staff")
        self._check(selector)

    def remove_collaborators(self):
        """
        移除协作者
        @return:
        """
        selector = self.read_yaml_element("authority_dropdown")
        self._click(selector)
        selector = self.read_yaml_element("remove_button")
        self._click(selector)
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        self._wait(0.5)

    def add_collaborators_cancel(self):
        """
        取消添加协作者
        @return:
        """
        selector = self.read_yaml_element("cancel_button")
        self._click(selector)

    def add_collaborators_confirm(self):
        """
        确认添加协作者
        @return:
        """
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        self._wait(1)
        selector = self.read_yaml_element("collaborator_num")
        return selector

    def attach_auth(self):
        """
        赋予分享权限
        @return:
        """
        selector = self.read_yaml_element("authority_dropdown")
        self._click(selector)
        selector = self.read_yaml_element("auth_share")
        self._click(selector)
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)































