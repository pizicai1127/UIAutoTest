#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/2 4:16 下午
# @Author  : wmt
# @File    : dam_member_page.py
# @Software: PyCharm
from playwright.sync_api import sync_playwright

from common.file_method import FileMethod
from pages.basepage import BasePage
from pages.user_center.login_page import LoginPage

file_path = FileMethod().get_file_path("pages","user_center","uc_ui_element.yaml")
elemParams = FileMethod().read_yaml(file_path)
group_name = "Members_page_selectors"

class DamMemberPage(BasePage):

    def add_one_only_email(self,name,email):
        """
        逐个添加-只添加邮箱
        """
        # 第一步，点击添加成员按钮
        self._click(element=elemParams[group_name]["add_member_btn"])
        # 第二步，点击逐个添加按钮
        self._click(element=elemParams[group_name]["add_one_btn"])
        self._wait(3)
        # 第三步，输入用户名，邮箱
        self._fill(element=elemParams[group_name]["addmember_name"], text=name)
        self._fill(element=elemParams[group_name]["addmember_email"], text=email)
        self._wait(2)
        #添加用户弹窗-选择部门
        self._click(element=elemParams[group_name]["addmember_dept"])
        self._wait(3)
        self._click(element=elemParams[group_name]["addmember_dept_select"])
        self._wait(2)
        # 添加用户弹窗-点击注册按钮
        self._click(element=elemParams[group_name]["add_confirm_btn"])



    def add_one_email_phone(self,name,email,phone):
        """
        逐个添加-只添加邮箱
        """
        # 第一步，点击添加成员按钮
        self._click(element=elemParams[group_name]["add_member_btn"])
        # 第二步，点击逐个添加按钮
        self._click(element=elemParams[group_name]["add_one_btn"])
        self._wait(3)
        # 第三步，输入用户名，邮箱
        self._fill(element=elemParams[group_name]["addmember_name"], text=name)
        self._fill(element=elemParams[group_name]["addmember_email"], text=email)
        self._wait(1)
        self._fill(element=elemParams[group_name]["addmember_phone"], text=phone)
        self._wait(2)
        #添加用户弹窗-选择部门
        self._click(element=elemParams[group_name]["addmember_dept"])
        self._wait(3)
        self._click(element=elemParams[group_name]["addmember_dept_select"])
        self._wait(2)
        # 添加用户弹窗-点击注册按钮
        self._click(element=elemParams[group_name]["add_confirm_btn"])

    def add_bulk(self,path):
        """
        批量添加企业成员-上传文件
        """
        # 第一步，点击添加成员按钮
        self._click(element=elemParams[group_name]["add_member_btn"])
        # 第二步，点击批量添加按钮
        self._click(element=elemParams[group_name]["add_bulk_btn"])
        self._wait(3)
        #第三步，点击选择文件按钮，上传文件
        self._upload_file_chooser(element=elemParams[group_name]["bulk_add_file_select"],path=path)
        self._wait(2)
        # 添加用户弹窗-选择部门
        self._click(element=elemParams[group_name]["addmember_dept"])
        self._wait(3)
        self._click(element=elemParams[group_name]["addmember_dept_select"])
        self._wait(2)
        # 添加用户弹窗-点击注册按钮
        self._click(element=elemParams[group_name]["add_confirm_btn"])



    def search_member(self,keyword):
        """
        成员信息-搜索用户方法
        """
        self._fill(element=elemParams[group_name]["search_input"],text=keyword)
        self._wait(4)
        self._keyboard_click("Enter")
        self._wait(3)


    def edit_member(self):
        """
        成员信息-编辑用户方法
        """

        #第一步 点击编辑按钮
        self._click(element=elemParams[group_name]["edit_btn"])
        #展示编辑弹窗
        self._wait(4)
        #编辑成员信息，点击确认编辑按钮
        self._click(element=elemParams[group_name]["edit_confirm_btn"])

    def delete_member(self):
        """
        成员信息-注销成员方法
        """

        #第一步，点击更多按钮
        self._click(element=elemParams[group_name]["more_btn"])
        self._wait(3)
        #第二步，点击注销按钮
        self._click(element=elemParams[group_name]["delete_btn"])
        self._wait(3)
        self._click(element=elemParams[group_name]["delete_confirm_btn"])
        # self._wait(1)


    def delete_member_serach(self,keyword):
        """
        已注销页面-搜索用户
        """
        # 第一步，点击已注销成员按钮
        self._click(element=elemParams[group_name]["delete_member_btn"])
        self._wait(4)
        #第二步，搜索框输入关键词搜索用户
        self._fill(element=elemParams[group_name]["search_input"], text=keyword)
        self._wait(3)
        self._keyboard_click("Enter")
        self._wait(3)






# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     # Open new page
#     page = context.new_page()
#     alg=LoginPage(page)
#     mip =DamMemberPage(page)
#
#     url="https://asset-stage.tezign.com/base/company/setting-member"
#     username="wangmengting@tezign.com"
#     passwprd="qq111111"
#     # alg.open_page(url=url)
#     alg.login(url=url,username=username,password=passwprd)
#     alg._wait(10)
#     # mip.search_member("wangmengting@tezign.com")
#     # mip.edit_member()
#     bulk_file = FileMethod().get_file_path("data", "", "成员导入模板.xlsx")
#     mip.add_bulk(bulk_file)
#     mip._wait(2)





