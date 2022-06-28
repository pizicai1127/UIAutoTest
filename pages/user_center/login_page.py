#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 2:01 下午
# @Author  : wmt
# @File    : login_page.py
# @Software: PyCharm
from common.exception_handle import element_not_found_exception
from common.file_method import FileMethod

from pages.basepage import BasePage
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# 方法一：直接取值获取用户中心元素路由
file_path = FileMethod().get_file_path("pages","user_center","uc_ui_element.yaml")

# file_path = FileMethod().get_file_path("pages/center/uc_ui_element.yaml")
# file_path="./pages/center/uc_ui_element.yaml"

elemParams = FileMethod().read_yaml(file_path)


# 方法二：新写一个文件处理读取元素的方法，感觉有点冗余，先把这个方法放弃
# elemParams = ElemParams("center","uc_ui_element.yaml")



class LoginPage(BasePage):

    # def __init__(self,page: Page):
    #
    #
    #    #BasePage
    #    super().__init__(page)

    #
    def open_page(self,url):

        self._go(urls=url)
        # 等待业务加载
        self._wait(5)
        # 获取当前用户中心登录也路由
        return self._get_url()




    def login(self,url,username,password):
        """
        该登录方法是指输入域名后跳转到id.tezign.com用户中心登录使用用户名/密码登录方法，
        比如输入vms-t2.tezign.com登录页跳转到idxx.tezign.com
        username：用户名
        password：密码
        """
        group_name = "Uc_login_page_selectors" #用户中心登录页元素分组名
        #第一步，打开浏览器路由
        self._go(urls=url)
        # 等待页面加载
        self._wait(5)
        # 等待页面加载

        # 接下来，输入用户名、密码，点击登录按钮
        username_elem=elemParams[group_name]["username"]
        # username_elem=self.elemParams.get_locator("Uc_login_page_selectors","username") #用户名输入框
        self._fill(element=username_elem,text=username) #用户名输入框输入用户名

        password_elem = elemParams[group_name]["password"] #密码输入框
        self._fill(element=password_elem, text=password)  # 用户名输入框输入用户名
        self._click(element=elemParams[group_name]["click_policy"])  #勾选用户协议
        self._click(element=elemParams[group_name]["login_btn"])   #勾选登录按钮

    def vercode_login(self,url,username,password):
        """
        该登录方法是指输入域名后跳转到id.tezign.com用户中心登录使用用户名/密码登录方法，
        比如输入vms-t2.tezign.com登录页跳转到idxx.tezign.com
        username：用户名
        password：密码
        """
        group_name = "Uc_login_page_selectors" #用户中心登录页元素分组名
        #第一步，打开浏览器路由
        self._go(urls=url)
        # 等待页面加载
        self._wait(5)
        # 等待页面加载

        # 接下来，输入用户名、密码，点击登录按钮
        username_elem=elemParams[group_name]["username"]
        # username_elem=self.elemParams.get_locator("Uc_login_page_selectors","username") #用户名输入框
        self._fill(element=username_elem,text=username) #用户名输入框输入用户名

        password_elem = elemParams[group_name]["password"] #密码输入框
        self._fill(element=password_elem, text=password)  # 用户名输入框输入用户名
        self._click(element=elemParams[group_name]["click_policy"])  #勾选用户协议
        self._click(element=elemParams[group_name]["login_btn"])   #勾选登录按钮




    def old_login(self,url,username,password):
        """
        该登录方法是指输入域名后显示的租户/user/login旧的登录页，比如输入vms-t2.tezign.com登录页依旧
        为vms-t2.tezign.com/user，不走用户中心登录
        该登录页面已经废弃
        """

        group_name = "Asset_login_page_selectors" #旧登录页分组名称
        # 第一步，打开浏览器路由
        self._go(urls=url)
        # 等待页面加载
        self._wait(5)
        #接下来，输入用户名、密码，点击登录按钮

        username_elem=elemParams[group_name]["username"]
        # username_elem=self.elemParams.get_locator("Uc_login_page_selectors","username") #用户名输入框
        self._fill(element=username_elem,text=username) #用户名输入框输入用户名

        password_elem = elemParams[group_name]["password"] #密码输入框
        self._fill(element=password_elem, text=password)  # 用户名输入框输入用户名
        self._click(element=elemParams[group_name]["checkbut"])  #勾选用户协议
        self._click(element=elemParams[group_name]["login_btn"])   #勾选登录按钮
        # 登录成功后，等待页面加载
        self._wait(8)




    def open_ssologinpage(self,url):

        self._go(urls=url)
        # 等待业务加载
        self._wait(5)

    def dinglogin(self,code_url,url,phone,password):
        group_name = "Ding_login_page_selectors"  # 旧登录页分组名称
        #url="https://oapi.dingtalk.com/connect/oauth2/sns_authorize?redirect_uri=https://service.tezign.com/user-center/oauth2/callback&appid=dingmnvf1o36hfuksq3r&response_type=code&scope=snsapi_login&state=10187_t2"
        self._go(code_url)
        #打开钉钉登录二维码界面
        self._go(url)
        # 等待业务加载
        self._click(element=elemParams[group_name]["goto_login"])
        self._wait(3)
        self._fill(element=elemParams[group_name]["input_phone"], text=phone)
        self._fill(element=elemParams[group_name]["input_pass"], text=password)
        self._click(element=elemParams[group_name]["login_btn"])
        self._wait(10)


    def feishulogin(self):
        pass






class LogoutSys(BasePage):

    def close_tzvideo_wrap(self):
        # 工作流首次登录会弹出新手引导，需要关闭新手引导
        if self._is_visible(elemParams["Workflow_page_selectors"]["tz_video"]):
            self._click(elemParams["Workflow_page_selectors"]["tz_video_btn"])



    def logout(self):
        """
        库组合并退出登录
        """
        self._wait(5)
        # 开始退出登录，点击用户头像-点击退出登录按钮
        group_name="Asset_logout_selectors"
        self._click(elemParams[group_name]["menu_btn"]) #库组合并 用户头像
        self._click(elemParams["Asset_logout_selectors"]["logout_btn"]) #库组合并 退出登录按钮
        self._wait(5)





#调试登录方法的
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     # Open new page
#     page = context.new_page()
#     alg=LoginPage(page)
#     out=LogoutSys(page)
#     code_url="https://oapi.dingtalk.com/connect/oauth2/sns_authorize?redirect_uri=https://service.tezign.com/user-center/oauth2/callback&appid=dingmnvf1o36hfuksq3r&response_type=code&scope=snsapi_login&state=10187_t2"#生产sso
#     url="https://oapi.dingtalk.com/connect/oauth2/sns_authorize?redirect_uri=https://service.tezign.com/user-center/oauth2/callback&appid=dingmnvf1o36hfuksq3r&response_type=code&scope=snsapi_login&state=10187_t2"
#
#     username="18817771750"
#     password="W15903757919"
#     # alg.open_page(url=url)
#     alg.dinglogin(code_url,url,phone=username,password=password)
    # alg._wait(12)










