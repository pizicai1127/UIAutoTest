#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : AllCollectionPage
# @Author: yanglun@tezign.com
# @Date  : 2022/2/25
# @Desc  :  
"""

from pages.basepage import BasePage
from conf.confs import url_assetGroupPage
from common.exception_handle import *


class AllCollectionPage(BasePage):
    """
    全部素材组页面
    """

    def goto_group(self):
        self._go(url_assetGroupPage)

    def group_list_view(self):
        """
        全部下素材组列表视图
        @return:
        """
        selector = self.read_yaml_element("view_list")
        self._click(selector)
        selector = self.read_yaml_element("group_list_title")
        return selector

    def group_enter_list(self):
        """
        列表视图下进入素材组
        @return:
        """
        selector = self.read_yaml_element("enter_group_list")
        self._click(selector)
        selector = self.read_yaml_element("collection_all_level")
        return selector

    def group_tile_view(self):
        """
        全部下素材组平铺视图
        @return:
        """
        selector = self.read_yaml_element("view_tile")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("all_enter_collection")
        return selector

    def group_enter(self):
        """
        进入素材组
        @return:
        """
        # 进入素材组
        selector = self.read_yaml_element("all_enter_collection")
        self._click(selector)

    def group_sort(self, selector):
        """
        全部下素材组排序
        @return:
        """
        hover_selector = self.read_yaml_element("sort")
        # hover排序组件
        self._hover(hover_selector)
        self._click(selector)

    def group_group_asc(self):
        """
        全部下素材组排序升序
        @return:
        """
        selector = self.read_yaml_element("sort_asc_desc")
        self._click(selector)

    def group_sort_desc(self):
        """
        全部下素材组排序降序
        @return:
        """
        selector = self.read_yaml_element("sort_asc_desc")
        # selector1 = self.read_yaml_element("sort")
        # self._hover(selector1)
        # self._wait(1)
        self._click(selector)

    @element_not_found_exception
    def group_new(self, text):
        """
        新建素材组
        @param text: 素材组名称及描述
        @return:
        """
        # 点击新建素材组按钮
        selector = self.read_yaml_element("all_new_collection")
        self._click(selector)
        # 输入素材组名称及描述
        selector = self.read_yaml_element("name_input")
        self._fill(selector, text)
        selector = self.read_yaml_element("description_input")
        self._fill(selector, text)
        # 点击确认按钮
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        selector = self.read_yaml_element("collection_all_level")
        return selector

    def group_new_cancel(self):
        """
        取消新建素材组
        @return:
        """
        # 点击新建素材组按钮
        selector = self.read_yaml_element("all_new_collection")
        self._click(selector)
        # 点击取消按钮
        selector = self.read_yaml_element("cancel_button")
        self._click(selector)
        self._wait(0.5)
        return selector

    def group_delete(self):
        """
        删除素材组
        @return:
        """
        selector = self.read_yaml_element("all_more")
        # hover...
        self._hover(selector)
        selector = self.read_yaml_element("all_delete_collection")
        self._click(selector)
        selector = self.read_yaml_element("all_confirm_delete_collection")
        self._click(selector)

    def group_search_text(self, text):
        """
        全部素材组下搜索：直接输入内容搜索
        @param text:
        @return:
        """
        # 聚焦搜索输入框
        selector = self.read_yaml_element("all_search_in_group")
        self._click(selector)
        # 模拟键盘输入搜索内容
        self._keyboard_input(text)
        # 模拟键盘回车搜索
        self._keyboard_click("Enter")
        selector = self.read_yaml_element("search_all_level")
        return selector

    @element_not_found_exception
    def group_search_backspace(self, text):
        """
        素材组搜索：删除搜索内容后继续搜索，测试backspace
        @param text: 输入的搜索内容请大于2个字符
        @return:
        """
        # 聚焦搜索输入框
        selector = self.read_yaml_element("all_search_in_group")
        self._click(selector)
        # 模拟键盘输入搜索内容
        self._keyboard_input(text)
        # 模拟键盘删除/backspace
        self._down("Shift")
        for i in range(len(text[:2])):
            self._keyboard_click("ArrowLeft")
        self._up("Shift")
        self._keyboard_click("Backspace")
        # 回车继续搜索
        self._keyboard_click("Enter")
        selector = self.read_yaml_element("search_all_level")
        return selector

    @element_not_found_exception
    def group_search_clear(self, text):
        """
        素材组搜索：清除搜索框
        @param text: 输入的搜索内容请大于2个字符
        @return:
        """
        # 聚焦搜索输入框
        selector = self.read_yaml_element("all_search_in_group")
        self._click(selector)
        # 模拟键盘输入搜索内容
        self._keyboard_input(text)
        # 模拟键盘回车搜索
        self._keyboard_click("Enter")
        # 清空搜索框
        selector = self.read_yaml_element("all_search_text_clear")
        self._click(selector)
        selector = self.read_yaml_element("all_search_in_group")
        return selector

    @element_not_found_exception
    def group_collect(self):
        """
        收藏素材组
        @return:
        """
        selector = self.read_yaml_element("all_enter_collection")
        self._hover(selector)
        self._wait(0.2)
        selector = self.read_yaml_element("collect_button")
        self._click(selector)

    def right_mouse_new_group(self):
        """
        右键-新建素材组
        @return:
        """
        selector = self.read_yaml_element("trigger_area")
        self._right_click(selector)
        selector = self.read_yaml_element("right_create_group")
        self._click(selector)
        selector = self.read_yaml_element("name_input")
        self._fill(selector, "右键-新建素材组")
        selector = self.read_yaml_element("description_input")
        self._fill(selector, "右键-新建素材组")
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        selector = self.read_yaml_element("collection_all_level")
        return selector

    def right_mouse(self):
        """
        右键动作
        @return:
        """
        # 右键触发区域
        selector = self.read_yaml_element("all_enter_collection")
        self._right_click(selector)
        self._wait(0.1)

    def right_mouse_new_tab(self):
        """
        右键-新标签页打开
        @return:
        """
        selector = self.read_yaml_element("right_new_tab")
        self._click(selector)

    def right_mouse_edit(self):
        """
        右键-编辑信息
        @return:
        """
        selector = self.read_yaml_element("right_edit")
        self._click(selector)
        # 输入素材组名称及描述
        selector = self.read_yaml_element("name_input")
        self._fill(selector, "右键-编辑素材组")
        selector = self.read_yaml_element("description_input")
        self._fill(selector, "右键-编辑素材组")
        # 点击确认按钮
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("all_enter_collection")
        return self._text_content(selector)

    def right_mouse_subscribe(self):
        """
        右键-订阅素材组
        @return:
        """
        selector = self.read_yaml_element("right_subscribe")
        self._click(selector)

    def right_mouse_collect(self):
        """
        右键-收藏素材组
        @return:
        """
        selector = self.read_yaml_element("right_collect")
        self._click(selector)

    def right_mouse_share(self):
        """
        右键-分享空素材组
        @return:
        """
        selector = self.read_yaml_element("right_share")
        self._click(selector)

    def right_mouse_copy_to_self(self):
        """
        右键-复制素材组至自身
        @return:
        """
        selector = self.read_yaml_element("right_copy")
        self._click(selector)
        selector = self.read_yaml_element("copy_search_text")
        self._click(selector)
        selector = self.read_yaml_element("copy_search_input")
        self._fill(selector, '右键-编辑素材组')
        selector = self.read_yaml_element("copy_target_group")
        self._click(selector)
        selector = self.read_yaml_element("copy_confirm_button")
        self._click(selector)

    def right_mouse_move_to_all(self):
        """
        右键-移动素材组至全部下
        @return:
        """
        selector = self.read_yaml_element("right_move")
        self._click(selector)
        selector = self.read_yaml_element("copy_confirm_button")
        self._click(selector)
        selector = self.read_yaml_element("copy_second_confirm_button")
        self._click(selector)

    def right_mouse_download_blank_group(self):
        """
        右键-下载空素材组
        @return:
        """
        selector = self.read_yaml_element("right_download")
        self._hover(selector)
        selector = self.read_yaml_element("right_download_group")
        self._click(selector)

    def right_mouse_delete(self):
        """
        右键-删除素材组
        @return:
        """
        selector = self.read_yaml_element("right_delete")
        self._click(selector)
        selector = self.read_yaml_element("right_delete_confirm")
        self._click(selector)

    def group_cover_picture(self, file_path):
        """
        素材组封面图
        @param file_path:
        @return:
        """
        selector = self.read_yaml_element("right_edit")
        self._click(selector)
        selector = self.read_yaml_element("group_cover_pic_upload")
        self._upload_file_chooser(selector, file_path)
        self._wait(3.5)
        # 点击确认按钮
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        selector = self.read_yaml_element("group_cover_pic_url")
        return self._get_attribute(selector, 'src')

    def group_cover_picture_clear(self):
        """
        删除素材组封面图
        @return:
        """
        selector = self.read_yaml_element("right_edit")
        self._click(selector)
        selector = self.read_yaml_element("group_cover_pic_clear")
        self._click(selector)
        # 点击确认按钮
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        selector = self.read_yaml_element("group_cover_pic_clear_assert")
        return self._get_attribute(selector, 'src')