# # -*- coding: utf-8 -*-
# # @Time : 2022/2/10 10:27 上午
# # @Author : liuzhijie
# # @File : test_my_collection_page.py

import allure
import pytest
from conf.confs import group_name, group_description, url_myCollectionPage


@allure.epic("素材组模块")
@allure.feature("我收藏的")
class TestMyCollectionPage:

    # 创建素材组
    @allure.title("创建素材组")
    @pytest.mark.run(order=1)
    def test_collection_create_group(self, my_collection_page_init):
        my_collection_page_init.collection_create_group(group_name,group_description)
        '''断言：创建素材组是否成功'''
        try:
            selector = my_collection_page_init.read_yaml_element("collection_create_group_assert")
            assert my_collection_page_init._text_content(selector) == "UI自动化测试-我收藏的 "
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 收藏素材组
    @allure.title("收藏素材组")
    @pytest.mark.run(order=2)
    def test_collection_collect_group(self, my_collection_page_init):
        my_collection_page_init.collection_search('UI自动化测试-我收藏的')
        my_collection_page_init.collection_hover_group()
        my_collection_page_init.collection_collect()
        '''断言：切换排列方式是否成功'''
        try:
            selector = my_collection_page_init.read_yaml_element("assert_massage")
            assert my_collection_page_init._text_content(selector) == '你已成功收藏该素材组'
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 搜索
    @allure.title("搜索")
    @pytest.mark.run(order=3)
    def test_collection_search(self,my_collection_page_init):
        text = 'UI自动化测试-我收藏的'
        my_collection_page_init.collection_search(text)
        '''断言：上传文件是否成功'''
        try:
            selector_group = my_collection_page_init.read_yaml_element("collection_search_group_first_name")
            assert text in my_collection_page_init._text_content(selector_group)
            print('-----上传文件断言成功-----')
        except Exception as err:
            raise err


    # 排序
    @allure.title("排序")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('style,ele', [("最近打开", "recently_opened_sort_assert"),
                                           ("素材热度", "material_heat_sort_assert"),
                                           ("历史总活跃", "history_total_activity_sort_assert"),
                                           ("名称排序", "material_name_sort_assert"),
                                           ("创建时间", "create_time_sort_assert"),
                                           ("更新时间", "update_time_sort_assert")])
    def test_collection_sort(self, style, ele, my_collection_page_init):
        my_collection_page_init._go(url_myCollectionPage)
        # 排序-更新时间
        my_collection_page_init.collection_sort(style)
        my_collection_page_init._wait(1)
        '''断言：排序是否成功'''
        try:
            selector = my_collection_page_init.read_yaml_element(ele)
            assert style in my_collection_page_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 素材组列表模式
    @allure.title("素材组列表模式")
    @pytest.mark.run(order=5)
    def test_collection_arrangement_list_mode(self,my_collection_page_init):
        my_collection_page_init._go(url_myCollectionPage)
        my_collection_page_init.collection_arrangement_list_mode()
        # my_collection_page_init._wait(2)
        # '''断言：切换排列方式是否成功'''
        # try:
        #     selector = my_collection_page_init.read_yaml_element("collection_list_mode_assert")
        #     assert my_collection_page_init._text_content(selector) == '素材组名称'
        #     print('-----排序断言成功-----')
        # except Exception as err:
        #     raise err


    # 素材组平铺模式
    @allure.title("素材组平铺模式")
    @pytest.mark.run(order=6)
    def test_collection_arrangement_tile_mode(self, my_collection_page_init):
        my_collection_page_init._go(url_myCollectionPage)
        my_collection_page_init.collection_arrangement_tile_mode()
        # my_collection_page_init._wait(2)
        # '''断言：切换排列方式是否成功'''
        # try:
        #     selector = my_collection_page_init.read_yaml_element("collection_list_mode_assert")
        #     assert my_collection_page_init._is_visible(selector) == False
        #     print('-----排序断言成功-----')
        # except Exception as err:
        #     raise err


    # 取消收藏素材组
    @allure.title("取消收藏素材组")
    @pytest.mark.run(order=7)
    def test_collection_cancel_collect_group(self, my_collection_page_init):
        my_collection_page_init._go(url_myCollectionPage)
        my_collection_page_init.collection_search('UI自动化测试-我收藏的')
        my_collection_page_init.collection_hover_group()
        my_collection_page_init.collection_collect()
        '''断言：切换排列方式是否成功'''
        try:
            selector = my_collection_page_init.read_yaml_element("assert_massage")
            assert my_collection_page_init._text_content(selector) == '你已取消收藏该素材组'
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 删除素材组
    @allure.title("删除素材组")
    @pytest.mark.run(order=8)
    def test_group_delete(self,my_collection_page_init):
        my_collection_page_init.collection_search('UI自动化测试')
        my_collection_page_init.group_delete_batch()

