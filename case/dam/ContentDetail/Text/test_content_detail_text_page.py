# -*- coding: utf-8 -*- 
# @Time : 2022/5/19 12:04 下午 
# @Author : liuzhijie
# @File : test_content_detail_text_page.py
import allure
import pytest

from conf.confs import url_assetPage


class TestContentDetailTextPage:

    # Text-tab-评论 切换
    @allure.feature("内容详情页模块")
    @allure.title("tab切换-评论")
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=1)
    def test_detail_tab_comments(self, asset_init, detail_text_init):
        detail_text_init.detail_tab_comments()
        detail_text_init._wait(0.2)
        '''断言：切换tab是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("detail_tab_assert")
            assert detail_text_init._text_content(selector) == '评论'
            print('-----切换tab断言成功-----')
        except Exception as err:
            raise err


    # 评论-发送
    @allure.feature("内容详情页模块")
    @allure.title("评论-发送")
    @pytest.mark.run(order=2)
    def test_detail_comment(self, asset_init, detail_text_init):
        detail_text_init.detail_comment('UI自动化测试-评论')
        '''断言：评论-发送是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("detail-comment_success_assert")
            assert detail_text_init._text_content(selector) == 'UI自动化测试-评论'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # Text-tab-log 切换
    @allure.feature("内容详情页模块")
    @allure.title("tab切换-log")
    @pytest.mark.run(order=3)
    def test_detail_tab_logs(self, asset_init, detail_text_init):
        detail_text_init.detail_tab_logs()
        '''断言：切换tab是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("detail_tab_assert")
            assert detail_text_init._text_content(selector) == '日志'
            print('-----切换tab断言成功-----')
        except Exception as err:
            raise err


    # log查看
    @allure.feature("内容详情页模块")
    @allure.title("log查看")
    @pytest.mark.run(order=4)
    def test_detail_log(self, asset_init, detail_text_init):
        '''断言：log查看是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("detail_logs_success")
            detail_text_init._wait_for_selector(selector)
            assert detail_text_init._is_visible(selector) == True
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # Text-tab-详情 切换
    @allure.feature("内容详情页模块")
    @allure.title("tab切换-详情")
    @pytest.mark.run(order=5)
    def test_detail_tab_details(self, asset_init, detail_text_init):
        detail_text_init.detail_tab_details()
        '''断言：切换tab是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("detail_tab_assert")
            assert detail_text_init._text_content(selector) == '详情'
            print('-----切换tab断言成功-----')
        except Exception as err:
            raise err


    # 分享
    @allure.feature("内容详情页模块")
    @allure.title("分享")
    @pytest.mark.run(order=6)
    def test_detail_share(self, asset_init, detail_text_init):
        detail_text_init.detail_share()
        '''断言：分享是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("message_text_assert")
            assert '链接创建并复制成功' in detail_text_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 编辑
    @allure.feature("内容详情页模块")
    @allure.title("编辑")
    @pytest.mark.run(order=7)
    def test_detail_edit(self, asset_init, detail_text_init):
        detail_text_init.detail_edit('UI自动化测试-Url描述-lzj')
        '''断言：编辑是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("message_text_assert")
            if detail_text_init._is_hidden(selector) is True:
                selector = detail_text_init.read_yaml_element("message_text_assert")
                assert '保存成功' in detail_text_init._text_content(selector)
                print('-----断言成功-----')
        except Exception as err:
            raise err


    # 添加到组-右上角入口
    @allure.feature("内容详情页模块")
    @allure.title("添加到组-右上角入口")
    @pytest.mark.run(order=8)
    def test_detail_add_to_group_upper_right(self, asset_init, detail_text_init):
        detail_text_init._wait_for_selector(detail_text_init.read_yaml_element("detail_more_button"))
        detail_text_init.detail_add_to_group_upper_right('test_group_001')
        '''断言：添加到组是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("message_text_assert")
            if detail_text_init._is_hidden(selector) is True:
                selector = detail_text_init.read_yaml_element("message_text_assert")
                assert '已成功添加到素材组' in detail_text_init._text_content(selector)
                print('-----断言成功-----')
        except Exception as err:
            raise err


    # 添加到组-右上角入口-移除素材组
    @allure.feature("内容详情页模块")
    @allure.title("添加到组-右上角入口-移除素材组")
    @pytest.mark.run(order=9)
    def test_detail_move_group_upper_right(self, asset_init, detail_text_init):
        detail_text_init.detail_move_group_upper_right()
        # '''断言：-移除素材组是否成功'''
        # try:
        #     selector = detail_text_init.read_yaml_element("detail_upper_right_button")
        #     assert detail_text_init._is_visible(selector) == True
        #     print('-----断言成功-----')
        # except Exception as err:
        #     raise err


    # 添加到组-现有组
    @allure.feature("内容详情页模块")
    @allure.title("添加到组-现有组")
    @pytest.mark.run(order=10)
    def test_detail_add_to_group(self, asset_init, detail_text_init):
        detail_text_init.detail_add_to_group('test_group_001')
        '''断言：添加到组是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("message_text_assert")
            assert detail_text_init._text_content(selector) == '已成功添加到素材组'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 添加到组-新建组
    @allure.feature("内容详情页模块")
    @allure.title("添加到组-新建组")
    @pytest.mark.run(order=11)
    def test_detail_add_to_group_build(self, asset_init, detail_text_init):
        detail_text_init.detail_add_to_group_build('UI自动化测试_新建组')
        '''断言：添加到组是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("message_text_assert")
            assert detail_text_init._text_content(selector) == '已成功添加到素材组'
            print('-----断言成功-----')
        except Exception as err:
            raise err
        detail_text_init._wait(4)


    # 复制全文
    @allure.feature("内容详情页模块")
    @allure.title("复制全文")
    @pytest.mark.run(order=12)
    def test_detail_copy_full_text(self, asset_init, detail_text_init):
        selector = detail_text_init.read_yaml_element("message_text_assert")
        if detail_text_init._is_hidden(selector) is True:
            detail_text_init.detail_copy_full_text()
        '''断言：复制全文是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("message_text_assert")
            assert detail_text_init._text_content(selector) == '复制成功'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 编辑（文本）
    @allure.feature("内容详情页模块")
    @allure.title("编辑（文本）")
    @pytest.mark.run(order=13)
    def test_detail_edit_text(self, asset_init, detail_text_init):
        detail_text_init.detail_edit_text('UI自动化测试-编辑文本')
        '''断言：编辑（文本）是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("detail_edit_text_success_assert")
            assert detail_text_init._text_content(selector) == 'UI自动化测试-编辑文本'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 删除
    @allure.feature("内容详情页模块")
    @allure.title("删除")
    @pytest.mark.run(order=14)
    def test_detail_delete(self, asset_init, detail_text_init):
        # 删除
        detail_text_init.detail_delete()
        '''断言：删除是否成功'''
        try:
            selector = detail_text_init.read_yaml_element("message_text_assert")
            if detail_text_init._is_hidden(selector) is True:
                selector = detail_text_init.read_yaml_element("message_text_assert")
                assert '删除素材成功' in detail_text_init._text_content(selector)
                print('-----断言成功-----')
        except Exception as err:
            raise err