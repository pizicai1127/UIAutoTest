#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : PendingAreaPage
# @Author: yanglun@tezign.com
# @Date  : 2022/1/21
# @Desc  :  待入库页面
"""

from pages.basepage import BasePage
from conf.confs import url_pendingAreaPage


class PendingAreaPage(BasePage):
    """
    待入库页面page
    """

    def goto_draft(self):
        """
        进入到待入库页面
        @return:
        """
        self._go(url_pendingAreaPage)

    def draft_detail(self):
        """
        待入库打开素材预览
        @return:
        """
        selector = self.read_yaml_element("draft_detail")
        self._click(selector)

    def draft_detail_close(self):
        """
        关闭素材预览弹窗
        @return:
        """
        selector = self.read_yaml_element("detail_close")
        self._click(selector)

    def draft_next_detail(self):
        """
        素材详情页左右切换
        @return:
        """
        selector = self.read_yaml_element("next_arrow")
        self._click(selector)
        selector = self.read_yaml_element("prev_arrow")
        self._wait(0.2)
        self._click(selector)

    def draft_detail_delete_cancel(self):
        """
        素材详情页取消删除
        @return:
        """
        selector = self.read_yaml_element("detail_delete")
        self._click(selector)
        selector = self.read_yaml_element("Pop-ups_cancel")
        self._click(selector)

    def draft_detail_delete(self):
        """
        素材详情页确认删除
        @return:
        """
        selector = self.read_yaml_element("detail_delete")
        self._click(selector)
        selector = self.read_yaml_element("Pop-ups_confirm")
        self._click(selector)

    def operation_delete_cancel(self):
        """
        操作栏删除素材-取消删除
        @return:
        """
        selector = self.read_yaml_element("operation_delete")
        self._click(selector)
        selector = self.read_yaml_element("Pop-ups_cancel")
        self._click(selector)

    def operation_delete(self):
        """
        操作栏删除素材-确认删除
        @return:
        """
        selector = self.read_yaml_element("operation_delete")
        self._click(selector)
        selector = self.read_yaml_element("Pop-ups_confirm")
        self._click(selector)

    def pending_delete_cancel(self):
        """
        待入库右上批量删除按钮-取消删除
        @return:
        """
        selector = self.read_yaml_element("single_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("multi_delete")
        self._click(selector)
        selector = self.read_yaml_element("Pop-ups_cancel")
        self._click(selector)

    def pending_delete(self):
        """
        待入库右上批量删除按钮-确认删除
        @return:
        """
        selector = self.read_yaml_element("single_checkbox")
        self._click(selector)
        selector = self.read_yaml_element("multi_delete")
        self._click(selector)
        selector = self.read_yaml_element("Pop-ups_confirm")
        self._click(selector)

    def draft_all_selected(self):
        """
        待入库素材列表-全选
        @return:
        """
        selector = self.read_yaml_element("draft_all_checkbox")
        # 全选
        self._check(selector)

    def draft_num_page(self):
        """
        数字翻页
        @return:
        """
        selector = self.read_yaml_element("second_page")
        self._click(selector)

    def draft_next_page(self):
        """
        上下翻页
        @return:
        """
        selector = self.read_yaml_element("next_page")
        self._click(selector)
        self._wait(0.2)
        self._click(selector)
        self._wait(0.2)
        selector = self.read_yaml_element("pre_page")
        self._click(selector)

    def draft_select_page_count(self):
        """
        切换列表一页的数量
        @return:
        """
        selector = self.read_yaml_element("select_page")
        self._click(selector)
        # 切换至40条/页
        selector = self.read_yaml_element("four_per_page")
        self._click(selector)

    def draft_ingest_no_repeat(self):
        """
        待入库列表操作栏-立即入库-无重复素材
        @return:
        """
        selector = self.read_yaml_element("single_ingest")
        self._click(selector)
        selector = self.read_yaml_element("draft_auth_selected")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("draft_personal_asset")
        self._click(selector)
        self._wait(0.3)
        selector = self.read_yaml_element("ingest_selected")
        self._click(selector)

    def draft_ingest_repeat(self):
        """
        待入库列表操作栏-立即入库-有重复/检测中素材-全部入库
        @return:
        """
        selector = self.read_yaml_element("single_ingest")
        self._click(selector)
        selector = self.read_yaml_element("no_filter")
        self._click(selector)
        self._wait(0.5)
        selector = self.read_yaml_element("draft_auth_selected")
        self._click(selector)
        selector = self.read_yaml_element("draft_personal_asset")
        self._click(selector)
        selector = self.read_yaml_element("ingest_selected")
        self._click(selector)

    def draft_ingest_filter(self):
        """
        待入库列表操作栏-立即入库-有重复/检测中素材-过滤入库
        @return:
        """
        selector = self.read_yaml_element("single_ingest")
        self._click(selector)
        selector = self.read_yaml_element("filter_repeat")
        self._click(selector)

    def draft_selected_ingest(self):
        """
        待入库素材入库入-入库所选
        @return:
        """
        selector = self.read_yaml_element("ingest_selected")
        self._click(selector)

    def draft_type_is(self):
        """
        待入库-素材类型判断
        @return: true:代表纯文本/url素材， false:代表是其他素材
        """
        selector = self.read_yaml_element("draft_type")
        text = self._text_content(selector)
        if text in ('纯文本', '网页'):
            return True
        return False

    def draft_repeat_is(self):
        """
        待入库-素材是否重复判断
        @return: 0：代表素材无重复，1：代表素材重复或者检测中
        """
        # 未重复状态selector
        selector = self.read_yaml_element("not_repeated")
        if self._text_content(selector) == "--":
            return 0
        return 1







































