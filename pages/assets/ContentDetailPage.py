# -*- coding: utf-8 -*- 
# @Time : 2022/5/16 11:37 上午 
# @Author : liuzhijie
# @File : ContentDetailPage.py


from pages.basepage import BasePage

class ContentDetailPage(BasePage):

    # 点击素材进入详情页
    def into_detail_page(self):
        selector = self.read_yaml_element("asset_name_first")
        self._wait_for_selector(selector)
        self._click(selector)


    # 点击素材进入详情页
    def into_detail_text_page(self):
        selector = self.read_yaml_element("asset_text_first_hover")
        self._wait_for_selector(selector)
        self._click(selector)



    # tab页切换-详情
    def detail_tab_details(self):
        # 切换到-详情tab
        selector = self.read_yaml_element("detail_tab_details")
        self._click(selector)


    # tab页切换-评论
    def detail_tab_comments(self):
        # 切换到-评论tab
        selector = self.read_yaml_element("detail_tab_comments")
        self._click(selector)


    # tab页切换-log
    def detail_tab_logs(self):
        # 切换到-日志tab
        selector = self.read_yaml_element("detail_tab_logs")
        self._click(selector)


    # 分享
    def detail_share(self):
        # 点击分享按钮
        selector = self.read_yaml_element("detail_share_button")
        self._click(selector)
        # 点击"创建分享"按钮
        selector = self.read_yaml_element("share_create_link_button")
        self._click(selector)
        # 关闭分享按钮
        selector = self.read_yaml_element("share_close_button")
        self._click(selector)


    # 编辑-名称\品牌
    def detail_edit(self, text):
        # 点击"编辑"按钮
        selector = self.read_yaml_element("detail_edit_button")
        self._click(selector)
        # 输入名称
        selector = self.read_yaml_element("edit_name_input")
        self._fill(selector, text)
        # 点击品牌输入框
        selector = self.read_yaml_element("edit_brand_input")
        self._click(selector)
        # 选择第一个品牌
        selector = self.read_yaml_element("edit_brand_result_one")
        self._click(selector)
        # 点击"保存"按钮
        selector = self.read_yaml_element("edit_save_button")
        self._click(selector)


    # hover 。。。更多选项
    def detail_more_hover(self):
        # hover ... 更多选项
        selector = self.read_yaml_element("detail_more_button")
        self._hover(selector)


    # 添加到组-已有组
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
        if self._is_visible(selector) is True:
            self._click(selector)
        # 点击确定按钮
        self._wait(1)
        selector = self.read_yaml_element("add_to_group_search_confirm_button")
        self._click(selector)


    # 添加到组-新建组
    def detail_add_to_group_build(self, group_name):
        # hover "..." 按钮
        selector = self.read_yaml_element("detail_more_button")
        self._hover(selector)
        # 点击"添加到组"按钮
        selector = self.read_yaml_element("detail_add_button")
        self._click(selector)
        self._wait(1)
        # 点击新建素材组按钮
        selector = self.read_yaml_element("add_to_group_build_button")
        self._click(selector)
        # 输入新建素材组名称：group_name
        selector = self.read_yaml_element("add_to_group_build_name_input")
        self._fill(selector, group_name)
        # 点击☑️按钮
        selector = self.read_yaml_element("add_to_group_build_confirm_button")
        self._click(selector)
        # 点击确定按钮
        self._wait(1)
        selector = self.read_yaml_element("add_to_group_search_confirm_button")
        self._click(selector)


    # 添加到组-右上角入口
    def detail_add_to_group_upper_right(self, group_name):
        # 点击"添加到组"按钮
        selector = self.read_yaml_element("detail_upper_right_button")
        self._wait(0.8)
        while self._is_enable(selector) is True:
            self._click(selector)
            break
        # 搜索素材组名称-UI自动化测试专用素材组
        selector = self.read_yaml_element("add_to_group_search_input")
        self._fill(selector, group_name)
        # 选择第一个搜索结果
        self._wait(1)
        selector = self.read_yaml_element("add_to_group_search_result_one")
        if self._is_visible(selector) is True:
            self._click(selector)
        # 点击确定按钮
        self._wait(1)
        selector = self.read_yaml_element("add_to_group_search_confirm_button")
        self._click(selector)


    # 添加到组-右上角入口-移除素材组
    def detail_move_group_upper_right(self):
        # hover右上角素材组
        selector = self.read_yaml_element("detail_upper_right_group_button")
        self._hover(selector)
        # hover第一个素材组
        selector = self.read_yaml_element("detail_upper_right_group_result_first_select")
        self._hover(selector)
        # 点击"x"按钮
        selector = self.read_yaml_element("detail_upper_right_group_result_first_select_delete_button")
        self._click(selector)
        # 二次确认
        selector = self.read_yaml_element("detail_upper_right_group_result_first_select_delete_confirm_button")
        self._click(selector)


    # 删除
    def detail_delete(self):
        # hover "..."按钮
        selector = self.read_yaml_element("detail_more_button")
        self._hover(selector)
        # 点击"删除"按钮
        selector = self.read_yaml_element("detail_delete_button")
        self._click(selector)
        # 二次确认
        selector = self.read_yaml_element("detail_delete_confirm_button")
        self._click(selector)


    # 评论发送：text
    def detail_comment(self, text):
        # 输入评论内容
        selector = self.read_yaml_element("detail_comment_input")
        self._fill(selector, text)
        # 点击发送按钮
        selector = self.read_yaml_element("detail_comment_send_button")
        self._click(selector)

    # 在浏览器打开链接
    def detail_open_url(self):
        # 点击"打开网页"按钮
        selector = self.read_yaml_element("detail_open_url_button")
        self._click(selector)


    # 复制链接
    def detail_copy_link(self):
        # 点击"复制链接"按钮
        selector = self.read_yaml_element("detail_copy_url_button")
        self._click(selector)


    # 提交错误
    def detail_submit_error(self):
        # 点击"提交错误"按钮
        selector = self.read_yaml_element("detail_submit_error_button")
        self._click(selector)


    # 复制全文
    def detail_copy_full_text(self):
        # 点击"复制全文"按钮
        selector = self.read_yaml_element("detail_copy_full_text_button")
        self._click(selector)


    # 编辑（文本）
    def detail_edit_text(self, text):
        # 点击"编辑"按钮
        selector = self.read_yaml_element("detail_edit_text_button")
        self._click(selector)
        # 输入text
        selector = self.read_yaml_element("detail_edit_text_input")
        self._fill(selector, text)
        # 点击"保存更新"按钮
        selector = self.read_yaml_element("detail_edit_text_save_button")
        self._click(selector)