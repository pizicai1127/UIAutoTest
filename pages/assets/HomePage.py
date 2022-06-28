# -*- coding: utf-8 -*- 
# @Time : 2022/3/16 10:34 上午 
# @Author : liuzhijie
# @File : HomePage.py


from pages.basepage import BasePage
from conf.confs import url_homePage

class HomePage(BasePage):

    # 路由跳转-首页
    def go_home_page(self):
        self._go(url_homePage)


    # 路由跳转-我加入的项目
    def go_my_join_items(self):
        selector = self.read_yaml_element("home_my_join_items")
        self._click(selector)

    # 路由跳转-我收藏的素材组
    def go_my_collection_groups(self):
        selector = self.read_yaml_element("home_my_collection_groups")
        self._click(selector)

    # 路由跳转 - 热门素材
    def go_hot_materials(self):
        selector = self.read_yaml_element("home_hot_materials")
        self._click(selector)

    # 路由跳转-热门素材组
    def go_hot_groups(self):
        selector = self.read_yaml_element("home_hot_groups")
        self._click(selector)

    # 路由跳转-最近访问
    def go_recent_visits(self):
        self._go('https://asset-stage.tezign.com/dam_enterprise/material_detail?assetId=7499')

    # 路由跳转-工作流
    def go_workflow(self):
        selector = self.read_yaml_element("homepage_project_1")
        self._click(selector)

    # 路由跳转-我的筛选项
    def go_my_filters(self):
        selector = self.read_yaml_element("homepage_my_filters")
        self._click(selector)

    # # 路由跳转-待办事项-素材库
    # def go_agency_matters_asset(self):
    #     selector = self.read_yaml_element("")
    #     self._click(selector)
    #
    # # 路由跳转-待办事项-工作流
    # def go_agency_matters_workflow(self):
    #     selector = self.read_yaml_element("")
    #     self._click(selector)
    #


    # 搜索-综合
    def home_search_all(self, text):
        # 输入text内容
        selector = self.read_yaml_element("home_search_input")
        self._fill(selector, text)
        # 点击搜索按钮
        selector = self.read_yaml_element("home_search_button")
        self._click(selector)

    # 搜索-素材
    def home_search_material(self, text):
        # 点击搜索输入框
        selector = self.read_yaml_element("home_search_input")
        self._click(selector)
        # 切换到搜索-素材tab
        selector = self.read_yaml_element("home_search_material_tab")
        self._click(selector)
        # 输入text内容
        selector = self.read_yaml_element("home_search_input")
        self._fill(selector, text)
        # 回车
        self._keyboard_click('Enter')


    # 搜索-素材组
    def home_search_groups(self, text):
        # 点击搜索输入框
        selector = self.read_yaml_element("home_search_input")
        self._click(selector)
        # 切换到搜索-素材组tab
        selector = self.read_yaml_element("home_search_group_tab")
        self._click(selector)
        # 输入text内容
        selector = self.read_yaml_element("home_search_input")
        self._fill(selector, text)
        # 点击搜索按钮
        selector = self.read_yaml_element("home_search_button")
        self._click(selector)