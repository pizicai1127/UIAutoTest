# -*- coding: utf-8 -*- 
# @Time : 2022/5/16 11:40 上午 
# @Author : liuzhijie
# @File : test_content_detail_url_page.py
import allure
import pytest

from conf.confs import url_import_baidu, url_assetPage


class TestContentDetailUrlPage:

    # url-tab-评论 切换
    @allure.feature("内容详情页模块")
    @allure.title("tab切换-评论")
    @pytest.mark.run(order=1)
    def test_detail_tab_comments(self, asset_init, detail_url_init):
        detail_url_init.detail_tab_comments()
        detail_url_init._wait(0.2)
        '''断言：切换tab是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("detail_tab_assert")
            assert detail_url_init._text_content(selector) == '评论'
            print('-----切换tab断言成功-----')
        except Exception as err:
            raise err


    # 评论-发送
    @allure.feature("内容详情页模块")
    @allure.title("评论-发送")
    @pytest.mark.run(order=2)
    def test_detail_comment(self, asset_init, detail_url_init):
        detail_url_init.detail_comment('UI自动化测试-评论')
        '''断言：评论-发送是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("detail-comment_success_assert")
            assert detail_url_init._text_content(selector) == 'UI自动化测试-评论'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # url-tab-log 切换
    @allure.feature("内容详情页模块")
    @allure.title("tab切换-log")
    @pytest.mark.run(order=3)
    def test_detail_tab_logs(self, asset_init, detail_url_init):
        detail_url_init.detail_tab_logs()
        '''断言：切换tab是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("detail_tab_assert")
            assert detail_url_init._text_content(selector) == '日志'
            print('-----切换tab断言成功-----')
        except Exception as err:
            raise err


    # log查看
    @allure.feature("内容详情页模块")
    @allure.title("log查看")
    @pytest.mark.run(order=4)
    def test_detail_log(self, asset_init, detail_url_init):
        '''断言：log查看是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("detail_logs_success")
            detail_url_init._wait_for_selector(selector)
            assert detail_url_init._is_visible(selector) == True
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # url-tab-详情 切换
    @allure.feature("内容详情页模块")
    @allure.title("tab切换-详情")
    @pytest.mark.run(order=5)
    def test_detail_tab_details(self, asset_init, detail_url_init):
        detail_url_init.detail_tab_details()
        '''断言：切换tab是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("detail_tab_assert")
            assert detail_url_init._text_content(selector) == '详情'
            print('-----切换tab断言成功-----')
        except Exception as err:
            raise err


    # 分享
    @allure.feature("内容详情页模块")
    @allure.title("分享")
    @pytest.mark.run(order=6)
    def test_detail_share(self, asset_init, detail_url_init):
        detail_url_init.detail_share()
        '''断言：分享是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("message_text_assert")
            assert '链接创建并复制成功' in detail_url_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 编辑
    @allure.feature("内容详情页模块")
    @allure.title("编辑")
    @pytest.mark.run(order=7)
    def test_detail_edit(self, asset_init, detail_url_init):
        detail_url_init.detail_edit('UI自动化测试-Url描述-lzj')
        '''断言：编辑是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("message_text_assert")
            if detail_url_init._is_hidden(selector) is True:
                selector = detail_url_init.read_yaml_element("message_text_assert")
                assert '保存成功' in detail_url_init._text_content(selector)
                print('-----断言成功-----')
        except Exception as err:
            raise err


    # 添加到组-右上角入口
    @allure.feature("内容详情页模块")
    @allure.title("添加到组-右上角入口")
    @pytest.mark.run(order=8)
    def test_detail_add_to_group_upper_right(self, asset_init, detail_url_init):
        detail_url_init._wait_for_selector(detail_url_init.read_yaml_element("detail_more_button"))
        detail_url_init.detail_add_to_group_upper_right('test_group_001')
        '''断言：添加到组是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("message_text_assert")
            if detail_url_init._is_hidden(selector) is True:
                selector = detail_url_init.read_yaml_element("message_text_assert")
                assert '已成功添加到素材组' in detail_url_init._text_content(selector)
                print('-----断言成功-----')
        except Exception as err:
            raise err


    # 添加到组-右上角入口-移除素材组
    @allure.feature("内容详情页模块")
    @allure.title("添加到组-右上角入口-移除素材组")
    @pytest.mark.run(order=9)
    def test_detail_move_group_upper_right(self, asset_init, detail_url_init):
        detail_url_init.detail_move_group_upper_right()
        # '''断言：-移除素材组是否成功'''
        # try:
        #     selector = detail_url_init.read_yaml_element("detail_upper_right_button")
        #     assert detail_url_init._is_visible(selector) == True
        #     print('-----断言成功-----')
        # except Exception as err:
        #     raise err


    # 添加到组-现有组
    @allure.feature("内容详情页模块")
    @allure.title("添加到组-现有组")
    @pytest.mark.run(order=10)
    def test_detail_add_to_group(self, asset_init, detail_url_init):
        detail_url_init.detail_add_to_group('test_group_001')
        '''断言：添加到组是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("message_text_assert")
            assert detail_url_init._text_content(selector) == '已成功添加到素材组'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 添加到组-新建组
    @allure.feature("内容详情页模块")
    @allure.title("添加到组-新建组")
    @pytest.mark.run(order=11)
    def test_detail_add_to_group_build(self, asset_init, detail_url_init):
        detail_url_init.detail_add_to_group_build('UI自动化测试_新建组')
        '''断言：添加到组是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("message_text_assert")
            assert detail_url_init._text_content(selector) == '已成功添加到素材组'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 提交错误
    @allure.feature("内容详情页模块")
    @allure.title("提交错误")
    @pytest.mark.run(order=12)
    def test_detail_submit_error(self, asset_init, detail_url_init):
        detail_url_init.detail_submit_error()
        '''断言：提交错误是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("message_text_assert")
            if detail_url_init._is_hidden(selector) is True:
                selector = detail_url_init.read_yaml_element("message_text_assert")
                assert '报错已提交成功' in detail_url_init._text_content(selector)
                print('-----断言成功-----')
        except Exception as err:
            raise err


    # 复制链接
    @allure.feature("内容详情页模块")
    @allure.title("复制链接")
    @pytest.mark.run(order=13)
    def test_detail_copy_link(self, asset_init, detail_url_init):
        detail_url_init.detail_copy_link()
        '''断言：提交错误是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("message_text_assert")
            if detail_url_init._is_hidden(selector) is True:
                selector = detail_url_init.read_yaml_element("message_text_assert")
                assert '复制链接成功' in detail_url_init._text_content(selector)
                print('-----断言成功-----')
        except Exception as err:
            raise err


    # 在浏览器打开链接
    @allure.feature("内容详情页模块")
    @allure.title("在浏览器打开链接")
    @pytest.mark.run(order=14)
    def test_detail_open_url(self, asset_init, detail_url_init):
        detail_url_init.detail_open_url()
        '''断言：在浏览器打开链接是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("open_url_success")
            if detail_url_init._is_visible(selector):
                assert detail_url_init._get_url() == url_import_baidu
                print('-----断言成功-----')
        except Exception as err:
            raise err


    # 删除
    @allure.feature("内容详情页模块")
    @allure.title("删除")
    @pytest.mark.run(order=15)
    def test_detail_delete(self, asset_init, detail_url_init):
        detail_url_init._go(url_assetPage)
        detail_url_init.into_detail_page()
        # 删除
        detail_url_init.detail_delete()
        '''断言：删除是否成功'''
        try:
            selector = detail_url_init.read_yaml_element("message_text_assert")
            if detail_url_init._is_hidden(selector) is True:
                selector = detail_url_init.read_yaml_element("message_text_assert")
                assert '删除素材成功' in detail_url_init._text_content(selector)
                print('-----断言成功-----')
        except Exception as err:
            raise err



