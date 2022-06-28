# -*- coding: utf-8 -*- 
# @Time : 2022/4/12 11:50 上午 
# @Author : liuzhijie
# @File : test_recycle_page.py

import allure
import pytest

from conf.confs import url_recyclePage, url_assetPage, url_assetGroupPage


class TestRecyclePage:


    @allure.title("Tab切换-素材tab")
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=1)
    # Tab切换-素材tab
    def test_recycle_asset_tab(self, asset_init, recycle_init):
        # 切换到素材tab
        recycle_init.recycle_asset_tab()


    @allure.title("Tab切换-素材组tab")
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=1)
    # Tab切换-素材组tab
    def test_recycle_group_tab(self, group_init, recycle_init):
        # 切换到素材组tab
        recycle_init.recycle_group_tab()


    @allure.title("排序-删除时间-升序")
    @pytest.mark.run(order=3)
    @pytest.mark.flaky(reruns=1)
    # 排序-删除时间-升序
    def test_recycle_sort_asc(self, recycle_init):
        # 进入回收站页面
        recycle_init._go(url_recyclePage)
        # 点击"删除时间"按钮-切到升序
        recycle_init.delete_time_sort_asc()


    @allure.title("排序-删除时间-降序")
    @pytest.mark.run(order=4)
    @pytest.mark.flaky(reruns=1)
    # 排序-删除时间-降序
    def test_recycle_sort_desc(self, recycle_init):
        # 进入回收站页面
        recycle_init._go(url_recyclePage)
        # 点击"删除时间"按钮-切到升序
        recycle_init.delete_time_sort_asc()
        # 模拟移动
        recycle_init._mouse_move(100,100)
        # 点击"删除时间"按钮-切到降序
        recycle_init.delete_time_sort_desc()


    @allure.title("放回原处-素材")
    @pytest.mark.run(order=5)
    @pytest.mark.flaky(reruns=1)
    # 放回原处-素材
    def test_recovery_asset(self, asset_init, recycle_init):
        # 放回原处
        recycle_init.recycle_asset_tab()
        recycle_init.recovery_asset()
        '''断言：放回是否成功'''
        try:
            selector = recycle_init.read_yaml_element("message_text_assert")
            assert '放回成功' in recycle_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("放回原处-素材组")
    @pytest.mark.run(order=6)
    @pytest.mark.flaky(reruns=1)
    # 放回原处-素材组
    def test_recovery_group(self, group_init, recycle_init):
        # 进入回收站页面
        group_init._go(url_recyclePage)
        # 放回原处
        recycle_init.recycle_group_tab()
        recycle_init.recovery_group()
        '''断言：放回是否成功'''
        try:
            selector = recycle_init.read_yaml_element("message_text_assert")
            assert '放回成功' in recycle_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("彻底删除-素材")
    @pytest.mark.run(order=7)
    @pytest.mark.flaky(reruns=1)
    # 彻底删除-素材
    def test_completely_delete_asset(self, asset_init, recycle_init):
        # 进入素材库页面
        asset_init._go(url_assetPage)
        # hover 素材
        asset_init.asset_hover()
        # 点击"。。。"按钮
        asset_init.asset_more_button()
        # 删除素材（让素材进入回收站）
        asset_init.asset_more_delete()
        # 进入回收站页面
        asset_init._go(url_recyclePage)
        # 切换到素材Tab
        recycle_init.recycle_asset_tab()
        # 彻底删除
        recycle_init.completely_delete_asset()
        '''断言：删除是否成功'''
        try:
            selector = recycle_init.read_yaml_element("message_text_assert")
            assert '删除成功' in recycle_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("彻底删除-素材组")
    @pytest.mark.run(order=8)
    @pytest.mark.flaky(reruns=1)
    # 彻底删除-素材组
    def test_completely_delete_group(self, group_init, recycle_init):
        # 进入素材组页面
        group_init._go(url_assetGroupPage)
        # 新建素材组
        group_init.group_new('UI自动化测试-回收站-测试组')
        # 删除素材组（让素材进入回收站）
        group_init.group_delete()
        # 进入回收站页面
        recycle_init._go(url_recyclePage)
        # 彻底删除
        recycle_init.completely_delete_group()
        '''断言：删除是否成功'''
        try:
            selector = recycle_init.read_yaml_element("message_text_assert")
            assert '删除成功' in recycle_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("清空回收站")
    @pytest.mark.run(order=9)
    @pytest.mark.flaky(reruns=1)
    # 清空回收站
    def test_recycle_empty(self, asset_init, group_init, recycle_init):
        # 进入素材组页面
        group_init._go(url_assetGroupPage)
        # 进入第一个素材组
        group_init.group_enter()
        # 删除素材组（让素材进入回收站）
        group_init.group_delete()
        # 进入回收站页面
        recycle_init._go(url_recyclePage)
        recycle_init._wait(1)
        # 清空回收站
        recycle_init.recycle_empty()
        '''断言：清空是否成功'''
        try:
            selector = recycle_init.read_yaml_element("message_text_assert")
            assert '清空成功' in recycle_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err