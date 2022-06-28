# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/4/29 2:20 下午
# @File:DashboardPage.py
from pages.basepage import BasePage
from conf.confs import url_dashboard


class DashboardPage(BasePage):
    """
    统计的页面
    """
    def goto_dashboard_use(self):
        """
        进入统计页面默认路径-素材使用页面
        @return:
        """
        self._go(url_dashboard)
        self._wait(4)

    def dashboard_asset_ranking(self):
        """
        切换素材排行tab页
        @return:
        """
        selector = self.read_yaml_element("asset_ranking")
        self._click(selector)
        self._wait(2)

    def dashboard_user_ranking(self):
        """
        切换用户排行tab页
        @return:
        """
        selector = self.read_yaml_element("user_ranking")
        self._wait(2)
        self._click(selector)
        self._wait(2)

    def dashboard_export(self):
        """
        切换导出列表tab页
        @return:
        """
        selector = self.read_yaml_element("export_list")
        self._click(selector)
