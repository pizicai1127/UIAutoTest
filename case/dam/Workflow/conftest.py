# -*- coding: utf-8 -*- 
# @Time : 2022/3/16 10:58 上午 
# @Author : liuzhijie
# @File : conftest.py
import os
import time
import pytest
from playwright.sync_api import Browser
from common.logger import logger
from conf.confs import Host2, account_LZJ_006, password_LZJ_006, url_workflowPage
from pages.assets.WorkFlowPage import WorkflowPage
from pages.user_center.login_page import LoginPage



@pytest.fixture(scope='module')
def login_init(browser: Browser):
    """
    登录初始化
    @return:
    """
    cookie_file = 'state_lzj.json'
    if os.path.exists(cookie_file):
        context = browser.new_context(storage_state=cookie_file)
        page = context.new_page()
    else:
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        login.login(Host2, account_LZJ_006, password_LZJ_006)
        time.sleep(2)
    yield page
    try:
        # 保存登录验证cookie
        context.storage_state(path=cookie_file)
    except Exception as e:
        logger.info(e)


@pytest.fixture(scope='class')
def workflow_init(login_init):
    """
    首页初始化
    """
    workflowObject = WorkflowPage(login_init)
    workflowObject._go(url_workflowPage)
    workflowObject._wait(2)
    # 关闭公告
    selector = workflowObject.read_yaml_element("notice_close_button")
    if workflowObject._is_visible(selector) is True:
        workflowObject._click(selector)
    # 关闭新手引导
    selector = workflowObject.read_yaml_element("workflow_novice_guide_close_button")
    if workflowObject._is_visible(selector) is True:
        workflowObject._click(selector)
    yield workflowObject
    # 数据清除
    workflowObject._go(url_workflowPage)
    workflowObject._wait(1)
    selector = workflowObject.read_yaml_element("workflow_first_project_name")
    while workflowObject._is_visible(selector) is True:
        if 'UI自动化测试' in workflowObject._text_content(selector):
            workflowObject._click(selector)
            workflowObject._wait(1)
            workflowObject.workflow_delete_project()
        break
