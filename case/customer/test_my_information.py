#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/24 5:00 下午
# @File : test_my_information.py
import pytest

from pages.customer.MyInformationPage import MyInformationPage


class TestMyInformation:
    shuju = [
        {
            "input_company_name_empty": "",
            "input_company_name": "测试公司",
            "input_company_introduction_empty": "",
            "introduction_name": "公司简介",
            "network_name": "www.baidu.com",
            "network_name_empty": "",
            "input_name_btn_empty": "",
            "input_name_btn": "测试用户",
            "input_position_btn_empty": "",
            "input_position_btn": "测试职位",

        }]

    # 查看客户的基本信息
    def test_my_information(self, test_login_btn):
        # test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.information()

    # 查看我的评价
    def test_my_evaluation(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.my_evaluation()

    # 查看对我的评价
    def test_to_be_evaluated(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.to_be_evaluated()

    # 公司名称
    @pytest.mark.parametrize("data", shuju)
    def test_company_name(self, test_login_btn, data):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.company_name(data["input_company_name_empty"], data["input_company_name"], )

    # 公司简介
    @pytest.mark.parametrize("data", shuju)
    def test_company_introduction(self, test_login_btn, data):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.company_introduction(data["input_company_introduction_empty"],data["introduction_name"],)

    # 公司网址
    @pytest.mark.parametrize("data", shuju)
    def test_company_network(self, test_login_btn, data):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.company_network(data["network_name"], data["network_name_empty"],)

    # 公司实名认证
    def test_company_real_name_authentication(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.company_real_name_authentication()

    # 账号设置
    def test_account_settings(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.account_settings()

    # 用户名称
    @pytest.mark.parametrize("data", shuju)
    def test_account_name(self, test_login_btn, data):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.account_name(data["input_name_btn_empty"], data["input_name_btn"], )

    # 用户职位
    @pytest.mark.parametrize("data", shuju)
    def test_position_name(self, test_login_btn, data):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.position_name(data["input_position_btn_empty"], data["input_position_btn"], )

    # 个人实名
    def test_personal_real_name(self, test_login_btn):
        test_login_btn[0].goto("https://www.tezign.com/client/#/account/profile")
        page = MyInformationPage(test_login_btn[0])
        page.personal_real_name()