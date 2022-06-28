#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_pending_area
# @Author: yanglun@tezign.com
# @Date  : 2022/1/24
# @Desc  :
"""

import pytest
import allure
from pages.assets.PendingAreaPage import PendingAreaPage


class TestPendingArea:
    """
    待入库测试用例集
    """

    @allure.title("待入库素材预览")
    def test_draft_detail(self, login_sys):
        """
        待入库素材预览
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        if draft_page.draft_type_is():
            draft_page.draft_detail()
            ele = draft_page.read_yaml_element("url_text_toast")
            assert draft_page._text_content(ele) == "暂不支持该类型预览"
        else:
            draft_page.draft_detail()
            ele = draft_page.read_yaml_element("draft_left_name")
            assert draft_page._text_content(ele) != ''

    @allure.title("待入库素材和已入库素材重复")
    def test_repeat_confirm(self, login_sys):
        """
        待入库重复素材确认-待入库素材和已入库素材重复
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        if draft_page.draft_type_is():
            pytest.skip("该素材是url/纯文本素材，不支持预览，跳过该测试用例")
        elif (draft_page.draft_type_is() is False) and (draft_page.draft_repeat_is() == 1):
            draft_page.draft_detail()
            ele = draft_page.read_yaml_element("repeat_confirm_title")
            assert draft_page._text_content(ele) == "素材库查重"

    @allure.title("待入库素材预览左右切换")
    def test_draft_next_detail(self, login_sys):
        """
        待入库素材预览左右切换
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        if draft_page.draft_type_is():
            pytest.skip("该素材是url/纯文本素材，不支持预览，跳过该测试用例")
        else:
            ele = draft_page.read_yaml_element("draft_detail")
            text = draft_page._text_content(ele)
            draft_page.draft_detail()
            draft_page.draft_next_detail()
            ele1 = draft_page.read_yaml_element("draft_left_name")
            assert text in draft_page._text_content(ele1)

    @allure.title("待入库详情弹窗删除操作-取消删除")
    def test_draft_detail_delete_cancel(self, login_sys):
        """
        待入库详情弹窗删除操作-取消删除
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        if draft_page.draft_type_is():
            pytest.skip("该素材是url/纯文本素材，不支持预览，跳过该测试用例")
        else:
            ele = draft_page.read_yaml_element("draft_detail")
            text = draft_page._text_content(ele)
            draft_page.draft_detail()
            draft_page.draft_detail_delete_cancel()
            ele1 = draft_page.read_yaml_element("draft_detail")
            assert draft_page._text_content(ele1) == text

    @allure.title("待入库详情弹窗删除操作-确认删除")
    def test_draft_detail_delete(self, login_sys):
        """
        待入库详情弹窗删除操作-确认删除
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        if draft_page.draft_type_is():
            pytest.skip("该素材是url/纯文本素材，不支持预览，跳过该测试用例")
        else:
            draft_page.draft_detail()
            draft_page.draft_detail_delete()
            ele = draft_page.read_yaml_element('delete_successful_toast')
            assert draft_page._text_content(ele) == "删除成功"

    @allure.title("待入库操作栏删除操作-取消删除")
    def test_operation_delete_cancel(self, login_sys):
        """
        待入库操作栏删除操作-取消删除
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        ele = draft_page.read_yaml_element("draft_detail")
        text = draft_page._text_content(ele)
        draft_page.operation_delete_cancel()
        ele1 = draft_page.read_yaml_element("draft_detail")
        assert draft_page._text_content(ele1) == text

    @allure.title("待入库操作栏删除操作-确认删除")
    def test_operation_delete(self, login_sys):
        """
        待入库操作栏删除操作-确认删除
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        draft_page.operation_delete()
        ele = draft_page.read_yaml_element('delete_successful_toast')
        assert draft_page._text_content(ele) == "删除成功"

    @allure.title("待入库右上角删除操作-取消删除")
    def test_pending_delete_cancel(self, login_sys):
        """
        待入库右上角删除操作-取消删除
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        ele = draft_page.read_yaml_element("draft_detail")
        text = draft_page._text_content(ele)
        draft_page.pending_delete_cancel()
        ele1 = draft_page.read_yaml_element("draft_detail")
        assert draft_page._text_content(ele1) == text

    @allure.title("待入库右上角删除操作-确认删除")
    def test_pending_delete(self, login_sys):
        """
        待入库右上角删除操作-确认删除
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        draft_page.pending_delete()
        ele = draft_page.read_yaml_element('delete_successful_toast')
        assert draft_page._text_content(ele) == "删除成功"

    @allure.title("待入库列表全选")
    def test_draft_all_selected(self, login_sys):
        """
        待入库列表全选
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        draft_page.draft_all_selected()
        # assert draft_page._is_checked(draft_page.read_yaml_element("all_checkbox")) is True
        ele = draft_page.read_yaml_element('selected_items')
        assert draft_page._text_content(ele) == '20'

    @allure.title("待入库列表数字翻页")
    def test_draft_num_page(self, login_sys):
        """
        待入库列表数字翻页
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        draft_page.draft_num_page()
        ele = draft_page.read_yaml_element("page_count")
        assert "第2/" in draft_page._text_content(ele)

    @allure.title("待入库列表上下翻页")
    def test_draft_next_page(self, login_sys):
        """
        待入库列表上下翻页
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        draft_page.draft_next_page()
        ele = draft_page.read_yaml_element("page_count")
        assert "第2/" in draft_page._text_content(ele)

    @allure.title("待入库列表每页数量切换")
    def test_draft_select_page_count(self, login_sys):
        """
        待入库列表每页数量切换
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        draft_page.draft_select_page_count()
        ele = draft_page.read_yaml_element("select_page_text")
        assert draft_page._text_content(ele) == "40 条/页"

    @allure.title("待入库-素材立即入库")
    def test_draft_ingest(self, login_sys):
        """
        待入库-素材立即入库
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        if draft_page.draft_repeat_is() == 1:
            draft_page.draft_ingest_repeat()
            ele = draft_page.read_yaml_element("ingest_successful_toast")
            assert ''.join(draft_page._text_content(ele).split()) == "入库成功，共1项，请刷新页面后查看"

        elif draft_page.draft_repeat_is() == 0:
            draft_page.draft_ingest_no_repeat()
            ele = draft_page.read_yaml_element("ingest_successful_toast")
            assert ''.join(draft_page._text_content(ele).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("素材立即入库-重复素材过滤入库")
    def test_draft_filter_ingest(self, login_sys):
        """
        待入库-素材立即入库-重复素材过滤入库
        @param login_sys:
        @return:
        """
        draft_page = PendingAreaPage(login_sys)
        draft_page.goto_draft()
        if draft_page.draft_repeat_is() == 1:
            draft_page.draft_ingest_filter()
            ele = draft_page.read_yaml_element("filter_ingest_toast")
            assert draft_page._text_content(ele) == "待入库项均重复，请重新选择"
        else:
            pytest.skip("该素材不是重复素材，所以该用例不执行")


if __name__ == '__main__':
    pytest.main(['-vs', 'test_pending_area.py::TestPendingArea::test_repeat_confirm'])
