# -*- coding: utf-8 -*- 
# @Time : 2022/2/9 2:43 下午 
# @Author : liuzhijie
# @File : test_asset_page.py


# -*- coding: utf-8 -*-
# @Time : 2022/1/25 2:26 下午
# @Author : liuzhijie
# @File : test_asset_page.py
import datetime
import allure
import pytest
from conf.asserts import asset_saved_filters_success, download_pack_success
from conf.confs import upload_success, asset_search_result, batch_share_message_text_assert, \
    batch_edit_message_text_assert, \
    batch_rename_message_text_assert, batch_add_to_group_text_assert, assert_delete_success, asset_saved_filters_name, \
    link_baidu, password_baidu, url_assetPage


class TestAssetPage:

    @pytest.fixture(autouse=True)
    def init_page(self, asset_init):
        asset_init._go(url_assetPage)
        asset_init._wait(1)


    # 上传文件
    @allure.title("上传文件")
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=1)
    def test_upload_file(self, asset_init):
        asset_init.upload_file()
        '''断言：上传文件是否成功'''
        try:
            selector = asset_init.read_yaml_element("upload_success")
            assert upload_success in asset_init._text_content(selector)
            print('-----上传文件断言成功-----')
        except Exception as err:
            raise err





    # 小铃铛列表打开
    @pytest.mark.run(order=2)
    @allure.title("打开小铃铛列表")
    def test_asset_bell_list(self, asset_init):
        asset_init.asset_bell_list()
        '''断言：小铃铛列表打开是否成功'''
        try:
            selector = asset_init.read_yaml_element("bell_list_open_success")
            assert  asset_init._is_visible(selector) == True
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 小铃铛列表消息全部已读
    @pytest.mark.run(order=3)
    @allure.title("小铃铛列表消息全部已读")
    def test_asset_bell_list_all_message_read(self,asset_init):
        asset_init.asset_bell_list_all_message_read()
        '''断言：小铃铛列表消息全部已读是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert  asset_init._text_content(selector) == '已成功将通知全部标记为已读'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # # 上传文件夹
    # def test_upload_folder(self,asset_init):
    #
    #     asset_init.upload_folder(ui_data_folder_path)
    #     '''断言：上传文件夹是否成功'''
    #     try:
    #         selector = asset_init.read_yaml_element("upload_success")
    #         assert upload_success in asset_init._text_content(selector)
    #         print('-----上传文件夹断言成功-----')
    #     except Exception as err:
    #         raise err

    # # 百度云盘同步
    # def test_baidu_transfer(self, asset_init):
    #
    #     asset_init.baidu_transfer(link_baidu,password_baidu)
    #     try:
    #         selector = asset_init.read_yaml_element("upload_success")
    #         assert upload_success in asset_init._text_content(selector)
    #         print('-----百度云盘同步断言成功-----')
    #     except Exception as err:
    #         raise err

    # # MUSE同步
    # def test_baidu_transfer(self, asset_init):
    #
    #     asset_init.muse_transfer(link='链接')
    #     '''断言：MUSE同步是否成功'''
    #     try:
    #         selector = asset_init.read_yaml_element("upload_success")
    #         assert upload_success in asset_init._text_content(selector)
    #         print('-----MUSE同步断言成功-----')
    #     except Exception as err:
    #         raise err


    # 搜索素材
    @allure.title("搜索素材")
    @pytest.mark.run(order=4)
    def test_asset_search(self,asset_init):
        # 搜索素材
        asset_init.asset_search('test_file_001')
        '''断言：搜索素材是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_search_result")
            asset_init._wait_for_selector(selector)
            assert asset_search_result in asset_init._text_content(selector)
            print('-----搜索素材断言成功-----')
        except Exception as err:
            raise err


    # 列表模式
    @allure.title("列表模式")
    @pytest.mark.run(order=5)
    def test_asset_arrangement_list_mode(self,asset_init):
        asset_init.asset_arrangement_list_mode()
        '''断言：切换排列方式是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_list_mode_assert")
            assert asset_init._is_visible(selector) == True
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 平铺模式
    @allure.title("平铺模式")
    @pytest.mark.run(order=6)
    def test_asset_arrangement_tile_mode(self, asset_init):
        asset_init.asset_arrangement_tile_mode()
        '''断言：切换平铺方式是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_name_first")
            assert asset_init._is_visible(selector) == True
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 排序
    @pytest.mark.parametrize('style,ele',[("更新时间","update_time_sort_assert"),
                                          ("最近打开","recently_opened_sort_assert"),
                                          ("素材热度","material_heat_sort_assert"),
                                          ("历史总活跃","history_total_activity_sort_assert"),
                                          ("素材名称","material_name_sort_assert"),
                                          ("创建时间","create_time_sort_assert"),
                                          ("文件大小","file_size_sort_assert"),
                                          ("更新时间", "update_time_sort_assert")
                                          ])
    @allure.title("排序-{style}")
    @pytest.mark.run(order=7)
    @pytest.mark.flaky(reruns=1)
    def test_asset_sort(self, style, ele, asset_init):
        # 排序
        asset_init.asset_sort(style)
        '''断言：排序是否成功'''
        try:
            selector = asset_init.read_yaml_element(ele)
            assert style in asset_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 筛选-我创建的素材
    @allure.title("筛选-我创建的素材")
    @pytest.mark.run(order=8)
    def test_asset_filters_creator_self(self,asset_init):
        #
        asset_init.asset_filters_creator_self()
        '''断言：筛选是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_filters_creator")
            assert '我创建的素材' in asset_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 筛选-品牌
    @allure.title("筛选-品牌")
    @pytest.mark.run(order=9)
    def test_asset_filters_brand(self,asset_init):
        # 品牌
        asset_init.asset_filters_brand()
        '''断言：筛选是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_filters_brand")
            assert 'Tezign 特赞' in asset_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 筛选-文件格式
    @allure.title("筛选-文件格式")
    @pytest.mark.run(order=10)
    def test_asset_filters_file_format(self,asset_init):
        # 文件格式
        asset_init.asset_filters_file_format()
        '''断言：筛选是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_filters_file_format")
            assert 'JPG' in asset_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 筛选-创建时间
    @allure.title("筛选-创建时间")
    @pytest.mark.run(order=11)
    def test_asset_filters_creation_time(self, asset_init):
        # 创建时间
        asset_init.asset_filters_creation_time()
        '''断言：筛选是否成功'''
        try:
            time_now = datetime.date.today().strftime('%Y.%m.%d')
            selector = asset_init.read_yaml_element("asset_filters_creation_time")
            assert time_now in asset_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 筛选-图片主色
    @allure.title("筛选-图片主色")
    @pytest.mark.run(order=12)
    def test_asset_filters_picture_main_color(self,asset_init):
        # 图片主色
        asset_init.asset_filters_picture_main_color()
        '''断言：筛选是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_filters_picture_main_color")
            assert '#e83a30' in asset_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 筛选-复选框
    # @allure.title("筛选-复选框")
    # @pytest.mark.run(order=13)
    # def test_asset_filters_checkbox(self,asset_init):
    #     # 复选框
    #     asset_init.asset_filters_checkbox()
    #     '''断言：筛选是否成功'''
    #     try:
    #         selector = asset_init.read_yaml_element("asset_filters_checkbox")
    #         assert '1' in asset_init._text_content(selector)
    #         print('-----排序断言成功-----')
    #     except Exception as err:
    #         raise err


    # 筛选-明星标签
    @allure.title("筛选-明星标签")
    @pytest.mark.run(order=14)
    def test_asset_filters_star_label(self,asset_init):
        # 复选框
        asset_init.asset_filters_star_label()
        '''断言：筛选是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_filters_star_label")
            assert '杨幂' in asset_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 保存常用筛选
    @allure.title("保存常用筛选")
    @pytest.mark.run(order=15)
    def test_asset_saved_filters(self, asset_init):
        asset_init.asset_saved_filters(asset_saved_filters_name)
        '''断言：保存常用筛选是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert asset_init._text_content(selector) == asset_saved_filters_success
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 常用筛选清除
    @allure.title("常用筛选清除")
    @pytest.mark.run(order=16)
    def test_asset_common_filters_dump(self, asset_init):
        asset_init.asset_common_filters_dump()
        '''断言：常用筛选清除是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert asset_init._text_content(selector) == "取消成功"
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 相似图筛选
    @allure.title("相似图筛选")
    @pytest.mark.run(order=17)
    def test_asset_search_similar_pic(self, asset_init):
        # hover上素材
        asset_init.asset_hover()
        # 点击查找相似图
        asset_init.asset_search_similar_pic()
        '''断言：相似图筛选是否成功'''
        try:
            selector = asset_init.read_yaml_element("asset_name_first")
            asset_init._wait_for_selector(selector)
            assert asset_init.page.is_visible(selector) == True
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 加入素材篮
    @allure.title("加入素材篮")
    @pytest.mark.run(order=18)
    def test_add_to_asset_basket(self,asset_init):
        # 加入素材篮
        asset_init.add_to_asset_basket()
        asset_init._wait(1.5)
        '''断言：加入素材篮是否成功-属性title不存在'''
        try:
            selector = asset_init.read_yaml_element("join_basket_success")
            assert asset_init._is_visible(selector) == True
            print('-----加入素材篮成功-----')
        except Exception as err:
            raise err

    # # 批量编辑-打包下载
    # def test_asset_batch_download(self,asset_init):
    #     # 再上传一个素材
    #     asset_init.upload_file(ui_data_file_path)
    #     # hover素材（第一个）
    #     asset_init.asset_hover()
    #     # 批量编辑
    #     asset_init.asset_batch()
    #     # 选中素材（第二个）
    #     asset_init.asset_second_click()
    #     # 下载
    #     asset_init.asset_batch_download()
    #     asset_init._wait(10)
    #     '''断言：批量下载是否成功'''
    #     try:
    #         selector = asset_init.read_yaml_element("download_pack_success")
    #         assert asset_init._text_content(selector) == download_pack_success
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err


    # 批量编辑-分享
    @allure.title("批量编辑-分享")
    @pytest.mark.run(order=19)
    @pytest.mark.flaky(reruns=1)
    def test_asset_batch_share(self,asset_init):
        # hover素材
        asset_init.asset_hover()
        # 批量编辑
        asset_init.asset_batch()
        # 分享
        asset_init.asset_batch_share()
        '''断言：批量分享是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert asset_init._text_content(selector) == batch_share_message_text_assert
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 批量编辑-素材名称
    @allure.title("批量编辑-素材名称")
    @pytest.mark.run(order=20)
    @pytest.mark.flaky(reruns=1)
    def test_asset_batch_edit(self,asset_init):
        # hover素材
        asset_init.asset_hover()
        # 批量编辑
        asset_init.asset_batch()
        # 编辑-素材名称
        asset_init.asset_batch_edit('UI自动化测试-批量编辑-名称')

        '''断言：批量编辑（名称）是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert asset_init._text_content(selector) == batch_edit_message_text_assert
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 批量编辑-重命名
    @allure.title("批量编辑-重命名")
    @pytest.mark.run(order=21)
    @pytest.mark.flaky(reruns=1)
    def test_asset_batch_rename(self,asset_init):
        # hover素材
        asset_init.asset_hover()
        # 进入多选模式
        asset_init.asset_batch()
        # 编辑-素材重命名
        asset_init.asset_batch_rename('UI自动化测试-批量编辑-重命名')
        '''断言：批量编辑重名称是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert asset_init._text_content(selector) == "正在保存，请勿关闭页面"
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 批量编辑-添加到组-新建组
    @allure.title("批量编辑-添加到组-新建组")
    @pytest.mark.run(order=22)
    def test_asset_batch_add_to_group_build(self, asset_init):
        # hover素材
        asset_init.asset_hover()
        # 进入多选模式
        asset_init.asset_batch()
        # 添加到新建素材组：UI自动化测试-添加到新建组
        asset_init.asset_batch_add_to_group_build('UI自动化测试-添加到新建组')
        '''断言：添加到组是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert asset_init._text_content(selector) == batch_add_to_group_text_assert
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 批量编辑-添加到组-已存在组
    @allure.title("批量编辑-添加到组-已存在组")
    @pytest.mark.run(order=23)
    def test_asset_batch_add_to_group_exist(self,asset_init):
        # hover素材
        asset_init.asset_hover()
        # 进入多选模式
        asset_init.asset_batch()
        # 添加到存在的素材组：test_group
        asset_init.asset_batch_add_to_group('test_group_001')
        '''断言：添加到组是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert asset_init._text_content(selector) == batch_add_to_group_text_assert
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 删除素材
    @allure.title("删除素材")
    @pytest.mark.run(order=24)
    @pytest.mark.flaky(reruns=1)
    def test_asset_batch_delete(self,asset_init):
        # hover素材
        asset_init.asset_hover()
        # 进入多选模式
        asset_init.asset_batch()
        # 删除素材
        asset_init.asset_batch_delete()
        '''断言：删除素材是否成功'''
        try:
            selector = asset_init.read_yaml_element("message_text_assert")
            assert asset_init._text_content(selector) == assert_delete_success
            print('-----断言成功-----')
        except Exception as err:
            raise err

