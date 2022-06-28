#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : test_sharing_page
# @Author: yanglun@tezign.com
# @Date  : 2022/4/10
# @Desc  :  
"""


import pytest
import allure
from pages.assets.ShareLandingPage import ShareLandingPage


class TestShareLandingPage:
    """
    分享落地页
    """

    @allure.title("分享素材组-游客可下载")
    @pytest.mark.flaky(reruns=1)
    def test_share_visitor_can_download(self, login_sys, new_browser_context):
        """
        分享素材组-游客可下载
        @param login_sys:
        @return:
        """
        share_page = ShareLandingPage(login_sys)
        share_page.goto_group()
        url = share_page.share_visitor_can_download()
        new_browser_context.goto(url)
        text1 = new_browser_context.text_content("text=下载")
        text2 = new_browser_context.text_content("text=登录")
        assert text1 == "下载" and text2 == "登录"

    @allure.title("分享素材组-游客可查看")
    @pytest.mark.flaky(reruns=1)
    def test_share_visitor_only_view(self, login_sys, new_browser_context):
        """
        分享素材组-游客可查看
        @param login_sys:
        @return:
        """
        share_page = ShareLandingPage(login_sys)
        share_page.goto_group()
        url = share_page.share_visitor_only_view()
        new_browser_context.goto(url)
        assert new_browser_context.is_visible("text=下载") is False

    @allure.title("分享素材组-系统内部用户可下载")
    @pytest.mark.flaky(reruns=1)
    def test_share_internal_can_download(self, login_sys, new_browser_context):
        """
        分享素材组-系统内部用户可下载
        @param login_sys:
        @return:
        """
        share_page = ShareLandingPage(login_sys)
        share_page.goto_group()
        url = share_page.share_internal_can_download()
        new_browser_context.goto(url)
        new_browser_context.click("[class='tz-btn type-primary shape-round']")
        new_browser_context.click("[placeholder=\"邮箱/手机\"]")
        new_browser_context.fill("[placeholder=\"邮箱/手机\"]", "yanglun@tezign.com")
        new_browser_context.click("[placeholder=\"密码\"]")
        new_browser_context.fill("[placeholder=\"密码\"]", "qq111111")
        new_browser_context.check("input[type=\"checkbox\"]")
        new_browser_context.click("button:has-text(\"登录\")")
        text = new_browser_context.text_content("text=下载")
        assert text == "下载"

    @allure.title("分享素材组-系统内部用户可查看")
    @pytest.mark.flaky(reruns=1)
    def test_share_internal_only_view(self, login_sys, new_browser_context):
        """
        分享素材组-系统内部用户可查看
        @param login_sys:
        @return:
        """
        share_page = ShareLandingPage(login_sys)
        share_page.goto_group()
        url = share_page.share_internal_only_view()
        new_browser_context.goto(url)
        new_browser_context.click("[class='tz-btn type-primary shape-round']")
        new_browser_context.click("[placeholder=\"邮箱/手机\"]")
        new_browser_context.fill("[placeholder=\"邮箱/手机\"]", "yanglun@tezign.com")
        new_browser_context.click("[placeholder=\"密码\"]")
        new_browser_context.fill("[placeholder=\"密码\"]", "qq111111")
        new_browser_context.check("input[type=\"checkbox\"]")
        new_browser_context.click("button:has-text(\"登录\")")
        assert new_browser_context.is_visible("text=下载") is False

    @allure.title("分享落地页-打包下载素材")
    def test_share_page_download(self, new_browser_context):
        """
        分享落地页-打包下载素材
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_download()
        ele = share_page.read_yaml_element("share_download_assert")
        assert share_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("分享落地页-切换多维视图")
    def test_share_page_switch_view(self, new_browser_context):
        """
        分享落地页-切换多维视图
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_switch_view()
        ele = share_page.read_yaml_element("kanban_view_assert")
        assert share_page._text_content(ele) == "素材组"

    @allure.title("分享落地页-素材组排序")
    def test_share_page_sort(self, new_browser_context):
        """
        分享落地页-素材组排序
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_sort()
        ele = share_page.read_yaml_element("share_sort_text")
        assert share_page._text_content(ele) == "创建时间"

    @allure.title("分享落地页-素材组升降序")
    def test_share_page_asc_desc(self, new_browser_context):
        """
        分享落地页-素材组升降序
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_asc_desc()
        assert True

    @allure.title("分享落地页-格式筛选")
    def test_share_page_format_filter(self, new_browser_context):
        """
        分享落地页-格式筛选
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_format_filter()
        ele = share_page.read_yaml_element("format_filter_assert")
        assert "JPG,JPEG,PNG,TIF,TIFF,GIF,SVG,BMP,HEIC,PIC" in share_page._text_content(ele)

    @allure.title("分享落地页-创建时间筛选")
    def test_share_page_create_time_filter(self, new_browser_context):
        """
        分享落地页-创建时间筛选
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_create_time_filter()
        assert share_page._text_content('text=下载') == "下载"

    @allure.title("分享落地页-搜索素材/素材组")
    def test_share_page_search_asset(self, new_browser_context):
        """
        分享落地页-搜索素材/素材组
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_search_asset()
        ele = share_page.read_yaml_element("share_sort_text")
        assert share_page._text_content(ele) == "综合排序"

    @allure.title("分享落地页-搜索后筛选")
    def test_share_page_search_and_filter(self, new_browser_context):
        """
        分享落地页-搜索后筛选
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_search_and_filter()
        ele = share_page.read_yaml_element("search_asset_assert")
        assert "素材" in share_page._text_content(ele)

    @allure.title("分享落地页-进入素材详情页")
    @pytest.mark.flaky(reruns=1)
    def test_share_page_asset_detail(self, new_browser_context):
        """
        分享落地页-进入素材详情页
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_asset_detail()
        ele = share_page.read_yaml_element("asset_detail_assert")
        assert share_page._text_content(ele) == "详情"

    @allure.title("分享落地页-关闭素材详情页弹窗")
    def test_share_page_asset_detail_close(self, new_browser_context):
        """
        分享落地页-关闭素材详情页弹窗
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_asset_detail_close()
        ele = share_page.read_yaml_element("share_page_download")
        assert share_page._text_content(ele) == "下载"

    @allure.title("分享落地页-详情页下载素材")
    def test_share_page_asset_detail_download(self, new_browser_context):
        """
        分享落地页-详情页下载素材
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_asset_detail_download()
        assert True

    @allure.title("素材详情页tab切换")
    def test_share_page_comment_tab(self, new_browser_context):
        """
        分享落地页-素材详情页tab切换
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_comment_tab()
        ele = share_page.read_yaml_element("no_comment_assert")
        assert share_page._text_content(ele) == "暂无评论"

    @allure.title("素材详情页-评论tab登录")
    def test_share_page_comment_tab_login(self, new_browser_context):
        """
        分享落地页-素材详情页-评论tab登录
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        ele = share_page.share_page_comment_tab_login()
        assert share_page._text_content(ele) != ""

    @allure.title("素材详情页-切换素材")
    def test_share_page_next_asset(self, new_browser_context):
        """
        分享落地页-素材详情页-切换素材
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_page_next_asset()
        assert True

    @allure.title("批量操作-下载全选素材")
    def test_share_batch_all_download(self, new_browser_context):
        """
        分享落地页-批量操作-下载全选素材
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_batch_all_download()
        ele = share_page.read_yaml_element("share_download_assert")
        assert share_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("批量操作-下载单个素材组")
    def test_share_batch_download_group(self, new_browser_context):
        """
        分享落地页-批量操作-下载单个素材组
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_batch_download_group()
        ele = share_page.read_yaml_element("share_download_assert")
        assert share_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("批量操作-下载空素材组")
    def test_share_batch_download_blank_group(self, new_browser_context):
        """
        分享落地页-批量操作-下载空素材组
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_batch_download_blank_group()
        ele = share_page.read_yaml_element("download_blank_assert")
        assert share_page._text_content(ele) == "当前选中了0个素材，请重新选择"

    @allure.title("批量操作-下载单个素材")
    def test_share_batch_download_asset(self, new_browser_context):
        """
        分享落地页-批量操作-下载单个素材
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_batch_download_asset()
        assert True

    @allure.title("筛选后批量操作打包下载素材")
    def test_share_filter_batch_download(self, new_browser_context):
        """
        分享落地页-筛选后批量操作打包下载素材
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_filter_batch_download()
        ele = share_page.read_yaml_element("share_download_assert")
        assert share_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("搜索后批量操作打包下载素材")
    def test_share_search_batch_download(self, new_browser_context):
        """
        分享落地页-搜索后批量操作打包下载素材
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_search_batch_download()
        ele = share_page.read_yaml_element("share_download_assert")
        assert share_page._text_content(ele) == "等待过程中您可以打开新窗口继续工作"

    @allure.title("分享落地页-进入子素材组")
    def test_share_enter_sub_group(self, new_browser_context):
        """
        分享落地页-进入子素材组
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_enter_sub_group()
        ele = share_page.read_yaml_element("share_second_level")
        assert share_page._text_content(ele) != ""

    @allure.title("分享落地页-面包屑切换层级")
    def test_share_bread_crumbs(self, new_browser_context):
        """
        分享落地页-面包屑切换层级
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        share_page.share_bread_crumbs()
        ele = share_page.read_yaml_element("bread_crumbs_assert")
        assert share_page._text_content(ele) == "分享落地页测试-石明（勿删除）"

    @allure.title("分享落地页-游客页面跳转登录")
    def test_share_visitor_login(self, new_browser_context):
        """
        分享落地页-游客页面跳转登录
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        ele = share_page.share_visitor_login()
        assert share_page._text_content(ele) != ""

    @allure.title("分享落地页-国际化切换")
    def test_share_globalization(self, new_browser_context):
        """
        分享落地页-国际化切换
        @param new_browser_context:
        @return:
        """
        share_page = ShareLandingPage(new_browser_context)
        text = share_page.share_globalization()
        assert text == "Bulk Selection"


if __name__ == '__main__':
    pytest.main(['-vs', 'test_sharing_page.py::TestShareLandingPage::test_share_page_asc_desc'])
