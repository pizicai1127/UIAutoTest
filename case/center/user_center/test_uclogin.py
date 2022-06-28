#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 5:52 下午
# @Author  : wmt
# @File    : test_uclogin.py
# @Software: PyCharm
import time

import allure
import pytest


from common.file_method import FileMethod
from conf.confs import Host2, Appid, account, password

file = FileMethod().get_file_path("case","center","user_center/login_casedata.json")
# file="./case/center/login_casedata.json"
case_data = FileMethod().read_json(file_path=file)
# app_id="t2"
# tenant_url="https://asset-stage.tezign.com"



class TestucLogin():

    @pytest.mark.center
    @pytest.mark.p0
    @allure.title("进入用户中心登录页")
    @allure.description("租户不同业务模块登录-跳转到用户中心登录页")
    @pytest.mark.parametrize("case_data",case_data["steps"])
    def test_to_loginpage(self,login_page_load,case_data):
        go_url =Host2+case_data["case_url"]
        result =login_page_load.open_page(url=go_url)
        login_page_load._wait(8)
        assert_url = "https://id-stage.tezign.com/login?app_id=" + Appid
        assert assert_url in result


    @pytest.mark.center
    @pytest.mark.p0
    @allure.title("用户中心-邮箱密码登录-邮箱+密码正确登录")
    @allure.description("邮箱+密码正确登录")
    @pytest.mark.parametrize("name,pwd",[('wangmengting@666.com','qq111111')])

    def test_email_login_success(self, login_page_load,name,pwd):
        assert_selectors="#user-portrait"
        login_page_load.login(url=Host2,username=name,password=pwd)
        login_page_load._wait(12)
        assert login_page_load._is_visible(assert_selectors)


    @pytest.mark.center
    @pytest.mark.p2
    @allure.title("用户中心-邮箱密码登录-邮箱+密码不正确登录")
    @allure.description("邮箱+密码不正确登录")
    @pytest.mark.parametrize("name,pwd", [('wangmengting@666.com', '111111')])

    def test_email_login_fail(self, login_page_load, name, pwd):
        assert_selectors="div.tz-message.type-error"
        except_context="用户名或者密码有误，忘记密码?"
        login_page_load.login(url=Host2, username=name, password=pwd)
        assert login_page_load._text_content(assert_selectors)==except_context

    @pytest.mark.center
    @pytest.mark.p0
    @allure.title("用户中心-手机密码登录-手机+密码正确登录")
    @allure.description("手机+密码正确登录")
    @pytest.mark.parametrize("name,pwd", [('18817771750', 'qq111111')]) #目前wangmengting@tezign.com账户的手机号 不知道后期会不会变

    def test_phone_login_success(self, login_page_load,name, pwd):

        assert_selectors = "#user-portrait"
        login_page_load.login(url=Host2, username=name, password=pwd)
        login_page_load._wait(12)
        assert login_page_load._is_visible(assert_selectors)

    @pytest.mark.center
    @pytest.mark.p0
    @allure.title("用户中心-手机密码登录-手机号+密码不正确登录")
    @allure.description("手机+密码不正确登录")
    @pytest.mark.parametrize("name,pwd",[('18817771750','111111')])

    def test_phone_login_fail(self, login_page_load,name,pwd):
        assert_selectors = "div.tz-message.type-error"
        expect_content = "用户名或者密码有误，忘记密码?"
        login_page_load.login(url=Host2, username=name, password=pwd)
        assert login_page_load._text_content(assert_selectors) == expect_content

    @pytest.mark.center
    @pytest.mark.p0
    @allure.title("租户退出登录页")
    @allure.description("租户不同业务模块登录-退出到用户中心登录页")
    @pytest.mark.parametrize("case_data", case_data["steps"])

    def test_logout(self, login_page_load,logout_page_load,case_data):
        go_url = Host2 + case_data["case_url"]
        # 第一步 登录
        login_page_load.login(Host2, account, password)
        logout_page_load._wait(8)
        # 第二步 登录后进入业务系统
        login_page_load._go(go_url)
        logout_page_load._wait(10)
        #工作流页面需要先关闭新手弹窗
        logout_page_load.close_tzvideo_wrap()
        #第三步，正式退出系统
        logout_page_load.logout()
        logout_page_load._wait(8)
        # 第三步，退出系统后回去当时页面路径
        result = logout_page_load._get_url()
        assert_url = "https://id-stage.tezign.com/login?app_id=" + Appid
        assert assert_url == result


    @pytest.mark.center
    @pytest.mark.p0
    @allure.title("用户中心-钉钉sso登录")
    @allure.description("钉钉sso登录")
    def test_dinglogin(self, login_page_load):
        code_url="https://oapi.dingtalk.com/connect/qrconnect?redirect_uri=https://service.tezign.com/user-center/oauth2/callback&appid=dingmnvf1o36hfuksq3r&response_type=code&scope=snsapi_login&state=10185_t2"
        url="https://oapi.dingtalk.com/connect/oauth2/sns_authorize?redirect_uri=https://service.tezign.com/user-center/oauth2/callback&appid=dingmnvf1o36hfuksq3r&response_type=code&scope=snsapi_login&state=10185_t2"
        phone="18817771750"
        password="W15903757919"
        assert_selectors = "#user-portrait"
        login_page_load.dinglogin(code_url,url,phone,password)
        login_page_load._wait(10)
        assert login_page_load._is_visible(assert_selectors)