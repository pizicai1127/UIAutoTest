#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : conftest.py"""

import pytest
from playwright.sync_api import Playwright
from pages.customer.LoginPage import LoginPage
# @pytest.mark.skipif(1 == 1, reason="调试中")


@pytest.fixture(scope='session', autouse=True)
# @pytest.mark.parametrize("data", pro_account),slow_mo=800,headless=False
def test_login_btn(playwright: Playwright):
    data = {
        "account": "13951515151",
        "password": "Zjb139056",
    }
    browser = playwright.chromium.launch(slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page1 = LoginPage(page)

    # 打开创意方登陆页面
    page1.goto("https://id.tezign.com/login?app_id=tz_customer")
    print("成功进入自然流量登陆网页")
    page1.check_element()
    # page.fill(LoginPage.selectors['password'], 542124953@qq.com)
    page1.login(data["account"], data["password"])

    yield page, page1

    # context.close()
    # browser.close()

# if __name__ == '__main__':
#     pytest.main(['-m designer'])
# print("1")
