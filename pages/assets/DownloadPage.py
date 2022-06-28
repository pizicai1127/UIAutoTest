#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : DownloadPage
# @Author: yanglun@tezign.com
# @Date  : 2022/5/6
# @Desc  :  
"""


from pages.basepage import BasePage
from conf.confs import url_assetGroupPage, url_assetPage
from common.exception_handle import *


class DownloadPage(BasePage):
    """
    下载逻辑页面
    """

    def goto_asset_group(self):
        """
        进入全部素材组下
        @return:
        """
        self._go(url_assetGroupPage)

    def goto_asset(self):
        """
        进入素材库
        @return:
        """
        self._go(url_assetPage)

    def download_enter_group(self):
        """
        进入素材组内
        @return:
        """
        selector = self.read_yaml_element("download_enter_group")
        self._click(selector)

    def download_tree_download_asset(self):
        """
        树结构-父结构下载素材
        @return:
        """
        # 点击树结构-素材组
        selector = self.read_yaml_element("download_tree_enter_group")
        self._click(selector)
        # hover树结构-素材组
        selector = self.read_yaml_element("download_tree_enter_group")
        self._hover(selector)
        selector = self.read_yaml_element("download_tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("download_tree_download_button")
        self._hover(selector)
        selector = self.read_yaml_element("download_tree_download_asset")
        self._click(selector)

    def download_tree_download_all(self):
        """
        树结构-父结构下载素材及附件
        @return:
        """
        # 点击树结构-素材组
        selector = self.read_yaml_element("download_tree_enter_group")
        self._click(selector)
        # hover树结构-素材组
        selector = self.read_yaml_element("download_tree_enter_group")
        self._hover(selector)
        selector = self.read_yaml_element("download_tree_right_dropdown")
        self._click(selector)
        self._wait(0.3)
        self._mouse_move(10, 10)
        selector = self.read_yaml_element("download_tree_download_button")
        self._hover(selector)
        selector = self.read_yaml_element("download_tree_download_all")
        self._click(selector)

    def download_apply_access(self):
        """
        下载申请权限
        @return:
        """
        # 点击申请权限
        selector = self.read_yaml_element("download_apply_access")
        self._click(selector)
        # 输入申请原因
        selector = self.read_yaml_element("download_apply_reason_textarea")
        self._click(selector)
        self._fill(selector, "素材下载-申请权限")
        # 提交申请
        selector = self.read_yaml_element("download_apply_commit")
        self._click(selector)

    def download_asset_cancel(self):
        """
        取消下载素材
        @return:
        """
        # 点击取消button
        selector = self.read_yaml_element("download_cancel")
        self._click(selector)
        self._wait(0.3)

    def download_normal_asset(self):
        """
        直接下载正常素材
        @return:
        """
        # 点击下载button
        selector = self.read_yaml_element("download_button")
        self._click(selector)

    def download_all_asset(self):
        """
        下载所有可下载的素材
        @return:
        """
        # 勾选谨慎下载checkbox
        selector = self.read_yaml_element("download_not_active_checkbox")
        self._check(selector)
        # 点击下载button
        selector = self.read_yaml_element("download_button")
        self._click(selector)

    def download_right_download(self):
        """
        右键-下载素材
        @return:
        """
        # 右键触发区域
        selector = self.read_yaml_element("download_enter_group")
        self._right_click(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("download_tree_download_button")
        self._hover(selector)
        selector = self.read_yaml_element("download_tree_download_asset")
        self._click(selector)

    def download_right_download_all(self):
        """
        右键-下载素材及附件
        @return:
        """
        # 右键触发区域
        selector = self.read_yaml_element("download_enter_group")
        self._right_click(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("download_tree_download_button")
        self._hover(selector)
        selector = self.read_yaml_element("download_tree_download_all")
        self._click(selector)

    def download_more_download(self):
        """
        素材组内more-下载素材
        @return:
        """
        # more
        selector = self.read_yaml_element("download_more")
        self._hover(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("download_more_download")
        self._hover(selector)
        selector = self.read_yaml_element("download_more_download_asset")
        self._click(selector)

    def download_more_download_all(self):
        """
        素材组内more-下载素材及附件
        @return:
        """
        # more
        selector = self.read_yaml_element("download_more")
        self._hover(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("download_more_download")
        self._hover(selector)
        selector = self.read_yaml_element("download_more_download_all")
        self._click(selector)

    def download_batch_download_asset(self):
        """
        素材组-批量操作下载素材
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_batch_button")
        self._click(selector)

    def download_batch_download_all(self):
        """
        素材组-批量操作下载素材及附件
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_batch_all_button")
        self._click(selector)

    def download_batch_specify(self):
        """
        素材组-批量操作下载指定尺寸和大小
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_specify_size")
        self._click(selector)
        selector = self.read_yaml_element("download_not_active_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_button")
        self._click(selector)
        selector = self.read_yaml_element("download_specify_size_input")
        self._click(selector)
        self._fill(selector, '50')
        selector = self.read_yaml_element("download_zoom_switch_button")
        self._click(selector)
        selector = self.read_yaml_element("download_zoom_base_length")
        self._click(selector)
        self._fill(selector, '50')
        selector = self.read_yaml_element("download_specify_button")
        self._click(selector)

    def download_batch_blank_group(self):
        """
        素材组-批量操作下载空素材组
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_blank_group")
        self._hover(selector)
        selector = self.read_yaml_element("download_blank_group_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_batch_button")
        self._click(selector)

    def download_batch_sub_group(self):
        """
        素材组-批量操作下载子素材组
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_sub_group")
        self._hover(selector)
        selector = self.read_yaml_element("download_sub_group_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_batch_button")
        self._click(selector)

    def download_batch_single_asset(self):
        """
        素材组-批量操作下载单个未生效素材
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_single_asset")
        self._hover(selector)
        selector = self.read_yaml_element("download_single_asset_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_batch_button")
        self._click(selector)

    def download_filter_my_create(self):
        """
        筛选-我创建的
        @return:
        """
        selector = self.read_yaml_element("download_mycreated_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_mycreated_checkbox")
        self._check(selector)
        self._mouse_move(10, 10)

    def download_list_batch_asset(self):
        """
        素材列表-批量操作下载
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_list_all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_batch_button")
        self._click(selector)

    def download_list_batch_all(self):
        """
        素材列表-批量操作下载素材及附件
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_list_all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_specify_size")
        self._click(selector)

    def download_list_batch_specify(self):
        """
        素材列表-批量操作下载指定尺寸和大小
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_list_all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_dropdown")
        self._hover(selector)
        selector = self.read_yaml_element("download_batch_all_button")
        self._click(selector)
        selector = self.read_yaml_element("download_not_active_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("download_button")
        self._click(selector)
        selector = self.read_yaml_element("download_specify_size_input")
        self._click(selector)
        self._fill(selector, '50')
        selector = self.read_yaml_element("download_zoom_switch_button")
        self._click(selector)
        selector = self.read_yaml_element("download_zoom_base_length")
        self._click(selector)
        self._fill(selector, '50')
        selector = self.read_yaml_element("download_specify_button")
        self._click(selector)

    def download_list_right_normal(self):
        """
        素材列表-右键下载单个正常素材
        @return:
        """
        selector = self.read_yaml_element("download_list_normal_asset")
        self._hover(selector)
        self._wait(0.1)
        self._right_click(selector)
        selector = self.read_yaml_element("download_card_right")
        self._hover(selector)
        selector = self.read_yaml_element("download_list_right_button")
        self._click(selector)
        return True

    def download_single_url_asset(self):
        """
        素材列表-右键下载单个未生效素材
        @return:
        """
        # 批量操作
        selector = self.read_yaml_element("download_list_not_active_asset")
        self._right_click(selector)
        selector = self.read_yaml_element("download_card_right")
        self._hover(selector)
        selector = self.read_yaml_element("download_list_right_button")
        self._click(selector)
























