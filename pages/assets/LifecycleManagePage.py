# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/4/20 11:51 上午
# @File:LifecycleManagePage.py
from pages.basepage import BasePage
from conf.confs import url_lifecyclePage


class LifeCyclePage(BasePage):
    """
    有效期管理的页面
    """
    def goto_Lifecycle(self):
        """
        跳转到有效期管理页面
        @rtype: object
        """
        self._go(url_lifecyclePage)
        self._wait(1.5)

    def Lifecycle_add(self, text):
        """
        添加规则
        @rtype: object
        """
        selector = self.read_yaml_element("add_Lifecycle_button")  # 添加按钮
        self._click(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("add_Lifecycle_inputname")  # 标签规则名称
        self._fill(selector1, text)
        # self._wait(1)
        selector2 = self.read_yaml_element("add_Lifecycle_condition")  # 条件字段
        self._click(selector2)
        self._wait(2)
        selector3 = self.read_yaml_element("add_Lifecycle_choice")
        self._click(selector3)
        # self._wait(2)
        selector4 = self.read_yaml_element("add_Lifecycle_date")  # 日期
        self._click(selector4)
        selector5 = self.read_yaml_element("add_Lifecycle_date_popup_start")
        self._click(selector5)
        selector6 = self.read_yaml_element("add_Lifecycle_date_popup_end")
        self._click(selector6)
        selector7 = self.read_yaml_element("add_Lifecycle_release")  # 发布
        self._click(selector7)
        self._wait(1)

    def lifecycle_search(self, text):
        """
        有效期管理-搜索规则名称或标签
        @param text:
        @return:
        """
        selector = self.read_yaml_element("lifecycle_search_input")
        self._fill(selector, text)
        self._keyboard_click("Enter")
        # self._wait(2)

    def lifecycle_edit(self):
        """
        有效期管理-编辑-发布
        @return:
        """
        selector = self.read_yaml_element("lifecycle_edit")
        self._click(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("lifecycle_edit_confirm")
        self._wait_for_selector(selector1)
        self._click(selector1)
        # self._wait(2)

    def lifecycle_related(self):
        """
        有效期管理-查看关联素材
        @return:
        """
        selector = self.read_yaml_element("lifecycle_related_material")
        self._click(selector)
        # self._wait(2)

    def lifecycle_delete(self):
        """
        有效期管理-删除
        @return:
        """
        selector = self.read_yaml_element("lifecycle_delete")
        self._click(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("lifecycle_delete_confirm")
        self._wait_for_selector(selector1)
        self._click(selector1)
        # self._wait(2)






