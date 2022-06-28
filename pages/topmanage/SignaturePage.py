#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/6/9 10:51 上午
# @File : SignaturePage.py
from pages.topmanage.TopBasePage import TopBasePage


class SignaturePage(TopBasePage):
    selectors = {
        "crm_tab": "text=CRM/业务管理",
        'signature_tab': 'text=业务签单',
        'open_btn': 'text=展开选项',
        'stow_btn': 'text=收起选项',
        'input_name': '[placeholder="输入签单名称关键词进行搜索"]',
        'reset_btn': 'text=重置筛选',
        'record_btn': 'text=导出签单相关记录 >',
        'signature_detail': ':nth-match(:text("预发测试3"), 2)',
        'expand_option': 'text=展开选项',
        'collapse_option': 'text=收起选项',
        'exception_exceed': 'text=交付超过15天未开票',
        'exception_exceed_accounting_period': 'text=超过账期未回款',
        'exception_gross_profit': 'text=毛利低于40%',
        'exception_signature': 'text=签单超过15天未关联成本',
        'exception_reminder_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'associated_item_project_not_ended': 'text=已关联但项目未完结',
        'associated_item_project_closing': 'text=已关联项目完结',
        'associated_item_not_associated': ':nth-match(span:has-text("未关联"), 2)',
        'associated_item_not_associated_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'in_review': 'text=全部审核中审核通过不通过 >> :nth-match(input[type="radio"], 2)',
        'approved': 'text=全部审核中审核通过不通过 >> :nth-match(input[type="radio"], 3)',
        'audit_failed': 'text=全部审核中审核通过不通过 >> :nth-match(input[type="radio"], 4)',
        'all': ':nth-match(:text("全部"), 2)',
        'signing_voucher_approval_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'delivered': 'text=已交付',
        'Undelivered': 'text=未交付',
        'all_btn': ':nth-match(:text("全部"), 3)',
        'delivery_status_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'partial_invoicing': 'text=部分开票',
        'complete_invoicing': 'text=完成开票',
        'not_invoiced': ':nth-match(:text("未开票"), 2)',
        'invoicing_status_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'partial_payment': 'text=部分结款',
        'complete_payment': 'text=完成结款',
        'not_payment': 'text=未结款',
        'partial_collection': 'text=部分收款',
        'complete_collection': 'text=完成收款',
        'not_collection': 'text=未收款',
        'payment_status_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'collection_status_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'not_associated': 'text=全部已关联未关联 >> :nth-match(input[type="radio"], 3)',
        'associated': 'text=全部已关联未关联 >> :nth-match(input[type="radio"], 2)',
        'all_associated': ':nth-match(:text("全部"), 4)',
        'related_cases_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'undelivered_for_approval': 'text=未交付审批中',
        'TP_calibration_delivered': 'text=已交付TP校准中',
        'delivered_calibrated': 'text=已交付已校准',
        'to_be_calibrated': 'text=待校准',
        'calibration_status': '',
        'calibration_status_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'start_time': '[placeholder="开始日期"]',
        'week': 'text=近一周',
        'month': 'text=本月',
        'three_months': 'text=近三个月',
        'half_a_year': 'text=近半年',
        'last_quarter': 'text=上季度',
        'quarter': 'text=本季度',
        'change_time_of_revenue_amount_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'background_creation': 'text=后台创建',
        'tenant_creation': 'text=租户下单',
        'tenant_ali': 'text=阿里订单',
        'tenant_all': 'text=全部',
        'source_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'customer_department': ':nth-match(:text("请输入关键字搜索"), 2)',
        'ali_department': 'li[role="option"]:has-text("阿里部门")',
        'huarun_department': 'text=华润创业品牌部',
        'ali_department_click': 'text=请输入关键字搜索阿里部门',
        'customer_department_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'invoicing_time': 'text=开票时间 ~ >> [placeholder="开始日期"]',
        'invoicing_time_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'keyword_search': 'text=请输入关键字搜索',
        'ali_company': 'li[role="option"]:has-text("阿里公司")',
        'parent_customer_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'delivery_time': 'text=交付时间 ~ >> [placeholder="开始日期"]',
        'delivery_time_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'business_type': 'text=选择业务类型',
        'M_Saas': 'li[role="option"]:has-text("M+SaaS")',
        'business_type_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'salesman': 'text=请选择销售人员',
        'technology_department': 'text=技术部',
        'salesman_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div.vpinfo > div.vpinfo-left',
        'ali_test_name': 'text=12,720.00',
        # '': '',


    }

    # 签单搜索
    def signature_search(self, input_name):
        # 点击CRM tab
        self._click(SignaturePage.selectors["crm_tab"])
        # 点击业务签单
        self._click(SignaturePage.selectors["signature_tab"])
        # 点击签单名称
        self._click(SignaturePage.selectors["input_name"])
        # 搜索签单名称
        self._fill(SignaturePage.selectors["input_name"], input_name)
        # 点击重置筛选
        self._click(SignaturePage.selectors["reset_btn"])
        # 悬浮签单相关记录
        self._hover(SignaturePage.selectors["record_btn"])

    # 点击签单展开选项异常提醒
    def exception_reminder(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 选择交付超过15天未开票选项
        self._click(SignaturePage.selectors["exception_exceed"])
        self._click(SignaturePage.selectors["exception_exceed"])
        # 选择超过账期未回款选项
        self._click(SignaturePage.selectors["exception_exceed_accounting_period"])
        self._click(SignaturePage.selectors["exception_exceed_accounting_period"])
        # 选择毛利低于40%选项
        self._click(SignaturePage.selectors["exception_gross_profit"])
        self._click(SignaturePage.selectors["exception_gross_profit"])
        # 选择签单超过15天未关联成本选项
        self._click(SignaturePage.selectors["exception_signature"])
        # self._wait(1)

    # 点击签单展开选项关联项目状态
    def associated_item_status(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 点击已关联但项目未完结
        self._click(SignaturePage.selectors["associated_item_project_not_ended"])
        self._click(SignaturePage.selectors["associated_item_project_not_ended"])
        # 点击已关联项目完结
        self._click(SignaturePage.selectors["associated_item_project_closing"])
        self._click(SignaturePage.selectors["associated_item_project_closing"])
        # 点击未关联
        self._click(SignaturePage.selectors["associated_item_not_associated"])

    # 点击签单展开选项签单凭证审核
    def signing_voucher_approval(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 在签单凭证审核中，点击审核中
        self._click(SignaturePage.selectors["in_review"])
        # 在签单凭证审核中，点击审核通过
        self._click(SignaturePage.selectors["approved"])
        # 在签单凭证审核中，点击审核不通过
        self._click(SignaturePage.selectors["audit_failed"])
        # 在签单凭证审核中，点击审核全部
        self._click(SignaturePage.selectors["all"])

    # 点击签单展开选项，交付状态
    def delivery_status(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 交付状态，未交付
        self._click(SignaturePage.selectors["Undelivered"])
        # 交付状态，全部
        self._click(SignaturePage.selectors["all_btn"])
        # 交付状态，已交付
        self._click(SignaturePage.selectors["delivered"])

    # 点击签单展开选项，开票状态
    def invoicing_status(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 开票状态，部分开票
        self._click(SignaturePage.selectors["partial_invoicing"])
        self._click(SignaturePage.selectors["partial_invoicing"])
        # 开票状态，完成开票
        self._click(SignaturePage.selectors["complete_invoicing"])
        self._click(SignaturePage.selectors["complete_invoicing"])
        # 开票状态，未开票
        self._click(SignaturePage.selectors["not_invoiced"])

    # 点击签单展开选项，创意方结款状态
    def payment_status(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 创意方结款状态，部分结款
        self._click(SignaturePage.selectors["partial_payment"])
        self._click(SignaturePage.selectors["partial_payment"])
        # 创意方结款状态，完成结款
        self._click(SignaturePage.selectors["complete_payment"])
        self._click(SignaturePage.selectors["complete_payment"])
        # 创意方结款状态，未结款
        self._click(SignaturePage.selectors["not_payment"])

    # 点击签单展开选项，收款状态
    def collection_status(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 收款状态，部分收款
        self._click(SignaturePage.selectors["partial_collection"])
        self._click(SignaturePage.selectors["partial_collection"])
        # 收款状态，完成收款
        self._click(SignaturePage.selectors["complete_collection"])
        self._click(SignaturePage.selectors["complete_collection"])
        # 收款状态，未收款
        self._click(SignaturePage.selectors["not_collection"])

    # 点击签单展开选项，关联案例
    def related_cases(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 关联案例，未关联
        self._click(SignaturePage.selectors["not_associated"])
        # 关联案例，全部
        self._click(SignaturePage.selectors["all_associated"])
        # 关联案例，已关联
        self._click(SignaturePage.selectors["associated"])

    # 点击签单展开选项，校准状态
    def calibration_status(self):
        # 点击展开选项
        self._click(SignaturePage.selectors["expand_option"])
        # 校准状态，未交付审批中
        self._click(SignaturePage.selectors["undelivered_for_approval"])
        # 校准状态，已交付TP校准中
        self._click(SignaturePage.selectors["TP_calibration_delivered"])
        # 校准状态，已交付已校准
        self._click(SignaturePage.selectors["delivered_calibrated"])
        # 校准状态，待校准
        self._click(SignaturePage.selectors["to_be_calibrated"])

    # 点击签单展开选项，收入金额变更时间
    def change_time_of_revenue_amount(self):
        # 点击收入金额变更时间
        self._click(SignaturePage.selectors["start_time"])
        # 鼠标悬浮近一周
        self._hover(SignaturePage.selectors["week"])
        # 鼠标悬浮本月
        self._hover(SignaturePage.selectors["month"])
        # 鼠标悬浮近三个月
        self._hover(SignaturePage.selectors["three_months"])
        # 鼠标悬浮近半年
        self._hover(SignaturePage.selectors["half_a_year"])
        # 鼠标悬浮上个季度
        self._hover(SignaturePage.selectors["last_quarter"])
        # 鼠标悬浮本季度
        self._hover(SignaturePage.selectors["quarter"])
        # 鼠标点击本季度
        self._click(SignaturePage.selectors["quarter"])

    # 点击来源搜索
    def source(self):
        # 来源，点击后台创建
        self._click(SignaturePage.selectors["background_creation"])
        # 来源，点击租户创建
        self._click(SignaturePage.selectors["tenant_creation"])
        # 来源，点击全部
        self._click(SignaturePage.selectors["tenant_all"])
        # 来源，点击阿里订单
        self._click(SignaturePage.selectors["tenant_ali"])

    # 点击客户、部门搜索
    def customer_department(self):
        # 点击客户部门
        self._click(SignaturePage.selectors["customer_department"])
        # 客户部门，选择阿里部门
        self._click(SignaturePage.selectors["ali_department"])
        # 客户部门,点击阿里部门
        self._click(SignaturePage.selectors["ali_department_click"])
        # 客户部门，选择华润部门
        self._click(SignaturePage.selectors["huarun_department"])

    #   选择开票时间
    def invoicing_time(self):
        # 点击收入金额变更时间
        self._click(SignaturePage.selectors["invoicing_time"])
        # 鼠标悬浮近一周
        self._hover(SignaturePage.selectors["week"])
        # 鼠标悬浮本月
        self._hover(SignaturePage.selectors["month"])
        # 鼠标悬浮近三个月
        self._hover(SignaturePage.selectors["three_months"])
        # 鼠标悬浮近半年
        self._hover(SignaturePage.selectors["half_a_year"])
        # 鼠标悬浮上个季度
        self._hover(SignaturePage.selectors["last_quarter"])
        # 鼠标悬浮本季度
        self._hover(SignaturePage.selectors["quarter"])
        # 鼠标点击本季度
        self._click(SignaturePage.selectors["quarter"])

    # 搜索上级客户
    def parent_customer(self):
        # 点击上级客户搜索框
        self._click(SignaturePage.selectors["keyword_search"])
        # 选择阿里公司
        self._click(SignaturePage.selectors["ali_company"])

    # 搜索交付时间
    def delivery_time(self):
        # 点击交付时间
        self._click(SignaturePage.selectors["delivery_time"])
        # 鼠标悬浮近一周
        self._hover(SignaturePage.selectors["week"])
        # 鼠标悬浮本月
        self._hover(SignaturePage.selectors["month"])
        # 鼠标悬浮近三个月
        self._hover(SignaturePage.selectors["three_months"])
        # 鼠标悬浮近半年
        self._hover(SignaturePage.selectors["half_a_year"])
        # 鼠标悬浮上个季度
        self._hover(SignaturePage.selectors["last_quarter"])
        # 鼠标悬浮本季度
        self._hover(SignaturePage.selectors["quarter"])
        # 鼠标点击本季度
        self._click(SignaturePage.selectors["quarter"])

    # 搜索业务类型
    def business_type(self):
        # 点击业务类型搜索框
        self._click(SignaturePage.selectors["business_type"])
        # 选择M_Saas业务类型
        self._click(SignaturePage.selectors["M_Saas"])

    # 搜索销售人员
    def salesman(self):
        # 点击销售人员搜索框
        self._click(SignaturePage.selectors["salesman"])
        # 选择M_Saas业务类型
        self._click(SignaturePage.selectors["technology_department"])

    #  签单列表，操作
    def operation(self):
        self._click(SignaturePage.selectors["input_name"])
        # 鼠标向下滑动
        self.page.mouse.wheel(0, 1000)
        self._click(SignaturePage.selectors["ali_test_name"])
        # 鼠标向左滑动
        self.page.mouse.wheel(1000, 0)

    # 点击签单进入详情页面
    def signature_detail(self):
        with self.page.expect_popup() as popup_info:
            self.page.click(SignaturePage.selectors["signature_detail"])
        page1 = popup_info.value
        page1.close()
