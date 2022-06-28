import time

import allure
import pytest
from conf.confs import url_assetPage
from pages.assets.AssetBasketPage import AssetBasketPage
from pages.assets.AssetPage import AssetPage

@allure.epic("素材篮主流程")
class TestMainAssetBasketPage:

    # ---主流程-素材篮页面主流程操作---
    @allure.title("素材篮页面主流程操作")
    @pytest.mark.flaky(reruns=1)
    def test_main_asset_basket(self, login_init):
        # 进入素材库页面
        asset_page = AssetPage(login_init)
        asset_page._go(url_assetPage)

        # 上传文件
        asset_page.upload_file()

        # 获取素材篮页面实例
        asset_basket_page = AssetBasketPage(login_init)

        # 点击加入素材篮
        asset_basket_page.add_to_basket()

        # 打开素材篮
        time.sleep(1)
        asset_basket_page._wait(2)
        asset_basket_page.open_basket()
        asset_basket_page._wait(2)

        # 点击清空素材篮
        asset_basket_page.basket_empty()

        # 点击加入素材篮
        asset_basket_page.add_to_basket()

        # 打开素材篮
        time.sleep(1)
        asset_basket_page._wait(2)
        asset_basket_page.open_basket()
        asset_basket_page._wait(2)

        # 分享
        asset_basket_page._wait(2)
        asset_basket_page.basket_share()

        # 点击加入素材篮
        asset_basket_page.add_to_basket()

        # 打开素材篮
        time.sleep(1)
        asset_basket_page._wait(2)
        asset_basket_page.open_basket()
        asset_basket_page._wait(2)

        # 下载
        asset_basket_page.basket_download()

        # 点击加入素材篮
        asset_basket_page.add_to_basket()

        # 打开素材篮
        time.sleep(1)
        asset_basket_page._wait(2)
        asset_basket_page.open_basket()
        asset_basket_page._wait(2)

        # 删除
        asset_basket_page.basket_delete()
        asset_basket_page._wait(5)

        '''断言'''
        selector = asset_basket_page.read_yaml_element("basket_title")
        assert asset_page._is_visible(selector) == False



