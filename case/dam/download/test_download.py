#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_download
# @Author: yanglun@tezign.com
# @Date  : 2022/5/6
# @Desc  :
"""

import pytest
import allure
from pages.assets.DownloadPage import DownloadPage
from common.file_method import FileMethod


class TestDownloadPage:
    """
    下载流程
    """

    @allure.title("树结构下载-素材申请权限")
    def test_tree_download_apply_access(self, login_sys):
        """
        树结构下载素材申请权限
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_tree_download_asset()
        download_page.download_apply_access()
        ele = download_page.read_yaml_element("download_apply_success")
        assert download_page._text_content(ele) == "申请已提交成功，审核结果会通过邮件发送给你"

    @allure.title("树结构下载-取消下载素材")
    def test_download_asset_cancel(self, login_sys):
        """
        取消下载素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_tree_download_asset()
        download_page.download_asset_cancel()
        ele = download_page.read_yaml_element("download_button")
        assert download_page._is_visible(ele) is False

    @allure.title("树结构-直接下载正常素材")
    def test_download_tree_normal_asset(self, login_sys):
        """
        树结构-直接下载正常素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_tree_download_asset()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("树结构-下载所有可下载素材")
    def test_download_tree_all_can(self, login_sys):
        """
        树结构-下载所有可下载素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_tree_download_asset()
        download_page.download_all_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("树结构-下载素材及附件")
    def test_download_tree_all_can(self, login_sys):
        """
        树结构-树结构-下载素材及附件
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_tree_download_all()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("不可下载校验")
    def test_download_can_not(self, login_sys):
        """
        不可下载校验
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_tree_download_asset()
        ele = download_page.read_yaml_element("download_can_not_tips")
        assert download_page._text_content(ele) == "不可下载"

    @allure.title("右键-直接下载正常素材")
    def test_download_right_normal_asset(self, login_sys):
        """
        右键-直接下载正常素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_right_download()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("右键-下载所有可下载素材")
    def test_download_right_all_can(self, login_sys):
        """
        右键-下载所有可下载素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_right_download()
        download_page.download_all_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("右键-下载素材及附件")
    def test_download_right_download_all(self, login_sys):
        """
        右键-下载素材及附件
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_right_download_all()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组内more-素材申请权限")
    def test_download_more_apply_access(self, login_sys):
        """
        素材组内more-素材申请权限
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_more_download()
        download_page.download_apply_access()
        ele = download_page.read_yaml_element("download_apply_success")
        assert download_page._text_content(ele) == "申请已提交成功，审核结果会通过邮件发送给你"

    @allure.title("素材组内more-下载正常素材")
    def test_download_more_normal(self, login_sys):
        """
        素材组内more-下载正常素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_more_download()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组内more-下载全部可下载素材")
    def test_download_more_all_can(self, login_sys):
        """
        素材组内more-下载全部可下载素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_more_download()
        download_page.download_all_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组内more-下载素材及附件")
    def test_download_more_all_asset(self, login_sys):
        """
        素材组内more-下载素材及附件
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_more_download_all()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组内批量操作-素材申请权限")
    def test_download_batch_apply_access(self, login_sys):
        """
        素材组内批量操作-素材申请权限
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_batch_download_asset()
        download_page.download_apply_access()
        ele = download_page.read_yaml_element("download_apply_success")
        assert download_page._text_content(ele) == "申请已提交成功，审核结果会通过邮件发送给你"

    @allure.title("素材组内批量操作-下载正常素材")
    def test_download_batch_normal(self, login_sys):
        """
        素材组内批量操作-下载正常素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_batch_download_asset()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组内批量操作-下载全部可下载素材")
    def test_download_batch_all_can(self, login_sys):
        """
        素材组内more-下载全部可下载素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_batch_download_asset()
        download_page.download_all_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组内批量操作-下载素材及附件")
    def test_download_batch_all_asset(self, login_sys):
        """
        素材组内批量操作-下载素材及附件
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_batch_download_all()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组-批量操作下载指定尺寸和大小")
    def test_download_batch_specify(self, login_sys):
        """
        素材组-批量操作下载指定尺寸和大小
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_batch_specify()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组-批量操作下载空素材组")
    def test_download_batch_blank_group(self, login_sys):
        """
        素材组-批量操作下载空素材组
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_batch_blank_group()
        ele = download_page.read_yaml_element("download_blank_toast")
        assert download_page._text_content(ele) == "当前选中了0个素材，请重新选择"

    @allure.title("素材组-批量操作下载子素材组")
    def test_download_batch_sub_group(self, login_sys):
        """
        素材组-批量操作下载子素材组
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_batch_sub_group()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组-批量操作下载单个未生效素材")
    def test_download_batch_single_asset(self, login_sys):
        """
        素材组-批量操作下载单个未生效素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset_group()
        download_page.download_enter_group()
        download_page.download_batch_single_asset()
        download_page.download_all_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._is_visible(ele) is False

    @allure.title("素材列表批量操作-下载正常素材")
    def test_download_batch_normal(self, login_sys):
        """
        素材列表批量操作-下载正常素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset()
        download_page.download_filter_my_create()
        download_page.download_list_batch_asset()
        download_page.download_normal_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材列表批量操作-下载所有能下载素材")
    def test_download_batch_all_can(self, login_sys):
        """
        素材列表批量操作-下载所有能下载素材
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset()
        download_page.download_filter_my_create()
        download_page.download_list_batch_asset()
        download_page.download_all_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材列表-批量操作下载素材及附件")
    def test_download_list_batch_all(self, login_sys):
        """
        素材列表-批量操作下载素材及附件
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset()
        download_page.download_filter_my_create()
        download_page.download_list_batch_all()
        download_page.download_all_asset()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材列表-批量操作下载指定尺寸和大小")
    def test_download_list_batch_specify(self, login_sys):
        """
        素材列表-批量操作下载指定尺寸和大小
        @param login_sys:
        @return:
        """
        download_page = DownloadPage(login_sys)
        download_page.goto_asset()
        download_page.download_filter_my_create()
        download_page.download_list_batch_specify()
        ele = download_page.read_yaml_element("tree_download_assert")
        assert download_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    # @pytest.skip()
    # @allure.title("素材列表-右键下载单个正常素材")
    # def test_download_list_right_normal(self, login_sys):
    #     """
    #     素材列表-右键下载单个正常素材
    #     @param login_sys:
    #     @return:
    #     """
    #     download_page = DownloadPage(login_sys)
    #     download_page.goto_asset()
    #     download_page.download_filter_my_create()
    #     bool_assert = download_page.download_list_right_normal()
    #     assert bool_assert is True

    # @pytest.mark.flaky(reruns=1)
    # @allure.title("素材列表-右键下载单个未生效素材")
    # def test_download_single_url_asset(self, login_sys):
    #     """
    #     素材列表-右键下载单个未生效素材
    #     @param login_sys:
    #     @return:
    #     """
    #     download_page = DownloadPage(login_sys)
    #     download_page.goto_asset()
    #     download_page.download_filter_my_create()
    #     download_page.download_single_url_asset()
    #     download_page.download_all_asset()
    #     assert True






