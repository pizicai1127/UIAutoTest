# -*- coding: utf-8 -*- 
# @Time : 2022/2/9 6:09 下午 
# @Author : liuzhijie/ruiyin
# @File : MyCooperationPage.py

from pages.basepage import BasePage
from conf.confs import url_myCooperationPage


class MyCooperationPage(BasePage):
    def goto_cooperation(self):
        """
        跳转到全部素材组-与我协作的页面下
        @rtype: object
        """
        self._go(url_myCooperationPage)
        self._wait(1.5)

    # 搜索
    def cooperation_search(self, text):
        # 输入搜索的素材组名或素材
        selector = self.read_yaml_element("cooperation_search_input")  # 输入框填入text
        self._fill(selector, text)
        self._keyboard_click('Enter')  # 按下"回车"键

    # 排序
    def cooperation_sort(self, selector):
        selector1 = self.read_yaml_element("cooperation_sort")  # hover排序组件
        self._hover(selector1)
        self._click(selector)

    # 素材组排列方式-平铺
    def cooperation_arrangement_tile_mode(self):
        selector = self.read_yaml_element("cooperation_tile_mode")
        self._click(selector)

    # 列表模式排列
    def cooperation_arrangement_list_mode(self):
        selector = self.read_yaml_element("cooperation_list_mode")
        self._click(selector)

    # 平铺模式进入第一个素材组
    def cooperation_in_group(self):
        selector1 = self.read_yaml_element("cooperation_in_group")
        self._click(selector1)

    # 收藏
    def cooperation_collect(self):
        selector = self.read_yaml_element("cooperation_collect")
        self._hover(selector)
        selector1 = self.read_yaml_element("cooperation_collect_click")
        self._click(selector1)

    # 列表模式-进入素材组中第一个素材/素材组
    def cooperation_Lgroup(self):
        selector = self.read_yaml_element("cooperation_list_first_group")
        self._click(selector)
