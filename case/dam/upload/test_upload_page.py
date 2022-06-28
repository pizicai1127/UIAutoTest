#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_upload_page
# @Author: yanglun@tezign.com
# @Date  : 2022/4/26
# @Desc  :
"""

import pytest
import allure
from pages.assets.UploadAssetPage import UploadAssetPage
from common.file_method import FileMethod
from conf.confs import douyin_url_import
from common.logger import logger


class TestUploadAssetPage:
    """
    上传/打标流程
    """

    @allure.title("上传完成弹窗-删除单个素材")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_upload_complete_delete_file(self, login_sys, file_path):
        """
        上传完成弹窗-删除单个素材
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_complete_delete_file()
        assert True

    @allure.title("上传完成弹窗-删除全部素材")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_upload_complete_delete_all_file(self, login_sys, file_path):
        """
        上传完成弹窗-删除全部素材
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_complete_delete_all_file()
        assert True

    @allure.title("上传完成弹窗-稍后处理")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_upload_complete_deal_later(self, login_sys, file_path):
        """
        上传完成弹窗-稍后处理
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_complete_deal_later()
        ele = upload_page.read_yaml_element("asset_got_it")
        assert upload_page._text_content(ele) == "知道了"

    @allure.title("上传完成弹窗-收取弹窗")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_upload_complete_fold(self, login_sys, file_path):
        """
        上传完成弹窗-收取弹窗
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_complete_fold()
        ele = upload_page.read_yaml_element("asset_fold_assert")
        assert upload_page._text_content(ele) == "上传完成"

    @allure.title("收起弹窗-查看详情")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_upload_complete_fold_detail(self, login_sys, file_path):
        """
        收起弹窗-查看详情
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_complete_fold_detail()
        ele = upload_page.read_yaml_element("asset_deal_later_1")
        assert upload_page._text_content(ele) == "稍后处理"

    @allure.title("收起弹窗-稍后处理")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_upload_complete_fold_deal_later(self, login_sys, file_path):
        """
        收起弹窗-稍后处理
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_complete_fold_deal_later()
        assert True

    @allure.title("打标弹窗-删除所选")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_upload_delete_selected(self, login_sys, file_path):
        """
        打标弹窗-删除所选
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_delete_selected()
        ele = upload_page.read_yaml_element("asset_delete_toast_assert")
        assert upload_page._text_content(ele) == "删除成功"

    @allure.title("打标弹窗-删除单个素材")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_upload_delete_single(self, login_sys, file_path):
        """
        打标弹窗-删除单个素材
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_delete_single()
        ele = upload_page.read_yaml_element("asset_delete_toast_assert")
        assert upload_page._text_content(ele) == "删除成功"

    @allure.title("打标弹窗-重命名所选")
    @pytest.mark.parametrize('file_path,text', [((FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')),
                                                "批量重名-UI")])
    def test_upload_rename_selected(self, login_sys, file_path, text):
        """
        打标弹窗-重命名所选
        @param login_sys:
        @param file_path:
        @param text:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_rename_selected(text)
        ele = upload_page.read_yaml_element("asset_first_name")
        assert upload_page._text_content(ele) == (text + '-1')

    @allure.title("打标弹窗-单个素材预览及重命名")
    @pytest.mark.parametrize('file_path,text', [((FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')),
                                                 "编辑素材名称")])
    def test_upload_rename_single(self, login_sys, file_path, text):
        """
        打标弹窗-单个素材预览及重命名
        @param login_sys:
        @param file_path:
        @param text:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.upload_rename_single(text)
        ele = upload_page.read_yaml_element("asset_name_edit_assert")
        assert upload_page._text_content(ele) == text

    @allure.title("上传弹窗-上传素材全部暂停and全部继续")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试8.jpg')])
    def test_upload_stop_continue(self, login_sys, file_path):
        """
        上传弹窗-上传素材全部暂停and全部继续
        @param login_sys:
        @param file_path:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file_test(file_path)
        upload_page.upload_stop_continue()
        ele = upload_page.read_yaml_element("asset_upload_stop_assert")
        assert upload_page._text_content(ele) == "正在上传  "

    @allure.title("上传弹窗-上传素材全部取消")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试8.jpg')])
    def test_upload_cancel_all(self, login_sys, file_path):
        """
        上传弹窗-上传素材全部取消
        @param login_sys:
        @param file_path:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file_test(file_path)
        upload_page.upload_cancel_all()
        assert True

    @allure.title("上传弹窗-上传素材单个暂停重试")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试8.jpg')])
    def test_upload_stop_and_try(self, login_sys, file_path):
        """
        上传弹窗-上传素材单个暂停重试
        @param login_sys:
        @param file_path:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file_test(file_path)
        upload_page.upload_stop_and_try()
        ele = upload_page.read_yaml_element("asset_upload_stop_assert")
        assert upload_page._text_content(ele) == "正在上传  "

    @allure.title("上传弹窗-上传素材单个暂停取消上传")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试8.jpg')])
    def test_upload_stop_and_cancel(self, login_sys, file_path):
        """
        上传弹窗-上传素材单个暂停取消上传
        @param login_sys:
        @param file_path:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file_test(file_path)
        upload_page.upload_stop_and_cancel()
        assert True

    @allure.title("上传弹窗-收起和展开")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试8.jpg')])
    def test_upload_window_fold_expand(self, login_sys, file_path):
        """
        上传弹窗-收起和展开
        @param login_sys:
        @param file_path:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file_test(file_path)
        upload_page.upload_window_fold_expand()
        ele = upload_page.read_yaml_element("asset_upload_expand_assert")
        assert upload_page._text_content(ele) == "上传"

    @allure.title("导入网页-取消")
    def test_asset_import_url(self, login_sys):
        """
        导入网页-取消
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_import_url()
        assert True

    @allure.title("导入网页-清空内容")
    def test_asset_import_url_clear(self, login_sys):
        """
        导入网页-清空内容
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.asset_import_url_clear(douyin_url_import)
        # 断言属性值为空
        assert upload_page._get_attribute(selector, 'value') == ''

    @allure.title("导入网页-查看支持的链接")
    def test_asset_check_support_url(self, login_sys):
        """
        导入网页-查看支持的链接
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_check_support_url()
        assert True

    @pytest.mark.parametrize("invalid_url", ['httada3dad1111'])
    @allure.title("导入网页-输入无效的url")
    def test_asset_import_invalid_url(self, login_sys, invalid_url):
        """
        导入网页-输入无效的url
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.asset_import_invalid_url(invalid_url)
        # 断言无效格式
        assert upload_page._text_content(selector) == "(无效格式)"

    @pytest.mark.parametrize("valid_url", [douyin_url_import])
    @allure.title("导入网页-输入有效的单条url")
    def test_asset_import_valid_url(self, login_sys, valid_url):
        """
        导入网页-输入有效的单条url
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.asset_import_valid_url(valid_url)
        # 断言toast提示
        assert ''.join(upload_page._text_content(selector).split()) == "入库成功，共1项，请刷新页面后查看"

    @pytest.mark.parametrize('valid_url,invalid_url', [((douyin_url_import), "ewqeqwe2342423")])
    @allure.title("导入网页-输入多条有效和无效的url")
    def test_asset_import_urls(self, login_sys, valid_url, invalid_url):
        """
        导入网页-输入多条有效和无效的url
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.asset_import_urls(valid_url, invalid_url)
        # 断言过滤后数量
        assert upload_page._text_content(selector) == "1"

    @allure.title("取消新建纯文本")
    def test_asset_import_text_cancel(self, login_sys):
        """
        取消新建纯文本
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_import_text_cancel()
        assert True

    @pytest.mark.parametrize("text", ['新建纯文本-UI自动化测试'])
    @allure.title("新建纯文本-清空内容")
    def test_asset_import_text_clear(self, login_sys, text):
        """
        新建纯文本-清空内容
        @param login_sys:
        @param text:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.asset_import_text_clear(text)
        assert upload_page._get_attribute(selector, "placeholder") == "请输入正文"

    @pytest.mark.parametrize("text", ['新建纯文本-UI自动化测试'])
    @allure.title("新建纯文本入库")
    def test_asset_import_text(self, login_sys, text):
        """
        新建纯文本入库
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.asset_import_text(text)
        # 断言toast提示
        assert ''.join(upload_page._text_content(selector).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("取消新建文章")
    def test_asset_import_article_cancel(self, login_sys):
        """
        取消新建文章
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.asset_import_article_cancel()
        assert upload_page._is_visible(selector) is True

    @pytest.mark.flaky(reruns=1)
    @allure.title("新建文章")
    def test_asset_import_article(self, login_sys):
        """
        新建文章
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.asset_import_article()
        assert ''.join(upload_page._text_content(selector).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("上传-取消新建组合")
    def test_asset_combination_cancel(self, login_sys):
        """
        上传-取消新建组合
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_combination_cancel()
        assert True

    @allure.title("上传-关闭素材选择器")
    def test_material_selector_close(self, login_sys):
        """
        上传-关闭素材选择器
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        text = upload_page.material_selector_close()
        assert text == "添加内容"

    @allure.title("上传-素材选择器搜索")
    def test_material_selector_search(self, login_sys):
        """
        上传-素材选择器搜索
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        text = upload_page.material_selector_search()
        assert "以下为搜索" in text

    @allure.title("上传-素材选择器可选校验")
    def test_material_selector_selected(self, login_sys):
        """
        上传-素材选择器可选校验
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        count = upload_page.material_selector_selected()
        assert count == "1"

    @allure.title("上传-素材选择器清空选择")
    def test_material_selector_clear(self, login_sys):
        """
        上传-素材选择器清空选择
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        bool_assert = upload_page.material_selector_clear()
        assert bool_assert is False

    @allure.title("新建组合-从素材库添加")
    def test_combination_add_from_assets(self, login_sys):
        """
        新建组合-从素材库添加
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.combination_add_from_assets()
        # 断言toast提示
        assert ''.join(upload_page._text_content(selector).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("新建组合-本地上传")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_combination_upload_from_pc(self, login_sys, file_path):
        """
        新建组合-本地上传
        @param login_sys:
        @param file_path:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.combination_upload_from_pc(file_path)
        # 断言toast提示
        assert ''.join(upload_page._text_content(selector).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("新建组合-添加文本")
    def test_combination_add_text(self, login_sys):
        """
        新建组合-添加文本
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        selector = upload_page.combination_add_text()
        # 断言toast提示
        assert ''.join(upload_page._text_content(selector).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("打标弹窗-加入素材组-全部")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_into_group_error(self, login_sys, file_path):
        """
        打标弹窗-加入素材组-全部
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.tag_into_group_error()
        ele = upload_page.read_yaml_element("asset_tag_into_group_all_toast")
        assert upload_page._text_content(ele) == "素材组首页不允许入库文件"

    @allure.title("打标-加入素材组-选择/删除")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_into_group_operate(self, login_sys, file_path):
        """
        打标-加入素材组-选择/删除
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.tag_into_group_operate()
        ele = upload_page.read_yaml_element("asset_tag_into_first_group_assert")
        assert upload_page._text_content(ele) == "添加"

    @allure.title("打标-描述输入框")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_description_textarea(self, login_sys, file_path):
        """
        打标-描述输入框
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        upload_page.tag_description_textarea()
        ele = upload_page.read_yaml_element("asset_tag_description_input")
        assert upload_page._text_content(ele) == "UI自动化测试"

    @allure.title("打标-下拉框多选tag")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_multi_choice(self, login_sys, file_path):
        """
        打标-下拉框多选tag
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        upload_page.tag_multi_choice()
        ele = upload_page.read_yaml_element("asset_multi_choice_tag_assert")
        assert upload_page._text_content(ele) == "多选tag"

    @allure.title("打标-多层级节点下拉框")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_multi_level_dropdown(self, login_sys, file_path):
        """
        打标-多层级节点下拉框
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        upload_page.tag_multi_level_dropdown()
        ele = upload_page.read_yaml_element("asset_tag_multi_level_assert")
        assert upload_page._text_content(ele) == "自动化测试多层级节点"

    @allure.title("打标-树形结构组件")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_tree_dropdown(self, login_sys, file_path):
        """
        打标-树形结构组件
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        upload_page.tag_tree_dropdown()
        ele = upload_page.read_yaml_element("asset_tag_tree_assert")
        assert upload_page._text_content(ele) == "子子分支1"

    @allure.title("打标-有效期达人/明星下拉框组件")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_star_dropdown(self, login_sys, file_path):
        """
        打标-有效期达人/明星下拉框组件
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        upload_page.tag_star_dropdown()
        ele = upload_page.read_yaml_element("asset_tag_star_assert")
        assert upload_page._text_content(ele) == "杨伦（2022～2024）"

    @allure.title("打标-素材附件预览")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_attach_file_preview(self, login_sys, file_path):
        """
        打标-素材附件预览
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        upload_page.tag_upload_attach_file(file_path)
        upload_page.tag_attach_file_preview()
        ele = upload_page.read_yaml_element("asset_attach_file_preview_assert")
        assert "tezign" in upload_page._get_attribute(ele, "src")

    @allure.title("打标-设置素材附件预览版本")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_set_preview(self, login_sys, file_path):
        """
        打标-设置素材附件预览版本
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        upload_page.tag_upload_attach_file(file_path)
        upload_page.tag_set_preview()
        ele = upload_page.read_yaml_element("asset_set_preview_assert")
        assert upload_page._text_content(ele) == "当前正在预览附件"

    @allure.title("打标-水印预览")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_set_watermark(self, login_sys, file_path):
        """
        打标-水印预览
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        text = upload_page.tag_set_watermark()
        assert 'inset' in text

    @allure.title("打标-素材发布日")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_asset_release_date(self, login_sys, file_path):
        """
        打标-素材发布日
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        text = upload_page.tag_asset_release_date()
        assert '素材未生效' in text

    @allure.title("打标-素材失效日")
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试7.jpg')])
    def test_tag_asset_expired_date(self, login_sys, file_path):
        """
        打标-素材失效日
        @param login_sys:
        @return:
        """
        upload_page = UploadAssetPage(login_sys)
        upload_page.goto_asset()
        upload_page.asset_upload_file(file_path)
        upload_page.asset_ingest()
        text = upload_page.tag_asset_expired_date()
        assert '素材已失效' in text


if __name__ == '__main__':
    pytest.main(['-vs', 'test_upload_page.py::TestUploadAssetPage::test_upload_complete_delete_file'])
