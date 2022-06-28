# -*- coding: utf-8 -*-
# @Time : 2022/3/16 10:34 上午
# @Author : liuzhijie
# @File : AssetDetailPage.py

from pages.basepage import BasePage

class AssetDetailPage(BasePage):

    # 点击素材进入详情页
    def into_asset_detail_page(self):
        selector = self.read_yaml_element("asset_name_first")
        self._wait_for_selector(selector)
        self._click(selector)
        self._wait(2)


    # 点击关闭素材详情页
    def close_asset_detail_page(self):
        selector = self.read_yaml_element("detail_close_page_button")
        self._click(selector)


    # 进入编辑状态(前提：在详情tab页面下)
    def into_detail_edit_page(self):
        # 切换到-详情tab
        selector = self.read_yaml_element("detail_tab_details")
        self._click(selector)
        # 点击鼠标
        self._mouse_left_click(500, 500)
        # 点击详情标签
        selector1 = self.read_yaml_element("detail_tab_details")
        self._wait_for_selector(selector1)
        if self._is_visible(selector1) is True:
            selector2 = self.read_yaml_element("detail_tab_details")
            self._click(selector2)
            self._wait(1)
            # 点击编辑按钮
            selector3 = self.read_yaml_element("detail_edit_button")
            self._click(selector3)
        else:
            self._mouse_left_click(500, 500)
            # 点击编辑按钮
            selector4 = self.read_yaml_element("detail_edit_button")
            self._click(selector4)


    # 切换tab
    def detail_tab_switch(self):
        # 切换到-智能识别tab
        selector = self.read_yaml_element("detail_tab_intelligent_identification")
        self._click(selector)
        self._wait(0.1)
        # 切换到-评论tab
        selector = self.read_yaml_element("detail_tab_comments")
        self._click(selector)
        self._wait(0.1)
        # 切换到-日志tab
        selector = self.read_yaml_element("detail_tab_logs")
        self._click(selector)
        self._wait(0.1)
        # 切换到-详情tab
        selector = self.read_yaml_element("detail_tab_details")
        self._click(selector)
        self._wait(0.1)


    # 格式导出
    def detail_export_format(self):
        # hover "下载素材"边上的... 按钮
        selector = self.read_yaml_element("detail_download_more_button")
        self._hover(selector)
        # 点击 格式导出 按钮
        selector = self.read_yaml_element("detail_format_export_button")
        self._click(selector)
        self._wait(0.2)
        # 格式转换-开始转换（JPEG）
        selector = self.read_yaml_element("detail_format_export_confirm_button")
        self._click(selector)


    # 格式导出取消
    def detail_export_format_cancel(self):
        # 点击取消
        selector = self.read_yaml_element("detail_tab_export_format_cancel")
        self._click(selector)


    # 下载素材
    def detail_download(self):
        # 点击下载按钮
        selector = self.read_yaml_element("detail_download_button")
        self._click(selector)



    # 下载指定尺寸或大小
    def detail_download_designated_size(self):
        # hover ... icon
        selector = self.read_yaml_element("detail_download_more_button")
        self._hover(selector)
        # 点击下载指定尺寸或大小按钮
        selector = self.read_yaml_element("detail_download_designated_size_button")
        self._click(selector)
        # 点击下载按钮（默认下载）
        self._wait(0.5)
        selector = self.read_yaml_element("detail_download_designated_size_confirm_button")
        self._wait_for_selector(selector)
        self._click(selector)


    # 下载素材及附件
    def detail_download_all(self):
        # hover ... icon
        selector = self.read_yaml_element("detail_download_more_button")
        self._hover(selector)
        self._wait(1)
        # 点击下载带附件按钮
        selector = self.read_yaml_element("detail_download_all_button")
        self._click(selector)
        self._wait(1)


    # 分享素材-直接分享
    def detail_share(self):
        # 点击分享按钮
        selector = self.read_yaml_element("detail_share_button")
        self._click(selector)
        # 点击"创建链接"按钮
        selector = self.read_yaml_element("detail_share_create_link_button")
        self._click(selector)
        # 关闭弹窗：点击"x"
        selector = self.read_yaml_element("detail_share_close_button")
        self._click(selector)


    # 分享素材-直接分享-Main
    def detail_share_main(self):
        # 点击分享按钮
        selector = self.read_yaml_element("detail_share_button")
        self._click(selector)
        # 点击"创建链接"按钮
        selector = self.read_yaml_element("detail_share_create_link_button")
        self._click(selector)
        # 关闭弹窗：点击"x"
        selector = self.read_yaml_element("main_detail_share_close_button")
        self._click(selector)


    # 编辑素材-修改素材名称、品牌、有效期规则
    def detail_edit(self,asset_name):
        # 点击"编辑"按钮
        selector = self.read_yaml_element("detail_edit_button")
        self._click(selector)
        # 修改素材名称
        selector = self.read_yaml_element("detail_edit_name_input")
        self._fill(selector,asset_name)
        # 修改品牌
        selector = self.read_yaml_element("detail_edit_brand_input")
        self._click(selector)
        # 选择第一个品牌
        selector = self.read_yaml_element("detail_edit_brand_result_one")
        self._click(selector)
        # 点击"有效期规则"-不同步按钮
        selector = self.read_yaml_element("detail_validity_rule_not_button")
        self._click(selector)
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)


    # 素材添加到组-现有组
    def detail_add_to_group(self, group_name):
        # hover "..." 按钮
        selector = self.read_yaml_element("detail_more_button")
        self._click(selector)
        # 点击"添加到组"按钮
        selector = self.read_yaml_element("detail_add_button")
        self._click(selector)
        # 搜索素材组名称-UI自动化测试专用素材组
        selector = self.read_yaml_element("add_to_group_search_input")
        self._fill(selector, group_name)
        # 选择第一个搜索结果
        self._wait(1)
        selector = self.read_yaml_element("add_to_group_search_result_one")
        while self._is_visible(selector) is True:
            self._click(selector)
        # 点击确定按钮
        self._wait(1)
        selector = self.read_yaml_element("add_to_group_search_confirm_button")
        self._click(selector)



    # 素材添加到组-新建组
    def detail_add_to_group_build(self, group_name):
        # hover "..." 按钮
        selector = self.read_yaml_element("detail_more_button")
        self._hover(selector)
        # 点击"添加到组"按钮
        selector = self.read_yaml_element("detail_add_button")
        self._click(selector)
        self._wait(1)
        # 点击新建素材组按钮
        selector = self.read_yaml_element("detail_add_to_group_build")
        self._click(selector)
        # 输入新建素材组名称：group_name
        selector = self.read_yaml_element("detail_add_to_group_build_name_input")
        self._fill(selector, group_name)
        # 点击☑️按钮
        selector = self.read_yaml_element("detail_add_to_group_build_confirm_button")
        self._click(selector)
        # 点击确定按钮
        self._wait(1)
        selector = self.read_yaml_element("add_to_group_search_confirm_button")
        self._click(selector)


    # 上传附件
    def detail_upload_enclosure(self,path):
        # 点击"编辑"按钮
        selector = self.read_yaml_element("detail_edit_button")
        self._click(selector)

        selector = self.read_yaml_element("detail_upload_enclosure_button")
        # 修改标签
        self.page.add_style_tag(content="[class='uploader']>div>input[class='input-wrap']")
        # 点击上传附件按钮
        self._upload(selector,path)


    # 附件预览
    def detail_enclosure_preview(self):
        # 点击附件预览按钮
        selector = self.read_yaml_element("detail_enclosure_preview_button")
        self._click(selector)


    # 附件下载
    def detail_enclosure_download(self):
        # 点击附件下载按钮
        selector = self.read_yaml_element("detail_enclosure_download_button")
        self._click(selector)


    # 附件设为预览版本
    def detail_enclosure_set_preview_version(self):
        # 点击附件设为预览版本按钮
        selector = self.read_yaml_element("detail_enclosure_set_preview_version_button")
        self._click(selector)
        # 点击保存按钮
        selector = self.read_yaml_element("detail_save_button")
        self._click(selector)


    # 附件删除
    def detail_enclosure_delete(self):
        # 点击附件删除按钮
        selector = self.read_yaml_element("detail_enclosure_delete_button")
        self._click(selector)
        # 二级删除确认
        selector = self.read_yaml_element("detail_enclosure_delete_confirm_button")
        self._click(selector)


    # 评论发送：text
    def detail_comment(self,text):
        # 切换到评论tab
        selector = self.read_yaml_element("detail_tab_comments")
        self._click(selector)
        # 输入评论内容
        selector = self.read_yaml_element("detail_comment_input")
        self._fill(selector,text)
        # 点击发送按钮
        selector = self.read_yaml_element("detail_comment_send_button")
        self._click(selector)


    # 历史版本-上传新版本
    def detail_version_upload(self,path):
        # hover 版本管理按钮
        selector = self.read_yaml_element("detail_version_management_button")
        self._hover(selector)
        # 点击 上传新版本按钮
        selector = self.read_yaml_element("detail_version_upload_button")
        self._upload(selector,path)
        # 点击保存新版本按钮
        selector = self.read_yaml_element("detail_version_upload_save_button")
        self._click(selector)

    # 历史版本-查看历史版本
    def detail_history_version(self):
        # hover 版本管理按钮
        selector = self.read_yaml_element("detail_version_management_button")
        self._hover(selector)
        # 点击历史版本按钮
        selector = self.read_yaml_element("detail_version__button")
        self._hover(selector)


    # 删除素材
    def detail_delete(self):
        # 切换到-详情tab
        selector = self.read_yaml_element("detail_tab_details")
        self._click(selector)
        # hover "..." 按钮
        selector = self.read_yaml_element("detail_more_button")
        self._click(selector)
        # 点击"删除"按钮
        selector = self.read_yaml_element("detail_delete_button")
        self._click(selector)
        # 点击二次"确认"按钮
        selector = self.read_yaml_element("delete_secondary_confirmation_button")
        self._click(selector)


    # 素材推荐
    def detail_recommend(self):
        pass


    # 智能打标-描述
    def detail_intelligent_marking_input_box(self, text):
        # 在"描述"框内输入内容
        selector = self.read_yaml_element("detail_describe_input")
        self._fill(selector, text)
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)



    # 智能打标-营销创意（下拉复选框）
    def detail_intelligent_marking_drop_down_check_box(self):
        # 点击"营销创意"栏
        selector = self.read_yaml_element("detail_marketing_creativity_input")
        self._click(selector)
        # 在"营销创意"栏下拉选项内选择"创意策划/文案"选项
        selector = self.read_yaml_element("detail_marketing_creativity_select")
        self._click(selector)
        self._wait(1)
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)
        # self._wait(5)


    # 智能打标-自定义标签（输入后变成标签）
    def detail_intelligent_marking_label_input_box(self, text):
        # 在"自定义标签"框内输入内容
        selector = self.read_yaml_element("detail_custom_label_input")
        self._fill(selector, text)
        self._wait(1)
        # 按下"回车"键
        self._keyboard_click('Enter')
        # self._wait(2)
        # 点击空白处
        self._mouse_left_click(500, 500)
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)
        # self._wait(5)


    # 智能打标-素材有效期规则
    def detail_validity_rule(self):
        # 点击"有效期规则"-不同步按钮
        selector = self.read_yaml_element("detail_validity_rule_not_button")
        self._click(selector)


    # 智能打标-素材发布日（日期控件）
    def detail_intelligent_marking_date_control_box(self):
        # 点击"素材发布日"框
        selector = self.read_yaml_element("detail_release_date_input")
        self._click(selector)
        # 点击"今天"按钮
        selector = self.read_yaml_element("detail_today_button")
        self._click(selector)
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)
        self._wait(2)



    # 智能打标-限制使用渠道（多选项）
    def detail_intelligent_marking_more_selects_box(self):
        # 点击"限制使用渠道"框
        selector = self.read_yaml_element("detail_limit_channel_input")
        self._click(selector)
        # 选择"官方公众号"按钮
        selector = self.read_yaml_element("detail_official_account_select")
        self._click(selector)
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)
        # self._wait(5)



    # 智能打标-测试类型为8的筛选（复选带出下层选项）
    def detail_intelligent_marking_more_level_check_box(self):
        # 点击"测试类型为8的筛选"框
        selector = self.read_yaml_element("detail_test_style_input")
        self._click(selector)
        # 选择"1"选项
        selector = self.read_yaml_element("detail_first_select")
        self._click(selector)
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)
        # self._wait(5)



    # 编辑-可见权限类型切换
    def detail_permission_type(self, text):
        # 点击权限范围框
        selector = self.read_yaml_element("permission_type_input")
        self._click(selector)
        # 选择权限类型
        tmp = self._input_permission(text)
        selector = self.read_yaml_element(tmp)
        self._click(selector)
        self._wait(0.3)


    # 编辑-保存
    def detail_save(self):
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)
        # self._wait(2)


    # 编辑-增加权限
    def detail_add_permission(self, text):
        # 点击"增加权限"按钮
        selector = self.read_yaml_element("detail_add_permission_button")
        self._click(selector)
        # 在输入框内输入"蔡智"
        selector = self.read_yaml_element("permission_input")
        self._fill(selector, text)
        # 勾选要添加的权限-"蔡智"
        selector = self.read_yaml_element("permission_checkbox")
        self._click(selector)


        # #
        # self._wait(1)
        # self._keyboard_click("Tab")
        # self._keyboard_click(" ")
        # self._wait(1)
        # # 点击"确认"按钮
        # self._keyboard_click("Tab")
        # self._keyboard_click("Tab")
        # self._keyboard_click(" ")
        # 点击"确认"按钮
        selector = self.read_yaml_element("permission_is_chek")
        while self._is_visible(selector) is True:
            selector = self.read_yaml_element("permission_confirm_button")
            self._click(selector)
            break


    # 编辑-清除权限
    def detail_remove_permission(self):
        # 点击"批量移除"按钮
        selector = self.read_yaml_element("permission_remove_button")
        self._click(selector)
        # 点击"全选"按钮
        selector = self.read_yaml_element("permission_remove_all_select_button")
        self._click(selector)
        # 点击"删除"按钮
        selector = self.read_yaml_element("permission_remove_delete_button")
        self._click(selector)
        # 点击二次确认按钮
        selector = self.read_yaml_element("permission_remove_delete_confirm_button")
        self._click(selector)


    # 日志
    def detail_logs(self):
        # 切换到日志tab
        selector = self.read_yaml_element("detail_tab_logs")
        self._click(selector)


    # 权限：下载权限申请
    def detail_permission_application_download(self, text):
        selector = self.read_yaml_element("detail_permission_application_download_button")
        self._click(selector)
        # 输入申请理由
        selector = self.read_yaml_element("permission_application_input")
        self._wait_for_selector(selector)
        self._fill(selector, text)
        self._wait(0.5)
        # 点击"申请权限"按钮
        selector = self.read_yaml_element("permission_application_button")
        self._wait_for_selector(selector)
        self._click(selector)


    # 权限：编辑权限申请
    def detail_permission_application_edit(self, text):
        selector = self.read_yaml_element("detail_permission_application_edit_button")
        self._click(selector)
        # 输入申请理由
        selector = self.read_yaml_element("permission_application_input")
        self._fill(selector, text)
        self._wait(0.5)
        # 点击"申请权限"按钮
        selector = self.read_yaml_element("permission_application_button")
        self._wait_for_selector(selector)
        self._click(selector)
