# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/4/27 5:03 下午
# @File:LogHistoryPage.py
from pages.basepage import BasePage
from conf.confs import url_log_history


class LogHistoryPage(BasePage):
    """
    用户动态
    """
    def goto_log_history(self):
        """
        跳转到用户动态页面
        @rtype: object
        """
        self._go(url_log_history)
        self._wait(1.5)

    def log_history_search(self):
        """
        搜索用户动态
        @return:
        """
        selector = self.read_yaml_element("log_history_search_input")
        self._click(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("log_history_input_user")
        self._click(selector1)
        # self._wait(2)

    def log_history_modular(self, selector):
        """
        按模块筛选
        @param selector:
        @return:
        """
        selector1 = self.read_yaml_element("log_modular_sort")  # hover排序组件
        self._hover(selector1)
        # self._wait(2)
        self._check(selector)
        # self._wait(2)

    def log_history_time(self, selector):
        """
        按时间范围筛选
        @param selector:
        @return:
        """
        selector1 = self.read_yaml_element("log_time_sort")  # hover排序组件
        self._wait_for_selector(selector1)
        self._hover(selector1)
        # self._wait(2)
        self._click(selector)
        # self._wait(2)









