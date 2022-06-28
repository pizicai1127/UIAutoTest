#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 6:39 下午
# @Author  : wmt
# @File    : login_page_backup.py
# @Software: PyCharm
from playwright.sync_api import sync_playwright

from playwright.sync_api import Page

from pages.basepage import BasePage


class AssetLoginPage(BasePage):
    # 用户中心登录页 元素
    login_selectors= {
        "username": "[placeholder='邮箱/手机']" , # 登录页 -账号输入框
        "password":"input[type='password']" , # 登录页-，密码输入框
        "click_policy":"[type='checkbox']" , # 登录页面-勾选（我已阅读并同意《用户协议》及隐私政策）
        "login_btn": "button[type='submit']" , # 登录页-登录按钮
    }
    #用户中心登录页 忘记密码元素
    forget_selectors={
        ""
    }

    #租户侧库组合并退出登录 页面元素
    logout_selectors={
        "tz_video": "div.ant-modal-content",  # 工作流-新手引导元素
        "tz_video_btn": "div.ant-modal-content>div>div>button",  # 工作流-新手引导按钮我知道了
        "menu_btn": "#user-portrait",  # 系统用户头像按钮
        "logout_btn": "#user-portrait > div > div > div > div > div:last-child",  # 退出登录按钮
    }
    #旧退出登录页面元素
    old_loginout_selectors = {
        "menu_button": "#navbar-user-page-menu",  # 系统用户头像按钮
        "logout_button": "li.ant-menu-item.menu-item-quit"  # 退出登录按钮
    }


    # 未登录用户输入业务路由，跳转到用户中心登录页
    def to_loginpage(self, url):
        #输入业务路由，跳转到登录页面
            self._go(urls=url)
        #等待业务加载
            self.page.wait_for_timeout(5000)
        #获取当前用户中心登录也路由
            return self._get_url()

    #租户侧-用户中心登录页-登录系统
    def login(self,url,username,password):
        #第一步：业务模块路由，跳转到用户中心登录页
        self.to_loginpage(url=url)
        #第二步：输入用户名和密码
        self._fill(self.login_selectors["username"], text=username)
        self._fill(self.login_selectors["password"], text=password)
        #第三步，勾选（我已阅读并同意《用户协议》及隐私政策）+登录按钮
        self._click(self.login_selectors["click_policy"])
        self._click(self.login_selectors["login_btn"])
        # 登录成功后，等待页面加载
        self.page.wait_for_timeout(5000)



    #租户侧-库组合并新导航-退出登录
    def logout(self):
        #第一步，先进入业务模块路由

        # 工作流首次登录会弹出新手引导，需要关闭新手引导
        if self.page.is_visible(self.logout_selectors["tz_video"]):
            self._click(self.logout_selectors["tz_video_btn"])

        self.page.wait_for_timeout(3000)
        #开始退出登录，点击用户头像-点击退出登录按钮
        self._click(self.logout_selectors["menu_btn"])
        self._click(self.logout_selectors["logout_btn"])
        self.page.wait_for_timeout(5000)
        #获取当前页面的url
        return self._get_url()





# # 调试登录方法的
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     # Open new page
#     page = context.new_page()
#     alg=AssetLoginPage(page)
#     url="https://data-stage.tezign.com"
#     username="wangmengting@tezign.com"
#     passwprd="tz111111"
#     alg.login(url=url,username=username,password=passwprd)


