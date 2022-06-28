#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_asset_group
# @Author: yanglun@tezign.com
# @Date  : 2022/2/14
# @Desc  :  素材组测试用例集
"""


import pytest
import allure
from pages.assets.AssetGroupPage import AssetGroupPage
from common.file_method import FileMethod
from conf.confs import baidu_transfer_link, baidu_transfer_password


class TestAssetGroup:
    """
    素材组测试类
    """

    @allure.title("素材组内-新建素材组")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("group_name", ['YL-UI自动化测试'])
    def test_group_new(self, group_name, login_sys):
        """
        测试新建素材组
        @param group_name:
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        # 进入素材组路由
        group_page.goto_group()
        # 新建素材组
        group_page.group_new(group_name)
        # 获取断言内容
        selector = group_page.read_yaml_element("group_all_bread_crumbs")
        assert group_page._text_content(selector).strip() == "全部"

    @allure.title("素材组内-进入素材组")
    def test_group_enter(self, login_sys):
        """
        进入素材组内
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        selector = group_page.read_yaml_element("group_all_bread_crumbs")
        assert group_page._text_content(selector).strip() == "全部"

    @allure.title("素材组内-订阅素材组")
    def test_group_subscribe(self, login_sys):
        """
        订阅素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_subscribe()
        ele = group_page.read_yaml_element("successful_subscribed_toast")
        assert group_page._text_content(ele) == "订阅成功，每周三10:00将邮件通知更新"

    @allure.title("素材组内-取消订阅素材组")
    def test_group_subscribe_cancel(self, login_sys):
        """
        取消订阅素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_subscribe_cancel()
        ele = group_page.read_yaml_element("cancle_subscribed_toast")
        assert group_page._text_content(ele) == "取消成功"

    @allure.title("素材组内-收藏素材组")
    def test_group_collect(self, login_sys):
        """
        测试收藏素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_collect()
        ele = group_page.read_yaml_element("successful_collected_toast")
        assert group_page._text_content(ele) == "你已成功收藏该素材组"

    @allure.title("素材组内-取消收藏素材组")
    def test_group_collect_cancel(self, login_sys):
        """
        测试取消收藏素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_collect_cancel()
        ele = group_page.read_yaml_element("cancle_collected_toast")
        assert group_page._text_content(ele) == "你已取消收藏该素材组"

    @allure.title("素材组内-编辑素材组")
    @pytest.mark.parametrize('text', ['杨伦-UI自动化测试-编辑'])
    def test_group_edit(self, text, login_sys):
        """
        测试素材组编辑信息
        @param text:
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_edit(text)
        ele = group_page.read_yaml_element("Crumb_level1")
        assert group_page._text_content(ele).strip() == text

    @allure.title("素材组内-上传文件")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试1.jpg')])
    def test_group_upload_file(self, login_sys, file_path):
        """
        素材组上传文件_右上角button
        @param login_sys:
        @param file_path:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_upload_file(file_path)
        ele = group_page.read_yaml_element("upload_successful_toast")
        assert ''.join(group_page._text_content(ele).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("素材组内-上传多个文件")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize('file_path', [[FileMethod().get_file_path('data/test_file', '', 'UI自动化测试2.jpg'),
                                            FileMethod().get_file_path('data/test_file', '', 'UI自动化测试3.jpg')]])
    def test_group_upload_multi_file(self, login_sys, file_path):
        """
        素材组上传文件_右上角button_多个素材上传
        @param login_sys:
        @param file_path:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_upload_file(file_path)
        ele = group_page.read_yaml_element("upload_successful_toast")
        assert ''.join(group_page._text_content(ele).split()) == "入库成功，共2项，请刷新页面后查看"

    # @pytest.mark.parametrize('folder_path', [upload_folder])
    # def test_group_upload_folder(self, login_sys, folder_path):
    #     """
    #     测试文件夹上传
    #     @param login_sys:
    #     @param folder_path:
    #     @return:
    #     """
    #     group_page = AssetGroupPage(login_sys)
    #     group_page.goto_group()
    #     group_page.group_enter()
    #     group_page.group_upload_folder(folder_path)

    @pytest.mark.parametrize('url,password', [[baidu_transfer_link, baidu_transfer_password]])
    def test_group_baidu_transfer(self, login_sys, url, password):
        """
        测试百度盘同步
        @param login_sys:
        @param url:
        @param password:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_baidu_transfer(url, password)
        selector = group_page.read_yaml_element("baidu_transfer_assert")
        assert "百度网盘导入" in group_page._text_content(selector)

    @allure.title("素材组内-从素材库添加素材")
    @pytest.mark.flaky(reruns=1)
    def test_add_from_asset_bank(self, login_sys):
        """
        从素材库添加素材
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.add_from_asset_bank()
        ele = group_page.read_yaml_element('add_successful_toast')
        assert group_page._text_content(ele) == "添加成功"

    @allure.title("素材组内-新建子素材组")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("sub_group_name", ['UI自动化测试-子素材组'])
    def test_sub_group_new(self, login_sys, sub_group_name):
        """
        新建子素材组
        @param login_sys:
        @param sub_group_name:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.sub_group_new(sub_group_name)
        ele = group_page.read_yaml_element("blank_tips")
        assert group_page._text_content(ele) == "暂无素材，你可以添加素材或新建子素材组"

    @allure.title("素材组内-子素材组上传素材")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize('file_path', [FileMethod().get_file_path('data/test_file', '', 'UI自动化测试4.jpg')])
    def test_sub_group_upload(self, login_sys, file_path):
        """
        子素材组上传素材
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_sub_enter()
        group_page.sub_group_upload_file(file_path)
        ele = group_page.read_yaml_element("upload_successful_toast")
        assert ''.join(group_page._text_content(ele).split()) == "入库成功，共1项，请刷新页面后查看"

    @allure.title("素材组内-素材组下载")
    def test_group_download(self, login_sys):
        """
        素材组下载
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_download()
        ele = group_page.read_yaml_element('download_assert')
        assert group_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组内-下载素材组及附件")
    def test_group_download_all(self, login_sys):
        """
        下载素材组及附件
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_download_all()
        ele = group_page.read_yaml_element('download_assert')
        assert group_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("素材组内-素材组分享")
    def test_group_share(self, login_sys):
        """
        素材组分享
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_share()
        ele = group_page.read_yaml_element("share_successful_toast")
        assert group_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"

    @allure.title("素材组内-右上角button分享")
    def test_group_share_button(self, login_sys):
        """
        素材组右上角button分享
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_share_button()
        ele = group_page.read_yaml_element("share_successful_toast")
        assert group_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"

    @allure.title("素材组内-二维码分享")
    def test_group_share_by_qr_code(self, login_sys):
        """
        素材组分享-二维码分享
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_share_by_qr_code()
        ele = group_page.read_yaml_element("share_successful_toast")
        assert group_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"

    @allure.title("素材组内-邮件分享")
    def test_group_share_by_email(self, login_sys):
        """
        素材组分享-邮件分享
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_share_by_email()
        ele = group_page.read_yaml_element("share_successful_toast")
        assert group_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"

    @allure.title("素材组内-分享设置")
    def test_group_share_set(self, login_sys):
        """
        素材组分享-分享设置
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_share_set()
        ele = group_page.read_yaml_element("share_successful_toast")
        assert group_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"

    @allure.title("素材组内-取消素材组分享")
    def test_group_share_cancel(self, login_sys):
        """
        取消素材组分享
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_share_cancel()
        assert True

    @allure.title("素材组内-分享记录")
    def test_sharing_records(self, login_sys):
        """
        素材组分享记录
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.sharing_records()
        ele = group_page.read_yaml_element("share_records_title")
        assert group_page._text_content(ele) == "分享记录"

    @allure.title("素材组内-搜索框输入内容搜索")
    @pytest.mark.parametrize('text', ['UI自动化测试'])
    def test_group_search_text(self, text, login_sys):
        """
        素材组下搜索框直接输入内容搜索
        @param text:
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_search_text(text)
        ele = group_page.read_yaml_element("search_result_level")
        assert "以下为搜索" in group_page._text_content(ele)

    @allure.title("素材组内-搜索框backspace删除输入内容")
    @pytest.mark.parametrize('text', ['UI自动化测试'])
    def test_group_search_backspace(self, text, login_sys):
        """
        素材组下模拟backspace删除输入内容
        @param text:
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_search_backspace(text)
        ele = group_page.read_yaml_element("search_result_level")
        assert "以下为搜索" in group_page._text_content(ele)

    @allure.title("素材组内-搜索框清空素材组搜索内容")
    @pytest.mark.parametrize('text', ['UI自动化测试'])
    def test_group_search_clear(self, text, login_sys):
        """
        素材组下模拟清空素材组搜索输入框
        @param text:
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_search_clear(text)
        ele = group_page.read_yaml_element("search_in_group")
        assert group_page._text_content(ele) == ''

    @allure.title("筛选-我创建的素材")
    def test_group_filter_my_created(self, login_sys):
        """
        素材组筛选-我创建的素材
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_filter_my_created()
        ele = group_page.read_yaml_element("filter_mycreated_checkbox")
        assert group_page._is_check(ele)

    @allure.title("筛选-筛选部门")
    @pytest.mark.parametrize("text", ['内容基建UI自动化测试'])
    def test_group_filter_dept(self, login_sys, text):
        """
        素材组筛选-筛选部门
        @param login_sys:
        @param text:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_filter_dept(text)
        ele = group_page.read_yaml_element("assert_filter_dept")
        assert "内容基建UI自动化测试" in group_page._text_content(ele)

    @allure.title("筛选-文件格式-JPG")
    def test_group_filter_file_format(self, login_sys):
        """
        素材组筛选-文件格式-JPG
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_filter_file_format()
        ele = group_page.read_yaml_element("filter_JPG")
        assert group_page._is_check(ele)

    @allure.title("筛选-创建时间")
    @pytest.mark.flaky(reruns=1)
    def test_group_filter_create_time(self, login_sys):
        """
        素材组筛选-创建时间
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_filter_create_time()
        ele = group_page.read_yaml_element("filter_create_time")
        assert "创建时间:" in group_page._text_content(ele)

    @allure.title("筛选-清空筛选")
    @pytest.mark.flaky(reruns=1)
    def test_group_filter_clear(self, login_sys):
        """
        筛选-清空筛选
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_filter_clear()
        ele = group_page.read_yaml_element("filter_mycreated_dropdown")
        assert group_page._text_content(ele) == "创建者/创建部门"

    @allure.title("筛选列表-收起展开")
    def test_group_filter_list(self, login_sys):
        """
        素材组筛选列表-收起展开
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        if group_page.group_filter_list() is None:
            ele = group_page.read_yaml_element("filter_fold")
            assert group_page._text_content(ele) == "收起"
        else:
            pytest.skip("Too few filters！")

    @allure.title("批量操作-打包下载素材")
    def test_group_batch_download(self, login_sys):
        """
        素材组批量操作-打包下载素材
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_download()
        ele = group_page.read_yaml_element("download_assert")
        assert group_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("批量操作-打包下载素材及附件")
    def test_group_batch_download_all(self, login_sys):
        """
        素材组批量操作-打包下载素材及附件
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_download_all()
        ele = group_page.read_yaml_element("download_assert")
        assert group_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("批量操作-打包下载指定尺寸素材")
    @pytest.mark.parametrize("size", ['50'])
    def test_group_batch_download_specify_size(self, login_sys, size):
        """
        素材组批量操作-打包下载指定尺寸素材
        @param size:
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_download_specify_size(size)
        ele = group_page.read_yaml_element("download_size_assert")
        assert group_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("批量操作-分享素材")
    def test_group_batch_share(self, login_sys):
        """
        素材组批量操作-分享素材
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_share()
        ele = group_page.read_yaml_element("batch_link_successful_toast")
        assert group_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"

    @allure.title("批量操作-编辑")
    def test_group_batch_edit(self, login_sys):
        """
        素材组批量操作-编辑
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_edit()
        ele = group_page.read_yaml_element("edit_save_successful_toast")
        assert group_page._text_content(ele) == "保存成功"

    @allure.title("批量操作-高级重命名")
    def test_group_batch_rename(self, login_sys):
        """
        素材组批量操作-高级重命名
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_rename()
        ele = group_page.read_yaml_element("rename_successful_toast")
        assert group_page._text_content(ele) == "重命名成功"

    @allure.title("批量操作-加入素材篮")
    def test_group_batch_add_basket(self, login_sys):
        """
        素材组批量操作-加入素材篮
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_add_basket()
        ele = group_page.read_yaml_element("add_basket_successful")
        assert group_page._text_content(ele) == "已成功加入素材篮"

    @allure.title("批量操作-二次加入素材篮")
    def test_group_batch_add_basket_again(self, login_sys):
        """
        素材组批量操作-二次加入素材篮
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_add_basket_again()
        ele = group_page.read_yaml_element("add_basket_again")
        assert group_page._text_content(ele) == "该素材已存在于素材篮"

    @allure.title("批量操作-复制素材组到列表第一个素材组下")
    def test_group_batch_copy(self, login_sys):
        """
        素材组批量操作-复制素材组到列表第一个素材组下
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_copy()
        ele = group_page.read_yaml_element("copy_successful")
        assert group_page._text_content(ele) == "已复制成功"

    @allure.title("批量操作-赋权给组内成员")
    def test_group_batch_empowerment(self, login_sys):
        """
        素材组批量操作-赋权给组内成员
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_empowerment()
        ele = group_page.read_yaml_element("empowerment_sucess_toast")
        assert group_page._text_content(ele) == "已成功赋权给组内成员"

    @allure.title("批量操作-修改素材组内素材权限类型")
    def test_group_batch_permission(self, login_sys):
        """
        素材组批量操作-修改素材组内素材权限类型
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_permission()
        ele = group_page.read_yaml_element("permission_sucess_toast")
        assert group_page._text_content(ele) == "已成功修改素材权限类型"

    @allure.title("批量操作-关闭批量操作组件")
    def test_group_batch_close(self, login_sys):
        """
        素材组批量操作-关闭批量操作组件
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_batch_close()
        ele = group_page.read_yaml_element("all_checkbox")
        assert group_page._is_check(ele) is False

    @allure.title("素材组下-素材组列表视图")
    def test_group_list_view(self, login_sys):
        """
        素材组下-素材组列表视图
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_list_view()
        ele = group_page.read_yaml_element("group_list_view_group")
        assert "素材组" in group_page._text_content(ele)

    @allure.title("列表视图下-切换至素材组tab")
    def test_group_list_to_group_tab(self, login_sys):
        """
        素材组列表视图下-切换至素材组tab
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter_list()
        group_page.group_list_to_group_tab()
        ele = group_page.read_yaml_element("group_list_view_group")
        assert "素材组" in group_page._text_content(ele)

    @allure.title("列表视图下-切换至素材tab")
    def test_group_list_to_asset_tab(self, login_sys):
        """
        素材组列表视图下-切换至素材tab
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter_list()
        group_page.group_list_to_asset_tab()
        ele = group_page.read_yaml_element("group_list_view_asset")
        assert "素材" in group_page._text_content(ele)

    @allure.title("素材组下-素材组平铺视图")
    @pytest.mark.flaky(reruns=1)
    def test_group_view_tile(self, login_sys):
        """
        素材组下-素材组平铺视图
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter_list()
        group_page.group_tile_view()
        ele = group_page.read_yaml_element("enter_second_collection")
        assert group_page._text_content(ele) != ''

    @allure.title("素材组下-素材组多维视图")
    @pytest.mark.flaky(reruns=1)
    def test_group_kanban_view(self, login_sys):
        """
        素材组下-素材组多维视图
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_kanban_view()
        ele = group_page.read_yaml_element("kanban_text")
        assert group_page._text_content(ele) == "素材组"

    @allure.title("素材组下-排序")
    @pytest.mark.flaky(reruns=1)
    def test_group_sort(self, login_sys):
        """
        素材组下排序
        @param login_sys:
        @return:
        """
        sort_dict = {
            'sort_recent': '最近打开',
            'sort_asset_hot': '素材热度',
            'sort_history_hot': '历史总活跃',
            'sort_name': '名称排序',
            'sort_create_time': '创建时间',
            'sort_update_time': '更新时间',
        }
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        for key, value in sort_dict.items():
            selector = group_page.read_yaml_element(key)
            group_page.group_sort(selector)
            ele = group_page.read_yaml_element("sort_text")
            assert group_page._text_content(ele) == value

    @allure.title("素材组下-排序升序")
    def test_group_asc(self, login_sys):
        """
        排序升序
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_group_asc()
        assert True

    @allure.title("素材组下-排序降序")
    def test_group_desc(self, login_sys):
        """
        排序降序
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_group_asc()
        assert True

    @allure.title("素材组移动-取消移动")
    def test_group_move_cancel(self, login_sys):
        """
        素材组移动-取消移动
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_move_cancel()
        assert True

    @allure.title("素材组移动-移动素材组到全部下")
    def test_group_move_to_all(self, login_sys):
        """
        素材组移动-移动素材组到全部下
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_move_to_all()
        ele = group_page.read_yaml_element("move_successful_toast")
        assert group_page._text_content(ele) == "操作成功"

    @allure.title("素材组下-取消复制素材组")
    def test_group_copy_cancel(self, login_sys):
        """
        取消复制素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_copy_cancel()
        assert True

    @allure.title("素材组下-复制素材组至全部下")
    def test_group_copy_to_all(self, login_sys):
        """
        复制素材组至全部下
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_copy_to_all()
        ele = group_page.read_yaml_element('copy_successful_toast')
        assert group_page._text_content(ele) == "已复制成功"

    @allure.title("素材组下-删除复制生成的素材组")
    def test_copy_delete(self, login_sys):
        """
        删除复制生成的素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_delete()
        ele = group_page.read_yaml_element('successful_deleted_toast')
        assert "已删除" in group_page._text_content(ele).strip()

    @allure.title("素材组下-复制素材组至新建素材组")
    @pytest.mark.parametrize('text', ['UI自动化-复制'])
    def test_group_copy_to_new(self, login_sys, text):
        """
        复制素材组至新建素材组
        @param login_sys:
        @param text:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_copy_to_new(text)
        ele = group_page.read_yaml_element('copy_successful_toast')
        assert group_page._text_content(ele) == "已复制成功"

    @allure.title("素材组下-删除新建生成的素材组")
    def test_copy_delete_new(self, login_sys):
        """
        删除新建生成的素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_delete()
        ele = group_page.read_yaml_element('successful_deleted_toast')
        assert "已删除" in group_page._text_content(ele).strip()

    # @allure.title("批量操作-移动素材组到自身")
    # def test_group_batch_move(self, login_sys):
    #     """
    #     批量操作-移动素材组到自身
    #     @param login_sys:
    #     @return:
    #     """
    #     group_page = AssetGroupPage(login_sys)
    #     group_page.goto_group()
    #     group_page.group_enter()
    #     group_page.group_batch_move()
    #     ele = group_page.read_yaml_element("batch_move_successful")
    #     assert group_page._text_content(ele) == "移动成功"

    @pytest.mark.flaky(reruns=1)
    @allure.title("批量操作-修改所有者")
    @pytest.mark.parametrize("text", ['杨伦'])
    def test_group_change_owner(self, login_sys, text):
        """
        素材组批量操作-修改所有者
        @param login_sys:
        @param text:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_change_owner(text)
        ele = group_page.read_yaml_element("owner_successful_toast")
        assert group_page._text_content(ele) == "已成功修改素材所有者为 杨伦 ，系统将会发送通知给原素材所有者及 杨伦"

    @allure.title("批量操作-移除/删除素材/素材组")
    def test_group_remove_asset(self, login_sys):
        """
        素材组批量操作-移除/删除素材/素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_remove_asset()
        ele = group_page.read_yaml_element("blank_tips")
        assert group_page._text_content(ele) == "暂无素材，你可以添加素材或新建子素材组"

    @allure.title("素材组下-取消素材组删除")
    def test_group_delete_cancel(self, login_sys):
        """
        测试取消素材组删除
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_url_last = group_page._get_url()
        group_page.group_delete_cancel()
        group_url_now = group_page._get_url()
        assert group_url_last == group_url_now

    @allure.title("素材组下-删除素材组")
    def test_group_delete(self, login_sys):
        """
        测试删除素材组
        @param login_sys:
        @return:
        """
        group_page = AssetGroupPage(login_sys)
        group_page.goto_group()
        group_page.group_enter()
        group_page.group_delete()
        ele = group_page.read_yaml_element('successful_deleted_toast')
        assert "已删除" in group_page._text_content(ele).strip()


if __name__ == '__main__':
    pytest.main(['-vs', 'test_asset_group.py::TestAssetGroup::test_group_remove_asset'])





























