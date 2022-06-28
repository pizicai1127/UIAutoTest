import allure
import pytest
from conf.confs import url_assetPage, assert_delete_success
from pages.assets.AssetPage import AssetPage
from pages.assets.AssetDetailPage import AssetDetailPage

@allure.epic("主流程")
class TestMainAsset:


    # ---主流程-素材详情页操作---
    @allure.title("素材详情页操作")
    @pytest.mark.flaky(reruns=1)
    def test_asset_main_001(self, main_init, login_init):

        # 上传文件
        main_init.upload_file()
        # 进入素材详情页
        assetDetail_page = AssetDetailPage(login_init)
        assetDetail_page.into_asset_detail_page()
        # 下载素材
        assetDetail_page.detail_download()
        # 分享素材
        assetDetail_page.detail_share_main()
        # 编辑素材-名称
        assetDetail_page.detail_edit("test_file_002")
        # 添加到组-素材组名称
        assetDetail_page.detail_add_to_group("test_group_001")
        # 删除素材
        assetDetail_page.detail_delete()



    # ---主流程-素材批量操作---
    @allure.title("素材批量操作")
    @pytest.mark.flaky(reruns=1)
    def test_asset_main_002(self, login_init, main_init):

        # 上传文件
        main_init.upload_file()

        # hover素材-第一个素材
        main_init.asset_hover()

        # 进入多选模式
        main_init.asset_batch()

        # 点击批量下载按钮
        main_init.asset_batch_download()

        # 点击批量分享按钮
        main_init.asset_batch_share()

        # 点击批量编辑素材
        main_init.asset_batch_edit("UI自动化_批量编辑")

        # hover素材-第一个素材
        main_init.asset_hover()

        # 进入多选模式
        main_init.asset_batch()

        # 重命名
        main_init.asset_batch_rename("UI自动化_重命名")

        # hover素材-第一个素材
        main_init.asset_hover()

        # 进入多选模式
        main_init.asset_batch()

        # 添加到组
        main_init.asset_batch_add_to_group("test_group_001")

        # 加入素材篮
        main_init.asset_batch_add_to_basket()

        # 点击批量删除素材
        main_init.asset_batch_delete()



if __name__ == '__main__':
    TestMainAsset()