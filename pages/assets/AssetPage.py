# -*- coding: utf-8 -*-
# @Time : 2022/3/16 10:34 上午
# @Author : liuzhijie
# @File : AssetPage.py

import time
from common.file_method import FileMethod
from pages.basepage import BasePage

class AssetPage(BasePage):
    # 上传文件
    def upload_file(self):
        # hover"上传"按钮
        selector1 = self.read_yaml_element("upload_button")
        self._hover(selector1)
        # 选择上传的文件
        ui_data_file_path = FileMethod().get_file_path('data', '', 'test_file_001.jpg')
        selector2 = self.read_yaml_element("upload_file_button_input")
        self._set_input_files(selector2, ui_data_file_path)
        self._wait(0.2)
        ele = self.read_yaml_element("asset_keep_both_button")
        if self._is_visible(ele) is True:
            # 点击"保留两者"
            selector = self.read_yaml_element("asset_keep_both_button")
            self._click(selector)
            self._wait(2)
            # 点击"立即入库"按钮
            selector3 = self.read_yaml_element("add_to_asset_button")
            self._click(selector3)
            # 点击"素材权限范围"框
            selector4 = self.read_yaml_element("upload_asset_permission_input")
            self._click(selector4)
            # 点击"自定义"选项
            selector5 = self.read_yaml_element("upload_asset_permission_custom_select")
            self._click(selector5)
            self._wait(0.5)
            # 选择"入库所选"按钮
            selector6 = self.read_yaml_element("add_to_asset_choice_button")
            self._click(selector6)
        else:
            self._wait(2)
            # 点击"立即入库"按钮
            selector3 = self.read_yaml_element("add_to_asset_button")
            self._click(selector3)
            # 点击"素材权限范围"框
            selector4 = self.read_yaml_element("upload_asset_permission_input")
            self._click(selector4)
            # 点击"自定义"选项
            selector5 = self.read_yaml_element("upload_asset_permission_custom_select")
            self._click(selector5)
            self._wait(0.5)
            # 选择"入库所选"按钮
            selector6 = self.read_yaml_element("add_to_asset_choice_button")
            self._click(selector6)




    # 上传文件夹
    def upload_folder(self, path):
        # 点击"上传"按钮
        selector = self.read_yaml_element("upload_button")
        self._hover(selector)
        # 选择"上传文件"按钮
        selector = self.read_yaml_element("upload_folder_button")
        self._set_input_files(selector, path)
        self._wait(12)
        # 点击"立即入库"按钮
        selector = self.read_yaml_element("add_to_asset_button")
        self._click(selector)
        # 选择"入库所选"按钮
        self._wait(1)
        time.sleep(1)
        selector = self.read_yaml_element("add_to_asset_choice_button")
        self._click(selector)

    # 百度网盘导入
    def baidu_transfer(self,link,password):
        # 点击"上传"按钮
        selector = self.read_yaml_element("upload_button")
        self._hover(selector)
        # 点击"百度网盘导入"按钮
        selector = self.read_yaml_element("baidu_transfer_button")
        self._click(selector)
        # 输入百度网盘链接
        selector = self.read_yaml_element("transfer_input")
        self._fill(selector, link)
        # 输入提取密码
        selector = self.read_yaml_element("transfer_password_input")
        self._fill(selector, password)
        # 点击"立即导入"按钮
        self._wait(1)
        time.sleep(2)
        selector = self.read_yaml_element("transfer_import_button")
        self._click(selector)
        # 选择"入库所选"按钮
        self._wait(1)
        time.sleep(1)
        selector = self.read_yaml_element("add_to_asset_choice_button")
        self._click(selector)

    # MUSE导入
    def muse_transfer(self,link):
        # 点击"上传"按钮
        selector = self.read_yaml_element("upload_button")
        self._hover(selector)
        # 点击"MUSE导入"按钮
        selector = self.read_yaml_element("transfer_button")
        self._click(selector)
        # 输入MUSE链接
        selector = self.read_yaml_element("transfer_button")
        self._fill(selector, link)
        # 点击"立即入库"按钮
        self._wait(1)
        time.sleep(2)
        selector = self.read_yaml_element("add_to_asset_button")
        self._click(selector)
        # 选择"入库所选"按钮
        self._wait(1)
        time.sleep(1)
        selector = self.read_yaml_element("add_to_asset_choice_button")
        self._click(selector)


    # 导入网页
    def upload_url(self, urls):
        # hover"上传"按钮
        selector = self.read_yaml_element("upload_button")
        self._hover(selector)
        # 点击"导入网页"按钮
        selector = self.read_yaml_element("upload_url_button")
        self._click(selector)
        # 输入网页
        selector = self.read_yaml_element("url_input")
        self._fill(selector, urls)
        # 点击"确认"按钮
        selector = self.read_yaml_element("url_save_button")
        self._click(selector)
        # 点击"立即入库"按钮
        selector = self.read_yaml_element("add_to_asset_button")
        self._wait_for_selector(selector)
        self._click(selector)
        # 点击"素材权限范围"框
        selector = self.read_yaml_element("upload_asset_permission_input")
        self._click(selector)
        # 点击"自定义"选项
        selector = self.read_yaml_element("upload_asset_permission_custom_select")
        self._click(selector)
        # 选择"入库所选"按钮
        selector = self.read_yaml_element("add_to_asset_choice_button")
        self._click(selector)


    # 新建纯文本
    def upload_text(self, text):
        # hover"上传"按钮
        selector = self.read_yaml_element("upload_button")
        self._hover(selector)
        # 点击"新建纯文本"按钮
        selector = self.read_yaml_element("create_text_button")
        self._click(selector)
        # 输入文本内容
        selector = self.read_yaml_element("text_input")
        self._fill(selector, text)
        # 点击"保存并入库"按钮
        selector = self.read_yaml_element("text_save_button")
        self._click(selector)
        # 点击"素材权限范围"框
        selector = self.read_yaml_element("upload_asset_permission_input")
        self._click(selector)
        # 点击"自定义"选项
        selector = self.read_yaml_element("upload_asset_permission_custom_select")
        self._click(selector)
        # 选择"入库所选"按钮
        selector = self.read_yaml_element("add_to_asset_choice_button")
        self._click(selector)


    # 新建文章
    def upload_article(self, articles):
        # hover"上传"按钮
        selector = self.read_yaml_element("upload_button")
        self._hover(selector)
        # 点击"新建文章"按钮
        selector = self.read_yaml_element("upload_articles_button")
        self._click(selector)
        self._wait(5)
        # 进入iframe
        selector = self.read_yaml_element("article_iframe1")
        iframe1 = self._iframe(selector)
        selector = self.read_yaml_element("article_iframe2")
        iframe2 = self._iframe(selector)
        selector = self.read_yaml_element("articles_input")
        # iframe1.fill(selector, articles)
        iframe2.fill(selector, articles)
        # iframe1 = self.page.query_selector("id='iframe-content-center'").content_frame()
        # iframe2 = iframe1.page.query_selector("id='ueditor_0'").content_frame()
        # iframe2.fill("[class='ueditor-placeholder ']", articles)
        # 输入文本内容

        # self._fill(selector, articles)
        # 点击"保存并入库"按钮
        selector = self.read_yaml_element("articles_save_button")
        self._click(selector)
        # 点击"素材权限范围"框
        selector = self.read_yaml_element("upload_asset_permission_input")
        self._click(selector)
        # 点击"自定义"选项
        selector = self.read_yaml_element("upload_asset_permission_custom_select")
        self._click(selector)
        # 选择"入库所选"按钮
        selector = self.read_yaml_element("add_to_asset_choice_button")
        self._click(selector)



    # 素材搜索
    def asset_search(self, text):
        selector = self.read_yaml_element("asset_search_input")  # 输入框填入text
        self._fill(selector, text)
        self._keyboard_click('Enter')  # 按下"回车"键
        self._wait(1)


    # 平铺模式排列
    def asset_arrangement_tile_mode(self):
        selector =self.read_yaml_element("asset_tile_mode")
        self._click(selector)

    # 列表模式排列
    def asset_arrangement_list_mode(self):
        selector = self.read_yaml_element("asset_list_mode")
        self._click(selector)


    # 素材排序
    def asset_sort(self,text):
        # hover排序按钮
        selector = self.read_yaml_element("asset_sort_button")
        self._hover(selector)
        # 点击要测试的排序方式
        tmp = self._input_sort(text)
        selector = self.read_yaml_element(tmp)
        self._click(selector)


    # 加入素材篮
    def add_to_asset_basket(self):
        # hover素材
        selector = self.read_yaml_element("asset_name_first")
        self._hover(selector)
        # 点击加入素材篮按钮
        selector = self.read_yaml_element("asset_add_to_asset_basket_button")
        self._click(selector)


    #关闭查找相似图
    def asset_search_similar_pic_close(self):
        selector = self.read_yaml_element("asset_search_similar_pic_close_button")  # 点击关闭查找相似图按钮
        self._click(selector)

    #清空相似图搜索
    def asset_search_similar_pic_empty(self):
        selector = self.read_yaml_element("asset_search_similar_pic_empty_button")  # 点击清空搜索按钮
        self._click(selector)


    #素材全选
    def asset_all_selected(self):
        selector = self.read_yaml_element("asset_all_selected_not")  # 点击全选按钮
        self._click(selector)


    # 素材取消全选
    def asset_all_selected_cancel(self):
        selector = self.read_yaml_element("asset_all_selected")  # 点击取消全选按钮
        self._click(selector)


    # 筛选自己创建到素材
    def asset_my_create(self):
        # hover"创建者/创建部门"筛选项
        selector = self.read_yaml_element("asset_filters_creator")
        self._hover(selector)
        # 点击"我创建到素材"按钮
        selector = self.read_yaml_element("asset_filters_creator_self")
        self._click(selector)
        # 移开鼠标焦点
        self._mouse_move(100, 100)
        self._wait(1)


    # hover素材
    def asset_hover(self):
        # 等待筛选器出现
        selector = self.read_yaml_element("asset_filters_creator")
        self._wait_for_selector(selector)
        # hover 素材
        selector = self.read_yaml_element("asset_name_first_hover")
        self._hover(selector)


    # 选中素材（第二个）
    def asset_second_click(self):
        # hover 素材
        selector = self.read_yaml_element("asset_name_second")
        self._click(selector)


    # 进入多选模式
    def asset_batch(self):
        #点击多选按钮
        selector = self.read_yaml_element("asset_batch_button")
        self._click(selector)
        self._wait(1)


    # 批量下载
    def asset_batch_download(self):
        ##hover "下载"按钮
        selector = self.read_yaml_element("asset_batch_download")
        self._hover(selector)
        self._wait(1)
        #点击批量下载按钮
        selector = self.read_yaml_element("asset_batch_download_button")
        self._click(selector)


    #批量下载素材及附件
    def asset_batch_download_all(self):
        #hover "下载"按钮
        selector = self.read_yaml_element("asset_batch_button")
        self._hover(selector)
        #点击"下载素材及附件"按钮
        selector = self.read_yaml_element("asset_batch_download_all_button")
        self._click(selector)



    # 批量分享
    def asset_batch_share(self):
        # 点击分享按钮
        selector = self.read_yaml_element("asset_batch_share")
        self._click(selector)
        # 点击"创建链接"按钮
        selector = self.read_yaml_element("asset_batch_share_create_link_button")
        self._click(selector)
        # 关闭弹窗：点击"x"
        selector = self.read_yaml_element("asset_more_share_close_button")
        self._click(selector)


    # 批量编辑-修改(名称)
    def asset_batch_edit(self, *args):
        # 点击批量编辑按钮
        selector = self.read_yaml_element("asset_batch_edit")
        self._click(selector)
        # 点击详情Tab
        selector = self.read_yaml_element("asset_detail_tab_details")
        self._click(selector)
        # 编辑素材-名称
        selector = self.read_yaml_element("detail_edit_name_input")
        self._fill(selector, *args)
        # 点击"保存"按钮
        selector = self.read_yaml_element("detail_edit_save_button")
        self._click(selector)


    # 批量重命名
    def asset_batch_rename(self,rename):
        # hover "..." 按钮
        selector = self.read_yaml_element("asset_batch_more")
        self._hover(selector)
        # 点击批量重命名按钮
        selector = self.read_yaml_element("asset_batch_rename")
        self._click(selector)
        # 输入重命名
        selector = self.read_yaml_element("rename_input")
        self._fill(selector, rename)
        # 点击"重命名"按钮
        selector = self.read_yaml_element("rename_button")
        self._click(selector)
        self._wait(0.2)
        # 重复检测判断
        selector = self.read_yaml_element("rename_confirm_button")
        while self._is_visible(selector) is True:
            self._click(selector)
            break


    # 批量添加到组-新建组
    def asset_batch_add_to_group_build(self, group_name):
        # 点击批量添加到组按钮
        selector = self.read_yaml_element("asset_batch_add_to_group")
        self._click(selector)
        # 点击新建素材组按钮
        selector = self.read_yaml_element("add_to_group_build")
        self._wait(1)
        self._click(selector)
        # 输入新建素材组名称：group_name
        selector = self.read_yaml_element("add_to_group_build_name_input")
        self._fill(selector, group_name)
        # 点击☑️按钮
        selector = self.read_yaml_element("add_to_group_build_confirm_button")
        self._click(selector)
        # 点击确定按钮
        selector = self.read_yaml_element("add_to_group_search_confirm_button")
        self._wait(1)
        self._click(selector)


    # 批量添加到组-已存在组
    def asset_batch_add_to_group(self, name):
        # 点击批量添加到组按钮
        selector = self.read_yaml_element("asset_batch_add_to_group")
        self._click(selector)
        selector = self.read_yaml_element("asset_batch_add_to_group_check")
        if self._is_enable(selector):
            # 搜索素材组名称-UI自动化测试专用素材组
            selector = self.read_yaml_element("add_to_group_search_input")
            self._fill(selector, name)
            self._wait(1)
            # 选择第一个搜索结果
            selector = self.read_yaml_element("add_to_group_search_result_one")
            while self._is_visible(selector) is True:
                self._click(selector)
            # 点击确定按钮
            selector = self.read_yaml_element("add_to_group_search_confirm_button")
            while self._is_enable(selector) is True:
                self._click(selector)
                break


    # 批量加入素材篮
    def asset_batch_add_to_basket(self):
        # 点击批量加入素材篮按钮
        selector = self.read_yaml_element("asset_batch_add_to_basket")
        self._click(selector)


    # 批量删除
    def asset_batch_delete(self):
        # 点击批量删除按钮
        selector = self.read_yaml_element("asset_batch_delete")
        self._click(selector)
        # 点击二次"确认"按钮
        selector = self.read_yaml_element("delete_secondary_confirmation_button")
        self._click(selector)


    # 常用筛选（我创建的素材+文件格式：图片）
    def asset_saved_filters(self, name):
        # 点击筛选条件：创建者
        selector = self.read_yaml_element("asset_filters_creator")
        self._hover(selector)
        # 勾选 我创建的素材
        selector = self.read_yaml_element("asset_filters_creator_self")
        self._click(selector)
        # 点击空白，关闭窗口
        self._mouse_move(200, 200)
        # 点击筛选条件：类型
        selector = self.read_yaml_element("asset_filters_file_format")
        self._click(selector)
        # 勾选 图片格式
        selector = self.read_yaml_element("asset_filters_file_format_picture_select")
        self._click(selector)
        # 点击空白，关闭窗口
        self._mouse_move(200, 200)
        # hover 常用筛选
        selector = self.read_yaml_element("asset_saved_filters_hover")
        self._hover(selector)
        # 点击 保存为常用筛选按钮
        selector = self.read_yaml_element("asset_saved_filters_save_button")
        self._click(selector)
        # 输入常用筛选条件名称
        selector = self.read_yaml_element("asset_saved_filters_name_input")
        self._fill(selector, name)
        # 点击确定按钮
        selector = self.read_yaml_element("asset_saved_filters_confirm_button")
        self._click(selector)


    # 常用筛选清除
    def asset_common_filters_dump(self):
        # hover 常用筛选按钮
        selector = self.read_yaml_element("asset_saved_filters_hover")
        self._hover(selector)
        # hover 需要删除的常用筛选项(第一个)
        selector = self.read_yaml_element("asset_common_filters_name_hover")
        self._hover(selector)
        # 点击删除按钮
        selector = self.read_yaml_element("asset_common_filters_delete_button")
        self._click(selector)


    # 查找相似图
    def asset_search_similar_pic(self):
        # 点击查找相似图
        selector = self.read_yaml_element("asset_search_similar_pic_button")
        self._click(selector)
        # 点击查找色彩相似图片
        selector = self.read_yaml_element("asset_search_similar_pic_color_button")
        self._click(selector)
        # 点击清空搜索
        selector = self.read_yaml_element("asset_search_similar_pic_empty_button")
        self._click(selector)
        # 点击关闭以图搜图
        selector = self.read_yaml_element("asset_search_similar_pic_close_button")
        self._click(selector)


    # 筛选-我创建的素材
    def asset_filters_creator_self(self):
        # 点击 创建这/创建部门
        selector = self.read_yaml_element("asset_filters_creator")
        self._click(selector)
        # 点击"我创建的素材"
        selector = self.read_yaml_element("asset_filters_creator_self")
        self._click(selector)

    # 筛选-品牌
    def asset_filters_brand(self):
        # 点击 创建这/创建部门
        selector = self.read_yaml_element("asset_filters_brand")
        self._click(selector)
        # 点击品牌输入框
        selector = self.read_yaml_element("asset_filters_brand_input")
        self._click(selector)
        # 点击"Tezign 特赞"品牌
        selector = self.read_yaml_element("asset_filters_brand_first_select")
        self._click(selector)


    # 筛选-文件格式-JPG格式
    def asset_filters_file_format(self):
        # 点击 文件格式
        selector = self.read_yaml_element("asset_filters_file_format")
        self._click(selector)
        # 点击 图片展开
        selector = self.read_yaml_element("asset_filters_file_format_picture")
        self._click(selector)
        # 点击 JPG格式
        selector = self.read_yaml_element("asset_filters_file_format_picture_JPG")
        self._click(selector)



    # 筛选-创建时间
    def asset_filters_creation_time(self):
        # 点击 创建时间
        selector = self.read_yaml_element("asset_filters_creation_time")
        self._click(selector)
        # 点击"今天"选项
        selector = self.read_yaml_element("asset_filters_creation_time_today")
        self._click(selector)


    # 筛选-图片主色
    def asset_filters_picture_main_color(self):
        # 点击 图片主色
        selector = self.read_yaml_element("asset_filters_picture_main_color")
        self._click(selector)
        # 点击"红色"（色号：#e83a30）
        selector = self.read_yaml_element("asset_filters_picture_main_color_red")
        self._click(selector)


    # 筛选-测试多选
    def asset_filters_checkbox(self):
        # 点击 测试ry
        selector = self.read_yaml_element("asset_filters_checkbox")
        self._click(selector)
        # # 点击 测试ry输入框
        # selector = self.read_yaml_element("asset_filters_checkbox_input")
        # self._click(selector)
        # self._wait(1)
        # 点击"1"选项
        selector = self.read_yaml_element("asset_filters_checkbox_1")
        self._click(selector)


    # 筛选-测试1616
    def asset_filters_brand6(self):
        # 点击 创建这/创建部门
        selector = self.read_yaml_element("asset_filters_brand")
        self._click(selector)
        # 点击第一个品牌
        selector = self.read_yaml_element("asset_filters_brand_first")
        self._click(selector)


    # 筛选-明星标签
    def asset_filters_star_label(self):
        # 点击 明星标签
        selector = self.read_yaml_element("asset_filters_star_label")
        self._click(selector)
        # 输入"杨幂"
        selector = self.read_yaml_element("asset_filters_star_label_YY_input")
        self._fill(selector, '杨幂')
        # 点击"杨幂"选项
        selector = self.read_yaml_element("asset_filters_star_label_YY_button")
        self._click(selector)


    # 小铃铛列表
    def asset_bell_list(self):
        # 点击小铃铛按钮
        selector = self.read_yaml_element("asset_bell_button")
        self._click(selector)


    # 小铃铛消息全部已读
    def asset_bell_list_all_message_read(self):
        # 点击小铃铛按钮
        selector = self.read_yaml_element("asset_bell_button")
        self._click(selector)
        # 点击"全部标为已读"按钮
        selector = self.read_yaml_element("asset_all_read_button")
        self._click(selector)


    # 右键
    def asset_more_button(self):
        # 点击右键更多
        selector = self.read_yaml_element("asset_more_button")
        self._click(selector)


    # 右键-重命名
    def asset_more_rename(self, text):
        # 点击重命名按钮
        selector = self.read_yaml_element("asset_more_rename_button")
        self._click(selector)
        # 输入"more-重命名"
        selector = self.read_yaml_element("asset_more_rename_input")
        self._fill(selector, text)
        # 点击"重命名"按钮进行保存
        selector = self.read_yaml_element("asset_more_rename_confirm_button")
        self._click(selector)


    # 右键-编辑
    def asset_more_edit(self, text):
        # 点击编辑按钮
        selector = self.read_yaml_element("asset_more_edit_button")
        self._click(selector)
        # 输入素材描述
        selector = self.read_yaml_element("asset_more_edit_describe_input")
        self._fill(selector, text)
        # 点击保存按钮
        selector = self.read_yaml_element("asset_more_edit_save_button")
        self._click(selector)


    # 右键-下载
    def asset_more_download(self):
        # hover下载按钮
        selector = self.read_yaml_element("asset_more_download_button")
        self._hover(selector)
        # 点击"下载"选项
        selector = self.read_yaml_element("asset_more_download_select")
        self._click(selector)


    # 右键-下载指定尺寸和大小
    def asset_more_download_designated_size(self, text):
        self._wait(1)
        # hover下载按钮
        selector = self.read_yaml_element("asset_more_download_button")
        self._wait_for_selector(selector)
        self._hover(selector)
        # 点击"下载指定尺寸和大小"选项
        selector = self.read_yaml_element("asset_more_download_designated_size_select")
        self._click(selector)
        # 输入"尺寸和大小"
        selector = self.read_yaml_element("asset_more_download_designated_size_input")
        self._wait_for_selector(selector)
        self._fill(selector, text)
        # 点击"下载"按钮
        selector = self.read_yaml_element("asset_more_download_designated_size_button")
        self._click(selector)


    # 右键-分享
    def asset_more_share(self):
        # 点击"分享"按钮
        selector = self.read_yaml_element("asset_more_share_button")
        self._click(selector)
        # 点击"创建链接"按钮
        selector = self.read_yaml_element("asset_more_share_create_link_button")
        self._click(selector)
        # 关闭弹窗：点击"x"
        selector = self.read_yaml_element("asset_more_share_close_button")
        self._click(selector)


    # 右键-添加到组
    def asset_more_add_to_group(self, text):
        # 点击添加到组按钮
        selector = self.read_yaml_element("asset_more_add_to_group")
        self._click(selector)
        # 搜索素材组名称-UI自动化测试专用素材组
        selector = self.read_yaml_element("add_to_group_search_input")
        self._fill(selector, text)
        # 选择第一个搜索结果
        self._wait(1)
        selector = self.read_yaml_element("add_to_group_search_result_one")
        if self._is_visible(selector) is True:
            self._click(selector)
        # 点击确定按钮
        selector = self.read_yaml_element("more_add_to_group_search_confirm_button")
        while self._is_enable(selector) is True:
            self._click(selector)
            break


    # 右键-加入素材篮
    def asset_more_add_to_basket(self):
        # 点击"加入素材篮"按钮
        selector = self.read_yaml_element("asset_more_add_to_asset_basket_button")
        self._click(selector)


    # 右键-导出Specs
    def asset_more_specs_export(self):
        # 点击"导出Specs"按钮
        selector = self.read_yaml_element("asset_more_specs_export_button")
        self._click(selector)


    # 右键-修改所有者
    def asset_more_reset_the_owner(self, text):
        # 点击"修改所有者"按钮
        selector = self.read_yaml_element("asset_more_reset_the_owner_button")
        self._click(selector)
        # 点击输入框
        selector = self.read_yaml_element("asset_more_reset_the_owner_click")
        self._click(selector)
        # 输入要修改的所有者：text
        selector = self.read_yaml_element("asset_more_reset_the_owner_input")
        self._fill(selector, text)
        # 点击搜索结果选择项
        selector = self.read_yaml_element("asset_more_reset_the_owner_select")
        self._click(selector)
        # 点击"确定"按钮
        selector = self.read_yaml_element("asset_more_reset_the_owner_confirm_button")
        self._click(selector)


    # 右键-修改权限类型
    def asset_more_modify_category(self):
        # 点击"修改权限类型"按钮
        selector = self.read_yaml_element("asset_more_modify_category_button")
        self._click(selector)
        # 点击权限类型输入框
        selector = self.read_yaml_element("asset_more_modify_category_input")
        self._click(selector)
        # 点击选择权限类型-"自定义"类型
        selector = self.read_yaml_element("asset_more_modify_category_custom_select")
        self._click(selector)
        # 点击"我知道了"保存
        selector = self.read_yaml_element("asset_more_modify_category_save_button")
        self._click(selector)


    # 右键删除-素材
    def asset_more_delete(self):
        # 点击"删除"按钮
        selector = self.read_yaml_element("asset_more_delete_button")
        self._click(selector)
        # 点击二次"确认"按钮
        selector = self.read_yaml_element("delete_secondary_confirmation_button")
        self._click(selector)

    # 右键删除-内容（网页/文章）
    def asset_more_delete_content(self):
        # 点击"删除"按钮
        selector = self.read_yaml_element("content_more_delete_button")
        self._click(selector)
        # 点击二次"确认"按钮
        selector = self.read_yaml_element("delete_secondary_confirmation_button")
        self._click(selector)


    # 右键删除-内容（纯文本）
    def asset_more_delete_content_text(self):
        # 点击"删除"按钮
        selector = self.read_yaml_element("content_text_more_delete_button")
        self._click(selector)
        # 点击二次"确认"按钮
        selector = self.read_yaml_element("delete_secondary_confirmation_button")
        self._click(selector)


    # 全部素材组-右键-新建素材组
    def asset_more_create_group(self, text):
        # 点击"全部素材组-+"按钮
        selector = self.read_yaml_element("asset_all_group_add_button")
        self._click(selector)
        # 输入素材组名称
        selector = self.read_yaml_element("group_name_input")
        self._fill(selector, text)
        # 点击保存
        selector = self.read_yaml_element("group_save_button")
        self._click(selector)