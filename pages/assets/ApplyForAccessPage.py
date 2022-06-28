#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : ApplyForAccessPage
# @Author: yanglun@tezign.com
# @Date  : 2022/5/5
# @Desc  :  
"""

from pages.basepage import BasePage
from conf.confs import url_assetPage
from common.exception_handle import *


class ApplyForAccessPage(BasePage):
    """
    权限申请页面
    """

    def goto_asset(self):
        """
        进入素材库
        @return:
        """
        selector = self.read_yaml_element("access_error_url")
        for _ in range(5):
            self._go(url_assetPage)
            self._wait(0.5)
            if self._is_visible(selector):
                break

    @element_not_found_exception
    def access_upload_file(self, path, text):
        """
        上传文件
        @param text:
        @param path: 文件路径
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("access_upload_button")
        self._hover(selector)
        # 上传文件
        selector = self.read_yaml_element("access_upload_file_button")
        self._click(selector)
        selector = self.read_yaml_element("access_upload_input")
        self._set_input_files(selector, path)
        ele = self.read_yaml_element("access_upload_repeat_title")
        if self._is_visible(ele) is False:
            self._wait(4)
            # 点击立即入库按钮
            selector = self.read_yaml_element("access_ingest_now")
            self._click(selector)
            # 选择权限-仅个人可见
            selector = self.read_yaml_element("access_auth_selected")
            self._click(selector)
            self._wait(0.1)
            selector = self.read_yaml_element("access_personal_asset")
            self._click(selector)
            self._wait(0.3)
            # 添加成员
            selector = self.read_yaml_element("access_add_staff")
            self._click(selector)
            selector = self.read_yaml_element("access_search_input")
            self._click(selector)
            self._fill(selector, text)
            self._wait(0.5)
            selector = self.read_yaml_element("access_search_result_checkbox")
            self._check(selector)
            selector = self.read_yaml_element("access_confirm_button")
            self._click(selector)
            # 点击入库所选按钮
            selector = self.read_yaml_element("access_ingest_checked")
            self._click(selector)
        else:
            selector = self.read_yaml_element("access_follow_up_checkbox")
            self._check(selector)
            selector = self.read_yaml_element("access_replace_original_file")
            self._click(selector)
            self._wait(4)
            # 点击立即入库按钮
            selector = self.read_yaml_element("access_ingest_now")
            self._click(selector)
            # 选择权限-仅个人可见
            selector = self.read_yaml_element("access_auth_selected")
            self._click(selector)
            self._wait(0.1)
            selector = self.read_yaml_element("access_personal_asset")
            self._click(selector)
            self._wait(0.3)
            # 添加成员
            selector = self.read_yaml_element("access_add_staff")
            self._click(selector)
            selector = self.read_yaml_element("access_search_input")
            self._click(selector)
            self._fill(selector, text)
            self._wait(0.5)
            selector = self.read_yaml_element("access_search_result_checkbox")
            self._check(selector)
            selector = self.read_yaml_element("access_confirm_button")
            self._click(selector)
            # 点击入库所选按钮
            selector3 = self.read_yaml_element("access_ingest_checked")
            self._click(selector3)

    def asset_detail_apply_for_download_blank(self):
        """
        素材详情页申请下载权限-空判断
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._click(selector)
        selector = self.read_yaml_element("access_apply_download")
        for _ in range(15):
            if self._is_visible(selector):
                self._click(selector)
                selector = self.read_yaml_element("access_apply_confirm")
                self._click(selector)
                break
            else:
                self._wait(1)

    def asset_detail_apply_for_download(self):
        """
        素材详情页申请下载权限
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._click(selector)
        selector = self.read_yaml_element("access_apply_download")
        for _ in range(15):
            if self._is_visible(selector):
                self._click(selector)
                selector = self.read_yaml_element("access_apply_textarea")
                self._click(selector)
                self._fill(selector, '申请下载权限-UI自动化lsm')
                selector = self.read_yaml_element("access_apply_confirm")
                self._click(selector)
                break
            else:
                self._wait(1)
        self._wait(0.2)

    def asset_detail_apply_for_edit(self):
        """
        素材详情页申请编辑权限
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._click(selector)
        selector = self.read_yaml_element("access_apply_edit")
        for _ in range(15):
            if self._is_visible(selector):
                self._click(selector)
                selector = self.read_yaml_element("access_apply_textarea")
                self._click(selector)
                self._fill(selector, '申请编辑权限-UI自动化lsm')
                selector = self.read_yaml_element("access_apply_confirm")
                self._click(selector)
                break
            else:
                self._wait(1)
        self._wait(0.2)

    def download_apply_audit_reject(self):
        """
        审核下载权限申请-拒绝
        @return:
        """
        selector = self.read_yaml_element("access_bell_notification")
        self._click(selector)
        selector = self.read_yaml_element("access_to_do_tab")
        self._click(selector)
        selector = self.read_yaml_element("access_go_approval_page")
        self._click(selector)
        selector = self.read_yaml_element("access_reject_button")
        self._click(selector)
        selector = self.read_yaml_element("access_reject_reason_input")
        self._click(selector)
        self._fill(selector, "我拒绝你的下载申请-UI自动化测试")
        selector = self.read_yaml_element("access_reject_confirm")
        self._click(selector)

    def check_reject_reason_download(self):
        """
        查看下载权限申请被拒绝详情
        @return:
        """
        selector = self.read_yaml_element("access_bell_notification")
        self._click(selector)
        selector = self.read_yaml_element("access_all_notification_tab")
        self._click(selector)
        selector = self.read_yaml_element("access_go_approval_page")
        self._click(selector)
        selector = self.read_yaml_element("access_reject_reason_assert")
        return self._text_content(selector)

    def download_apply_audit_pass(self):
        """
        审核下载权限申请-通过
        @return:
        """
        selector = self.read_yaml_element("access_bell_notification")
        self._click(selector)
        selector = self.read_yaml_element("access_to_do_tab")
        self._click(selector)
        selector = self.read_yaml_element("access_go_approval_page")
        self._click(selector)
        selector = self.read_yaml_element("access_pass_button")
        self._click(selector)
        selector = self.read_yaml_element("access_pass_second_confirm")
        self._click(selector)

    def check_pass_reason_download(self):
        """
        查看下载权限申请被通过详情
        @return:
        """
        selector = self.read_yaml_element("access_bell_notification")
        self._click(selector)
        selector = self.read_yaml_element("access_all_notification_tab")
        self._click(selector)
        selector = self.read_yaml_element("access_go_approval_page")
        self._click(selector)
        selector = self.read_yaml_element("access_reject_reason_assert")
        return self._is_visible(selector)

    def edit_apply_audit_reject(self):
        """
        审核编辑权限申请-拒绝
        @return:
        """
        selector = self.read_yaml_element("access_bell_notification")
        self._click(selector)
        selector = self.read_yaml_element("access_to_do_tab")
        self._click(selector)
        selector = self.read_yaml_element("access_go_approval_page")
        self._click(selector)
        selector = self.read_yaml_element("access_reject_button")
        self._click(selector)
        selector = self.read_yaml_element("access_reject_reason_input")
        self._click(selector)
        self._fill(selector, "我拒绝你的编辑申请-UI自动化测试")
        selector = self.read_yaml_element("access_reject_confirm")
        self._click(selector)

    def edit_apply_audit_pass(self):
        """
        审核编辑权限申请-通过
        @return:
        """
        selector = self.read_yaml_element("access_bell_notification")
        self._click(selector)
        selector = self.read_yaml_element("access_to_do_tab")
        self._click(selector)
        selector = self.read_yaml_element("access_go_approval_page")
        self._click(selector)
        selector = self.read_yaml_element("access_pass_button")
        self._click(selector)
        selector = self.read_yaml_element("access_pass_second_confirm")
        self._click(selector)

    def access_apply_success_confirm(self):
        """
        进入详情页查看申请的权限是否生效
        @return: False代表未生效，True代表生效
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._click(selector)
        selector = self.read_yaml_element("access_download_button")
        selector1 = self.read_yaml_element("access_edit_button")
        for _ in range(15):
            if self._is_visible(selector) and self._is_visible(selector1):
                return True
            else:
                self._wait(1)

    def access_batch_apply_download_blank(self):
        """
        素材列表批量操作申请下载权限-空判断
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._hover(selector)
        selector = self.read_yaml_element("access_asset_list_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_download")
        self._hover(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("access_batch_download_asset")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_apply")
        self._click(selector)
        selector = self.read_yaml_element("access_apply_commit")
        self._click(selector)

    def access_batch_apply_download(self):
        """
        素材列表批量操作申请下载权限
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._hover(selector)
        selector = self.read_yaml_element("access_asset_list_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_download")
        self._hover(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("access_batch_download_asset")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_apply")
        self._click(selector)
        selector = self.read_yaml_element("access_apply_reason_textarea")
        self._click(selector)
        self._fill(selector, "素材列表-申请权限")
        selector = self.read_yaml_element("access_apply_commit")
        self._click(selector)

    def access_batch_apply_download_cancel(self):
        """
        素材列表批量操作-取消申请下载权限
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._hover(selector)
        selector = self.read_yaml_element("access_asset_list_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_download")
        self._hover(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("access_batch_download_asset")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_apply")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_apply_cancel")
        self._click(selector)

    def access_download_success_confirm(self):
        """
        在素材列表查看申请的下载权限是否生效
        @return: False代表未生效，True代表生效
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._hover(selector)
        selector = self.read_yaml_element("access_asset_list_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_download")
        self._hover(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("access_batch_download_asset")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_apply")
        if self._is_visible(selector):
            return False
        return True

    def access_batch_apply_edit_know(self):
        """
        素材列表批量操作申请编辑权限-我知道了
        @return:
        """
        self._wait(1)
        selector = self.read_yaml_element("access_asset_detail")
        self._hover(selector)
        self._wait(0.5)
        selector = self.read_yaml_element("access_asset_list_checkbox")
        self._click(selector)
        self._wait(0.2)
        selector = self.read_yaml_element("access_batch_edit_asset")
        self._click(selector)
        self._wait(0.5)
        selector = self.read_yaml_element("access_batch_edit_know")
        self._click(selector)

    def access_batch_apply_edit_blank(self):
        """
        素材列表批量操作申请编辑权限-空提交验证
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._hover(selector)
        selector = self.read_yaml_element("access_asset_list_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_edit_asset")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_edit_apply")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_edit_commit")
        self._click(selector)

    def access_batch_apply_edit(self):
        """
        素材列表批量操作申请编辑权限
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._hover(selector)
        selector = self.read_yaml_element("access_asset_list_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_edit_asset")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_edit_apply")
        self._click(selector)
        selector = self.read_yaml_element("access_apply_reason_textarea")
        self._click(selector)
        self._fill(selector, "素材列表申请编辑权限-UI自动化")
        selector = self.read_yaml_element("access_batch_edit_commit")
        self._click(selector)
        self._wait(0.2)

    def batch_apply_edit_success_confirm(self):
        """
        素材列表批量操作申请编辑权限通过结果验证
        @return:
        """
        selector = self.read_yaml_element("access_asset_detail")
        self._hover(selector)
        selector = self.read_yaml_element("access_asset_list_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_edit_asset")
        self._click(selector)
        selector = self.read_yaml_element("access_batch_edit_apply")
        if self._is_visible(selector):
            return False
        return True





