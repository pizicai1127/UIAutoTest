#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : AssetGroupPage
# @Author: yanglun@tezign.com
# @Date  : 2022/2/9
# @Desc  :  
"""

from pages.basepage import BasePage
from conf.confs import url_assetGroupPage
from common.exception_handle import *
import random


class AssetGroupPage(BasePage):
    """
    素材组页面
    """

    def goto_group(self):
        self._go(url_assetGroupPage)

    @element_not_found_exception
    def group_new(self, text):
        """
        新建素材组-带封面图
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

    def group_new_cancel(self):
        """
        取消新建素材组
        @param : 素材组名称及描述
        @return:
        """
        # 点击新建素材组按钮
        selector = self.read_yaml_element("all_new_collection")
        self._click(selector)
        # 点击取消按钮
        selector = self.read_yaml_element("cancel_button")
        self._click(selector)

    def group_enter(self):
        """
        进入素材组
        @return:
        """
        # 进入素材组
        selector = self.read_yaml_element("enter_collection")
        self._click(selector)

    def group_enter_list(self):
        """
        列表视图下进入素材组
        @return:
        """
        selector = self.read_yaml_element("enter_group_list")
        self._click(selector)

    def group_sub_enter(self):
        """
        平铺视图下进入子素材组
        @return:
        """
        # 进入一级素材组
        selector = self.read_yaml_element("enter_collection")
        self._click(selector)
        # 进入二级素材组
        selector = self.read_yaml_element("enter_second_collection")
        self._click(selector)

    def group_subscribe(self):
        """
        订阅素材组
        @return:
        """
        selector = self.read_yaml_element("subscribe")
        self._click(selector)

    def group_subscribe_cancel(self):
        """
        取消订阅素材组
        @return:
        """
        selector = self.read_yaml_element("subscribe")
        self._click(selector)

    def group_collect(self):
        """
        收藏素材组
        @return:
        """
        # 收藏素材组
        selector = self.read_yaml_element("collect")
        self._click(selector)

    def group_collect_cancel(self):
        """
        取消收藏素材组
        @return:
        """
        selector = self.read_yaml_element("collect")
        self._click(selector)

    def group_edit(self, text):
        """
        编辑素材组信息
        @param text:
        @return:
        """
        # 编辑素材组信息
        # hover ...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击编辑按钮
        selector = self.read_yaml_element("edit_collection")
        self._click(selector)
        # 输入素材组名称
        selector = self.read_yaml_element("name_input")
        self._fill(selector, text)
        # 输入素材组描述信息
        selector = self.read_yaml_element("description_input")
        self._fill(selector, text)
        # 点击确认按钮
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        self._wait(0.5)

    @element_not_found_exception
    def group_upload_file(self, path):
        """
        上传文件
        @param path: 文件路径
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("add")
        self._hover(selector)
        # 上传文件
        selector = self.read_yaml_element("upload_files")
        self._click(selector)
        selector = self.read_yaml_element("upload_files_input")
        self._set_input_files(selector, path)
        ele = self.read_yaml_element("upload_repeat_title")
        if self._is_visible(ele) is False:
            self._wait(3)
            # 点击立即入库按钮
            selector = self.read_yaml_element("ingest_now")
            self._click(selector)
            # 选择权限-仅个人可见
            selector = self.read_yaml_element("auth_selected")
            self._click(selector)
            self._wait(0.2)
            selector = self.read_yaml_element("personal_asset")
            self._click(selector)
            self._wait(0.2)
            # 点击入库所选按钮
            selector = self.read_yaml_element("ingest_checked")
            self._click(selector)
        else:
            selector = self.read_yaml_element("Follow-up_checkbox")
            self._check(selector)
            selector = self.read_yaml_element("replace_original_file")
            self._click(selector)
            self._wait(3)
            # 点击立即入库按钮
            selector = self.read_yaml_element("ingest_now")
            self._click(selector)
            # 选择权限-仅个人可见
            selector = self.read_yaml_element("auth_selected")
            self._click(selector)
            self._wait(0.2)
            selector = self.read_yaml_element("personal_asset")
            self._click(selector)
            self._wait(0.2)
            # 点击入库所选按钮
            selector = self.read_yaml_element("ingest_checked")
            self._click(selector)

    @element_not_found_exception
    def sub_group_upload_file(self, path):
        """
        上传文件
        @param path: 文件路径
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("sub_add")
        self._hover(selector)
        # 上传文件
        selector = self.read_yaml_element("upload_files")
        self._click(selector)
        selector = self.read_yaml_element("upload_files_input")
        self._set_input_files(selector, path)
        ele = self.read_yaml_element("upload_repeat_title")
        if self._is_visible(ele) is False:
            self._wait(3)
            # 点击立即入库按钮
            selector = self.read_yaml_element("ingest_now")
            self._click(selector)
            # 选择权限-仅个人可见
            selector = self.read_yaml_element("auth_selected")
            self._click(selector)
            self._wait(0.2)
            selector = self.read_yaml_element("personal_asset")
            self._click(selector)
            self._wait(0.2)
            # 点击入库所选按钮
            selector = self.read_yaml_element("ingest_checked")
            self._click(selector)
        else:
            selector = self.read_yaml_element("Follow-up_checkbox")
            self._check(selector)
            selector = self.read_yaml_element("replace_original_file")
            self._click(selector)
            self._wait(3)
            # 点击立即入库按钮
            selector = self.read_yaml_element("ingest_now")
            self._click(selector)
            # 选择权限-仅个人可见
            selector = self.read_yaml_element("auth_selected")
            self._click(selector)
            self._wait(0.2)
            selector = self.read_yaml_element("personal_asset")
            self._click(selector)
            self._wait(0.2)
            # 点击入库所选按钮
            selector = self.read_yaml_element("ingest_checked")
            self._click(selector)

    @element_not_found_exception
    def group_upload_file_repeat(self, path):
        """
        上传文件-如果待入库存在重名素材-替换原文件
        @param path: 文件路径
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("add")
        self._hover(selector)
        # 上传文件
        selector1 = self.read_yaml_element("upload_files")
        selector4 = self.read_yaml_element("upload_files_input")
        self._click(selector1)
        self._set_input_files(selector4, path)
        self._wait(3)
        # 点击立即入库按钮
        selector2 = self.read_yaml_element("ingest_now")
        self._click(selector2)
        self._wait(0.5)
        # 选择权限-仅个人可见
        selector5 = self.read_yaml_element("auth_selected")
        self._click(selector5)
        self._wait(0.3)
        selector6 = self.read_yaml_element("personal_asset")
        self._click(selector6)
        self._wait(0.3)
        # 点击入库所选按钮
        selector3 = self.read_yaml_element("ingest_checked")
        self._click(selector3)

    @element_not_found_exception
    def group_upload_folder(self, path):
        """
        上传文件夹
        @param path: 文件夹路径
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("add")
        self._hover(selector)
        # 上传文件夹
        selector = self.read_yaml_element("upload_folders")
        self._click(selector)
        selector = self.read_yaml_element("upload_folders_input")
        self._upload_file_chooser(selector, path)
        self._wait(3.5)
        # 点击立即入库按钮
        selector = self.read_yaml_element("ingest_now")
        self._click(selector)
        # 点击入库所选按钮
        self._wait(1)
        selector = self.read_yaml_element("ingest_checked")
        self._click(selector)

    def group_baidu_transfer(self, url, password):
        """
        百度云同步
        @param url:
        @param password:
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("add")
        self._hover(selector)
        selector = self.read_yaml_element("baidu_transfer")
        self._click(selector)
        selector = self.read_yaml_element("baidu_transfer_link")
        self._fill(selector, url)
        selector = self.read_yaml_element("baidu_transfer_password")
        self._fill(selector, password)
        selector = self.read_yaml_element("baidu_transfer_import_confirm")
        self._click(selector)

    def group_muse_transfer(self, url, password):
        """
        Muse同步
        @param url:
        @param password:
        @return:
        """
        pass

    @element_not_found_exception
    def add_from_asset_bank(self):
        """
        从素材库中添加素材
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("add")
        self._hover(selector)
        # 从素材库添加素材
        selector = self.read_yaml_element("add_from_assets")
        self._click(selector)
        self._wait(1)
        # 选择第一个素材
        selector = self.read_yaml_element("add_asset")
        self._click(selector)
        # 点击确定按钮
        selector = self.read_yaml_element("add_confirm")
        self._click(selector)

    def group_share(self):
        """
        分享素材组
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击分享按钮
        selector = self.read_yaml_element("share_collection")
        self._click(selector)
        # 点击创建链接按钮
        selector = self.read_yaml_element("create_link")
        self._click(selector)

    def group_share_button(self):
        """
        分享素材组-右上角分享button
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("share_button")
        self._click(selector)
        # 点击创建链接按钮
        selector = self.read_yaml_element("create_link")
        self._click(selector)

    def group_share_cancel(self):
        """
        取消分享素材组
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("share_button")
        self._click(selector)
        # 点击取消按钮
        selector = self.read_yaml_element("close_share_win")
        self._click(selector)

    def group_download(self):
        """
        下载素材组
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # hover下载button
        selector = self.read_yaml_element("download")
        self._hover(selector)
        # 点击下载素材按钮
        selector = self.read_yaml_element("download_asset")
        self._click(selector)

    def group_download_all(self):
        """
        下载素材组及附件
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # hover下载button
        selector = self.read_yaml_element("download")
        self._hover(selector)
        # 点击下载素材及附件按钮
        selector = self.read_yaml_element("download_all")
        self._click(selector)

    def group_copy_to_search(self):
        """
        复制素材组至搜索目录下
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击复制素材组按钮
        selector = self.read_yaml_element("copy_collection")
        self._click(selector)
        # 搜索目标组
        selector = self.read_yaml_element("copy_search")
        # 聚焦搜索框
        self._click(selector)
        # 输入搜索内容
        self._fill(selector, "真的不要删除和编辑呀")
        selector = self.read_yaml_element("copy_search_result")
        # 点击搜索结果
        self._click(selector)
        selector = self.read_yaml_element("copy_confirm")
        # 点击确认
        self._click(selector)

    def group_copy_to_all(self):
        """
        复制素材组至全部下
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击复制素材组按钮
        selector = self.read_yaml_element("copy_collection")
        self._click(selector)
        selector = self.read_yaml_element("copy_confirm")
        self._click(selector)

    def group_copy_to_new(self, text):
        """
        复制素材组至新增素材组下
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击复制素材组按钮
        selector = self.read_yaml_element("copy_collection")
        self._click(selector)
        # 新建素材组
        selector = self.read_yaml_element("copy_new")
        self._click(selector)
        # 输入素材组名称
        selector = self.read_yaml_element("copy_input")
        self._fill(selector, text)
        # 确认新建素材组
        selector = self.read_yaml_element("copy_new_confirm")
        self._click(selector)
        self._wait(0.5)
        selector = self.read_yaml_element("copy_confirm")
        self._click(selector)

    def group_copy_cancel(self):
        """
        取消复制素材组
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击复制素材组按钮
        selector = self.read_yaml_element("copy_collection")
        self._click(selector)
        selector = self.read_yaml_element("copy_cancel")
        self._click(selector)

    def group_move_search(self):
        """
        移动素材组
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击移动素材组按钮
        selector = self.read_yaml_element("move_collection")
        self._click(selector)
        # 搜索目标组
        selector = self.read_yaml_element("copy_search")
        # 聚焦搜索框
        self._click(selector)
        # 输入搜索内容
        self._fill(selector, "真的不要删除和编辑呀")
        selector = self.read_yaml_element("copy_search_result")
        # 点击搜索结果
        self._click(selector)
        selector = self.read_yaml_element("copy_confirm")
        # 点击确认
        self._click(selector)

    def group_move_to_all(self):
        """
        移动素材组到全部下
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击移动素材组按钮
        selector = self.read_yaml_element("move_collection")
        self._click(selector)
        # 点击确认
        selector = self.read_yaml_element("move_confirm")
        self._click(selector)
        # 二次确认取消/确认
        selector = self.read_yaml_element("move_popup_cancel")
        self._click(selector)
        selector = self.read_yaml_element("move_confirm")
        self._click(selector)
        selector = self.read_yaml_element("move_popup_confirm")
        self._click(selector)

    def group_move_cancel(self):
        """
        移动素材组-取消移动
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击移动素材组按钮
        selector = self.read_yaml_element("move_collection")
        self._click(selector)
        # 点击取消
        selector = self.read_yaml_element("move_cancel")
        self._click(selector)

    def sharing_records(self):
        """
        查看分享记录
        @return:
        """
        # hover...
        selector = self.read_yaml_element("more")
        self._hover(selector)
        # 点击分享记录按钮
        selector = self.read_yaml_element("share_records")
        self._click(selector)
        # 关闭分享记录弹窗
        # selector3 = self.read_yaml_element("share_records_close")
        # self._click(selector3)

    def sub_group_new(self, text):
        """
        新建子素材组
        @param text:
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("add")
        self._hover(selector)
        # 新建子素材组
        selector = self.read_yaml_element("add_sub_collection")
        self._click(selector)
        # 输入素材组名称及描述
        selector = self.read_yaml_element("name_input")
        self._fill(selector, text)
        selector = self.read_yaml_element("description_input")
        self._fill(selector, text)
        # 点击确认按钮
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)
        self._wait(0.5)

    def group_delete_cancel(self):
        """
        取消删除素材组
        @return:
        """
        selector = self.read_yaml_element("more")
        # hover...
        self._hover(selector)
        selector = self.read_yaml_element("delete_collection")
        self._click(selector)
        selector = self.read_yaml_element("cancel_delete_collection")
        self._click(selector)

    def group_delete(self):
        """
        删除素材组
        @return:
        """
        selector = self.read_yaml_element("more")
        # hover...
        self._hover(selector)
        selector = self.read_yaml_element("delete_collection")
        self._click(selector)
        selector = self.read_yaml_element("confirm_delete_collection")
        self._click(selector)

    def group_filter(self):
        """
        素材组筛选：筛选后结果只有素材，不包含素材组
        @return:
        """
        pass

    def group_sort(self, selector):
        """
        素材组下排序
        @return:
        """
        hover_selector = self.read_yaml_element("sort")
        #hover排序组件
        self._hover(hover_selector)
        self._click(selector)

    def group_group_asc(self):
        """
        素材组排序升序
        @return:
        """
        selector = self.read_yaml_element("sort_asc_desc")
        # self._hover(selector)
        # self._wait(0.5)
        self._click(selector)

    def group_sort_desc(self):
        """
        素材组排序降序
        @return:
        """
        selector = self.read_yaml_element("sort_asc_desc")
        # self._hover(selector)
        # self._wait(0.5)
        self._click(selector)

    def get_asc_desc_text(self):
        """
        获取升降序text
        @return:
        """
        selector = self.read_yaml_element('sort_asc_desc')
        self._hover(selector)
        selector = self.read_yaml_element("asc_desc_text")
        text = self._text_content(selector)
        return text

    def group_list_view(self):
        """
        素材组下素材组列表视图
        @return:
        """
        selector = self.read_yaml_element("group_list_view")
        self._click(selector)

    def group_list_to_group_tab(self):
        """
        列表视图下-切换至素材组
        @return:
        """
        selector = self.read_yaml_element("group_list_view_group")
        self._click(selector)

    def group_list_to_asset_tab(self):
        """
        列表视图下-切换至素材
        @return:
        """
        selector = self.read_yaml_element("group_list_view_asset")
        self._click(selector)

    def group_tile_view(self):
        """
        素材组下素材组平铺视图
        @return:
        """
        selector = self.read_yaml_element("group_grid_view")
        self._click(selector)

    def group_kanban_view(self):
        """
        素材组下素材组多维视图
        @return:
        """
        selector = self.read_yaml_element("group_kanban_view")
        self._click(selector)

    def group_new_sub_middle(self, text):
        """
        空白页面中间新建子素材组
        @param text:
        @return:
        """
        selector = self.read_yaml_element("middle_new_sub_collection")
        self._click(selector)
        self._wait(0.5)
        selector = self.read_yaml_element("name_input")
        self._fill(selector, text)
        selector = self.read_yaml_element("description_input")
        self._fill(selector, text)
        # 点击确认按钮
        selector = self.read_yaml_element("confirm_button")
        self._click(selector)

    def group_new_sub_middle_cancel(self):
        """
        空白页面中间新建子素材组
        @param :
        @return:
        """
        self._click(1)
        selector = self.read_yaml_element("middle_new_sub_collection")
        self._click(selector)
        # 点击取消按钮
        selector = self.read_yaml_element("new_sub_collection_cancel")
        self._click(selector)

    @element_not_found_exception
    def group_search_text(self, text):
        """
        全部素材组下搜索：直接输入内容搜索
        @param text:
        """
        # 聚焦搜索输入框
        selector = self.read_yaml_element("search_in_group")
        self._click(selector)
        # 模拟键盘输入搜索内容
        self._keyboard_input(text)
        # 模拟键盘回车搜索
        self._keyboard_click("Enter")

    @element_not_found_exception
    def group_search_backspace(self, text):
        """
        素材组搜索：删除搜索内容后继续搜索，测试backspace
        @param text: 输入的搜索内容请大于2个字符
        @return:
        """
        # 聚焦搜索输入框
        selector = self.read_yaml_element("search_in_group")
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

    @element_not_found_exception
    def group_search_clear(self, text):
        """
        素材组搜索：清除搜索框
        @param text:
        @return:
        """
        # 聚焦搜索输入框
        selector = self.read_yaml_element("search_in_group")
        self._click(selector)
        # 模拟键盘输入搜索内容
        self._keyboard_input(text)
        # 模拟键盘回车搜索
        self._keyboard_click("Enter")
        # 清空搜索框
        selector = self.read_yaml_element("search_text_clear")
        self._click(selector)


    def group_filter_my_created(self):
        """
        素材组筛选：创建者/部门-我创建的
        @return:
        """
        selector = self.read_yaml_element("filter_mycreated_dropdown")
        # 点击创建者/创建部门 dropdown
        self._click(selector)
        selector = self.read_yaml_element("filter_mycreated_checkbox")
        # 勾选我创建的素材checkbox
        self._check(selector)

    def group_filter_dept(self, text):
        """
        素材组筛选：创建者/部门
        @param text:
        @return:
        """
        selector = self.read_yaml_element("filter_mycreated_dropdown")
        # 点击创建者/创建部门 dropdown
        self._click(selector)
        selector = self.read_yaml_element("filter_mycreated_search")
        self._click(selector)
        selector = self.read_yaml_element("filter_search_text")
        self._fill(selector, text)
        selector = self.read_yaml_element("mycreated_search_result")
        self._click(selector)

    def group_filter_file_format(self):
        """
        素材组筛选：图片-JPG
        @return:
        """
        selector = self.read_yaml_element("filter_file_format")
        self._click(selector)
        selector = self.read_yaml_element("filter_pic")
        self._click(selector)
        selector = self.read_yaml_element("filter_JPG")
        self._check(selector)

    @element_not_found_exception
    def group_filter_create_time(self):
        """
        素材组筛选：创建日期
        @return:
        """
        selector = self.read_yaml_element("filter_create_time")
        self._click(selector)
        selector = self.read_yaml_element("filter_recent_radio")
        self._click(selector)
        # selector = self.read_yaml_element("filter_datetime")
        # self._click(selector)
        # self._wait(0.5)
        # selector = self.read_yaml_element("filter_start_day")
        # self._click(selector)
        # self._wait(0.5)
        # selector = self.read_yaml_element("filter_next_year")
        # self._click(selector)
        # selector = self.read_yaml_element("filter_end_day")
        # self._click(selector)
        # self._wait(1)
        # selector = self.read_yaml_element("filter_create_time")
        # self._hover(selector)
        # selector = self.read_yaml_element("filter_clear")
        # self._click(selector)

    @element_not_found_exception
    def group_filter_clear(self):
        """
        素材组筛选：清空筛选
        @return:
        """
        selector = self.read_yaml_element("filter_mycreated_dropdown")
        # 点击创建者/创建部门 dropdown
        self._click(selector)
        selector = self.read_yaml_element("filter_mycreated_checkbox")
        # 勾选我创建的素材checkbox
        self._check(selector)
        # 失焦
        self._mouse_move(10, 10)
        # 清空筛选
        selector = self.read_yaml_element("filter_clear")
        self._click(selector)

    @element_not_found_exception
    def group_filter_list(self):
        """
        素材组筛选列表-收起展开
        @return:
        """
        selector = self.read_yaml_element("filter_fold")
        if self._is_visible(selector):
            self._click(selector)
            selector = self.read_yaml_element("filter_unfold")
            self._click(selector)
            return None
        else:
            return True

    def group_batch_download(self):
        """
        素材组批量操作-打包下载
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_button")
        self._click(selector)

    def group_batch_download_all(self):
        """
        素材组批量操作-打包下载附件
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_all_button")
        self._click(selector)

    def group_batch_download_specify_size(self, size):
        """
        素材组批量操作-打包下载指定尺寸大小
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_specify_size")
        self._click(selector)
        selector = self.read_yaml_element("download_specify_size_input")
        self._click(selector)
        self._fill(selector, size)
        selector = self.read_yaml_element("zoom_switch_button")
        self._click(selector)
        selector = self.read_yaml_element("zoom_base_length")
        self._click(selector)
        self._fill(selector, size)
        selector = self.read_yaml_element("download_specify_button")
        self._click(selector)

    def group_batch_share(self):
        """
        素材组批量操作-分享
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_share_button")
        self._click(selector)
        selector = self.read_yaml_element("batch_create_link")
        self._click(selector)

    def group_batch_edit(self):
        """
        素材组批量操作-编辑
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_edit")
        self._click(selector)
        selector = self.read_yaml_element("edit_description_input")
        self._click(selector)
        self._fill(selector, "UI自动化测试")
        selector = self.read_yaml_element("none_radio")
        self._check(selector)
        selector = self.read_yaml_element("edit_auth")
        self._click(selector)
        selector = self.read_yaml_element("edit_auth_cancel_button")
        self._click(selector)
        selector = self.read_yaml_element("edit_save")
        self._click(selector)
        selector = self.read_yaml_element("second_popup_sure")
        self._click(selector)

    def group_batch_rename(self):
        """
        素材组批量操作-高级重命名
        @return:
        """
        random_name = str(random.randint(1, 999)) + '-'
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_rename")
        self._click(selector)
        selector = self.read_yaml_element("batch_rename_name_input")
        self._click(selector)
        self._fill(selector, random_name)
        selector = self.read_yaml_element("batch_rename_brand_tag")
        self._click(selector)
        selector = self.read_yaml_element("batch_rename_asc")
        self._click(selector)
        selector = self.read_yaml_element("batch_rename_confirm")
        self._click(selector)

    def group_batch_add_basket(self):
        """
        素材组批量操作-加入素材篮
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_add_to_basket")
        self._click(selector)

    def group_batch_add_basket_again(self):
        """
        素材组批量操作-重复加入素材篮
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_add_to_basket")
        self._click(selector)

    def group_batch_copy(self):
        """
        素材组批量操作-复制
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_add_to_group")
        self._click(selector)
        selector = self.read_yaml_element("only_my_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("add_first_group")
        self._click(selector)
        selector = self.read_yaml_element("add_confirm_button")
        self._click(selector)

    def group_batch_move(self):
        """
        素材组批量操作-移动到指定素材组
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_move_button")
        self._click(selector)
        selector = self.read_yaml_element("only_my_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("move_to_specify_group")
        self._click(selector)
        selector = self.read_yaml_element("add_confirm_button")
        self._click(selector)

    def group_batch_empowerment(self):
        """
        素材组批量操作-赋权给组内成员
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_more")
        self._hover(selector)
        selector = self.read_yaml_element("batch_empowerment")
        self._click(selector)
        selector = self.read_yaml_element("empowerment_dropdown")
        self._click(selector)
        selector = self.read_yaml_element("empowerment_download")
        self._click(selector)
        selector = self.read_yaml_element("empowerment_confirm")
        self._click(selector)

    def group_batch_permission(self):
        """
        素材组批量操作-修改组内素材权限类型
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_more")
        self._hover(selector)
        selector = self.read_yaml_element("batch_permission_type")
        self._click(selector)
        selector = self.read_yaml_element("permission_type_dropdown")
        self._click(selector)
        selector = self.read_yaml_element("self_permission_type")
        self._click(selector)
        selector = self.read_yaml_element("empowerment_confirm")
        self._click(selector)

    def group_batch_close(self):
        """
        素材组批量操作-关闭批量操作组件
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_close")
        self._click(selector)

    def group_change_owner(self, text):
        """
        素材组批量操作-修改所有者
        @param text:
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_more")
        self._hover(selector)
        selector = self.read_yaml_element("batch_change_owner")
        self._click(selector)
        selector = self.read_yaml_element("change_owner_search")
        self._click(selector)
        selector = self.read_yaml_element("change_owner_input")
        self._fill(selector, text)
        self._wait(0.2)
        selector = self.read_yaml_element("search_result")
        self._click(selector)
        selector = self.read_yaml_element("change_owner_confirm")
        self._click(selector)

    def group_remove_asset(self):
        """
        素材组批量操作-移除/删除素材
        @return:
        """
        selector = self.read_yaml_element("all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("batch_remove_asset")
        self._click(selector)
        selector = self.read_yaml_element("batch_delete_asset")
        self._check(selector)
        selector = self.read_yaml_element("batch_delete_confirm")
        self._click(selector)

    def group_share_by_qr_code(self):
        """
        素材组分享-扫码分享
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("share_button")
        self._click(selector)
        # 点击扫描二维码按钮
        selector = self.read_yaml_element("share_QR_code")
        self._click(selector)

    def group_share_by_email(self):
        """
        素材组分享-邮件分享
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("share_button")
        self._click(selector)
        # 点击邮件按钮
        selector = self.read_yaml_element("share_by_email")
        self._click(selector)

    def group_share_set(self):
        """
        素材组分享-分享设置
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("share_button")
        self._click(selector)
        # 点击分享设置按钮
        selector = self.read_yaml_element("share_set_button")
        self._click(selector)
        # 点击水印展开设置按钮
        selector = self.read_yaml_element("share_watermark_set")
        self._click(selector)
        # 开启水印开关
        selector = self.read_yaml_element("share_watermark_open")
        self._click(selector)
        # 开启附件开关
        selector = self.read_yaml_element("share_attach_file_open")
        self._click(selector)
        # 开启密码开关
        selector = self.read_yaml_element("share_password_open")
        self._click(selector)
        # 开启分享备注开关
        selector = self.read_yaml_element("share_remark_open")
        self._click(selector)
        # 输入分享备注信息
        selector = self.read_yaml_element("share_remark_textarea")
        self._click(selector)
        selector = self.read_yaml_element("share_remark_textarea")
        self._fill(selector, "这是UI自动化测试分享测试备注")
        # 点击创建链接按钮
        selector = self.read_yaml_element("share_create_link_set")
        self._click(selector)





































