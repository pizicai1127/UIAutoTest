# -*- coding: utf-8 -*- 
# @Time : 2022/2/9 6:06 下午 
# @Author : liuzhijie/ruiyin
# @File : MyCreaterPage.py

from pages.basepage import BasePage
from conf.confs import url_myCreatedPage


class MyCreatedPage(BasePage):
    def goto_created(self):
        """
        跳转到全部素材组-我创建的页面下
        @rtype: object
        """
        self._go(url_myCreatedPage)
        self._wait(1)

    def created_group(self, text):
        """
        新建素材组
        @rtype: object
        """
        selector1 = self.read_yaml_element("created_group_button")  # 点击新建素材组按钮
        self._click(selector1)
        selector2 = self.read_yaml_element("created_group_name_input")  # 输入素材组的名称
        self._fill(selector2, text)
        selector3 = self.read_yaml_element("created_group_desc_input")  # 输入素材组的描述
        self._fill(selector3, text)
        selector4 = self.read_yaml_element("created_group_confirm_button")  # 点击确定按钮
        self._click(selector4)

    def created_ingroup(self):
        """
        进入第一个素材组
        @rtype: object
        """
        selector1 = self.read_yaml_element("created_in_group")
        self._click(selector1)

    def created_group_delete(self):
        """
        删除素材组
        @rtype: object
        """
        # hover操作
        selector1 = self.read_yaml_element("created_more")
        self._hover(selector1)
        # 点击删除素材组按钮
        selector2 = self.read_yaml_element("created_delete_group")
        self._click(selector2)
        # 点击确定删除按钮
        selector3 = self.read_yaml_element("created_delete_group_yes")
        self._click(selector3)

    # 搜索
    def created_search(self, text):
        # 输入搜索的素材组名或素材
        selector = self.read_yaml_element("created_search_input")  # 输入框填入text
        self._fill(selector, text)
        self._keyboard_click('Enter')  # 按下"回车"键

    # 排序
    def created_sort(self,selector):
        selector1 = self.read_yaml_element("created_sort")  # hover排序组件
        self._hover(selector1)
        # tmp = self._input_sort(text)
        # selector = self.read_yaml_element("created_sort_button")  # 点击要测试的排序方式
        self._click(selector)

    # 素材组排列方式-平铺
    def created_arrangement_tile_mode(self):
        selector = self.read_yaml_element("created_tile_mode")
        self._click(selector)

    # 列表模式排列
    def created_arrangement_list_mode(self):
        selector = self.read_yaml_element("created_list_mode")
        self._click(selector)

    # 收藏
    def created_collect(self):
        selector = self.read_yaml_element("created_collect")
        self._hover(selector)
        selector1 = self.read_yaml_element("created_collect_click")
        self._click(selector1)

    # 列表模式-进入素材组中第一个素材/素材组
    def created_in_Lgroup(self):
        selector = self.read_yaml_element("created_list_first_group")
        self._click(selector)




