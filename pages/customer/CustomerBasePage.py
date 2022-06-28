#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : CustomerBasePage.py"""

"""
    用来存放项目中的一些 公共方法，比如 获取验证码等
    """
import pymysql
from playwright.sync_api import Page
import re
# from pages.basepage import BasePage
from pages.designer.BasePage import BasePage


class CustomerBasePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page=page)

    @staticmethod

    def get_auth_code():
        """从数据库中获取验证码"""
        # 建立链接
        conn = pymysql.connect(
            host="rr-2ze77jq079wm3y975.mysql.rds.aliyuncs.com",
            port=3306,
            user="sop_developer",
            password="DWF23RDC@erf234d",
            db="tezign"
        )

        # 创建游标
        cur = conn.cursor()

        # 查询 邮件内容
        cur.execute(
            "select content from tezign.tbl_email where `to` = 'tzvirtual1@tezign.com' order by create_time desc limit 1;")

        # 获取邮件数据
        result = cur.fetchall()
        print(result)
        # 获取 到验证码 n
        auth_code = re.findall(r"邮箱登录验证码「(.+?)」", str(result))
        return auth_code


