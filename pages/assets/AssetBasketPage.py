# -*- coding: utf-8 -*-
# @Time : 2022/3/16 10:34 上午
# @Author : liuzhijie
# @File : AssetBasketPage.py

from pages.basepage import BasePage
class AssetBasketPage(BasePage):

    # 加入素材篮
    def add_to_basket(self):
        # over 素材
        selector = self.read_yaml_element("asset_selected_hover")
        self._hover(selector)
        self._wait(1)
        # 点击加入素材篮按钮
        selector = self.read_yaml_element("asset_add_to_basket")
        self._click(selector)

    # 打开素材篮页面
    def open_basket(self):
        # hover 素材篮图片
        selector = self.read_yaml_element("asset_selected_hover")
        self._hover(selector)
        # 点击素材篮按钮，打开素材篮页面
        selector = self.read_yaml_element("basket_button")
        self._click(selector)

    # 分享素材篮素材
    def basket_share(self):
        # 点击分享按钮
        selector = self.read_yaml_element("basket_share")
        self._click(selector)
        # 点击"创建链接"按钮
        selector = self.read_yaml_element("basket_share_create_link_button")
        self._click(selector)
        # 关闭弹窗：点击"x"
        selector = self.read_yaml_element("basket_share_close_button")
        self._click(selector)


    # 下载素材篮素材
    def basket_download(self):
        # 点击下载按钮
        selector = self.read_yaml_element("basket_download")
        self._click(selector)
        self._wait(2)

    # 删除素材
    def basket_delete(self):
        # 点击删除按钮
        selector = self.read_yaml_element("basket_delete")
        self._wait_for_selector(selector)
        self._click(selector)


    # 清空素材篮
    def basket_empty(self):
        # 点击清空素材篮按钮
        selector = self.read_yaml_element("basket_empty")
        self._wait_for_selector(selector)
        self._click(selector)


