# -*- coding: utf-8 -*- 
# @Time : 2022/3/25 1:05 下午 
# @Author : liuzhijie
# @File : test_asset_more_page.py
import allure
import pytest
from conf.confs import url_assetPage

class TestAssetMorePage:

    @pytest.fixture(autouse=True)
    def asset_more_general(self, asset_more_init):
        asset_more_init._go(url_assetPage)
        selector = asset_more_init.read_yaml_element("asset_filters_creator")
        asset_more_init._wait_for_selector(selector)
        # hover 首个素材
        asset_more_init.asset_hover()
        # 点击更多按钮
        asset_more_init.asset_more_button()


    # 右键-重命名
    @allure.title("右键-重命名")
    @pytest.mark.run(order=1)
    def test_asset_more_rename(self, asset_more_init):
        # 重命名
        asset_more_init.asset_more_rename('more_重命名')
        # '''断言：右键-重命名是否成功'''
        # try:
        #     selector = asset_more_init.read_yaml_element("message_text_assert")
        #     assert asset_more_init._text_content(selector) == '正在保存，请勿关闭页面' or '重命名成功'
        #     print('-----上传文件断言成功-----')
        # except Exception as err:
        #     raise err

    # 右键-编辑
    @allure.title("右键-编辑")
    @pytest.mark.run(order=2)
    def test_asset_more_edit(self, asset_more_init):
        # 重命名
        asset_more_init.asset_more_edit('more_编辑描述')
        '''断言：右键-重命名是否成功'''
        try:
            selector = asset_more_init.read_yaml_element("message_text_assert")
            assert asset_more_init._text_content(selector) == '保存成功'
            print('-----上传文件断言成功-----')
        except Exception as err:
            raise err


    # 右键-下载
    @allure.title("右键-下载")
    @pytest.mark.run(order=3)
    def test_asset_more_download(self, asset_more_init):
        # 下载
        asset_more_init.asset_more_download()
        asset_more_init._wait(1)


    # 右键-下载指定尺寸和大小
    @allure.title("右键-下载指定尺寸和大小")
    @pytest.mark.run(order=4)
    def test_asset_more_download_designated_size(self, asset_more_init):
        # 下载指定尺寸和大小
        asset_more_init.asset_more_download_designated_size('100')
        asset_more_init._wait(1)


    # 右键-分享
    @allure.title("右键-分享")
    @pytest.mark.run(order=5)
    def test_asset_more_share(self, asset_more_init):
        # 分享
        asset_more_init.asset_more_share()


    # 右键-添加到组
    @allure.title("右键-添加到组")
    @pytest.mark.run(order=6)
    def test_asset_more_add_to_group(self, asset_more_init):
        # 添加到组
        asset_more_init.asset_more_add_to_group('test_group_001')


    # 右键-加入素材篮
    @allure.title("右键-加入素材篮")
    @pytest.mark.run(order=7)
    def test_asset_more_add_to_basket(self, asset_more_init):
        # 加入素材篮
        asset_more_init.asset_more_add_to_basket()


    # 右键-修改所有者
    @allure.title("右键-修改所有者")
    @pytest.mark.run(order=8)
    def test_asset_more_reset_the_owner(self, asset_more_init):
        # 修改所有者
        asset_more_init.asset_more_reset_the_owner('刘志杰')


    # 右键-修改权限类型
    @allure.title("右键-修改权限类型")
    @pytest.mark.run(order=9)
    def test_asset_more_modify_category(self, asset_more_init):
        # 修改权限类型
        asset_more_init.asset_more_modify_category()


    # 右键-删除
    @allure.title("右键-删除")
    @pytest.mark.run(order=10)
    def test_asset_more_delete(self, asset_more_init):
        # 删除
        asset_more_init.asset_more_delete()