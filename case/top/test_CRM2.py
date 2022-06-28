#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_CRM2.py

import pytest
from pages.top.CRM02 import CRM2

class TestCRM:

    @pytest.mark.p0
    def test_soso_enquiry(self, topLogin):
        # 嗖嗖询价/报价
        page = CRM2(topLogin)
        text_assert1 = page.soso_enquiry()
        assert text_assert1 == "这是一个测试报价单"

    @pytest.mark.p0
    def test_business_signing(self, topLogin):
        # 业务签单
        page = CRM2(topLogin)
        text_assert2 = page.business_signing()
        assert text_assert2[0] == "收入金额"
        assert text_assert2[1] == "销售机会详情页"



    @pytest.mark.p0
    def test_enterprise_projects(self, topLogin):
        # 企业项目
        page = CRM2(topLogin)
        text_assert3 = page.enterprise_projects()
        assert text_assert3[0] == "大C测试预发1"
        assert text_assert3[1] == "项目完结"


    @pytest.mark.p0
    def test_enterprise_contacts(self, topLogin):
        # 企业客户/联系人
        page = CRM2(topLogin)
        text_assert4 = page.enterprise_contacts()


    @pytest.mark.p0
    def test_operational_audits(self, topLogin):
        # 运营审核审批
        page = CRM2(topLogin)
        text_assert5 = page.operational_audits()
        assert text_assert5 == "签单凭证"
