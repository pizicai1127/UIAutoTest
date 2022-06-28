# -*- coding: utf-8 -*- 
# @Time : 2022/3/16 11:04 上午 
# @Author : liuzhijie
# @File : test_home_page.py


import allure
import pytest

from conf.confs import url_myCollectionPage, url_myCollectionPage_home


class TestHomePage:

    # 路由跳转 - 首页
    @allure.title("路由跳转-首页")
    @pytest.mark.run(order=1)
    def test_go_home_page(self, home_init):
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("home_title")
            home_init._wait_for_selector(home_init.read_yaml_element("home"))
            assert home_init._text_content(selector) == '特赞数字资产管理平台'
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err

    # 路由跳转 - 我加入的项目
    @allure.title("路由跳转-我加入的项目")
    @pytest.mark.run(order=2)
    def test_go_my_join_items(self, home_init):
        home_init.go_my_join_items()
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("assert_my_join_items")
            home_init._wait_for_selector(selector)
            assert home_init._is_visible(selector) == True
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # 路由跳转 - 我收藏的素材组
    @allure.title("路由跳转-我收藏的素材组")
    @pytest.mark.run(order=3)
    def test_go_my_collection_groups(self, home_init):
        home_init.go_my_collection_groups()
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("home_my_collection_groups_assert")
            home_init._wait_for_selector(selector)
            assert home_init._get_url() == url_myCollectionPage or url_myCollectionPage_home
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # 路由跳转 - 热门素材
    @allure.title("路由跳转-热门素材")
    @pytest.mark.run(order=4)
    def test_go_hot_materials(self, home_init):
        home_init.go_hot_materials()
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("assert_hot_materials")

            assert home_init._text_content(selector) == '素材热度'
            home_init._wait_for_selector(selector)
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # 路由跳转 - 热门素材组
    @allure.title("路由跳转-热门素材组")
    @pytest.mark.run(order=5)
    def test_go_hot_groups(self, home_init):
        home_init.go_hot_groups()
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("assert_hot_groups")
            assert home_init._text_content(selector) == '素材热度'
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # 路由跳转 - 最近访问
    @allure.title("路由跳转-最近访问")
    @pytest.mark.run(order=6)
    def test_go_hot_groups(self, home_init):
        home_init.go_recent_visits()
        home_init._wait(2)
        home_init.go_home_page()
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("assert_recent_visits")
            assert home_init._text_content(selector) == 'quanxianshenqing'
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # 路由跳转 - 工作流
    @allure.title("路由跳转-工作流")
    @pytest.mark.run(order=7)
    def test_go_workflow(self, home_init):
        home_init.go_workflow()
        '''断言：路由跳转是否成功'''
        try:
            assert 'workflow' in home_init._get_url()
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # 路由跳转 - 我的筛选项
    @allure.title("路由跳转-我的筛选项")
    @pytest.mark.run(order=8)
    def test_go_my_filters(self, home_init):
        home_init.go_my_filters()
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("homepage_my_filters_assert")
            assert '我创建的素材' in home_init._text_content(selector)
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # 搜索-综合
    @allure.title("搜索-综合")
    @pytest.mark.run(order=7)
    def test_home_search_all(self, home_init):
        home_init.home_search_all('home_search_all')
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("first_material_name")
            assert home_init._text_content(selector) == 'home_search_all'
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # 搜索-素材
    @allure.title("搜索-素材")
    @pytest.mark.run(order=8)
    def test_home_search_material(self, home_init):
        home_init.home_search_material('home_search_material')
        '''断言：路由跳转是否成功'''
        try:
            selector = home_init.read_yaml_element("first_material_name")
            assert home_init._text_content(selector) == 'home_search_material'
            print('-----路由跳转成功-----')
        except Exception as err:
            raise err


    # # 搜索-素材组
    # @allure.title("搜索-素材组")
    # @pytest.mark.run(order=9)
    # def test_home_search_groups(self, home_init):
    #     home_init.home_search_groups('home_search_group')
    #     home_init._wait(5)
    #     '''断言：路由跳转是否成功'''
    #     try:
    #         selector = home_init.read_yaml_element("first_group_name")
    #         assert home_init._text_content(selector) == 'home_search_group'
    #         print('-----路由跳转成功-----')
    #     except Exception as err:
    #         raise err