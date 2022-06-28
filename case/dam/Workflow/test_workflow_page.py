# -*- coding: utf-8 -*- 
# @Time : 2022/4/24 3:17 下午 
# @Author : liuzhijie
# @File : test_workflow_page.py
from datetime import date

import allure
import pytest

from common.file_method import FileMethod
from conf.confs import url_workflowPage, account_LZJ_006
file_path = FileMethod().get_file_path('data', '', 'test_workflow_file.jpg')


class TestWorkflowPage:


    @allure.title("切换Tab")
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=1)
    # 切换Tab
    def test_workflow_tab(self, workflow_init):
        # Tab-协作设计中项目
        workflow_init.workflow_tab_cooperation_project()
        # Tab-审批中项目
        workflow_init.workflow_tab_in_audit_project()
        # Tab-审批未通过项目
        workflow_init.workflow_tab_audit_fail_project()
        # Tab-审批已通过项目
        workflow_init.workflow_tab_audit_adopt_project()
        # Tab-所有项目
        workflow_init.workflow_tab_all_project()


    @allure.title("排序-修改时间")
    @pytest.mark.run(order=2)
    # 排序-修改时间
    def test_workflow_sort_update_time(self, workflow_init):
        # 修改时间
        workflow_init.workflow_sort_update_time()
        try:
            selector = workflow_init.read_yaml_element("workflow_sort_button")
            assert '修改时间' in workflow_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("排序-创建时间")
    @pytest.mark.run(order=3)
    # 排序-创建时间
    def test_workflow_sort_create_time(self, workflow_init):
        # 创建时间
        workflow_init.workflow_sort_create_time()
        try:
            selector = workflow_init.read_yaml_element("workflow_sort_button")
            assert '创建时间' in workflow_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("新建项目")
    @pytest.mark.run(order=4)
    # 新建项目
    def test_workflow_create_project(self, workflow_init):
        # 新建项目
        workflow_init.workflow_create_project(f'UI自动化测试项目-{account_LZJ_006}', 'UI自动化测试项目-描述', '上海', '特赞供应商',)
        '''断言：新建项目是否否成功'''
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '项目创建成功' in workflow_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("上传素材")
    @pytest.mark.run(order=5)
    # 上传素材
    def test_workflow_upload_file(self, workflow_init):
        # 上传素材
        workflow_init.workflow_upload_file(file_path)
        '''断言：上传素材是否成功'''
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '保存成功' in workflow_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("素材-批量编辑-编辑")
    @pytest.mark.run(order=6)
    # 素材-批量编辑-编辑
    def test_workflow_batch_edit_project(self, workflow_init):
        # 素材-批量编辑-编辑
        workflow_init.workflow_batch_edit_project('素材-批量编辑-编辑-描述')
        '''断言：批量编辑素材是否成功'''
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '保存成功' in workflow_init._text_content(selector)
            print('-----断言成功-----')
            # 取消选择-回到批量操作
            selector = workflow_init.read_yaml_element("batch_control_select_button")
            workflow_init._click(selector)
            workflow_init._mouse_move(300, 300)
            workflow_init._wait(1)
        except Exception as err:
            raise err


    @allure.title("素材-批量编辑-分享")
    @pytest.mark.run(order=7)
    # 素材-批量编辑-分享
    def test_workflow_batch_share_project(self, workflow_init):
        # 素材-批量编辑-分享
        workflow_init.workflow_batch_share_project()
        '''断言：批量分享素材是否成功'''
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '链接创建并复制成功' in workflow_init._text_content(selector)
            print('-----断言成功-----')
            # 关闭分享弹窗
            workflow_init._wait(1)
            selector = workflow_init.read_yaml_element("workflow_share_close_button")
            workflow_init._click(selector)
            # 取消选择-回到批量操作
            selector = workflow_init.read_yaml_element("batch_control_select_button")
            workflow_init._click(selector)
            workflow_init._mouse_move(300, 300)
        except Exception as err:
            raise err


    @allure.title("素材-批量编辑-删除")
    @pytest.mark.run(order=8)
    # 素材-批量编辑-删除
    def test_workflow_batch_delete_project(self, workflow_init):
        # 素材-批量编辑-删除
        workflow_init.workflow_batch_delete_project()
        # 取消选择-回到批量操作
        selector = workflow_init.read_yaml_element("batch_control_select_button")
        workflow_init._click(selector)
        workflow_init._mouse_move(300, 300)


    @allure.title("编辑项目")
    @pytest.mark.run(order=9)
    # 编辑项目
    def test_workflow_edit_project(self, workflow_init):
        # 上传素材
        workflow_init.workflow_upload_file(file_path)
        # 编辑项目
        workflow_init.workflow_edit_project(f'UI自动化测试项目_编辑', 'UI自动化测试项目-描述_编辑', '上海_编辑', '特赞供应商_编辑',)
        '''断言：编辑项目是否否成功'''
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '修改成功' in workflow_init._text_content(selector)
            print('-----断言成功-----')
            workflow_init._wait(4)
        except Exception as err:
            raise err


    @allure.title("分享项目")
    @pytest.mark.run(order=10)
    # 分享项目
    def test_workflow_share_project(self, workflow_init):
        # 分享项目
        workflow_init.workflow_share_project()
        '''断言：分享项目是否成功'''
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '分享链接' in workflow_init._text_content(selector)
            print('-----断言成功-----')
            # 关闭分享弹窗
            workflow_init._wait(0.5)
            workflow_init._mouse_move(300, 300)
            workflow_init._mouse_left_click(300, 300)
        except Exception as err:
            raise err


    @allure.title("项目审批-简单审批模板")
    @pytest.mark.run(order=11)
    def test_workflow_submit_audit_project_one(self, workflow_init):
        # 项目审批-简单审批
        workflow_init.workflow_submit_audit_project_one('lzj001')
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '提交成功' in workflow_init._text_content(selector)
            print('-----断言成功-----')
            workflow_init._wait(3)
        except Exception as err:
            raise err


    @allure.title("项目撤销审批")
    @pytest.mark.run(order=12)
    def test_workflow_project_submit_audit_revoke(self, workflow_init):
        # 项目撤销审批
        workflow_init.workflow_project_submit_audit_revoke()
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '撤回成功' in workflow_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("项目审批-或签审批模板-重新提交")
    @pytest.mark.run(order=13)
    def test_workflow_submit_audit_project_more(self, workflow_init):
        # 项目审批-或签审批模板
        workflow_init.workflow_submit_audit_project_more('lzj001', 'lzj002')
        try:
            selector = workflow_init.read_yaml_element("message_text_assert")
            assert '提交成功' in workflow_init._text_content(selector)
            print('-----断言成功-----')
            workflow_init.workflow_project_submit_audit_revoke()
        except Exception as err:
            raise err


    @allure.title("项目-评论")
    @pytest.mark.run(order=14)
    def test_workflow_comment(self, workflow_init):
        # 切换到评论Tab
        workflow_init.workflow_comment_tab()
        # 项目-评论
        workflow_init.workflow_comment('UI自动化测试-评论')
        try:
            selector = workflow_init.read_yaml_element("workflow_comment_first")
            assert 'UI自动化测试-评论' in workflow_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("项目-评论-删除")
    @pytest.mark.run(order=15)
    def test_workflow_comment_delete(self, workflow_init):
        # 项目-评论-删除
        workflow_init.workflow_comment_delete()


    @allure.title("项目-日志")
    @pytest.mark.run(order=16)
    def test_workflow_project_log_tab(self, workflow_init):
        # 切换到日志Tab
        workflow_init.workflow_project_log_tab()
        try:
            time = f'{date.today()}'
            selector = workflow_init.read_yaml_element("workflow_project_log_assert")
            assert time in workflow_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("搜索项目")
    @pytest.mark.run(order=17)
    # 搜索项目
    def test_workflow_search_project(self, workflow_init):
        # 回到项目首页
        workflow_init._go(url_workflowPage)
        # 搜索项目
        workflow_init.workflow_search_project('UI自动化测试')
        '''断言：搜索项目是否成功'''
        try:
            selector = workflow_init.read_yaml_element("workflow_project_name")
            assert 'UI自动化测试' in workflow_init._text_content(selector)
            print('-----断言成功-----')
        except Exception as err:
            raise err


    @allure.title("删除项目")
    @pytest.mark.run(order=18)
    # 删除项目
    def test_workflow_delete_project(self, workflow_init):
        # 删除项目
        workflow_init.workflow_delete_project()