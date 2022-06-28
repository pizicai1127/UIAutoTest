# -*- coding: utf-8 -*- 
# @Time : 2022/4/24 3:24 下午 
# @Author : liuzhijie
# @File : WorkFlowPage.py


from pages.basepage import BasePage

class WorkflowPage(BasePage):

    # 新建项目
    def workflow_create_project(self, name, describe, city, supplier):
        # 点击"新建项目"按钮
        selector = self.read_yaml_element("workflow_create_project_button")
        self._click(selector)
        # 输入"项目名称"
        selector = self.read_yaml_element("workflow_project_name_input")
        self._fill(selector, name)
        # 输入"描述"
        selector = self.read_yaml_element("workflow_describe_input")
        self._fill(selector, describe)
        # 输入"下单城市"
        selector = self.read_yaml_element("workflow_order_city_input")
        self._fill(selector, city)
        # 选择"下单日期"-点击"日期"输入框
        selector = self.read_yaml_element("workflow_order_date_input")
        self._click(selector)
        # 选择"下单日期"-点击"今天"按钮
        selector = self.read_yaml_element("workflow_order_date_today_button")
        self._click(selector)
        # 输入"供应商"
        selector = self.read_yaml_element("workflow_supplier_input")
        self._fill(selector, supplier)
        # 点击"下一步"按钮
        selector = self.read_yaml_element("workflow_next_step_button")
        self._click(selector)
        # 点击"确认"按钮
        selector = self.read_yaml_element("workflow_confirm_button")
        self._click(selector)


    # 批量新建项目
    def workflow_batch_create_project(self, path):
        # 点击"新建项目"按钮
        selector = self.read_yaml_element("workflow_batch_create_project_button")
        self._click(selector)
        # 输入文件路径
        selector = self.read_yaml_element("workflow_batch_create_project_upload_input")
        self._upload(selector, path)
        # 点击"确认"按钮
        selector = self.read_yaml_element("workflow_batch_create_project_confirm_button")
        self._click(selector)


    # 所有项目Tab切换
    def workflow_tab_all_project(self):
        # 点击"所有项目"Tab
        selector = self.read_yaml_element("workflow_tab_all_project")
        self._click(selector)


    # 协作设计项目Tab切换
    def workflow_tab_cooperation_project(self):
        # 点击"协作设计中"Tab
        selector = self.read_yaml_element("workflow_tab_cooperation_project")
        self._click(selector)


    # 审批中Tab切换
    def workflow_tab_in_audit_project(self):
        # 点击"审批中"Tab
        selector = self.read_yaml_element("workflow_tab_in_audit_project")
        self._click(selector)


    # 审批未通过Tab切换
    def workflow_tab_audit_fail_project(self):
        # 点击"审批中"Tab
        selector = self.read_yaml_element("workflow_tab_audit_fail_project")
        self._click(selector)


    # 审批已通过Tab切换
    def workflow_tab_audit_adopt_project(self):
        # 点击"审批中"Tab
        selector = self.read_yaml_element("workflow_tab_audit_adopt_project")
        self._click(selector)


    # 排序-创建时间
    def workflow_sort_create_time(self):
        # hover排序按钮
        selector = self.read_yaml_element("workflow_sort_button")
        self._hover(selector)
        # 点击"创建时间"
        selector = self.read_yaml_element("workflow_sort_create_time_select")
        self._click(selector)


    # 排序-修改时间
    def workflow_sort_update_time(self):
        # hover排序按钮
        selector = self.read_yaml_element("workflow_sort_button")
        self._hover(selector)
        # 点击"修改时间"
        selector = self.read_yaml_element("workflow_sort_update_time_select")
        self._click(selector)


    # 上传素材
    def workflow_upload_file(self, path):
        # 输入文件路径
        selector = self.read_yaml_element("workflow_upload_file_button")
        self._upload_file_chooser(selector, path)
        # 等待元素出现
        selector = self.read_yaml_element("workflow_upload_file_confirm_button")
        self._wait_for_selector(selector)
        if self._is_visible(selector) is True:
            # 点击品牌输入框
            selector = self.read_yaml_element("workflow_filters_brand_input")
            self._click(selector)
            # 点击"Tezign 特赞"品牌
            selector = self.read_yaml_element("workflow_brand_first_select")
            self._click(selector)
            # 点击"素材权限范围"框
            selector = self.read_yaml_element("workflow_upload_asset_permission_input")
            self._click(selector)
            # 点击"自定义"选项
            selector = self.read_yaml_element("workflow_upload_asset_permission_custom_select")
            self._click(selector)
            # 点击"上传素材"按钮
            selector = self.read_yaml_element("workflow_upload_file_confirm_button")
            self._click(selector)
        else:
            print('素材上传失败！')


    # 搜索项目
    def workflow_search_project(self, name):
        # 点击搜索框，打开搜索界面
        selector = self.read_yaml_element("workflow_search_open_button")
        self._click(selector)
        # 输入项目名称
        selector = self.read_yaml_element("workflow_search_input")
        self._fill(selector, name)
        # 点击目标项目
        selector = self.read_yaml_element("workflow_search_result_select")
        self._wait_for_selector(selector)
        self._click(selector)


    # 编辑项目
    def workflow_edit_project(self, name, describe, city, supplier):
        # 点击"编辑项目"按钮
        selector = self.read_yaml_element("workflow_edit_project_button")
        self._click(selector)
        # 修改"项目名称"
        selector = self.read_yaml_element("workflow_project_name_edit_input")
        self._fill(selector, name)
        # 输入"项目描述"
        selector = self.read_yaml_element("workflow_describe_edit_input")
        self._fill(selector, describe)
        # 输入"下单城市"
        selector = self.read_yaml_element("workflow_order_city_edit_input")
        self._fill(selector, city)
        # 输入"供应商"
        selector = self.read_yaml_element("workflow_supplier_edit_input")
        self._fill(selector, supplier)
        # 点击"确定"按钮
        selector = self.read_yaml_element("workflow_edit_confirm_button")
        self._click(selector)


    # 进入第一个项目中
    def workflow_open_project_first(self):
        selector = self.read_yaml_element("workflow_first_project_name")
        self._click(selector)


    # 删除项目
    def workflow_delete_project(self):
        # 点击"删除"按钮
        selector = self.read_yaml_element("workflow_delete_project_button")
        self._click(selector)
        # 二次确认
        selector = self.read_yaml_element("workflow_delete_project_confirm_button")
        self._click(selector)


    # 提交审批-简单审批模板
    def workflow_submit_audit_project_one(self, member):
        # 点击"提交审批"按钮
        selector = self.read_yaml_element("workflow_submit_audit_button")
        self._click(selector)
        # 点击"添加"按钮
        selector = self.read_yaml_element("workflow_one_add_button")
        self._click(selector)
        self._wait(0.5)
        # 点击输入框
        selector = self.read_yaml_element("workflow_search_member_input_click")
        self._click(selector)
        # 输入审批人
        selector = self.read_yaml_element("workflow_search_member_input")
        self._fill(selector, member)
        # 点击搜索结果中的"添加"按钮
        selector = self.read_yaml_element("workflow_search_add_button")
        self._click(selector)
        # 点击"确定"按钮
        selector = self.read_yaml_element("workflow_search_confirm_button")
        self._click(selector)
        # 点击"提交审批"按钮
        selector = self.read_yaml_element("workflow_submit_audit_submit_button")
        self._click(selector)
        # 二次确认
        selector = self.read_yaml_element("workflow_submit_audit_confirm_button")
        self._click(selector)


    # 提交审批-或签审批模板-重新提交
    def workflow_submit_audit_project_more(self, member1, member2):
        # 点击"重新提交"按钮
        selector = self.read_yaml_element("workflow_submit_audit_again_button")
        self._click(selector)
        # 点击"新建流程"按钮
        selector = self.read_yaml_element("workflow_more_new_create_audit_button")
        self._click(selector)
        # 点击或签审批模板Tab
        selector = self.read_yaml_element("workflow_more_tab_button")
        self._click(selector)
        # 点击"添加"按钮
        selector = self.read_yaml_element("workflow_more_add_button")
        self._click(selector)
        # 点击输入框
        selector = self.read_yaml_element("workflow_search_member_input_click")
        self._click(selector)
        # 输入"lzj001"
        selector = self.read_yaml_element("workflow_search_member_input")
        self._fill(selector, member1)
        # 点击搜索结果中的"添加"按钮
        selector = self.read_yaml_element("workflow_search_add_button")
        self._click(selector)
        # 点击输入框
        selector = self.read_yaml_element("workflow_search_member_input_click")
        self._click(selector)
        # 输入"lzj002"
        selector = self.read_yaml_element("workflow_search_member_input")
        self._fill(selector, member2)
        # 点击"添加"按钮
        selector = self.read_yaml_element("workflow_search_add_button")
        self._click(selector)
        # 点击"确定"按钮
        selector = self.read_yaml_element("workflow_search_confirm_button")
        self._click(selector)
        # 点击"提交审批"按钮
        selector = self.read_yaml_element("workflow_submit_audit_submit_button")
        self._click(selector)
        # 二次确认
        selector = self.read_yaml_element("workflow_submit_audit_confirm_button")
        self._click(selector)


    # 分享项目
    def workflow_share_project(self):
        # 点击"分享"按钮
        selector = self.read_yaml_element("workflow_share_button")
        self._click(selector)
        # 点击"复制链接"按钮
        selector = self.read_yaml_element("workflow_share_copy_link_button")
        self._click(selector)

    # 切换到评论-Tab
    def workflow_comment_tab(self):
        # 点击"评论"tab
        selector = self.read_yaml_element("workflow_comment_tab")
        self._click(selector)

    # 切换到log-Tab
    def workflow_project_log_tab(self):
        # 点击"项目日志"tab
        selector = self.read_yaml_element("workflow_project_log_tab")
        self._click(selector)

    # 素材-评论
    def workflow_comment(self, text):
        # 点击"评论"按钮，弹出评论框
        selector = self.read_yaml_element("workflow_comment_button")
        self._click(selector)
        # self._wait(1)
        # 点击评论输入框
        selector = self.read_yaml_element("workflow_comment_input_click")
        self._click(selector)
        # self._wait(1)
        # 输入
        selector = self.read_yaml_element("workflow_comment_input")
        self._fill(selector, text)
        # self._wait(1)
        # 点击"发送"按钮
        selector = self.read_yaml_element("workflow_comment_send_out_button")
        self._click(selector)

    # 素材-删除评论
    def workflow_comment_delete(self):
        # hover 第一条评论
        selector = self.read_yaml_element("workflow_comment_first")
        self._hover(selector)
        # 点击"删除"按钮
        selector = self.read_yaml_element("workflow_comment_first_delete_button")
        self._click(selector)
        # 二次确认
        selector = self.read_yaml_element("workflow_comment_first_delete_confirm_button")
        self._click(selector)


    # 批量操作-批量编辑-素材
    def workflow_batch_edit_project(self, text):
        # hover"批量操作"按钮
        selector = self.read_yaml_element("workflow_batch_button")
        self._hover(selector)
        # 点击"批量编辑"按钮
        selector = self.read_yaml_element("workflow_batch_edit_project_button")
        self._click(selector)
        self._wait(1)
        # 点击全选按钮
        selector = self.read_yaml_element("workflow_batch_all_select_button")
        self._click(selector)
        # 点击素材"编辑"按钮
        selector = self.read_yaml_element("workflow_batch_edit_project_asset_edit_button")
        self._click(selector)
        self._wait(1)
        # 修改描述
        selector = self.read_yaml_element("workflow_batch_edit_project_asset_edit_dec_input")
        self._fill(selector, text)
        # 点击保存按钮
        selector = self.read_yaml_element("workflow_batch_edit_project_asset_edit_save_button")
        self._click(selector)


    # 批量操作-批量分享-素材
    def workflow_batch_share_project(self):
        # hover"批量操作"按钮
        selector = self.read_yaml_element("workflow_batch_button")
        self._hover(selector)
        self._wait(1)
        # 点击"批量分享"按钮
        selector = self.read_yaml_element("workflow_batch_share_project_button")
        self._click(selector)
        self._wait(1)
        # 点击全选按钮
        selector = self.read_yaml_element("workflow_batch_all_select_button")
        self._click(selector)
        # 点击素材"分享"按钮
        selector = self.read_yaml_element("workflow_batch_share_project_asset_share_button")
        self._click(selector)
        # 点击"创建分享"按钮
        selector = self.read_yaml_element("workflow_batch_share_project_create_link_button")
        self._click(selector)



    # 批量操作-批量删除-素材
    def workflow_batch_delete_project(self):
        # hover"批量操作"按钮
        selector = self.read_yaml_element("workflow_batch_button")
        self._hover(selector)
        # 点击"批量删除"按钮
        selector = self.read_yaml_element("workflow_batch_delete_project_button")
        self._click(selector)
        self._wait(1)
        # 点击全选按钮
        selector = self.read_yaml_element("workflow_batch_all_select_button")
        self._click(selector)
        # 点击素材"删除"按钮
        selector = self.read_yaml_element("workflow_batch_delete_project_asset_delete_button")
        self._click(selector)
        # 二次确认
        selector = self.read_yaml_element("workflow_batch_delete_project_confirm_button")
        self._click(selector)


    # 撤销审批流程
    def workflow_project_submit_audit_revoke(self):
        # 点击"审批意见"按钮
        selector = self.read_yaml_element("revoke_approval_opinions_button")
        self._click(selector)
        # 点击"项目进度"tab
        selector = self.read_yaml_element("revoke_tab_project_schedule_button")
        self._click(selector)
        # 点击"撤回审批流程"按钮
        selector = self.read_yaml_element("revoke_tab_project_schedule_revoke_audit_button")
        self._click(selector)
        # 二次确认
        selector = self.read_yaml_element("revoke_tab_project_schedule_revoke_audit_confirm_button")
        self._click(selector)


    # 审批项目-通过
    def workflow_project_audit_adopt(self):
        # 点击"批量审批"按钮
        pass
        # 勾选项目

        # 点击"通过"按钮

        # 点击"提交审批结果"按钮

        # 输入"审批意见"


    # 审批项目-不通过
    def workflow_project_audit_fail(self):
        # 点击"批量审批"按钮
        pass
        # 勾选项目

        # 点击"不通过"按钮

        # 点击"提交审批结果"按钮

        # 输入"审批意见"


    # 素材入库
    def workflow_ingest_to_all_assets(self):
        # 点击"素材入库"按钮
        pass
        # 勾选素材

        # 点击"确认素材入库"按钮

        # 二次确认


    # 素材入组
    def workflow_ingest_to_group(self):
        # 点击"素材入组"按钮
        pass
        # 勾选素材

        # 点击"确认素材入组"按钮

        # 输入"test_group_001"

        # 选择结果

        # 点击"确定"按钮
