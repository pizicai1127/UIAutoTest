#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : ShareLandingPage
# @Author: yanglun@tezign.com
# @Date  : 2022/4/9
# @Desc  :  
"""

from pages.basepage import BasePage
from conf.confs import (url_sharingGroupPage, visitor_can_download_url,
                        visitor_only_view_url, internal_can_download_url,
                        internal_only_view_url
                        )
from common.exception_handle import *


class ShareLandingPage(BasePage):
    """
    分享落地页
    """
    def goto_group(self):
        self._go(url_sharingGroupPage)

    @element_not_found_exception
    def share_visitor_can_download(self):
        """
        分享素材组-游客可下载url
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("land_share_button")
        self._click(selector)
        self._wait(0.7)
        # hover分享权限dropdown
        selector = self.read_yaml_element("land_share_auth")
        self._hover(selector)
        # 永久有效
        selector = self.read_yaml_element("land_visitor_can_download")
        self._click(selector)
        # 链接有效期-永久有效
        selector = self.read_yaml_element("land_link_valid")
        self._hover(selector)
        selector = self.read_yaml_element("land_link_never_expires")
        self._click(selector)
        #创建链接
        selector = self.read_yaml_element("land_create_link")
        self._click(selector)
        # 提取链接
        selector = self.read_yaml_element("land_get_link_url")
        share_url = self._get_attribute(selector, 'value')
        return share_url

    @element_not_found_exception
    def share_visitor_only_view(self):
        """
        分享素材组-游客可查看
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("land_share_button")
        self._click(selector)
        self._wait(0.7)
        # hover分享权限dropdown
        selector = self.read_yaml_element("land_share_auth")
        self._hover(selector)
        # 分享给互联网用户-可查看
        selector = self.read_yaml_element("land_visitor_view_only")
        self._click(selector)
        # 链接有效期-永久有效
        selector = self.read_yaml_element("land_link_valid")
        self._hover(selector)
        selector = self.read_yaml_element("land_link_never_expires")
        self._click(selector)
        # 创建链接
        selector = self.read_yaml_element("land_create_link")
        self._click(selector)
        # 提取链接
        selector = self.read_yaml_element("land_get_link_url")
        share_url = self._get_attribute(selector, 'value')
        return share_url

    @element_not_found_exception
    def share_internal_can_download(self):
        """
        分享素材组-系统内部用户可下载
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("land_share_button")
        self._click(selector)
        self._wait(0.7)
        # hover分享权限dropdown
        selector = self.read_yaml_element("land_share_auth")
        self._hover(selector)
        # 内部可下载
        selector = self.read_yaml_element("land_internal_can_download")
        self._click(selector)
        # 链接有效期-永久有效
        selector = self.read_yaml_element("land_link_valid")
        self._hover(selector)
        selector = self.read_yaml_element("land_link_never_expires")
        self._click(selector)
        # 创建链接
        selector = self.read_yaml_element("land_create_link")
        self._click(selector)
        # 提取链接
        selector = self.read_yaml_element("land_get_link_url")
        share_url = self._get_attribute(selector, 'value')
        return share_url

    @element_not_found_exception
    def share_internal_only_view(self):
        """
        分享素材组-系统内部用户可下载
        @return:
        """
        # 点击分享按钮
        selector = self.read_yaml_element("land_share_button")
        self._click(selector)
        self._wait(0.7)
        # hover分享权限dropdown
        selector = self.read_yaml_element("land_share_auth")
        self._hover(selector)
        # 内部可下载
        selector = self.read_yaml_element("land_internal_view_only")
        self._click(selector)
        # 链接有效期-永久有效
        selector = self.read_yaml_element("land_link_valid")
        self._hover(selector)
        selector = self.read_yaml_element("land_link_never_expires")
        self._click(selector)
        # 创建链接
        selector = self.read_yaml_element("land_create_link")
        self._click(selector)
        # 提取链接
        selector = self.read_yaml_element("land_get_link_url")
        share_url = self._get_attribute(selector, 'value')
        return share_url

    def share_page_download(self):
        """
        分享落地页-打包下载素材
        @return:
        """
        # 进入分享落地页
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_page_download")
        self._click(selector)

    def share_page_switch_view(self):
        """
        分享落地页-视图切换至多维视图
        @return:
        """
        # 进入分享落地页
        self._go(visitor_can_download_url)
        # 切换至多维视图
        selector = self.read_yaml_element("share_kanban_view")
        self._click(selector)

    def share_page_sort(self):
        """
        分享落地页-排序切换
        @return:
        """
        sort_lst = [
            'share_sort_update_time',
            'share_sort_recent',
            'share_sort_asset_hot',
            'share_sort_history_hot',
            'share_sort_name',
            'share_sort_create_time',
        ]
        # 进入分享落地页
        self._go(visitor_can_download_url)
        selector1 = self.read_yaml_element("share_sort")
        for key in sort_lst:
            # hover排序组件
            self._hover(selector1)
            selector = self.read_yaml_element(key)
            self._click(selector)
            self._wait(0.2)

    def share_page_asc_desc(self):
        """
        分享落地页-升降序
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_sort_asc_desc")
        for _ in range(5):
            if self._is_visible(selector):
                self._click(selector)
                self._wait(0.1)
                self._click(selector)
                break
            else:
                self._wait(1)

    def share_page_format_filter(self):
        """
        分享落地页-格式筛选
        @return:
        """
        self._go(visitor_can_download_url)
        selector1 = self.read_yaml_element("share_sort")
        selector = self.read_yaml_element("share_format")
        for _ in range(5):
            if self._is_visible(selector1):
                self._hover(selector)
                selector = self.read_yaml_element("pic_checkbox")
                self._check(selector)
                break
            self._wait(1)

    def share_page_create_time_filter(self):
        """
        分享落地页-创建时间筛选
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("create_time")
        for _ in range(5):
            if self._is_visible(selector):
                self._hover(selector)
                selector = self.read_yaml_element("latest_7_days")
                self._check(selector)
                break
            self._wait(1)

    def share_page_search_asset(self):
        """
        分享落地页-搜索素材/素材组
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_page_search")
        self._click(selector)
        selector = self.read_yaml_element("share_page_search_input")
        self._fill(selector, "分享落地页")
        self._keyboard_click("Enter")

    def share_page_search_and_filter(self):
        """
        分享落地页-搜索后筛选
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_page_search")
        self._click(selector)
        selector = self.read_yaml_element("share_page_search_input")
        self._fill(selector, "分享落地页")
        self._keyboard_click("Enter")
        self._wait(0.5)
        selector = self.read_yaml_element("share_format")
        self._hover(selector)
        selector = self.read_yaml_element("pic_checkbox")
        self._check(selector)

    def share_page_asset_detail(self):
        """
        分享落地页-进入素材详情页
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_asset_detail")
        self._click(selector)
        self._wait(0.5)

    def share_page_asset_detail_close(self):
        """
        分享落地页-进入素材详情页
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_asset_detail")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_detail_close")
        self._click(selector)

    def share_page_asset_detail_download(self):
        """
        分享落地页-素材详情页下载素材
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_asset_detail")
        self._click(selector)
        selector = self.read_yaml_element("asset_detail_download")
        self._click(selector)

    def share_page_comment_tab(self):
        """
        分享落地页-素材详情页tab切换
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_asset_detail")
        self._click(selector)
        selector = self.read_yaml_element("comment_tab")
        self._click(selector)

    def share_page_comment_tab_login(self):
        """
        分享落地页-素材详情页-评论tab登录
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_asset_detail")
        self._click(selector)
        selector = self.read_yaml_element("comment_tab")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("comment_tab_login")
        self._click(selector)
        selector = self.read_yaml_element("share_login_assert")
        for _ in range(5):
            if self._is_visible(selector):
                return selector
            else:
                self._wait(2.5)

    def share_page_next_asset(self):
        """
        分享落地页-素材详情页-素材切换
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_asset_detail")
        self._click(selector)
        self._wait(2)
        selector = self.read_yaml_element("share_next_asset")
        self._click(selector)
        self._wait(1)
        selector = self.read_yaml_element("share_pre_asset")
        self._click(selector)

    def share_batch_all_download(self):
        """
        分享落地页-批量操作-下载全选素材
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("batch_button")
        self._click(selector)
        selector = self.read_yaml_element("share_all_checkbox")
        self._check(selector)
        selector = self.read_yaml_element("share_batch_download")
        self._click(selector)

    def share_batch_download_group(self):
        """
        分享落地页-批量操作-下载单个素材组
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("batch_button")
        self._click(selector)
        selector = self.read_yaml_element("share_group_radio")
        self._click(selector)
        selector = self.read_yaml_element("share_batch_download")
        self._click(selector)

    def share_batch_download_blank_group(self):
        """
        分享落地页-批量操作-下载空素材组
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("batch_button")
        self._click(selector)
        selector = self.read_yaml_element("share_blank_group")
        self._click(selector)
        selector = self.read_yaml_element("share_batch_download")
        self._click(selector)

    def share_batch_download_asset(self):
        """
        分享落地页-批量操作-下载单个素材
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("batch_button")
        self._click(selector)
        selector = self.read_yaml_element("share_asset_radio")
        self._click(selector)
        selector = self.read_yaml_element("share_batch_download")
        self._click(selector)

    def share_filter_batch_download(self):
        """
        分享落地页-筛选后批量操作打包下载素材
        @return:
        """
        self._go(visitor_can_download_url)
        selector1 = self.read_yaml_element("share_sort")
        selector = self.read_yaml_element("share_format")
        for _ in range(5):
            if self._is_visible(selector1):
                self._hover(selector)
                selector = self.read_yaml_element("pic_checkbox")
                self._check(selector)
                break
            self._wait(1)
        selector = self.read_yaml_element("batch_button")
        self._click(selector)
        selector = self.read_yaml_element("share_all_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("share_batch_download")
        self._click(selector)

    def share_search_batch_download(self):
        """
        分享落地页-搜索后批量操作打包下载素材
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_page_search")
        self._click(selector)
        selector = self.read_yaml_element("share_page_search_input")
        self._fill(selector, "UI")
        self._keyboard_click("Enter")
        selector = self.read_yaml_element("batch_button")
        self._click(selector)
        selector = self.read_yaml_element("share_all_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("share_batch_download")
        self._click(selector)

    def share_enter_sub_group(self):
        """
        分享落地页-进入子素材组
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_enter_group")
        self._click(selector)

    def share_bread_crumbs(self):
        """
        分享落地页-面包屑切换层级
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("share_enter_group")
        self._click(selector)
        selector = self.read_yaml_element("share_first_level")
        self._click(selector)

    def share_visitor_login(self):
        """
        分享落地页-游客页面跳转登录
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("visitor_login")
        self._click(selector)
        selector = self.read_yaml_element("share_login_assert")
        for _ in range(5):
            if self._is_visible(selector):
                return selector
            else:
                self._wait(2.5)

    def share_globalization(self):
        """
        分享落地页-国际化切换
        @return:
        """
        self._go(visitor_can_download_url)
        selector = self.read_yaml_element("globalization_button")
        self._click(selector)
        self._wait(0.5)
        selector = self.read_yaml_element("globalization_assert")
        return self._text_content(selector)