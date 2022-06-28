# -*- coding: utf-8 -*- 
# @Time : 2022/2/9 5:53 下午 
# @Author : liuzhijie
# @File : MyCollectionPage.py


from pages.basepage import BasePage

class MyCollectionPage(BasePage):



    # 新建素材组
    def collection_create_group(self, name, description):
        selector = self.read_yaml_element("collection_create_group_button")       # 新建素材组按钮
        self._click(selector)
        selector = self .read_yaml_element("collection_create_group_name_input")      # 输入组名
        self._fill(selector,name)
        selector = self.read_yaml_element("collection_create_group_description_input")       # 输入描述
        self._fill(selector,description)
        selector = self.read_yaml_element("collection_create_group_confirm_button")       # 点击确定按钮
        self._click(selector)


    # hover 素材组（第一个素材组名称）
    def collection_hover_group(self):
        # hover素材组名称
        selector = self.read_yaml_element("collection_group_name_first")   #名称元素（第一个组）
        self._hover(selector)

    # 点击收藏/取消收藏
    def collection_collect(self):
        # 收藏素材组
        selector = self.read_yaml_element("collection_collect_button")       # 收藏按钮
        self._click(selector)

    # 搜索
    def collection_search(self, text):
        # 输入搜索的素材组名或素材
        selector = self.read_yaml_element("collection_search_input")  # 输入框填入text
        self._fill(selector, text)
        self._keyboard_click('Enter')  # 按下"回车"键

    # 排序
    def collection_sort(self, text):
        selector = self.read_yaml_element("collection_sort_button")  # hover排序按钮
        self._hover(selector)
        tmp = self._input_sort(text)
        selector = self.read_yaml_element(tmp)  # 点击要测试的排序方式
        self._click(selector)


    # 素材组排列方式-平铺
    def collection_arrangement_tile_mode(self):
        selector = self.read_yaml_element("collection_tile_mode")
        self._click(selector)

    # 素材组排列方式-列表
    def collection_arrangement_list_mode(self):
        selector = self.read_yaml_element("collection_list_mode")
        self._click(selector)

    # 删除素材组
    def group_delete_batch(self):
        selector = self.read_yaml_element("group_name")
        if 'UI自动化' in self._text_content(selector):
            self._hover(selector)
            # 点击。。。菜单按钮
            selector = self.read_yaml_element("group_more_button")
            self._click(selector)
            # 点击"删除素材组"按钮
            selector = self.read_yaml_element("group_more_delete_button")
            self._click(selector)
            # 二次删除确认按钮
            selector = self.read_yaml_element("all_confirm_delete_collection")
            self._click(selector)
