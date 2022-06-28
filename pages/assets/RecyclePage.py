# -*- coding: utf-8 -*- 
# @Time : 2022/4/12 11:55 上午 
# @Author : liuzhijie
# @File : RecyclePage.py


from pages.basepage import BasePage


class RecyclePage(BasePage):

    # 切换Tab-素材
    def recycle_asset_tab(self):
        selector = self.read_yaml_element("recycle_asset_tab")
        self._click(selector)

    # 切换Tab-素材组
    def recycle_group_tab(self):
        selector = self.read_yaml_element("recycle_group_tab")
        self._click(selector)

    # 彻底删除-素材
    def completely_delete_asset(self):
        # 点击"彻底删除"按钮
        selector = self.read_yaml_element("completely_delete_asset_button")
        self._click(selector)
        # 二次删除确认
        selector = self.read_yaml_element("completely_delete_asset_confirm_button")
        self._click(selector)

    # 彻底删除-素材组
    def completely_delete_group(self):
        # 点击"彻底删除"按钮
        selector = self.read_yaml_element("completely_delete_group_button")
        self._click(selector)
        # 二次删除确认
        selector = self.read_yaml_element("completely_delete_group_confirm_button")
        self._click(selector)

    # 恢复-素材
    def recovery_asset(self):
        # 点击"恢复"按钮
        selector = self.read_yaml_element("recovery_asset_button")
        self._click(selector)
        # 二次恢复确认
        selector = self.read_yaml_element("recovery_asset_confirm_button")
        self._click(selector)

    # 恢复-素材组
    def recovery_group(self):
        # 点击"恢复"按钮
        selector = self.read_yaml_element("recovery_group_button")
        self._click(selector)
        # 二次恢复确认
        selector = self.read_yaml_element("recovery_group_confirm_button")
        self._click(selector)

    # 清空
    def recycle_empty(self):
        # 点击"清空"按钮
        selector = self.read_yaml_element("recycle_empty_button")
        self._click(selector)
        # 二次清空确认
        selector = self.read_yaml_element("recycle_empty_confirm_button")
        self._click(selector)

    # 排序-删除时间
    def delete_time_sort_asc(self):
        # 点击排序按钮
        selector = self.read_yaml_element("delete_time_sort_asc_button")
        self._click(selector)

    # 排序-删除时间
    def delete_time_sort_desc(self):
        # 点击排序按钮
        selector = self.read_yaml_element("delete_time_sort_desc_button")
        self._click(selector)

    # 勾选-进入批量编辑模式
    def check_first(self):
        # 勾选中第一个素材/素材组
        selector = self.read_yaml_element("check_first_button")
        self._click(selector)

    # 批量操作-彻底删除-素材
    def batch_completely_delete_asset(self):
        # 点击"彻底删除"按钮
        selector = self.read_yaml_element("batch_completely_delete_asset_button")
        self._click(selector)
        # 二次彻底删除确认
        selector =self.read_yaml_element("batch_completely_delete_asset_confirm_button")
        self._click(selector)

    # 批量操作-彻底删除-素材组
    def batch_completely_delete_group(self):
        # 点击"彻底删除"按钮
        selector = self.read_yaml_element("batch_completely_delete_group_button")
        self._click(selector)
        # 二次彻底删除确认
        selector =self.read_yaml_element("batch_completely_delete_group_confirm_button")
        self._click(selector)

    # 批量操作-恢复-素材
    def batch_recovery_asset(self):
        # 点击"恢复"按钮
        selector = self.read_yaml_element("batch_recovery_asset_button")
        self._click(selector)
        # 二次恢复确认
        selector =self.read_yaml_element("batch_recovery_asset_confirm_button")
        self._click(selector)

    # 批量操作-恢复-素材组
    def batch_recovery_group(self):
        # 点击"恢复"按钮
        selector = self.read_yaml_element("batch_recovery_group_button")
        self._click(selector)
        # 二次恢复确认
        selector =self.read_yaml_element("batch_recovery_group_confirm_button")
        self._click(selector)

    # 批量操作-取消
    def batch_cancel(self):
        # 点击"取消"按钮
        selector = self.read_yaml_element("batch_cancel_button")
        self._click(selector)

