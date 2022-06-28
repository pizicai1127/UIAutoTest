#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : conftest.py"""

import pytest

from pages.designer.ProjectPage import ProjectPage


class Testproject:

    # 对创意方项目进行查看
    def test_project(self, test_login):
        test_login[0].goto("https://www.tezign.com/designer/#/projects")
        page = ProjectPage(test_login[0])
        page.project_case()


