#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : CollectionTreeListPage
# @Author: yanglun@tezign.com
# @Date  : 2022/4/18
# @Desc  :  
"""

from pages.basepage import BasePage
from conf.confs import url_assetGroupPage
from common.exception_handle import *


class CollectionTreeListPage(BasePage):
    """
    素材组-左侧树列表
    """

    def goto_group(self):
        self._go(url_assetGroupPage)

    def tree_new_group_error(self):
        """
        新建素材组-空判断：直接点击确认按钮
        @param:
        @return:
        """
        selector = self.read_yaml_element("tree_new_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_new_group_confirm")
        self._click(selector)

    def tree_new_group_cancel(self):
        """
        新建素材组-取消新建
        @param:
        @return:
        """
        selector = self.read_yaml_element("tree_new_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_new_group_cancel")
        self._click(selector)

    def tree_new_group(self, text):
        """
        新建素材组-封面图
        @param text:
        @return:
        """
        selector = self.read_yaml_element("tree_new_group")
        self._click(selector)
        # 输入素材组名称及描述
        selector = self.read_yaml_element("tree_name_input")
        self._fill(selector, text)
        selector = self.read_yaml_element("tree_description_input")
        self._fill(selector, text)
        # # 上传封面图
        # selector = self.read_yaml_element("tree_upload_button")
        # self._click(selector)
        # selector = self.read_yaml_element("tree_upload_input")
        # self._set_input_files(selector, path)
        # self._wait(1)
        # 点击确认按钮
        selector = self.read_yaml_element("tree_new_group_confirm")
        self._click(selector)

    def tree_enter_group(self):
        """
        进入素材组
        @return:
        """
        selector = self.read_yaml_element("tree_enter_group")
        self._click(selector)

    def tree_expand_fold(self):
        """
        素材组树结构的展开与收起
        @return:
        """
        selector = self.read_yaml_element("tree_expand_fold")
        self._click(selector)
        self._wait(0.3)
        self._click(selector)

    def tree_bread_crumbs(self):
        """
        素材组树结构-面包屑切换
        @return:
        """
        selector = self.read_yaml_element("tree_enter_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_enter_sub_group")
        self._click(selector)
        # 第二层面包屑
        selector = self.read_yaml_element("tree_second_bread_crumb")
        self._click(selector)
        selector = self.read_yaml_element("tree_all_bread_crumb")
        self._click(selector)

    def tree_open_new_tab(self):
        """
        素材组树结构-新标签页打开
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_new_tab")
        self._click(selector)

    def tree_new_sub_group(self, text):
        """
        素材组树结构-新建子素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_new_sub_group")
        self._click(selector)
        # 输入素材组名称及描述
        selector = self.read_yaml_element("tree_name_input")
        self._fill(selector, text)
        selector = self.read_yaml_element("tree_description_input")
        self._fill(selector, text)
        # 点击确认按钮
        selector = self.read_yaml_element("tree_new_group_confirm")
        self._click(selector)

    def tree_edit_group(self, text):
        """
        素材组树结构-编辑素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_edit_group")
        self._click(selector)
        # 输入素材组名称及描述
        selector = self.read_yaml_element("tree_name_input")
        self._fill(selector, text)
        selector = self.read_yaml_element("tree_description_input")
        self._fill(selector, text)
        # 点击确认按钮
        selector = self.read_yaml_element("tree_new_group_confirm")
        self._click(selector)
        self._wait(2)

    def tree_subscribe_group(self):
        """
        素材组树结构-订阅素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_subscribe_group")
        self._click(selector)

    def tree_cancel_subscribe_group(self):
        """
        素材组树结构-取消订阅素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_subscribe_group")
        self._click(selector)

    def tree_collect_group(self):
        """
        素材组树结构-收藏素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_collect_group")
        self._click(selector)

    def tree_cancel_collect_group(self):
        """
        素材组树结构-取消收藏素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_collect_group")
        self._click(selector)

    def tree_share_blank_group(self):
        """
        素材组树结构-分享素材组-空素材组分享
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_share_group")
        self._click(selector)

    def tree_share_group(self):
        """
        素材组树结构-分享非空素材组
        @return:
        """
        selector = self.read_yaml_element("tree_enter_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_enter_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown_first")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_first_group_share")
        self._click(selector)
        selector = self.read_yaml_element("tree_create_share_link")
        self._click(selector)

    def tree_download_blank_group(self):
        """
        素材组树结构-下载空素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_download_button")
        self._hover(selector)
        selector = self.read_yaml_element("tree_download_asset")
        self._click(selector)

    def tree_download_group(self):
        """
        素材组树结构-下载非空素材组
        @return:
        """
        selector = self.read_yaml_element("tree_enter_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_enter_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown_first")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_download_button")
        self._hover(selector)
        selector = self.read_yaml_element("tree_download_asset")
        self._click(selector)

    def tree_copy_group(self):
        """
        素材组树结构-复制素材组至自身
        @return:
        """
        selector = self.read_yaml_element("tree_enter_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_enter_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_download_button")
        self._hover(selector)
        selector = self.read_yaml_element("tree_download_asset")
        self._click(selector)

    def tree_cancel_delete_group(self):
        """
        素材组树结构-取消删除素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_delete_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_delete_cancel")
        self._click(selector)

    def tree_delete_group(self):
        """
        素材组树结构-确认删除素材组
        @return:
        """
        selector = self.read_yaml_element("tree_last_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_last_group")
        self._hover(selector)
        selector = self.read_yaml_element("tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("tree_delete_group")
        self._click(selector)
        selector = self.read_yaml_element("tree_delete_confirm")
        self._click(selector)
























