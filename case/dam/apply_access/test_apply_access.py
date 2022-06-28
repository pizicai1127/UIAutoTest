#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_apply_access
# @Author: yanglun@tezign.com
# @Date  : 2022/5/5
# @Desc  :
"""

import pytest
import allure
from pages.assets.ApplyForAccessPage import ApplyForAccessPage
from common.file_method import FileMethod


class TestApplyAccessPage:
    """
    上传流程
    """

    @allure.title("上传权限申请使用的素材")
    @pytest.mark.parametrize('file_path,text', [((FileMethod().get_file_path('data/test_file', '', '权限申请UI自动化测试.jpg')),
                                              "刘绍明")])
    def test_access_upload_file(self, login_sys, file_path, text):
        """
        上传权限申请使用的素材
        @param login_sys:
        @param file_path:
        @param text:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_sys)
        apply_access_page.goto_asset()
        apply_access_page.access_upload_file(file_path, text)
        ele = apply_access_page.read_yaml_element("access_upload_successful_toast")
        assert ''.join(apply_access_page._text_content(ele).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("素材详情页申请下载权限-空判断")
    def test_asset_detail_apply_for_download_blank(self, login_init):
        """
        素材详情页申请下载权限-空判断
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.asset_detail_apply_for_download_blank()
        ele = apply_access_page.read_yaml_element("access_apply_blank_text")
        assert apply_access_page._text_content(ele) == "请输入所属部门及申请原因"

    @allure.title("素材详情页申请下载权限")
    def test_asset_detail_apply_for_download_1(self, login_init):
        """
        素材详情页申请下载权限
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.asset_detail_apply_for_download()
        ele = apply_access_page.read_yaml_element("access_apply_assert")
        assert apply_access_page._text_content(ele) == "提交成功"

    @allure.title("审核下载权限申请-拒绝")
    def test_download_apply_audit_reject(self, login_sys):
        """
        审核下载权限申请-拒绝
        @param login_sys:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_sys)
        apply_access_page.goto_asset()
        apply_access_page.download_apply_audit_reject()
        ele = apply_access_page.read_yaml_element("access_reject_toast")
        assert apply_access_page._text_content(ele) == "已拒绝此次申请"

    @allure.title("查看下载权限申请被拒绝详情")
    def test_check_reject_reason_download(self, login_init):
        """
        查看下载权限申请被拒绝详情
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        text = apply_access_page.check_reject_reason_download()
        assert "拒绝理由" in text

    @allure.title("素材详情页二次申请下载权限")
    def test_asset_detail_apply_for_download_2(self, login_init):
        """
        素材详情页二次申请下载权限
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.asset_detail_apply_for_download()
        ele = apply_access_page.read_yaml_element("access_apply_assert")
        assert apply_access_page._text_content(ele) == "提交成功"

    @allure.title("审核下载权限申请-通过")
    def test_download_apply_audit_pass(self, login_sys):
        """
        审核下载权限申请-通过
        @param login_sys:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_sys)
        apply_access_page.goto_asset()
        apply_access_page.download_apply_audit_pass()
        ele = apply_access_page.read_yaml_element("access_pass_toast")
        assert apply_access_page._text_content(ele) == "已通过此次申请"

    @allure.title("查看下载权限申请被通过详情")
    def test_check_pass_reason_download(self, login_init):
        """
        查看下载权限申请被通过详情
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        assert_bool = apply_access_page.check_pass_reason_download()
        assert assert_bool is False

    @allure.title("素材详情页申请编辑权限")
    def test_asset_detail_apply_for_edit_1(self, login_init):
        """
        素材详情页申请编辑权限
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.asset_detail_apply_for_edit()
        ele = apply_access_page.read_yaml_element("access_apply_assert")
        assert apply_access_page._text_content(ele) == "提交成功"

    @allure.title("审核编辑权限申请-拒绝")
    def test_edit_apply_audit_reject(self, login_sys):
        """
        审核编辑权限申请-拒绝
        @param login_sys:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_sys)
        apply_access_page.goto_asset()
        apply_access_page.edit_apply_audit_reject()
        ele = apply_access_page.read_yaml_element("access_reject_toast")
        assert apply_access_page._text_content(ele) == "已拒绝此次申请"

    @allure.title("素材详情页二次申请编辑权限")
    def test_asset_detail_apply_for_edit_2(self, login_init):
        """
        素材详情页二次申请编辑权限
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.asset_detail_apply_for_edit()
        ele = apply_access_page.read_yaml_element("access_apply_assert")
        assert apply_access_page._text_content(ele) == "提交成功"

    @allure.title("审核编辑权限申请-通过")
    def test_edit_apply_audit_pass(self, login_sys):
        """
        审核编辑权限申请-通过
        @param login_sys:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_sys)
        apply_access_page.goto_asset()
        apply_access_page.edit_apply_audit_pass()
        ele = apply_access_page.read_yaml_element("access_pass_toast")
        assert apply_access_page._text_content(ele) == "已通过此次申请"

    @allure.title("入详情页查看申请的权限是否生效")
    def test_access_apply_success_confirm(self, login_init):
        """
        入详情页查看申请的权限是否生效
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        assert_bool = apply_access_page.access_apply_success_confirm()
        assert assert_bool is True

    @allure.title("再次上传权限申请使用的素材")
    @pytest.mark.parametrize('file_path,text', [((FileMethod().get_file_path('data/test_file', '', '权限申请UI自动化测试1.jpg')),
                                                 "刘绍明")])
    def test_access_upload_file_1(self, login_sys, file_path, text):
        """
        再次上传权限申请使用的素材
        @param login_sys:
        @param file_path:
        @param text:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_sys)
        apply_access_page.goto_asset()
        apply_access_page.access_upload_file(file_path, text)
        ele = apply_access_page.read_yaml_element("access_upload_successful_toast")
        assert ''.join(apply_access_page._text_content(ele).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("素材列表批量操作申请下载权限-空判断")
    def test_access_batch_apply_download_blank(self, login_init):
        """
        素材列表批量操作申请下载权限-空判断
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.access_batch_apply_download_blank()
        ele = apply_access_page.read_yaml_element("access_blank_apply")
        assert apply_access_page._text_content(ele) == "请输入所属部门及申请原因"

    @allure.title("素材列表批量操作-取消申请下载权限")
    def test_access_batch_apply_download_cancel(self, login_init):
        """
        素材列表批量操作-取消申请下载权限
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.access_batch_apply_download_cancel()
        assert True

    @allure.title("素材列表批量操作申请下载权限")
    def test_access_batch_apply_download(self, login_init):
        """
        素材列表批量操作申请下载权限
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.access_batch_apply_download()
        ele = apply_access_page.read_yaml_element("access_apply_success")
        assert apply_access_page._text_content(ele) == "申请已提交成功，审核结果会通过邮件发送给你"

    @allure.title("审核下载权限申请(素材列表)-通过")
    def test_download_apply_audit_pass_1(self, login_sys):
        """
        审核下载权限申请(素材列表)-通过
        @param login_sys:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_sys)
        apply_access_page.goto_asset()
        apply_access_page.download_apply_audit_pass()
        ele = apply_access_page.read_yaml_element("access_pass_toast")
        assert apply_access_page._text_content(ele) == "已通过此次申请"

    @allure.title("在素材列表页查看申请的下载权限是否生效")
    def test_access_download_success_confirm(self, login_init):
        """
        在素材列表页查看申请的下载权限是否生效
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        assert_bool = apply_access_page.access_download_success_confirm()
        assert assert_bool is True

    @allure.title("素材列表批量操作申请编辑权限-我知道了")
    def test_access_batch_apply_edit_know(self, login_init):
        """
        素材列表批量操作申请编辑权限-我知道了
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.access_batch_apply_edit_know()
        assert True

    @allure.title("素材列表批量操作申请编辑权限-空判断")
    def test_access_batch_apply_edit_blank(self, login_init):
        """
        素材列表批量操作申请编辑权限-空判断
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.access_batch_apply_edit_blank()
        ele = apply_access_page.read_yaml_element("access_batch_edit_commit_blank")
        assert apply_access_page._text_content(ele) == "请输入所属部门及申请原因"

    @allure.title("素材列表批量操作申请编辑权限")
    def test_access_batch_apply_edit(self, login_init):
        """
        素材列表批量操作申请编辑权限
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        apply_access_page.access_batch_apply_edit()
        ele = apply_access_page.read_yaml_element("access_apply_success_assert")
        assert apply_access_page._text_content(ele) == "提交成功"

    @allure.title("审核编辑权限申请(素材列表)-通过")
    def test_edit_apply_audit_pass_1(self, login_sys):
        """
        审核编辑权限申请(素材列表)-通过
        @param login_sys:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_sys)
        apply_access_page.goto_asset()
        apply_access_page.download_apply_audit_pass()
        ele = apply_access_page.read_yaml_element("access_pass_toast")
        assert apply_access_page._text_content(ele) == "已通过此次申请"

    @allure.title("在素材列表页查看申请的编辑权限是否生效")
    def test_batch_apply_edit_success_confirm(self, login_init):
        """
        在素材列表页查看申请的编辑权限是否生效
        @param login_init:
        @return:
        """
        apply_access_page = ApplyForAccessPage(login_init)
        apply_access_page.goto_asset()
        assert_bool = apply_access_page.batch_apply_edit_success_confirm()
        assert assert_bool is True


if __name__ == '__main__':
    pytest.main(['-vs', 'test_upload_page.py::TestUploadAssetPage::test_upload_complete_delete_file'])
