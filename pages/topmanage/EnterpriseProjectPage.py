#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/7 11:28 上午
# @File : EnterpriseProjectPage.py
from pages.topmanage.TopBasePage import TopBasePage


class EnterpriseProjectPage(TopBasePage):
    selectors = {
        "crm": "#rc-root > div.main > div.side > div.side_row1 > ul > li:nth-child(3) > div > span > span",
        "enterprise_project":"#subMenu-2\$Menu > li:nth-child(6)",
        "draft": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(1) > span:nth-child(2)",
        "not_pushed": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(2) > span:nth-child(2)",
        "customer_selection_in_progress": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(3) > span:nth-child(2)",
        "customer_confirmation_in_progress": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(4) > span:nth-child(2)",
        "the_project_has_expired": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(5) > span:nth-child(2)",
        "project_startup": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(6) > span:nth-child(2)",
        "project_in_progress": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(7) > span:nth-child(2)",
        "unpaid": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(8) > span:nth-child(2)",
        "project_termination": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(9) > span:nth-child(2)",
        "project_closing": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-20 > div > label:nth-child(10) > span:nth-child(2)",
        "query_btn": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(8) > div > button.tz-btn.type-primary.shape-round",
        "reset": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(8) > div > button.tz-btn.type-neutral.shape-round.ghost-solid",
        "background_creation": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(2) > div.ant-col.ant-col-20 > div > label:nth-child(1) > span:nth-child(2)",
        "tenant_creation": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(2) > div.ant-col.ant-col-20 > div > label:nth-child(2) > span:nth-child(2)",
        "one_on_one": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(3) > div.ant-col.ant-col-20 > div > label:nth-child(1) > span:nth-child(2)",
        "one_to_many_master_project": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(3) > div.ant-col.ant-col-20 > div > label:nth-child(2) > span:nth-child(2)",
        "one_to_many_subprojects": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(3) > div.ant-col.ant-col-20 > div > label:nth-child(3) > span:nth-child(2)",
        "no_TP_docking_project": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(4) > div.ant-col.ant-col-20 > div > label > span:nth-child(2)",
        "input_personnel": 'ul[role="group"] >> :nth-match(span, 3)',
        "blank": ".tz-panel",
        "input": '[aria-label="filter select"]',
        "keyword_search": "input[placeholder=\"项目名称/企业名称\"]",
        "open": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div.ant-collapse-header > i",
        "put_away": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div.ant-collapse-header > i",
        "left_btn": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(2) > div > div.panel-pagination > ul > li.ant-pagination-disabled.ant-pagination-prev",
        "second_page": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(2) > div > div.panel-pagination > ul > li.ant-pagination-item.ant-pagination-item-2 > a",
        "back_5_pages": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(2) > div > div.panel-pagination > ul > li.ant-pagination-jump-next.ant-pagination-jump-next-custom-icon > a > div > span",
        "right_btn": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(2) > div > div.panel-pagination > ul > li.ant-pagination-next > a",
        "previous_page": "#rc-root > div.main > div.wrap > div > div.project-list > div:nth-child(2) > div > div.panel-pagination > ul > li.ant-pagination-prev",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",
        # "enterprise_project": "#subMenu-2\$Menu > li:nth-child(6)",

    }

    def enterprise_project_state(self):
        # # 点击crm，企业项目
        # self._click(EnterpriseProjectPage.selectors['crm'])
        # self._click(EnterpriseProjectPage.selectors['enterprise_project'])
        # 项目状态，草稿
        self._check(EnterpriseProjectPage.selectors['draft'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态，未推送
        self._check(EnterpriseProjectPage.selectors['not_pushed'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态客户选择中
        self._check(EnterpriseProjectPage.selectors['customer_selection_in_progress'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态，客户确认中
        self._check(EnterpriseProjectPage.selectors['customer_confirmation_in_progress'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态，项目失效
        self._check(EnterpriseProjectPage.selectors['the_project_has_expired'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态，项目启动
        self._check(EnterpriseProjectPage.selectors['project_startup'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态，项目进行中
        self._check(EnterpriseProjectPage.selectors['project_in_progress'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态，未支付
        self._check(EnterpriseProjectPage.selectors['unpaid'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态，项目终止
        self._check(EnterpriseProjectPage.selectors['project_termination'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        # 项目状态，项目完结
        self._check(EnterpriseProjectPage.selectors['project_closing'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        self._click(EnterpriseProjectPage.selectors['reset'])

    def enterprise_project_source(self):
        # 点击来源，后台和租户创建
        self._check(EnterpriseProjectPage.selectors['background_creation'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        self._check(EnterpriseProjectPage.selectors['tenant_creation'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])

    def cooperation_mode(self):
        # 点击其他，查询
        self._check(EnterpriseProjectPage.selectors['one_on_one'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        self._check(EnterpriseProjectPage.selectors['one_to_many_master_project'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        self._check(EnterpriseProjectPage.selectors['one_to_many_subprojects'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        self._check(EnterpriseProjectPage.selectors['no_TP_docking_project'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])

    def business_personnel(self, personnel):
        # 点击业务来源，选择top业务人员查询
        self._fill(EnterpriseProjectPage.selectors['input'], personnel)
        self._click(EnterpriseProjectPage.selectors['input_personnel'])
        self._click(EnterpriseProjectPage.selectors['blank'])
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        self._click(EnterpriseProjectPage.selectors['reset'])

    def keyword_search(self, keyword):
        # 点击业务来源，选择top业务人员查询
        self._fill(EnterpriseProjectPage.selectors['keyword_search'], keyword)
        self._click(EnterpriseProjectPage.selectors['query_btn'])
        self._click(EnterpriseProjectPage.selectors['reset'])
        self._click(EnterpriseProjectPage.selectors['open'])
        self._click(EnterpriseProjectPage.selectors['put_away'])

    def paging(self):
        # 点击分页
        self._hover(EnterpriseProjectPage.selectors['left_btn'])
        self._click(EnterpriseProjectPage.selectors['second_page'])
        self._hover(EnterpriseProjectPage.selectors['back_5_pages'])
        self._click(EnterpriseProjectPage.selectors['back_5_pages'])
        self._click(EnterpriseProjectPage.selectors['right_btn'])
        self._click(EnterpriseProjectPage.selectors['previous_page'])
