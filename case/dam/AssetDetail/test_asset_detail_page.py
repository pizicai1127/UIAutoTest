# -*- coding: utf-8 -*- 
# @Time : 2022/2/14 7:03 下午 
# @Author : liuzhijie
# @File : test_asset_detail_page.py
import datetime

import allure
import pytest

from conf.asserts import detail_tab_export_format_success, share_success, detail_edit_save_success, \
    detail_add_to_group_success, delete_success, detail_enclosure_set_preview_version_success, \
    detail_version_upload_success, detail_download_designated_size_success
from conf.confs import asset_name, ui_data_enclosure_path, detail_comment_text, ui_data_file_path, url_assetPage


class TestAssetDetailPage:

    @pytest.fixture(autouse=True)
    def init_page(self, asset_init):
        asset_init._wait(1)

    # tab 切换
    @allure.feature("素材详情页模块")
    @allure.title("tab切换")
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=1)
    def test_detail_tab(self,asset_init,asset_detail_init):
        asset_detail_init.detail_tab_switch()
        '''断言：切换tab是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_tab_details")
            assert asset_detail_init._text_content(selector) == '详情'
            print('-----切换tab断言成功-----')
        except Exception as err:
            raise err


    # # 下载
    # def test_detail_download(self,asset_detail_init):
    #     asset_detail_init.detail_download()
    #     time.sleep(5)
    #     '''断言：下载是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_download_success")
    #         assert asset_detail_init._is_visible(selector)
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err


    # # 下载带附件
    # def test_detail_download_all(self,asset_detail_init):
    #     asset_detail_init.detail_download_all()
    #     '''断言：下载是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_tab_export_format_success")
    #         event = asset_detail_init.detail_download_all()
    #         assert asset_detail_init._expect_download(event)
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err

    # 格式转换
    @allure.title("格式转换")
    @pytest.mark.run(order=2)
    def test_detail_export_format(self,asset_detail_init):
        asset_detail_init.detail_export_format()
        '''断言：格式导出是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_tab_export_format_success")
            asset_detail_init._wait_for_selector(selector)
            selector = asset_detail_init.read_yaml_element("detail_tab_export_format_success_assert")
            assert asset_detail_init._text_content(selector) == detail_tab_export_format_success
            print('-----断言成功-----')
            asset_detail_init.detail_export_format_cancel()
        except Exception as err:
            raise err


    # 下载指定尺寸或大小
    @allure.title("格式转换")
    @pytest.mark.run(order=2)
    def test_detail_download_designated_size(self, asset_detail_init):
        asset_detail_init.detail_download_designated_size()
        asset_detail_init._wait(1)
    #     '''断言：格式导出是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_download_designated_size_success")
    #         assert asset_detail_init._text_content(selector) == detail_download_designated_size_success
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err



    # # 下载带水印
    # def test_detail_download_watermark(self):
    #     pass


    # 分享
    @allure.title("分享")
    @pytest.mark.run(order=3)
    def test_detail_share(self, asset_detail_init):
        asset_detail_init.detail_share()
        '''断言：分享是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("message_text_assert")
            assert asset_detail_init._text_content(selector) == share_success
            print('-----断言成功-----')
            asset_detail_init._wait(2)
        except Exception as err:
            raise err


    # 编辑
    @allure.title("编辑")
    @pytest.mark.run(order=4)
    def test_detail_edit(self, asset_detail_init):
        asset_detail_init.detail_edit(asset_name)
        asset_detail_init._wait(1)
        '''断言：编辑是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("message_text_assert")
            assert asset_detail_init._text_content(selector) == detail_edit_save_success
            print('-----断言成功-----')
            asset_detail_init._wait(2)
        except Exception as err:
            raise err


    # 添加到组（现有组）
    @allure.title("添加到组（现有组）")
    @pytest.mark.run(order=5)
    def test_detail_add_to_group(self,asset_detail_init):
        asset_detail_init.detail_add_to_group('test_group_001')
        asset_detail_init._wait(1)
        '''断言：添加到组是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("message_text_assert")
            assert asset_detail_init._text_content(selector) == detail_add_to_group_success
            print('-----断言成功-----')
            asset_detail_init._wait(2)
        except Exception as err:
            raise err


    # 添加到组（新建组）
    @allure.title("添加到组（新建组）")
    @pytest.mark.run(order=6)
    def test_detail_add_to_group_build(self,asset_detail_init):
        asset_detail_init.detail_add_to_group_build('UI自动化测试-添加到新建组')
        asset_detail_init._wait(1)
        '''断言：添加到组是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("message_text_assert")
            assert asset_detail_init._text_content(selector) == detail_add_to_group_success
            print('-----断言成功-----')
            asset_detail_init._wait(2)
        except Exception as err:
            raise err


    # #上传附件
    # def test_detail_upload_enclosure(self,asset_detail_init):
    #     asset_detail_init.detail_upload_enclosure(ui_data_enclosure_path)
    #     '''断言：上传附件是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_upload_enclosure_name")
    #         assert asset_detail_init._text_content(selector) == 'test_enclosure_001.jpeg'
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err


    # # 附件预览
    # def test_detail_enclosure_preview(self,asset_detail_init):
    #     asset_detail_init.detail_enclosure_preview()
    #     '''断言：附件预览是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_enclosure_preview_name")
    #         assert asset_detail_init._text_content(selector) == 'test_enclosure_001.jpeg'
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err


    # # 附件下载
    # def test_detail_enclosure_download(self, asset_detail_init):
    #     asset_detail_init.detail_enclosure_download()
    #     '''断言：附件下载是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_enclosure_preview_name")
    #         assert asset_detail_init._text_content(selector) == 'test_enclosure_001.jpeg'
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err


    # # 附件设为预览版本
    # def test_detail_enclosure_set_preview_version(self, asset_detail_init):
    #     asset_detail_init.detail_enclosure_set_preview_version()
    #     '''断言：附件设为预览版本是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_enclosure_set_preview_version_success")
    #         assert asset_detail_init._text_content(selector) == detail_enclosure_set_preview_version_success
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err


    # # 附件删除
    # def test_detail_enclosure_delete(self, asset_detail_init):
    #     # 进入编辑状态
    #     selector = asset_detail_init.read_yaml_element("detail_edit_button")
    #     asset_detail_init._click(selector)
    #     # 点击删除按钮
    #     asset_detail_init.detail_enclosure_delete()
    #     '''断言：附件删除是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_enclosure_delete_success")
    #         assert asset_detail_init._is_visible(selector) == False
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err


    # 智能打标-描述(输入框)
    @allure.title('智能打标-描述')
    @pytest.mark.run(order=7)
    def test_detail_intelligent_marking_input_box(self,asset_detail_init):
        # 进入编辑状态
        asset_detail_init.into_detail_edit_page()
        # 打标-输入描述内容
        asset_detail_init.detail_intelligent_marking_input_box('UI自动化测试-智能打标-描述')
        '''断言：打标是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_intelligent_marking_success")
            assert asset_detail_init._text_content(selector) == 'UI自动化测试-智能打标-描述'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 智能打标-营销创业（下拉复选框）
    @allure.title('智能打标-营销创业')
    @pytest.mark.run(order=8)
    def test_detail_intelligent_marking_drop_down_check_box(self, asset_detail_init):
        # 进入编辑状态
        asset_detail_init.into_detail_edit_page()
        # 打标-营销创业
        asset_detail_init.detail_intelligent_marking_drop_down_check_box()
        # '''断言：打标是否成功'''
        # try:
        #     selector = asset_detail_init.read_yaml_element("detail_marketing_creativity_success")
        #     assert asset_detail_init._text_content(selector) == '创意策划 / 文案'
        #     print('-----断言成功-----')
        # except Exception as err:
        #     raise err


    # 智能打标-自定义标签（输入后变成标签）
    @allure.title('智能打标-自定义标签')
    @pytest.mark.run(order=9)
    def test_intelligent_marking_label_input_box(self, asset_detail_init):
        # 进入编辑状态
        asset_detail_init.into_detail_edit_page()
        # 打标-自定义标签
        asset_detail_init.detail_intelligent_marking_label_input_box('UI自动化测试-智能打标-自定义标签')
        '''断言：打标是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_custom_label_success")
            asset_detail_init._wait_for_selector(selector)
            assert asset_detail_init._text_content(selector) == 'UI自动化测试-智能打标-自定义标签'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 智能打标-素材发布日（日期控件）
    @allure.title('智能打标-素材发布日')
    @pytest.mark.run(order=10)
    def test_detail_intelligent_marking_date_control_box(self, asset_detail_init):
        # 进入编辑状态
        asset_detail_init.into_detail_edit_page()
        # 打标-素材发布日
        asset_detail_init.detail_intelligent_marking_date_control_box()
        '''断言：打标是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_release_date_success")
            assert asset_detail_init._text_content(selector) == datetime.date.today().strftime('%Y.%m.%d')
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 智能打标-限制使用渠道（多选项）
    @allure.title('智能打标-限制使用渠道')
    @pytest.mark.run(order=11)
    def test_detail_intelligent_marking_more_selects_box(self, asset_detail_init):
        # 进入编辑状态
        asset_detail_init.into_detail_edit_page()
        # 打标-限制使用渠道
        asset_detail_init.detail_intelligent_marking_more_selects_box()
        '''断言：打标是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_limit_channel_success")
            assert asset_detail_init._text_content(selector) == '官方公众号'
            print('-----断言成功-----')
        except Exception as err:
            raise err

    # 智能打标-测试类型为8的筛选（复选带出下层选项）
    @allure.title('智能打标-测试类型为8的筛选')
    @pytest.mark.run(order=12)
    def test_detail_intelligent_marking_more_level_check_box(self, asset_detail_init):
        # 进入编辑状态
        asset_detail_init.into_detail_edit_page()
        # 打标-测试类型为8的筛选
        asset_detail_init.detail_intelligent_marking_more_level_check_box()
        '''断言：打标是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_test_style_success")
            asset_detail_init._wait_for_selector(selector)
            assert '1' in asset_detail_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # # 编辑素材-权限类型切换
    # @pytest.mark.parametrize("permission_type, ele",[("企业内外部全员可下载","company_inside_and_outside_all_download_assert"),
    #                                                  ("企业全员通用素材","company_all_download_assert"),
    #                                                  ("部门管控类素材","department_control_assert"),
    #                                                  ("部门私有素材","department_private_assert",),
    #                                                  ("个人管理素材","personal_management_assert",),
    #                                                  ("个人管控类素材","personal_control_assert",),
    #                                                  ("自定义权限","custom")
    #                                                  ]
    #                          )
    # @allure.title("权限类型切换-{permission_type}")
    # def test_detail_permission_type(self, permission_type, ele, asset_detail_init):
    #     # 进入编辑状态
    #     asset_detail_init.into_detail_edit_page()
    #     asset_detail_init._wait(1)
    #     # 权限类型切换
    #     asset_detail_init.detail_permission_type(permission_type)
    #     '''断言：排序是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element(ele)
    #         assert permission_type in asset_detail_init._text_content(selector)
    #         print('-----排序断言成功-----')
    #         asset_detail_init.detail_save()
    #     except Exception as err:
    #         raise err



    # 编辑素材-权限类型切换-企业全员通用素材
    @allure.title("权限类型切换-企业全员通用素材")
    @pytest.mark.run(order=13)
    def test_detail_permission_type_company_inside_and_outside_all_download(self, asset_detail_init):
        #进入编辑状态
        asset_detail_init.into_detail_edit_page()
        # 权限类型切换
        asset_detail_init.detail_permission_type("企业全员通用素材")
        '''断言：排序是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("company_inside_and_outside_all_download_assert")
            assert "企业全员通用素材" in asset_detail_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 编辑素材-权限类型切换-部门私有素材
    @allure.title("权限类型切换-部门私有素材")
    @pytest.mark.run(order=14)
    def test_detail_permission_type_department_control(self, asset_detail_init):
        # 权限类型切换
        asset_detail_init.detail_permission_type("部门私有素材")
        '''断言：排序是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("department_control_assert")
            assert "部门私有素材" in asset_detail_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 编辑素材-权限类型切换-部门管控类素材
    @allure.title("权限类型切换-部门管控类素材")
    @pytest.mark.run(order=15)
    def test_detail_permission_type_department_private(self, asset_detail_init):
        # 权限类型切换
        asset_detail_init.detail_permission_type("部门管控类素材")
        '''断言：排序是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("department_private_assert")
            assert "部门管控类素材" in asset_detail_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 编辑素材-权限类型切换-个人管理素材
    @allure.title("权限类型切换-个人管理素材")
    @pytest.mark.run(order=16)
    def test_detail_permission_type_personal_management(self, asset_detail_init):
        # 权限类型切换
        asset_detail_init.detail_permission_type("个人管理素材")
        '''断言：排序是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("personal_management_assert")
            assert "个人管理素材" in asset_detail_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 编辑素材-权限类型切换-个人管控类素材
    @allure.title("权限类型切换-个人管控类素材")
    @pytest.mark.run(order=17)
    def test_detail_permission_type_personal_control(self, asset_detail_init):
        # 权限类型切换
        asset_detail_init.detail_permission_type("个人管控类素材")
        '''断言：排序是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("personal_control_assert")
            assert "个人管控类素材" in asset_detail_init._text_content(selector)
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 编辑素材-权限类型切换-自定义权限
    @allure.title("权限类型切换-自定义权限")
    @pytest.mark.run(order=18)
    def test_detail_permission_type_custom(self, asset_detail_init):
        # 权限类型切换
        asset_detail_init.detail_permission_type("自定义权限")
        '''断言：排序是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("custom_assert")
            assert "自定义权限" in asset_detail_init._text_content(selector)
            print('-----排序断言成功-----')
            asset_detail_init._wait(1)
            asset_detail_init.detail_save()
        except Exception as err:
            raise err


    # 编辑素材-增加权限
    @allure.title("编辑素材-增加权限")
    @pytest.mark.run(order=19)
    def test_detail_add_permission(self, asset_detail_init):
        asset_detail_init.into_detail_edit_page()
        # 增加权限
        asset_detail_init.detail_add_permission("蔡智")
        '''断言：排序是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("permission_first_name")
            assert asset_detail_init._text_content(selector) == '蔡智'
            print('-----排序断言成功-----')
        except Exception as err:
            raise err


    # 编辑素材-清除权限
    @allure.title("编辑素材-清除权限")
    @pytest.mark.run(order=20)
    def test_detail_remove_permission(self, asset_detail_init):
        # 清除权限
        asset_detail_init.detail_remove_permission()
        '''断言：排序是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("permission_remove_success")
            assert asset_detail_init._text_content(selector) != '蔡智'
            print('-----排序断言成功-----')
            asset_detail_init.detail_save()
        except Exception as err:
            raise err


    # 评论
    @allure.title("评论")
    @pytest.mark.run(order=21)
    def test_detail_comment(self,asset_detail_init):
        asset_detail_init.detail_comment(detail_comment_text)
        '''断言：评论是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_comment_success")
            assert asset_detail_init._text_content(selector) == detail_comment_text
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 日志
    @allure.title("日志")
    @pytest.mark.run(order=22)
    def test_detail_logs(self, asset_detail_init):
        asset_detail_init.detail_logs()
        '''断言：日志是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("detail_logs_success")
            asset_detail_init._wait_for_selector(selector)
            assert asset_detail_init._is_visible(selector) == True
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # # 版本管理-上传新版本
    # def test_detail_version_upload(self,asset_detail_init):
    #     # 上传新版本
    #     asset_detail_init.detail_version_upload(ui_data_enclosure_path)
    #     '''断言：评论是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("message_text_assert")
    #         assert asset_detail_init._text_content(selector) == detail_version_upload_success
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err


    # # 版本管理-查看历史版本
    # def test_detail_history_version(self,asset_detail_init):
    #     # 上传新版本
    #     asset_detail_init.detail_version_upload(ui_data_enclosure_path)
    #     # 查看历史版本
    #     asset_detail_init.detail_history_version()
    #     '''断言：查看历史版本是否成功'''
    #     try:
    #         selector = asset_detail_init.read_yaml_element("detail_history_version_success")
    #         assert asset_detail_init._is_visible(selector) == True
    #         print('-----断言成功-----')
    #     except Exception as err:
    #         raise err



    # 删除
    @allure.title("删除")
    @pytest.mark.run(order=23)
    def test_detail_delete(self,asset_detail_init):
        asset_detail_init._wait(2)
        # 删除素材
        asset_detail_init.detail_delete()
        '''断言：删除是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("message_text_assert")
            assert asset_detail_init._text_content(selector) == delete_success
            print('-----断言成功-----')
            asset_detail_init._wait(2)
        except Exception as err:
            raise err


    # 下载权限申请
    @allure.title("下载权限申请")
    @pytest.mark.run(order=24)
    def test_detail_permission_application_download(self, asset_init, asset_detail_init):
        asset_init._go(url_assetPage)
        asset_init._wait(0.5)
        asset_init.asset_search('quanxianshenqing')
        asset_detail_init.into_asset_detail_page()
        asset_detail_init.detail_permission_application_download('UI自动化测试-下载权限测试理由')

        '''断言：下载权限申请是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("permission_application_success")
            asset_detail_init._wait_for_selector(asset_detail_init.read_yaml_element("permission_application_know_button"))
            assert asset_detail_init._text_content(selector) == '提交成功'
            print('-----断言成功-----')
        except Exception as err:
            raise err


    # 编辑权限申请
    @allure.title("编辑权限申请")
    @pytest.mark.run(order=25)
    def test_detail_permission_application_edit(self, asset_init, asset_detail_init):
        asset_init._go(url_assetPage)
        asset_init._wait(0.5)
        asset_init.asset_search('quanxianshenqing')
        asset_detail_init.into_asset_detail_page()
        asset_detail_init.detail_permission_application_edit('UI自动化测试-编辑权限测试理由')
        '''断言：编辑权限申请是否成功'''
        try:
            selector = asset_detail_init.read_yaml_element("permission_application_success")
            asset_detail_init._wait_for_selector(asset_detail_init.read_yaml_element("permission_application_know_button"))
            assert asset_detail_init._text_content(selector) == '提交成功'
            print('-----断言成功-----')
        except Exception as err:
            raise err



if __name__ == '__main__':
    pytest.main(['-vs', 'test_asset_detail_page::TestAssetDetailPage'])