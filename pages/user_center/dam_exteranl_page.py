#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 4:11 下午
# @Author  : wmt
# @File    : dam_exteranl_page.py
# @Software: PyCharm
from playwright.sync_api import sync_playwright

from common.file_method import FileMethod
from pages.basepage import BasePage
from pages.user_center.login_page import LoginPage

file_path = FileMethod().get_file_path("pages","user_center","uc_ui_element.yaml")
elemParams = FileMethod().read_yaml(file_path)
group_name = "External_page_selectors"

class DamExternalPage(BasePage):

    def add_one_btn(self):
        """
        逐个添加按钮
        """
        # 第一步，点击添加成员按钮
        self._click(element=elemParams[group_name]["add_member_btn"])
        # 第二步，点击逐个添加按钮
        self._click(element=elemParams[group_name]["add_one_btn"])

    def add_bulk_btn(self):
        """
        批量添加按钮
        """
        # 第一步，点击添加成员按钮
        self._click(element=elemParams[group_name]["add_member_btn"])
        # 第二步，点击逐个添加按钮
        self._click(element=elemParams[group_name]["add_bulk_btn"])

    def input_name(self,name):
        """
        添加外部成员-单个添加弹窗，输入姓名方法
        """
        self._fill(element=elemParams[group_name]["addmember_name"], text=name)
    def input_email(self,email):
        """
        添加外部成员-单个添加弹窗，输入邮箱方法
        """
        self._fill(element=elemParams[group_name]["addmember_email"], text=email)
    def input_phone(self,email):
        """
        添加外部成员-单个添加弹窗，输入手机号方法
        """
        self._fill(element=elemParams[group_name]["addmember_phone"], text=email)

    def select_dimension(self):
        """
        添加外部用户弹窗-添加所属维度方法
        """
        # 添加用户弹窗-点击所属维度维度弹窗
        self._click(element=elemParams[group_name]["addmember_dimension"])
        self._wait(2)
        # 添加用户弹窗-维度列表-点击第一个维度（自动化测试维度）
        self._click(element=elemParams[group_name]["addmember_dimension_select_p"])
        self._wait(2)
        # 添加用户弹窗-维度列表-点击第一个维度（自动化测试维度）的子维度-自动化测试
        self._click(element=elemParams[group_name]["admember_dimension_select_get"])
        self._wait(2)

    def noinit_select(self):
        """
        取消勾选初始化权限
        """
        self._click(element=elemParams[group_name]["not_init_checkbox"])



    def add_one_init(self,name,email=None,phone=None):
        """
        逐个添加-外部联系人-邮箱+初始化账户
        """
        #第一步，点击添加外部成员按钮，弹出添加成员弹窗
        self.add_one_btn()
        self._wait(3)
        # 第二步，输入用户名，邮箱
        self.input_name(name=name)
        self._wait(1)
        if email !=None:
           self.input_email(email)
           self._wait(1)
        if phone !=None:
            self.input_phone(phone)
            self._wait(1)
        #
        self.select_dimension()
        self._wait(2)
        # 添加用户弹窗-所有信息填写完毕，点击导入按钮
        self._click(element=elemParams[group_name]["add_confirm_btn"])
        self._wait(1)

    def add_bulk_init(self,path):
        """
        批量添加-外部联系人-初始化账户
        """
        # 第一步，点击添加外部成员按钮，弹出添加成员弹窗
        self.add_bulk_btn()
        self._wait(3)
        # 第二步，点击成员文件上传，弹出添加成员弹窗
        self._upload_file_chooser(element=elemParams[group_name]["bulk_add_file_select"], path=path)
        self._wait(2)
        self.select_dimension()
        self._wait(2)
        # 所有信息填写完毕，点击导入按钮
        self._click(element=elemParams[group_name]["add_confirm_btn"])
        self._wait(1)


    def search_dimension(self):
        """
        搜索外部维度的方法
        """
        self.dimension="auto_ui"
        # 第一步 点击维度搜索输入框
        self._click(element=elemParams[group_name]["search_dimension"])
        self._wait(1)
        # 第二步，输入搜索的维度
        # self._fill(element=elemParams[group_name]["search_dimension_input"],text=self.dimension)

        self._keyboard_input(text=self.dimension)
        self._wait(2)
        self._keyboard_click("Enter")
        self._wait(2)

    def search_member(self,keyword):
        """
        成员信息-搜索用户方法
        """
        self._fill(element=elemParams[group_name]["search_input"],text=keyword)
        self._wait(3)
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
        self._hover(element=elemParams[group_name]["more_btn"])
        self._wait(2)
        #第二步，点击注销按钮
        self._click(element=elemParams[group_name]["delete_btn"])
        self._wait(2)
        self._click(element=elemParams[group_name]["delete_confirm_btn"])





# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     # Open new page
#     page = context.new_page()
#     alg=LoginPage(page)
#     mip =DamExternalPage(page)
#     url="https://asset-stage.tezign.com/base/company/external-contacts"
#     username="wangmengting@tezign.com"
#     passwprd="qq111111"
#     # alg.open_page(url=url)
#     alg.login(url=url,username=username,password=passwprd)
#     alg._wait(10)
#     # mip.search_member("wangmengting@tezign.com")
#     # mip.edit_member()
#     # mip.add_one_init(name="自动化测试ui",email="auto_ui02@tester.com")
#     # mip.search_dimension()
#     mip.search_member(keyword="sus@tester.com")
#     # mip.delete_member()
#     # path=FileMethod().get_file_path("data", "", "外部联系人导入模板.xlsx")
#     # mip.add_bulk_init(path)
#     mip._wait(3)
