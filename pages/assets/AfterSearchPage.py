# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/3/18 10:43 上午
# @File:AfterSearchPage.py
from pages.basepage import BasePage
from conf.confs import url_assetGroupPage


class AfterSearchPage(BasePage):
    """
    全部素材组下-搜索后的相关操作页面
    """
    def goto_search(self):
        """
        跳转到全部素材组页面
        @rtype: object
        """
        self._go(url_assetGroupPage)
        self._wait(1.5)

    def after_search(self, text):
        """
        输入素材或素材组名称
        @rtype: text
        """
        selector = self.read_yaml_element("search_input_in")
        self._fill(selector, text)
        # self._wait(2)
        self._keyboard_click("Enter")
        # self._wait(2)

    '''以下是搜索后第一个是素材组'''
    def search_first_group(self):
        """
        hover第一个素材，点击更多
        @rtype: object
        """
        selector = self.read_yaml_element("search_first")
        self._hover(selector)  # hover第一个素材
        # self._wait(3)
        selector1 = self.read_yaml_element("search_more_group")
        self._click(selector1)  # 点击更多...
        # self._wait(2)

    def search_newpage(self):
        """
        搜索后第一个是素材组-新标签页打开
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_newpage")
        self._click(selector2)
        # self._wait(2)

    def search_edit_group(self):
        """
        搜索后第一个是素材组-编辑素材组
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_edit_group")
        self._click(selector2)
        self._wait(2)

    def search_subscribe_group(self):
        """
        搜索后第一个是素材组-订阅/取消订阅
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_subscribe")
        self._click(selector2)
        # self._wait(2)

    def search_collection_group(self):
        """
        搜索后第一个是素材组-收藏/取消收藏
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_collection")
        self._click(selector2)
        # self._wait(2)

    def search_share_group(self):
        """
        搜索后第一个是素材组-分享
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_share")
        self._click(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_share_confirm")
        self._click(selector3)
        selector4 = self.read_yaml_element("search_share_copy")
        self._click(selector4)
        # self._wait(2)

    def search_copy_group(self):
        """
        搜索后第一个是素材组-复制素材组
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_copy")
        self._click(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_copy_confirm")
        self._click(selector3)
        # self._wait(2)

    def search_download_group(self):
        """
        搜索后第一个是素材组-下载
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_download_group")
        self._hover(selector2)  # hover 下载
        # self._wait(2)

    def search_delete_group(self):
        """
        搜索后第一个是素材组-删除素材组
        @rtype: object
        """
        selector = self.read_yaml_element("search_first")
        self._hover(selector)  # hover第一个素材组或素材
        # self._wait(2)
        selector1 = self.read_yaml_element("search_more_group")
        self._click(selector1)  # 点击更多...
        # self._wait(2)
        selector2 = self.read_yaml_element("search_delete")
        self._click(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_delete_confirm")
        self._click(selector3)
        # self._wait(2)

    '''以下是搜索后第一个是素材'''
    def search_first_asset(self):
        """
        hover第一个素材，点击更多
        @rtype: object
        """
        selector = self.read_yaml_element("search_first")
        self._wait_for_selector(selector)
        self._hover(selector)  # hover第一个素材
        # self._wait(2)
        selector1 = self.read_yaml_element("search_more_asset")
        self._wait_for_selector(selector1)
        self._click(selector1)  # 点击更多...
        # self._wait(2)

    def search_rename(self):
        """
        搜索后第一个是素材-重命名
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_rename")
        self._click(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_rename_old")
        self._click(selector3)
        selector4 = self.read_yaml_element("search_rename_confirm")
        self._click(selector4)
        # self._wait(1)
        selector5 = self.read_yaml_element("search_rename_continue")
        self._click(selector5)

    def search_edit_asset(self):
        """
        搜索后第一个是素材-编辑
        @rtype: object
        """
        selector1 = self.read_yaml_element("search_edit_asset")
        self._click(selector1)
        # self._wait(2)
        # selector2 = self.read_yaml_element("search_edit_asset_cancel")
        # self._click(selector2)
        # self._wait(2)

    def seach_download_asset(self):
        """
        搜索后第一个是素材-下载
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_download2")
        self._hover(selector2)  # hover 下载
        # self._wait(2)

    def search_share_asset(self):
        """
        搜索后第一个是素材-分享
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_share")
        self._click(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_share_confirm")
        self._click(selector3)
        selector4 = self.read_yaml_element("search_share_copy")
        self._click(selector4)
        # self._wait(2)

    def search_add_group(self):
        """
        搜索后第一个是素材-添加素材组
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_add_group")
        self._click(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_add_group_ry")
        self._click(selector3)
        # self._wait(2)
        selector4 = self.read_yaml_element("search_add_group_confirm")
        self._click(selector4)
        # self._wait(2)

    def search_add_basket_asset(self):
        """
        搜索后第一个是素材-添加素材篮
        @rtype: object
        """
        selector2 = self.read_yaml_element("search_add_basket")
        self._wait_for_selector(selector2)
        self._click(selector2)
        # self._wait(2)

    def search_basket(self):
        """
        清空素材篮
        @rtype: object
        """
        selector = self.read_yaml_element("search_basket")
        self._click(selector)
        selector1 = self.read_yaml_element("search_basket_empty")
        self._click(selector1)
        self._wait(1.5)

    def search_owner(self):
        """
        修改所有者
        @rtype: object
        """
        selector = self.read_yaml_element("search_owner")
        self._click(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("search_owner_cancel")  # 没有实现修改所有者功能下拉框输入和选择没有成功，下次优化
        self._click(selector1)
        # self._wait(2)

    def search_type(self):
        """
        修改素材权限
        @rtype: object
        """
        selector = self.read_yaml_element("search_type")
        self._click(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("search_type_confirm")
        self._click(selector1)
        # self._wait(2)

    def search_Multiple_download_group(self):
        """
        搜索后素材组-批量操作-下载
        @rtype: object
        """
        selector = self.read_yaml_element("search_first")
        self._hover(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("search_Multiple_choice1")
        self._click(selector1)
        # self._wait(2)
        selector2 = self.read_yaml_element("search_second")
        self._hover(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_Multiple_choice2")
        self._click(selector3)
        # self._wait(2)
        selector4 = self.read_yaml_element("search_Multiple_download_group")
        self._click(selector4)
        selector5 = self.read_yaml_element("search_Multiple_download_group1")
        self._click(selector5)
        # self._wait(2)

    def search_Multiple_download_asset(self):
        """
        搜索后素材-批量操作-下载
        @rtype: object
        """
        selector = self.read_yaml_element("search_first")
        self._hover(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("search_Multiple_choice1")
        self._click(selector1)
        # self._wait(2)
        selector2 = self.read_yaml_element("search_Multiple_second")
        self._hover(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_Multiple_choice2_asset")
        self._click(selector3)
        # self._wait(2)
        selector4 = self.read_yaml_element("search_Multiple_download_group")
        self._click(selector4)
        selector5 = self.read_yaml_element("search_Multiple_download_group1")
        self._click(selector5)
        # self._wait(2)

    def search_Multiple_basket_group(self):
        """
        搜索后素材组-批量操作-加入素材篮
        @rtype: object
        """
        selector = self.read_yaml_element("search_first")
        self._hover(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("search_Multiple_choice1")
        self._click(selector1)
        # self._wait(2)
        selector2 = self.read_yaml_element("search_second")
        self._hover(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_Multiple_choice2")
        self._click(selector3)
        # self._wait(2)
        selector4 = self.read_yaml_element("search_Multiple_basket")
        self._click(selector4)
        # self._wait(1)

    def search_Multiple_basket_asset(self):
        """
        搜索后素材-批量操作-加入素材篮
        @rtype: object
        """
        selector = self.read_yaml_element("search_first")
        self._hover(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("search_Multiple_choice1")
        self._click(selector1)
        # self._wait(2)
        selector2 = self.read_yaml_element("search_Multiple_second")
        self._hover(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_Multiple_choice2_asset")
        self._click(selector3)
        # self._wait(2)
        selector4 = self.read_yaml_element("search_Multiple_basket")
        self._click(selector4)
        # self._wait(1)

    def search_Multiple_cancel_group(self):
        """
        搜索后素材组-批量操作-取消
        @rtype: object
        """
        selector = self.read_yaml_element("search_first")
        self._hover(selector)
        # self._wait(2)
        selector1 = self.read_yaml_element("search_Multiple_choice1")
        self._click(selector1)
        # self._wait(2)
        selector2 = self.read_yaml_element("search_second")
        self._hover(selector2)
        # self._wait(2)
        selector3 = self.read_yaml_element("search_Multiple_choice2")
        self._click(selector3)
        # self._wait(2)
        selector4 = self.read_yaml_element("search_Multiple_cancel")
        self._click(selector4)
        # self._wait(2)








