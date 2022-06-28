#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : UploadAssetPage
# @Author: yanglun@tezign.com
# @Date  : 2022/4/26
# @Desc  :  
"""

from pages.basepage import BasePage
from conf.confs import url_assetPage
from common.exception_handle import *


class UploadAssetPage(BasePage):
    """
    上传/入库页面
    """
    def goto_asset(self):
        """
        进入素材库
        @return:
        """
        self._go(url_assetPage)

    def asset_upload_file(self, path):
        """
        上传素材
        @param path:
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 上传文件
        selector = self.read_yaml_element("asset_upload_file_button")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_input")
        self._set_input_files(selector, path)
        ele = self.read_yaml_element("asset_upload_repeat_title")
        if self._is_visible(ele) is False:
            self._wait(2.5)
        else:
            selector = self.read_yaml_element("asset_follow_up_checkbox")
            self._check(selector)
            selector = self.read_yaml_element("asset_replace_original_file")
            self._click(selector)
            self._wait(2.5)

    def asset_upload_file_test(self, path):
        """
        上传素材-测试（实际不上传成功）
        @param path:
        @return:
        """
        # hover新增按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 上传文件
        selector = self.read_yaml_element("asset_upload_file_button")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_input")
        self._set_input_files(selector, path)
        ele = self.read_yaml_element("asset_upload_repeat_title")
        if self._is_visible(ele) is False:
            return None
        else:
            selector = self.read_yaml_element("asset_follow_up_checkbox")
            self._check(selector)
            selector = self.read_yaml_element("asset_replace_original_file")
            self._click(selector)

    def upload_complete_delete_file(self):
        """
        上传完成弹窗-删除单个素材
        @return:
        """
        # 点击素材后面的删除button
        selector = self.read_yaml_element("asset_delete_single_file")
        self._click(selector)
        # 取消删除
        selector = self.read_yaml_element("asset_delete_single_file_cancel")
        self._click(selector)
        self._wait(0.2)
        # 再次点击素材后面的删除button
        selector = self.read_yaml_element("asset_delete_single_file")
        self._click(selector)
        # 确认删除
        selector = self.read_yaml_element("asset_delete_single_file_confirm")
        self._click(selector)

    def upload_complete_delete_all_file(self):
        """
        上传完成弹窗-删除全部素材
        @return:
        """
        selector = self.read_yaml_element("asset_delete_all")
        self._click(selector)
        # 取消删除
        selector = self.read_yaml_element("asset_delete_single_file_cancel")
        self._click(selector)
        self._wait(0.2)
        # 再次点击素材后面的删除button
        selector = self.read_yaml_element("asset_delete_all")
        self._click(selector)
        # 确认删除
        selector = self.read_yaml_element("asset_delete_single_file_confirm")
        self._click(selector)

    def upload_complete_deal_later(self):
        """
        上传完成弹窗-稍后处理
        @return:
        """
        # 点击稍后处理
        selector = self.read_yaml_element("asset_deal_later_1")
        self._click(selector)
        self._wait(0.5)

    def upload_complete_fold(self):
        """
        上传完成弹窗-收取弹窗
        @return:
        """
        # 收起弹窗
        selector = self.read_yaml_element("asset_fold_upload_window")
        self._click(selector)
        self._wait(0.2)

    def upload_complete_fold_detail(self):
        """
        收起弹窗-查看详情
        @return:
        """
        selector = self.read_yaml_element("asset_fold_upload_window")
        self._click(selector)
        self._wait(0.2)
        selector = self.read_yaml_element("asset_show_detail")
        self._click(selector)

    def upload_complete_fold_deal_later(self):
        """
        收起弹窗-稍后处理
        @return:
        """
        selector = self.read_yaml_element("asset_fold_upload_window")
        self._click(selector)
        selector = self.read_yaml_element("asset_deal_later_2")
        self._click(selector)
        selector = self.read_yaml_element("asset_got_it")
        self._click(selector)

    def upload_delete_selected(self):
        """
        打标弹窗-删除所选
        @return:
        """
        # 立即入库
        selector = self.read_yaml_element("asset_ingest_now_1")
        self._click(selector)
        selector = self.read_yaml_element("asset_delete_selected")
        self._click(selector)
        selector = self.read_yaml_element("asset_delete_cancel")
        self._click(selector)
        selector = self.read_yaml_element("asset_delete_selected")
        self._click(selector)
        selector = self.read_yaml_element("asset_delete_confirm")
        self._click(selector)

    def upload_delete_single(self):
        """
        打标弹窗-删除单个素材
        @return:
        """
        # 立即入库
        selector = self.read_yaml_element("asset_ingest_now_1")
        self._click(selector)
        selector = self.read_yaml_element("asset_delete_single")
        self._click(selector)
        selector = self.read_yaml_element("asset_delete_cancel")
        self._click(selector)
        selector = self.read_yaml_element("asset_delete_single")
        self._click(selector)
        selector = self.read_yaml_element("asset_delete_confirm")
        self._click(selector)

    def upload_rename_selected(self, text):
        """
        打标弹窗-重命名所选
        @return:
        """
        # 立即入库
        selector = self.read_yaml_element("asset_ingest_now_1")
        self._click(selector)
        selector = self.read_yaml_element("asset_all_checkbox")
        self._check(selector)
        self._check(selector)
        selector = self.read_yaml_element("asset_rename_selected")
        self._click(selector)
        selector = self.read_yaml_element("asset_prefix_input")
        self._click(selector)
        self._fill(selector, text)
        selector = self.read_yaml_element("asset_suffix_num")
        self._click(selector)
        self._fill(selector, '1')
        selector = self.read_yaml_element("asset_rename_confirm")
        self._click(selector)
        self._wait(0.5)

    def upload_rename_single(self, text):
        """
        打标弹窗-单个素材预览及重命名
        @return:
        """
        # 立即入库
        selector = self.read_yaml_element("asset_ingest_now_1")
        self._click(selector)
        selector = self.read_yaml_element("asset_name_edit_assert")
        self._click(selector)
        selector = self.read_yaml_element("asset_single_detail_close")
        self._click(selector)
        selector = self.read_yaml_element("asset_name_edit")
        self._click(selector)
        selector = self.read_yaml_element("asset_name_edit_span")
        self._fill(selector, text)
        self._wait(0.5)
        self._mouse_move(10, 10)
        self._mouse_left_click(10, 10)

    def upload_stop_continue(self):
        """
        上传弹窗-上传素材全部暂停and全部继续
        @return:
        """
        selector = self.read_yaml_element("asset_upload_stop")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_stop")
        self._click(selector)

    def upload_cancel_all(self):
        """
        上传弹窗-上传素材全部取消
        @return:
        """
        selector = self.read_yaml_element("asset_upload_cancel")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_cancel_confirm")
        self._click(selector)

    def upload_stop_and_try(self):
        """
        上传弹窗-上传素材单个暂停重试
        @return:
        """
        selector = self.read_yaml_element("asset_upload_stop_single")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_retry_single")
        self._click(selector)

    def upload_stop_and_cancel(self):
        """
        上传弹窗-上传素材单个暂停取消上传
        @return:
        """
        selector = self.read_yaml_element("asset_upload_stop_single")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_cancel_single")
        self._click(selector)

    def upload_window_fold_expand(self):
        """
        上传弹窗-收起和展开
        @return:
        """
        selector = self.read_yaml_element("asset_upload_stop")
        self._click(selector)
        self._wait(0.2)
        selector = self.read_yaml_element("asset_upload_fold")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_expand")
        self._click(selector)

    def asset_import_url(self):
        """
        导入网页-取消
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 导入网页
        selector = self.read_yaml_element("asset_import_url")
        self._click(selector)
        selector = self.read_yaml_element("asset_import_url_cancel")
        self._click(selector)
        # selector = self.read_yaml_element("asset_import_url_input")
        # self._click(selector)
        # self._fill(selector, url)

    def asset_import_url_clear(self, url):
        """
        导入网页-清空内容
        @param url:
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 导入网页
        selector = self.read_yaml_element("asset_import_url")
        self._click(selector)
        # 输入url
        selector = self.read_yaml_element("asset_import_url_input1")
        self._click(selector)
        self._fill(selector, url)
        # 清空url
        selector = self.read_yaml_element("asset_import_url_clear")
        self._click(selector)
        selector = self.read_yaml_element("asset_import_url_input1")
        return selector

    def asset_check_support_url(self):
        """
        导入网页-查看支持的链接
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 导入网页
        selector = self.read_yaml_element("asset_import_url")
        self._click(selector)
        selector = self.read_yaml_element("asset_check_support_url")
        self._click(selector)

    def asset_import_invalid_url(self, url):
        """
        导入网页-输入无效的url
        @param url:
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 导入网页
        selector = self.read_yaml_element("asset_import_url")
        self._click(selector)
        # 输入url
        selector = self.read_yaml_element("asset_import_url_input1")
        self._click(selector)
        self._fill(selector, url)
        # 确认
        selector = self.read_yaml_element("asset_import_url_confirm")
        self._click(selector)
        selector = self.read_yaml_element("asset_import_invalid_format")
        return selector

    def asset_import_valid_url(self, url):
        """
        导入网页-输入单个有效的url
        @param url:
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 导入网页
        selector = self.read_yaml_element("asset_import_url")
        self._click(selector)
        # 输入url
        selector = self.read_yaml_element("asset_import_url_input1")
        self._click(selector)
        self._fill(selector, url)
        # 确认
        selector = self.read_yaml_element("asset_import_url_confirm")
        self._click(selector)
        selector = self.read_yaml_element("asset_ingest_now_1")
        for _ in range(10):
            if self._is_visible(selector):
                self._click(selector)
                break
            else:
                self._wait(1)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_successful_toast")
        return selector

    def asset_import_urls(self, url1, url2):
        """
        导入网页-输入多条有效和无效的url
        @param url2:
        @param url1:
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 导入网页
        selector = self.read_yaml_element("asset_import_url")
        self._click(selector)
        # 输入url1
        selector = self.read_yaml_element("asset_import_url_input1")
        self._click(selector)
        self._fill(selector, url1)
        self._wait(0.1)
        self._keyboard_click("Enter")
        # 输入url2
        selector = self.read_yaml_element("asset_import_url_input2")
        self._click(selector)
        self._fill(selector, url2)
        # 确认
        selector = self.read_yaml_element("asset_import_url_confirm")
        self._click(selector)
        selector = self.read_yaml_element("asset_ingest_now_1")
        for _ in range(10):
            if self._is_visible(selector):
                break
            else:
                self._wait(2)
        selector = self.read_yaml_element("asset_filter_invalid_url_assert")
        return selector

    def asset_import_text_cancel(self):
        """
        取消新建纯文本
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 新建纯文本
        selector = self.read_yaml_element("asset_new_text")
        self._click(selector)
        selector = self.read_yaml_element("asset_new_text_cancel")
        self._click(selector)

    def asset_import_text_clear(self, text):
        """
        新建纯文本-清空内容
        @param text:
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 新建纯文本
        selector = self.read_yaml_element("asset_new_text")
        self._click(selector)
        selector = self.read_yaml_element("asset_new_text_input")
        self._click(selector)
        self._fill(selector, text)
        self._wait(0.1)
        selector = self.read_yaml_element("asset_new_text_clear")
        self._click(selector)
        selector = self.read_yaml_element("asset_new_text_input")
        return selector

    def asset_import_text(self, text):
        """
        新建纯文本-保存入库
        @param text:
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 新建纯文本
        selector = self.read_yaml_element("asset_new_text")
        self._click(selector)
        selector = self.read_yaml_element("asset_new_text_input")
        self._click(selector)
        self._fill(selector, text)
        self._wait(0.1)
        selector = self.read_yaml_element("asset_new_text_save")
        self._click(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_successful_toast")
        return selector

    def asset_import_article_cancel(self):
        """
        取消新建文章
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 新建文章
        selector = self.read_yaml_element("asset_new_article")
        self._click(selector)
        self._wait(0.1)
        selector = self.read_yaml_element("asset_new_article_cancel")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_button")
        return selector

    def asset_import_article(self):
        """
        新建文章
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        # 新建文章
        selector = self.read_yaml_element("asset_new_article")
        self._click(selector)
        # 新建iframe对象
        selector = self.read_yaml_element("asset_new_article_iframe")
        iframe = self._iframe(selector)
        selector = self.read_yaml_element("asset_article_asset")
        iframe.hover(selector)
        iframe.click(selector)
        selector = self.read_yaml_element("asset_article_first")
        self._wait(1)
        for _ in range(5):
            if self._is_enable(selector):
                break
            self._wait(2)
        self._hover(selector)
        self._click(selector)
        selector = self.read_yaml_element("asset_article_confirm")
        self._click(selector)
        self._wait(1)
        self._keyboard_input("新建文章-Ui自动化测试")
        self._keyboard_click('Enter')
        selector = self.read_yaml_element("asset_new_article_save")
        self._click(selector)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_successful_toast")
        return selector

    def asset_ingest(self):
        """
        立即入库
        @return:
        """
        # 立即入库
        selector = self.read_yaml_element("asset_ingest_now_1")
        self._click(selector)

    def tag_into_group_error(self):
        """
        打标-加入素材组-全部下
        @return:
        """
        selector = self.read_yaml_element("asset_ingest_now_1")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_into_group")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_into_group_all")
        self._click(selector)

    def tag_into_group_operate(self):
        """
        打标-加入素材组-选择/删除
        @return:
        """
        selector = self.read_yaml_element("asset_ingest_now_1")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_into_group")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_into_first_group")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_clear_group")
        self._click(selector)

    def tag_into_group_first(self):
        """
        打标-加入素材组-加入第一个素材组
        @return:
        """
        selector = self.read_yaml_element("asset_ingest_now_1")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_into_group")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_into_first_group")
        self._click(selector)

    def tag_description_textarea(self):
        """
        打标-描述输入框
        @return:
        """
        selector = self.read_yaml_element("asset_tag_description_input")
        self._click(selector)
        self._fill(selector, 'UI自动化测试')

    def tag_multi_choice(self):
        """

        打标-下拉框多选tag
        @return:
        """
        selector = self.read_yaml_element("asset_multi_choice_tag")
        self._click(selector)
        self._keyboard_input("多选tag")
        self._keyboard_click("Enter")

    def tag_multi_level_dropdown(self):
        """
        打标-多层级节点下拉框
        @return:
        """
        selector = self.read_yaml_element("asset_tag_multi_level_dropdown")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_multi_level_checkbox")
        self._click(selector)

    def tag_tree_dropdown(self):
        """
        打标-树形结构组件
        @return:
        """
        selector = self.read_yaml_element("asset_tag_tree_dropdown")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_tree_dropdown_expand")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_tree_options")
        self._click(selector)

    def tag_star_dropdown(self):
        """
        打标-有效期达人/明星下拉框组件
        @return:
        """
        selector = self.read_yaml_element("asset_tag_star_dropdown")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_star_option")
        self._click(selector)

    def tag_upload_attach_file(self, path):
        """
        打标-上传素材附件
        @param path:
        @return:
        """
        selector = self.read_yaml_element("asset_attach_file_input")
        self._upload_file_chooser(selector, path)
        self._wait(1.3)

    def tag_attach_file_preview(self):
        """
        打标-素材预览
        @return:
        """
        selector = self.read_yaml_element("asset_attach_file_preview")
        self._click(selector)

    def tag_set_preview(self):
        """
        打标-附件设为预览版本
        @return:
        """
        selector = self.read_yaml_element("asset_attach_file_set_preview")
        self._click(selector)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_asset_detail")
        for _ in range(5):
            if self._is_visible(selector):
                self._click(selector)
                return
            else:
                self._wait(0.5)

    def tag_set_watermark(self):
        """
        打标-水印
        @return:
        """
        selector = self.read_yaml_element("asset_tag_watermark_open")
        self._check(selector)
        selector = self.read_yaml_element("asset_watermark_validity_period")
        self._click(selector)
        selector = self.read_yaml_element("asset_start_date")
        self._click(selector)
        selector = self.read_yaml_element("asset_end_date")
        self._click(selector)
        selector = self.read_yaml_element("asset_watermark_template")
        self._click(selector)
        selector = self.read_yaml_element("asset_watermark_template_option")
        self._click(selector)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_asset_detail")
        for _ in range(5):
            if self._is_visible(selector):
                self._click(selector)
                break
            self._wait(1)
        selector = self.read_yaml_element("asset_watermark_assert")
        for _ in range(5):
            if self._is_visible(selector):
                return self._get_attribute(selector, 'style')
            self._wait(1)

    def tag_asset_release_date(self):
        """
        打标-素材发布日
        @return:
        """
        selector = self.read_yaml_element("out_of_sync_radio")
        self._check(selector)
        selector = self.read_yaml_element("asset_tag_release_dropdown")
        self._click(selector)
        self._wait(0.2)
        selector = self.read_yaml_element("asset_tag_release_date")
        self._click(selector)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_asset_detail")
        for _ in range(5):
            if self._is_visible(selector):
                self._click(selector)
                break
            self._wait(1)
        selector = self.read_yaml_element("asset_release_assert")
        return self._text_content(selector)

    def tag_asset_expired_date(self):
        """
        打标-素材失效日
        @return:
        """
        selector = self.read_yaml_element("out_of_sync_radio")
        self._check(selector)
        selector = self.read_yaml_element("asset_tag_expired")
        self._click(selector)
        self._wait(0.2)
        selector = self.read_yaml_element("asset_tag_expired_date")
        self._click(selector)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_tag_asset_detail")
        for _ in range(5):
            if self._is_visible(selector):
                self._click(selector)
                break
            self._wait(1)
        selector = self.read_yaml_element("asset_release_assert")
        return self._text_content(selector)

    def asset_combination_cancel(self):
        """
        上传-取消新建组合
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        selector = self.read_yaml_element("asset_new_combination")
        self._click(selector)
        selector = self.read_yaml_element("asset_new_combination_cancel")
        self._click(selector)

    def material_selector_close(self):
        """
        上传-关闭素材选择器
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        selector = self.read_yaml_element("asset_new_combination")
        self._click(selector)
        selector = self.read_yaml_element("asset_add_content")
        self._hover(selector)
        selector = self.read_yaml_element("asset_add_from_assets")
        self._click(selector)
        # 获取iframe
        selector = self.read_yaml_element("material_selector_iframe")
        iframe = self._iframe(selector)
        selector = self.read_yaml_element("asset_selector_close")
        iframe.click(selector)
        selector = self.read_yaml_element("asset_add_content")
        return self._text_content(selector)

    def material_selector_search(self):
        """
        上传-素材选择器搜索
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        selector = self.read_yaml_element("asset_new_combination")
        self._click(selector)
        selector = self.read_yaml_element("asset_add_content")
        self._hover(selector)
        selector = self.read_yaml_element("asset_add_from_assets")
        self._click(selector)
        # 获取iframe
        selector = self.read_yaml_element("material_selector_iframe")
        iframe = self._iframe(selector)
        selector = self.read_yaml_element("asset_selector_search_input")
        iframe.click(selector)
        iframe.fill(selector, "JPG")
        self._keyboard_click("Enter")
        selector = self.read_yaml_element("asset_search_result")
        return iframe.text_content(selector)

    def material_selector_selected(self):
        """
        上传-素材选择器可选校验
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        selector = self.read_yaml_element("asset_new_combination")
        self._click(selector)
        selector = self.read_yaml_element("asset_add_content")
        self._hover(selector)
        selector = self.read_yaml_element("asset_add_from_assets")
        self._click(selector)
        # 获取iframe
        selector = self.read_yaml_element("material_selector_iframe")
        iframe = self._iframe(selector)
        selector = self.read_yaml_element("asset_selector_search_input")
        iframe.click(selector)
        iframe.fill(selector, "JPG")
        self._keyboard_click("Enter")
        selector = self.read_yaml_element("asset_card")
        iframe.click(selector)
        selector = self.read_yaml_element("asset_selected_pic_count")
        return iframe.get_attribute(selector, "title")

    def material_selector_clear(self):
        """
        上传-素材选择器清空选择
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        selector = self.read_yaml_element("asset_new_combination")
        self._click(selector)
        selector = self.read_yaml_element("asset_add_content")
        self._hover(selector)
        selector = self.read_yaml_element("asset_add_from_assets")
        self._click(selector)
        # 获取iframe
        selector = self.read_yaml_element("material_selector_iframe")
        iframe = self._iframe(selector)
        selector = self.read_yaml_element("asset_card")
        iframe.click(selector)
        selector = self.read_yaml_element("asset_selector_clear")
        iframe.click(selector)
        return iframe.is_visible(selector)

    def combination_add_from_assets(self):
        """
        新建组合-从素材库添加
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        selector = self.read_yaml_element("asset_new_combination")
        self._click(selector)
        # 命名
        selector = self.read_yaml_element("asset_title_name")
        self._click(selector)
        selector = self.read_yaml_element("asset_title_input")
        self._fill(selector, "UI-新建组合-素材库")
        selector = self.read_yaml_element("asset_add_content")
        self._hover(selector)
        selector = self.read_yaml_element("asset_add_from_assets")
        self._click(selector)
        # 获取iframe
        selector = self.read_yaml_element("material_selector_iframe")
        iframe = self._iframe(selector)
        # # 预览
        self._wait(1.5)
        # selector = self.read_yaml_element("asset_card")
        # iframe.hover(selector)
        # selector = self.read_yaml_element("asset_selector_preview")
        # iframe.click(selector)
        # selector = self.read_yaml_element("asset_close_preview")
        # self._click(selector)
        # 选择素材
        selector = self.read_yaml_element("asset_card")
        iframe.click(selector)
        selector = self.read_yaml_element("asset_combination_confirm")
        iframe.click(selector)
        selector = self.read_yaml_element("asset_combination_save")
        self._click(selector)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_successful_toast")
        return selector

    def combination_upload_from_pc(self, path):
        """
        新建组合-从本地上传
        @param path:
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        selector = self.read_yaml_element("asset_new_combination")
        self._click(selector)
        # 命名
        selector = self.read_yaml_element("asset_title_name")
        self._click(selector)
        selector = self.read_yaml_element("asset_title_input")
        self._fill(selector, "UI-新建组合-本地上传")
        selector = self.read_yaml_element("asset_add_content")
        self._hover(selector)
        selector = self.read_yaml_element("asset_upload_from_pc")
        self._upload_file_chooser(selector, path)
        self._wait(2)
        # 添加
        selector = self.read_yaml_element("asset_upload_from_pc_add")
        self._click(selector)
        selector = self.read_yaml_element("asset_combination_save")
        self._click(selector)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_successful_toast")
        return selector

    def combination_add_text(self):
        """
        新建组合-添加文本
        @return:
        """
        # hover上传按钮
        selector = self.read_yaml_element("asset_upload_button")
        self._hover(selector)
        selector = self.read_yaml_element("asset_new_combination")
        self._click(selector)
        # 命名
        selector = self.read_yaml_element("asset_title_name")
        self._click(selector)
        selector = self.read_yaml_element("asset_title_input")
        self._fill(selector, "UI-新建组合-文本")
        selector = self.read_yaml_element("asset_add_content")
        self._hover(selector)
        selector = self.read_yaml_element("asset_add_text")
        self._click(selector)
        # 添加
        selector = self.read_yaml_element("asset_text_area")
        self._fill(selector, '新建组合-组合类型-纯文本')
        selector = self.read_yaml_element("asset_text_save")
        self._click(selector)
        selector = self.read_yaml_element("asset_combination_save")
        self._click(selector)
        selector = self.read_yaml_element("asset_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("asset_ingest_checked")
        self._click(selector)
        selector = self.read_yaml_element("asset_upload_successful_toast")
        return selector































































