# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/4/29 3:01 下午
# @File:test_dashboard_page.py
from pages.assets.DashboardPage import DashboardPage


class TestDashboard:
    def test_dashboard_page(self, login_i):
        """
        进入统计默认页面-素材使用页面
        @param login_i:
        @return:
        """
        dashboard_page = DashboardPage(login_i)
        dashboard_page.goto_dashboard_use()
        ele = dashboard_page.read_yaml_element("asset_user_title")
        dashboard_page._wait_for_selector(ele)
        assert dashboard_page._text_content(ele) == '数据总览'

    def test_dashboard_asset_ranking(self, login_i):
        """
        进入统计默认页面-素材排行页面
        @param login_i:
        @return:
        """
        dashboard_page = DashboardPage(login_i)
        dashboard_page.goto_dashboard_use()
        dashboard_page.dashboard_asset_ranking()
        ele = dashboard_page.read_yaml_element("asset_ranking_title")
        dashboard_page._wait_for_selector(ele)
        assert dashboard_page._text_content(ele) == '素材分类排行榜'

    def test_dashboard_user_ranking(self, login_i):
        """
        进入统计默认页面-用户排行页面
        @param login_i:
        @return:
        """
        dashboard_page = DashboardPage(login_i)
        dashboard_page.goto_dashboard_use()
        dashboard_page.dashboard_user_ranking()
        ele = dashboard_page.read_yaml_element("user_ranking_title")
        dashboard_page._wait_for_selector(ele)
        assert dashboard_page._text_content(ele) == '用户分类排行榜'

    def test_dashboard_export_list(self, login_i):
        """
        进入统计默认页面-用户排行页面
        @param login_i:
        @return:
        """
        dashboard_page = DashboardPage(login_i)
        dashboard_page.goto_dashboard_use()
        dashboard_page.dashboard_export()
        ele = dashboard_page.read_yaml_element("export_list_title")
        dashboard_page._wait_for_selector(ele)
        assert dashboard_page._text_content(ele) == '导出历史'
