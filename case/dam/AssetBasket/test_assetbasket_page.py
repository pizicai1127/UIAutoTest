# -*- coding: utf-8 -*- 
# @Time : 2022/2/9 2:45 下午 
# @Author : liuzhijie
# @File : test_assetbasket_page.py

import allure
import pytest
from conf.asserts import basket_empty_success, share_success
from conf.confs import basket_add_same_asset_assert



class TestAssetBasketPage:

    # 清空素材篮
    @pytest.mark.p0
    @allure.title("清空素材篮")
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=1)
    def test_basket_empty(self, asset_basket_init):
        # 点击清空素材篮
        asset_basket_init.basket_empty()

        '''断言：素材篮清空是否成功'''
        try:
            selector = asset_basket_init.read_yaml_element("basket_empty_success")
            asset_basket_init._wait_for_selector(selector)
            assert asset_basket_init._text_content(selector) == basket_empty_success
            print('-----素材篮清空成功-----')
        except Exception as err:
            raise err


    # 分享
    @pytest.mark.p0
    @allure.title("分享")
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=1)
    def test_basket_share(self,asset_basket_init):
        # 点击分享按钮
        asset_basket_init.basket_share()

        '''断言：素材篮分享是否成功'''
        try:
            selector = asset_basket_init.read_yaml_element("share_success")
            assert asset_basket_init._text_content(selector) == share_success
            print('-----素材篮分享成功-----')
        except Exception as err:
            raise err


    # 下载
    @pytest.mark.p0
    @allure.title("下载")
    @pytest.mark.run(order=3)
    @pytest.mark.flaky(reruns=1)
    def test_basket_download(self,asset_basket_init):
        # 点击下载按钮
        asset_basket_init.basket_download()
        '''断言：素材篮下载是否成功'''
        try:
            asset_basket_init.open_basket()
            selector = asset_basket_init.read_yaml_element("basket_empty_assert")
            assert asset_basket_init._is_visible(selector) == True
            print('-----素材篮下载成功-----')
        except Exception as err:
            raise err


    # 删除素材篮里的素材
    @pytest.mark.p0
    @allure.title("删除素材篮里的素材")
    @pytest.mark.run(order=4)
    @pytest.mark.flaky(reruns=1)
    def test_basket_delete(self, asset_basket_init):
        # 点击删除按钮
        asset_basket_init.basket_delete()


    # 素材篮重复添加相同素材
    @pytest.mark.p0
    @allure.title("素材篮重复添加相同素材")
    @pytest.mark.run(order=5)
    @pytest.mark.flaky(reruns=1)
    def test_basket_add_same_asset(self,asset_basket_init):
        # 素材篮重复添加相同素材
        asset_basket_init._wait(1)
        asset_basket_init.add_to_basket()

        '''断言：素材是否重复加入素材篮'''
        try:
            selector = asset_basket_init.read_yaml_element("basket_message_text_assert")
            assert asset_basket_init._text_content(selector) == basket_add_same_asset_assert
            print('-----测试通过-----')
        except Exception as err:
            raise err

if __name__ == '__main__':
    TestAssetBasketPage()